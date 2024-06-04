import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.StringTokenizer;

class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();
	static StringTokenizer st;
	static final int MAX = 2000000000;
	static int[] dx = { 1, -1, 0, 0 };
	static int[] dy = { 0, 0, 1, -1 };

	static LinkedList<int[]> q = new LinkedList<>();

	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		int k = Integer.parseInt(st.nextToken());
		LinkedList<Integer>[] mat = new LinkedList[n];
		for (int i = 0; i < n; i++) {
			mat[i] = new LinkedList<>();
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < m; j++)
				mat[i].addLast(Integer.parseInt(st.nextToken()));
		}
		for (int i = 0; i < k; i++) {
			st = new StringTokenizer(br.readLine());
			int t = Integer.parseInt(st.nextToken());
			int r = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			for (int j1 = t - 1; j1 < n; j1 += t) {
				for (int j2 = 0; j2 < c % m; j2++) {
					if (r == 0)
						mat[j1].addFirst(mat[j1].removeLast());
					else
						mat[j1].addLast(mat[j1].removeFirst());
				}
			}

			int sum = 0;
			int cnt = 0;
			boolean ers = false;
			for (int x = 0; x < n; x++) {
				for (int y = 0; y < m; y++) {
					int mxy = mat[x].get(y);
					if (mxy == -1)
						continue;
					q.clear();
					q.add(new int[] { x, y });
					while (q.size() > 0) {
						int[] now = q.remove();
						int xx = now[0];
						int yy = now[1];
						for (int d = 0; d < 4; d++) {
							int nx = xx + dx[d];
							int ny = (yy + dy[d] + m) % m;
							if (nx < 0 || nx >= n || mat[nx].get(ny) != mxy)
								continue;
							ers = true;
							mat[nx].set(ny, -1);
							q.add(new int[] { nx, ny });
						}
					}
					if (mat[x].get(y) != -1) {
						cnt++;
						sum += mxy;
					}
				}
			}

			if (ers)
				continue;
			double avg = sum / (double) cnt;
			for (int x = 0; x < n; x++) {
				for (int y = 0; y < m; y++) {
					int mxy = mat[x].get(y);
					if (mxy == -1)
						continue;
					if (mxy < avg)
						mat[x].set(y, mxy + 1);
					else if (mxy > avg)
						mat[x].set(y, mxy - 1);
				}
			}
		}

		int result = 0;
		for (int x = 0; x < n; x++) {
			for (int y = 0; y < m; y++) {
				int mxy = mat[x].get(y);
				//System.out.print((mxy == -1 ? 0 : mxy) + " ");
				result += mxy == -1 ? 0 : mxy;
			}
			//System.out.println();
		}
		sb.append(result);

		// -----------------------------------------------------

		System.out.println(sb);
	}

}
