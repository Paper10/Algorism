# k3s 전환을 위한 YAML 파일 변경 사항 요약

## 변경된 파일 목록

### 1. Ingress 파일들 (nginx → traefik)

다음 파일들의 `ingressClassName`이 `nginx`에서 `traefik`으로 변경되었습니다:

- ✅ `filebrowser/filebrowser_ingress.yaml`
- ✅ `jellyfin/jellyfin_ingress.yaml`
- ✅ `jellyfin2/jellyfin2_ingress.yaml`
- ✅ `rancher/rancher_ingress.yaml`
- ✅ `ttyd/ttyd_ingress.yaml`

**변경 내용:**
```yaml
# 변경 전
spec:
  ingressClassName: nginx

# 변경 후
spec:
  ingressClassName: traefik
```

### 2. ClusterIssuer 파일

- ✅ `ingress/ingress_clusterissuer.yaml`

**변경 내용:**
```yaml
# 변경 전
    solvers:
    - http01:
        ingress:
          class: nginx

# 변경 후
    solvers:
    - http01:
        ingress:
          class: traefik
```

## 변경되지 않은 파일들 (k3s와 호환)

다음 파일들은 k3s 환경에서도 그대로 사용 가능합니다:

### StatefulSet 파일들
- `filebrowser/filebrowser_statefulset.yaml`
- `jellyfin/jellyfin_statefulset.yaml`
- `jellyfin2/jellyfin2_ingress.yaml`
- `rancher/rancher_statefulset.yaml`
- `minecraft/minecraft_statefulset.yaml`
- `ttyd/ttyd_statefulet.yaml`

### Service 파일들
- 모든 `*_service.yaml` 파일들

### PV/PVC 파일들
- 모든 `*_pv.yaml` 파일들
- 모든 `*_pvc.yaml` 파일들

### Certificate 파일
- `ingress/ingress_certificate.yaml`

### 기타 파일들
- `rancher/rancher_serviceaccount.yaml`
- `rancher/rancher_clusterrolebinding.yaml`

## 주요 변경 사항 요약

1. **Ingress Controller 변경**: nginx → Traefik (k3s 기본 제공)
2. **Ingress Class 변경**: `nginx` → `traefik`
3. **cert-manager 설정**: Traefik용으로 수정

## 다음 단계

자세한 전환 절차는 `K3S_MIGRATION_GUIDE.md` 파일을 참조하세요.

