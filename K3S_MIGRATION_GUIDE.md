# Kubernetes에서 k3s로 전환 가이드

이 가이드는 Rocky Linux 9 환경에서 기존 Kubernetes 클러스터를 k3s로 전환하고, Docker CRI를 containerd로 전환하는 과정을 설명합니다.

## 목차
1. [사전 준비](#사전-준비)
2. [기존 Kubernetes 및 Docker 제거](#기존-kubernetes-및-docker-제거)
3. [k3s 설치](#k3s-설치)
4. [containerd를 Docker처럼 사용하기 (nerdctl)](#containerd를-docker처럼-사용하기-nerdctl)
5. [cert-manager 설치](#cert-manager-설치)
6. [리소스 재배포](#리소스-재배포)
7. [검증](#검증)

---

## 사전 준비

### 1. 현재 리소스 백업

```bash
# 현재 네임스페이스의 모든 리소스 백업
kubectl get all -n kube-ns -o yaml > kube-ns-backup.yaml

# 모든 PVC 정보 백업
kubectl get pvc -n kube-ns -o yaml > pvc-backup.yaml

# 모든 PV 정보 백업
kubectl get pv -o yaml > pv-backup.yaml

# Ingress 리소스 백업
kubectl get ingress -n kube-ns -o yaml > ingress-backup.yaml
```

**명령어 설명:**
- `kubectl get all`: 네임스페이스의 모든 리소스(Pod, Service, Deployment, StatefulSet 등) 조회
- `-n kube-ns`: kube-ns 네임스페이스 지정
- `-o yaml`: YAML 형식으로 출력
- `>`: 출력을 파일로 저장

### 2. 데이터 디렉토리 확인

k3s는 기본적으로 `/var/lib/rancher/k3s`에 데이터를 저장합니다. 기존 데이터 경로를 확인하세요:

```bash
# 현재 PV가 사용하는 호스트 경로 확인
ls -la /drive/filebrowser/
ls -la /drive/jellyfin/
# 기타 데이터 디렉토리 확인
```

---

## 기존 Kubernetes 및 Docker 제거

### 1. Kubernetes 리소스 삭제

```bash
# 모든 리소스 삭제 (주의: 데이터는 유지됨)
kubectl delete statefulset --all -n kube-ns
kubectl delete deployment --all -n kube-ns
kubectl delete service --all -n kube-ns
kubectl delete ingress --all -n kube-ns
kubectl delete pvc --all -n kube-ns
kubectl delete pv --all
kubectl delete certificate --all -n kube-ns
kubectl delete clusterissuer --all
```

**명령어 설명:**
- `kubectl delete`: 리소스 삭제
- `--all`: 해당 타입의 모든 리소스 선택
- PVC를 먼저 삭제한 후 PV를 삭제해야 함 (의존성 때문)

### 2. Kubernetes 클러스터 제거

```bash
# kubeadm으로 설치된 경우
sudo kubeadm reset -f

# kubectl, kubelet, kubeadm 제거
sudo dnf remove -y kubelet kubeadm kubectl

# Kubernetes 관련 패키지 제거
sudo dnf remove -y kubernetes-cni cri-tools
```

**명령어 설명:**
- `kubeadm reset`: 클러스터 초기화 및 정리
- `-f`: 확인 없이 강제 실행
- `dnf remove`: 패키지 제거 (Rocky Linux 9는 dnf 사용)

### 3. Docker 제거

**⚠️ 중요: k3s는 자체 containerd를 사용하므로, Docker의 containerd.io를 제거해도 k3s에는 영향이 없습니다.**

```bash
# 실행 중인 컨테이너 중지
sudo docker stop $(sudo docker ps -aq) 2>/dev/null || true

# 모든 컨테이너 제거
sudo docker rm $(sudo docker ps -aq) 2>/dev/null || true

# Docker 서비스 중지 및 비활성화
sudo systemctl stop docker 2>/dev/null || true
sudo systemctl disable docker 2>/dev/null || true

# Docker 패키지 제거 (containerd.io 포함)
# k3s는 자체 containerd를 설치하므로 Docker의 containerd.io를 제거해도 문제 없습니다
sudo dnf remove -y docker docker-client docker-client-latest docker-common docker-latest docker-latest-logrotate docker-logrotate docker-engine docker-ce docker-ce-cli containerd.io

# Docker 데이터 디렉토리 정리 (선택사항, 필요시만)
# sudo rm -rf /var/lib/docker
# sudo rm -rf /var/lib/containerd  # k3s가 자체 containerd를 사용하므로 제거 가능
```

**명령어 설명:**
- `docker stop`: 실행 중인 컨테이너 중지
- `docker ps -aq`: 모든 컨테이너 ID 조회 (-a: 모든 컨테이너, -q: ID만)
- `docker rm`: 컨테이너 제거
- `systemctl stop/disable`: 서비스 중지 및 부팅 시 자동 시작 비활성화
- `2>/dev/null || true`: 에러 무시 (Docker가 설치되지 않은 경우 대비)
- **참고**: k3s는 `/var/lib/rancher/k3s/agent/containerd`에 자체 containerd를 설치하므로, Docker의 containerd를 제거해도 k3s에는 영향이 없습니다

### 4. 제거 확인

```bash
# Kubernetes 관련 프로세스 확인
ps aux | grep kube
ps aux | grep etcd

# Docker 관련 프로세스 확인
ps aux | grep docker

# Kubernetes 관련 서비스 확인
sudo systemctl list-units | grep -E 'kube|etcd'

# Docker 서비스 확인
sudo systemctl status docker

# 포트 사용 확인 (6443: k8s API, 10250: kubelet)
sudo netstat -tlnp | grep -E '6443|10250|2379|2380'
```

**명령어 설명:**
- `ps aux`: 실행 중인 모든 프로세스 조회
- `grep`: 특정 문자열 검색
- `systemctl list-units`: 모든 systemd 유닛 목록
- `netstat -tlnp`: TCP 리스닝 포트와 프로세스 정보 확인

### 5. 네트워크 정리

```bash
# iptables 규칙 확인
sudo iptables -L -n

# CNI 네트워크 인터페이스 확인 및 제거
sudo ip link show | grep cni
sudo ip link delete cni0 2>/dev/null || true
sudo ip link delete flannel.1 2>/dev/null || true

# CNI 설정 디렉토리 정리
sudo rm -rf /etc/cni/net.d
sudo rm -rf /opt/cni/bin
```

**명령어 설명:**
- `iptables -L`: iptables 규칙 목록 조회
- `ip link show`: 네트워크 인터페이스 목록
- `ip link delete`: 네트워크 인터페이스 삭제
- `2>/dev/null || true`: 에러 무시 (존재하지 않을 수 있음)

### 6. Kubernetes 데이터 및 설정 파일 완전 삭제

```bash
# kubeconfig 파일 삭제
rm -rf ~/.kube/config
sudo rm -rf /root/.kube

# Kubernetes 데이터 디렉토리 삭제
sudo rm -rf /var/lib/kubelet
sudo rm -rf /var/lib/etcd
sudo rm -rf /etc/kubernetes
sudo rm -rf /var/lib/kubernetes

# kubeadm 설정 파일 삭제
sudo rm -rf /etc/systemd/system/kubelet.service.d
sudo rm -rf /etc/systemd/system/kubelet.service

# Kubernetes 로그 파일 삭제
sudo rm -rf /var/log/kubelet.log
sudo rm -rf /var/log/kube-proxy.log
sudo rm -rf /var/log/pods
sudo rm -rf /var/log/containers

# Kubernetes 관련 환경 변수 파일 정리
sudo rm -f /etc/profile.d/k8s.sh
sudo rm -f /etc/environment.d/k8s.conf
```

**명령어 설명:**
- `rm -rf`: 디렉토리 및 파일 재귀적 삭제 (-r: 재귀, -f: 강제)
- `/var/lib/kubelet`: kubelet 데이터 디렉토리
- `/var/lib/etcd`: etcd 데이터 디렉토리 (있는 경우)
- `/etc/kubernetes`: Kubernetes 설정 디렉토리
- `/var/log/pods`: Pod 로그 디렉토리

### 7. iptables 규칙 완전 정리

**⚠️ 중요: 이 단계는 k3s 설치 전에 수행해야 합니다!**

k3s는 설치 시 자체적으로 필요한 iptables 규칙을 자동으로 생성합니다. 따라서 기존 Kubernetes의 iptables 규칙을 삭제해도 k3s에는 영향이 없습니다. 다만, **k3s가 이미 설치된 상태에서 이 명령어를 실행하면 k3s의 네트워크가 깨질 수 있으므로 주의하세요.**

```bash
# iptables 규칙 백업 (필요시)
sudo iptables-save > ~/iptables-backup.txt

# Kubernetes 관련 iptables 체인 제거
sudo iptables -F
sudo iptables -X
sudo iptables -t nat -F
sudo iptables -t nat -X
sudo iptables -t mangle -F
sudo iptables -t mangle -X
sudo iptables -t raw -F
sudo iptables -t raw -X

# iptables 규칙 저장 (시스템에 따라 다름)
# Rocky Linux 9는 기본적으로 firewalld를 사용하므로, iptables 규칙을 직접 저장하지 않아도 됩니다
# firewalld가 활성화되어 있으면 자동으로 관리됩니다
sudo systemctl status firewalld

# 만약 firewalld를 사용하지 않고 iptables를 직접 사용하는 경우
# sudo iptables-save | sudo tee /etc/sysconfig/iptables
# sudo systemctl enable iptables
# sudo systemctl start iptables
```

**명령어 설명:**
- `iptables -F`: 모든 규칙 플러시
- `iptables -X`: 사용자 정의 체인 삭제
- `iptables -t nat`: NAT 테이블 작업
- `iptables-save`: 현재 규칙 저장
- **주의사항:**
  - ✅ **k3s 설치 전에 실행**: k3s가 필요한 규칙을 자동으로 다시 생성하므로 문제 없음
  - ❌ **k3s 설치 후에 실행 금지**: k3s의 네트워크가 깨질 수 있음
  - ⚠️ **다른 서비스 영향**: 이 명령어는 모든 iptables 규칙을 삭제하므로 다른 네트워크 서비스에도 영향을 줄 수 있습니다

### 8. systemd 서비스 파일 정리

```bash
# Kubernetes 관련 systemd 서비스 파일 확인
sudo systemctl list-unit-files | grep -E 'kube|etcd'

# Kubernetes 관련 서비스 파일 삭제
sudo rm -f /etc/systemd/system/kubelet.service
sudo rm -f /etc/systemd/system/kubelet.service.d/*
sudo rm -f /usr/lib/systemd/system/kubelet.service
sudo rm -f /usr/lib/systemd/system/etcd.service

# systemd 데몬 리로드
sudo systemctl daemon-reload
sudo systemctl reset-failed
```

**명령어 설명:**
- `systemctl list-unit-files`: 설치된 모든 유닛 파일 목록
- `systemctl daemon-reload`: systemd 설정 다시 로드
- `systemctl reset-failed`: 실패한 서비스 상태 초기화

### 9. 추가 패키지 확인 및 제거

```bash
# Kubernetes 관련 모든 패키지 확인
sudo dnf list installed | grep -E 'kube|kubernetes|etcd'

# 추가로 제거할 수 있는 패키지들
sudo dnf remove -y \
  kubernetes-cni \
  cri-tools \
  socat \
  conntrack-tools

# 설치된 패키지 캐시 정리
sudo dnf clean all
```

**명령어 설명:**
- `dnf list installed`: 설치된 패키지 목록
- `grep -E`: 확장 정규식 사용
- `dnf clean all`: 패키지 캐시 정리

### 10. 최종 확인 및 정리

```bash
# 모든 Kubernetes 관련 프로세스 확인 (없어야 함)
ps aux | grep -E 'kube|etcd' | grep -v grep

# 모든 Kubernetes 관련 디렉토리 확인 (없어야 함)
sudo ls -la /var/lib/ | grep -E 'kube|etcd'
sudo ls -la /etc/ | grep -E 'kube|etcd'

# Kubernetes 관련 포트 확인 (사용 중이 아니어야 함)
sudo netstat -tlnp | grep -E '6443|10250|2379|2380|10259|10257'

# kubectl 명령어가 작동하지 않는지 확인 (에러가 나야 정상)
kubectl get nodes 2>&1

# Docker 관련 프로세스 확인 (없어야 함)
ps aux | grep docker | grep -v grep

# Docker 관련 디렉토리 확인
sudo ls -la /var/lib/ | grep docker
```

**명령어 설명:**
- `grep -v grep`: grep 프로세스 자체는 제외
- `2>&1`: 표준 에러를 표준 출력으로 리다이렉션
- 모든 명령어가 결과를 반환하지 않거나 에러가 나면 정상적으로 제거된 것입니다.

### 11. 시스템 재부팅 (선택사항, 권장)

**⚠️ 중요: 이 단계는 k3s 설치 전에 수행하세요!**

```bash
# 모든 정리가 완료된 후 시스템 재부팅 권장
# 재부팅 후에도 Kubernetes 관련 프로세스가 시작되지 않는지 확인
sudo reboot

# 재부팅 후 확인 (k3s 설치 전에 실행)
ps aux | grep -E 'kube|etcd|docker' | grep -v grep
sudo systemctl list-units | grep -E 'kube|etcd|docker'

# 확인 결과가 비어있어야 정상입니다
```

**명령어 설명:**
- `reboot`: 시스템 재부팅
- 재부팅 후 확인하여 완전히 제거되었는지 검증
- **주의**: 재부팅 후 k3s 설치를 진행하세요

---

## k3s 설치

### 1. k3s 설치

```bash
# k3s 설치 (기본 설정)
curl -sfL https://get.k3s.io | sh -

# 또는 특정 버전 설치
# curl -sfL https://get.k3s.io | INSTALL_K3S_VERSION=v1.28.0 sh -
```

**명령어 설명:**
- `curl -sfL`: URL에서 스크립트 다운로드 (-s: 조용히, -f: 실패 시 에러, -L: 리다이렉션 따르기)
- `| sh -`: 다운로드한 스크립트를 실행

### 2. k3s 서비스 상태 확인

```bash
# k3s 서비스 상태 확인
sudo systemctl status k3s

# k3s가 정상 실행 중인지 확인
sudo systemctl is-active k3s

# k3s가 정상적으로 시작될 때까지 대기 (최대 60초)
timeout 60 bash -c 'until sudo systemctl is-active --quiet k3s; do sleep 2; done' && echo "k3s가 정상적으로 시작되었습니다"
```

**명령어 설명:**
- `systemctl status`: 서비스 상태 상세 확인
- `systemctl is-active`: 서비스가 활성 상태인지 확인 (active/inactive 반환)
- `timeout`: 명령어 실행 시간 제한
- k3s가 완전히 시작되려면 몇 초가 걸릴 수 있습니다

### 3. kubectl 설정

```bash
# kubeconfig 파일 복사 (일반 사용자용)
mkdir -p ~/.kube
sudo cp /etc/rancher/k3s/k3s.yaml ~/.kube/config
sudo chown $USER:$USER ~/.kube/config

# k3s의 기본 API 서버 주소를 localhost로 변경 (원격 접속이 아닌 경우)
# sed -i 's/127.0.0.1/localhost/g' ~/.kube/config

# kubectl이 정상 작동하는지 확인
kubectl cluster-info
kubectl get nodes

# k3s가 정상적으로 작동하는지 확인
kubectl get pods --all-namespaces
```

**명령어 설명:**
- `mkdir -p`: 디렉토리 생성 (-p: 부모 디렉토리도 생성)
- `cp`: 파일 복사
- `chown`: 파일 소유자 변경
- `kubectl cluster-info`: 클러스터 정보 확인
- `kubectl get nodes`: 노드 목록 조회
- `kubectl get pods --all-namespaces`: 모든 네임스페이스의 Pod 조회
- **참고**: k3s.yaml 파일의 서버 주소가 `127.0.0.1` 또는 `localhost`로 설정되어 있어야 로컬에서 kubectl이 정상 작동합니다

### 4. 네임스페이스 생성

```bash
# 기존 네임스페이스 생성
kubectl create namespace kube-ns

# 네임스페이스 확인
kubectl get namespace
```

---

## containerd를 Docker처럼 사용하기 (nerdctl)

k3s는 containerd를 컨테이너 런타임으로 사용합니다. Docker 명령어와 유사한 `nerdctl`을 설치하여 Docker처럼 사용할 수 있습니다.

### 1. nerdctl 설치

```bash
# 시스템 아키텍처 확인
ARCH=$(uname -m)
if [ "$ARCH" = "x86_64" ]; then
  ARCH="amd64"
elif [ "$ARCH" = "aarch64" ]; then
  ARCH="arm64"
fi

# nerdctl 다운로드 및 설치 (버전 지정)
NERDCTL_VERSION=1.7.0
wget https://github.com/containerd/nerdctl/releases/download/v${NERDCTL_VERSION}/nerdctl-${NERDCTL_VERSION}-linux-${ARCH}.tar.gz
tar -xzf nerdctl-${NERDCTL_VERSION}-linux-${ARCH}.tar.gz
sudo mv nerdctl /usr/local/bin/
sudo chmod +x /usr/local/bin/nerdctl
rm nerdctl-${NERDCTL_VERSION}-linux-${ARCH}.tar.gz

# 또는 최신 버전 자동 설치 (권장)
# curl -sSL https://github.com/containerd/nerdctl/releases/latest/download/nerdctl-$(uname -s | tr '[:upper:]' '[:lower:]')-$(uname -m | sed 's/x86_64/amd64/').tar.gz | sudo tar -xz -C /usr/local/bin --strip-components=1
```

**명령어 설명:**
- `uname -m`: 시스템 아키텍처 확인 (x86_64 → amd64, aarch64 → arm64)
- `wget`: 파일 다운로드
- `tar -xzf`: tar.gz 압축 해제
- `mv`: 파일 이동
- `chmod +x`: 실행 권한 부여
- **참고**: 최신 버전을 사용하려면 주석 처리된 자동 설치 명령어를 사용하거나 [nerdctl 릴리스 페이지](https://github.com/containerd/nerdctl/releases)에서 최신 버전을 확인하세요

### 2. nerdctl 네임스페이스 설정

```bash
# k3s의 containerd 네임스페이스 사용하도록 설정
export CONTAINERD_NAMESPACE=k8s.io

# 영구적으로 설정하려면 ~/.bashrc에 추가
echo 'export CONTAINERD_NAMESPACE=k8s.io' >> ~/.bashrc
source ~/.bashrc
```

**명령어 설명:**
- `export`: 환경 변수 설정
- `echo '...' >> ~/.bashrc`: 파일에 내용 추가 (>>: append)
- `source ~/.bashrc`: 변경사항 즉시 적용

### 3. nerdctl 사용법 (Docker 명령어와 유사)

```bash
# 컨테이너 목록 조회 (docker ps)
nerdctl ps

# 모든 컨테이너 조회 (docker ps -a)
nerdctl ps -a

# 이미지 목록 조회 (docker images)
nerdctl images

# 컨테이너 실행 (docker run)
nerdctl run -d --name test nginx:latest

# 컨테이너 실행 중 명령어 실행 (docker exec)
nerdctl exec -it test sh

# 컨테이너 중지 (docker stop)
nerdctl stop test

# 컨테이너 시작 (docker start)
nerdctl start test

# 컨테이너 제거 (docker rm)
nerdctl rm test

# 이미지 제거 (docker rmi)
nerdctl rmi nginx:latest

# 로그 확인 (docker logs)
nerdctl logs test

# 컨테이너 정보 확인 (docker inspect)
nerdctl inspect test
```

**명령어 설명:**
- `nerdctl ps`: 실행 중인 컨테이너 목록
- `nerdctl images`: 이미지 목록
- `nerdctl run`: 컨테이너 실행 (-d: 백그라운드, --name: 이름 지정)
- `nerdctl exec`: 실행 중인 컨테이너에서 명령어 실행 (-it: 인터랙티브 터미널)
- `nerdctl stop/start`: 컨테이너 중지/시작
- `nerdctl rm/rmi`: 컨테이너/이미지 제거
- `nerdctl logs`: 컨테이너 로그 확인
- `nerdctl inspect`: 컨테이너 상세 정보

### 4. Docker 명령어 별칭 설정 (선택사항)

```bash
# ~/.bashrc에 별칭 추가
cat >> ~/.bashrc << 'EOF'
# Docker 명령어를 nerdctl로 매핑
alias docker='nerdctl'
alias docker-compose='nerdctl compose'
EOF

source ~/.bashrc
```

**명령어 설명:**
- `alias`: 명령어 별칭 생성
- `cat >>`: 여러 줄을 파일에 추가
- `<< 'EOF'`: heredoc 문법 (EOF까지의 내용을 입력)

---

## cert-manager 설치

k3s는 Traefik을 기본 Ingress Controller로 제공하지만, cert-manager는 별도 설치가 필요합니다.

### 1. cert-manager 설치

```bash
# cert-manager CRD 설치 (네임스페이스는 자동으로 생성됨)
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.13.0/cert-manager.yaml

# 설치 확인 (cert-manager 네임스페이스가 자동 생성됨)
kubectl get pods -n cert-manager

# cert-manager 네임스페이스 확인
kubectl get namespace cert-manager
```

**명령어 설명:**
- `kubectl apply -f URL`: URL에서 YAML 파일을 다운로드하여 적용
- `kubectl get pods`: Pod 목록 조회
- cert-manager YAML 파일에는 네임스페이스 정의가 포함되어 있어 자동으로 `cert-manager` 네임스페이스가 생성됩니다
- **참고**: 최신 버전을 사용하려면 [cert-manager 릴리스 페이지](https://github.com/cert-manager/cert-manager/releases)에서 최신 버전을 확인하세요

### 2. cert-manager 준비 대기

```bash
# cert-manager Pod들이 준비될 때까지 대기
kubectl wait --for=condition=ready pod --all -n cert-manager --timeout=300s

# cert-manager 설치 확인
kubectl get pods -n cert-manager
kubectl get crd | grep cert-manager

# 모든 cert-manager Pod가 Running 상태인지 확인
kubectl get pods -n cert-manager | grep -v Running
```

**명령어 설명:**
- `kubectl wait`: 리소스가 특정 조건이 될 때까지 대기
- `--for=condition=ready`: Ready 조건이 될 때까지
- `--timeout=300s`: 최대 300초 대기
- `kubectl get crd`: CustomResourceDefinition 목록 조회
- cert-manager가 정상 설치되면 CRD(Custom Resource Definition)가 생성됩니다

---

## 리소스 재배포

### 1. ClusterIssuer 배포

```bash
# ClusterIssuer 배포 (Traefik용으로 수정된 버전)
# cert-manager가 완전히 준비된 후 배포해야 합니다
kubectl apply -f ingress/ingress_clusterissuer.yaml

# ClusterIssuer 확인
kubectl get clusterissuer
kubectl describe clusterissuer letsencrypt-http01
```

**명령어 설명:**
- `kubectl apply -f`: YAML 파일을 적용하여 리소스 생성/업데이트
- `kubectl get clusterissuer`: ClusterIssuer 목록 조회
- `kubectl describe`: 리소스 상세 정보 확인

### 2. PV 및 PVC 배포

```bash
# PV 배포 (PVC보다 먼저 배포)
kubectl apply -f filebrowser/filebrowser_pv.yaml
kubectl apply -f jellyfin/jellyfin_pv.yaml
kubectl apply -f jellyfin2/jellyfin2_pv.yaml
kubectl apply -f rancher/rancher_pv.yaml

# PV 상태 확인
kubectl get pv

# PVC 배포
kubectl apply -f filebrowser/filebrowser_pvc.yaml
kubectl apply -f jellyfin/jellyfin_pvc.yaml
kubectl apply -f jellyfin2/jellyfin2_pvc.yaml
kubectl apply -f rancher/rancher_pvc.yaml

# PVC 상태 확인 (Bound 상태가 되어야 함)
kubectl get pvc -n kube-ns
```

**명령어 설명:**
- `kubectl get pv`: PersistentVolume 목록 조회
- `kubectl get pvc`: PersistentVolumeClaim 목록 조회
- PVC가 Bound 상태가 되어야 StatefulSet이 정상적으로 시작됩니다

### 3. StatefulSet 및 Service 배포

```bash
# ServiceAccount 및 ClusterRoleBinding 배포 (Rancher용, 필요시)
kubectl apply -f rancher/rancher_serviceaccount.yaml
kubectl apply -f rancher/rancher_clusterrolebinding.yaml

# Service 배포 (StatefulSet보다 먼저 배포하는 것을 권장)
kubectl apply -f filebrowser/filebrowser_service.yaml
kubectl apply -f jellyfin/jellyfin_service.yaml
kubectl apply -f jellyfin2/jellyfin2_service.yaml
kubectl apply -f rancher/rancher_service.yaml
kubectl apply -f minecraft/minecraft_service.yaml
kubectl apply -f ttyd/ttyd_service.yaml

# StatefulSet 배포
kubectl apply -f filebrowser/filebrowser_statefulset.yaml
kubectl apply -f jellyfin/jellyfin_statefulset.yaml
kubectl apply -f jellyfin2/jellyfin2_statefulset.yaml
kubectl apply -f rancher/rancher_statefulset.yaml
kubectl apply -f minecraft/minecraft_statefulset.yaml
kubectl apply -f ttyd/ttyd_statefulet.yaml

# 배포 상태 확인
kubectl get pods -n kube-ns
kubectl get svc -n kube-ns
```

**명령어 설명:**
- Service를 먼저 배포하면 StatefulSet이 시작될 때 서비스를 찾을 수 있습니다
- `kubectl get pods`: Pod 상태 확인
- `kubectl get svc`: Service 목록 확인

### 4. Certificate 배포

```bash
# Certificate 배포
kubectl apply -f ingress/ingress_certificate.yaml
```

### 5. Ingress 배포

```bash
# Ingress 배포 (Traefik용으로 수정된 버전)
kubectl apply -f filebrowser/filebrowser_ingress.yaml
kubectl apply -f jellyfin/jellyfin_ingress.yaml
kubectl apply -f jellyfin2/jellyfin2_ingress.yaml
kubectl apply -f rancher/rancher_ingress.yaml
kubectl apply -f ttyd/ttyd_ingress.yaml
```

---

## 검증

### 1. Pod 상태 확인

```bash
# 모든 Pod 상태 확인
kubectl get pods -n kube-ns

# Pod 상세 정보 확인
kubectl describe pod <pod-name> -n kube-ns

# Pod 로그 확인
kubectl logs <pod-name> -n kube-ns
```

### 2. Service 확인

```bash
# Service 목록 확인
kubectl get svc -n kube-ns
```

### 3. Ingress 확인

```bash
# Ingress 목록 확인
kubectl get ingress -n kube-ns

# Ingress 상세 정보 확인
kubectl describe ingress <ingress-name> -n kube-ns
```

### 4. Certificate 확인

```bash
# Certificate 상태 확인
kubectl get certificate -n kube-ns

# Certificate 상세 정보 확인
kubectl describe certificate <cert-name> -n kube-ns
```

### 5. Traefik 확인

```bash
# Traefik Pod 확인
kubectl get pods -n kube-system | grep traefik

# Traefik 로그 확인
kubectl logs -n kube-system -l app.kubernetes.io/name=traefik
```

### 6. 웹 서비스 접속 테스트

```bash
# 각 도메인으로 HTTPS 접속 테스트
curl -I https://filebrowser.jhh1749.kro.kr
curl -I https://jellyfin.jhh1749.kro.kr
curl -I https://j6n.jhh1749.kro.kr
curl -I https://rancher.jhh1749.kro.kr
curl -I https://ttyd.jhh1749.kro.kr
```

**명령어 설명:**
- `curl -I`: HTTP 헤더만 조회 (HEAD 요청)

---

## 문제 해결

### 1. Pod가 시작되지 않는 경우

```bash
# Pod 이벤트 확인
kubectl describe pod <pod-name> -n kube-ns

# Pod 로그 확인
kubectl logs <pod-name> -n kube-ns

# 이전 컨테이너 로그 확인
kubectl logs <pod-name> -n kube-ns --previous
```

### 2. PVC가 바인딩되지 않는 경우

```bash
# PVC 상태 확인
kubectl get pvc -n kube-ns

# PV 상태 확인
kubectl get pv

# PVC 상세 정보 확인
kubectl describe pvc <pvc-name> -n kube-ns
```

### 3. 인증서가 발급되지 않는 경우

```bash
# cert-manager Pod 상태 확인
kubectl get pods -n cert-manager

# cert-manager 컨트롤러 로그 확인
kubectl logs -n cert-manager -l app.kubernetes.io/name=cert-manager --tail=100

# cert-manager webhook 로그 확인
kubectl logs -n cert-manager -l app.kubernetes.io/name=webhook --tail=100

# cert-manager cainjector 로그 확인
kubectl logs -n cert-manager -l app.kubernetes.io/name=cainjector --tail=100

# Certificate 이벤트 확인
kubectl describe certificate <cert-name> -n kube-ns

# CertificateRequest 확인
kubectl get certificaterequest -n kube-ns
kubectl describe certificaterequest <cr-name> -n kube-ns

# Challenge 확인 (HTTP-01 인증 사용 시)
kubectl get challenge -n kube-ns
```

### 4. Ingress가 작동하지 않는 경우

```bash
# Traefik Pod 상태 확인
kubectl get pods -n kube-system | grep traefik

# Traefik 로그 확인
kubectl logs -n kube-system -l app.kubernetes.io/name=traefik

# Ingress 이벤트 확인
kubectl describe ingress <ingress-name> -n kube-ns
```

---

## 주요 변경사항 요약

1. **Ingress Controller**: nginx → Traefik
2. **컨테이너 런타임**: Docker → containerd (nerdctl로 Docker 명령어 사용 가능)
3. **Ingress Class**: `nginx` → `traefik`
4. **k3s 기본 경로**: `/var/lib/rancher/k3s`

---

## 참고 자료

- [k3s 공식 문서](https://docs.k3s.io/)
- [nerdctl GitHub](https://github.com/containerd/nerdctl)
- [cert-manager 문서](https://cert-manager.io/docs/)
- [Traefik Ingress 문서](https://doc.traefik.io/traefik/providers/kubernetes-ingress/)

