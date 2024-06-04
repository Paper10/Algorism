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

	static int n;
	static int result = MAX;
	static boolean[][] mat;
	static int[][] land;
	static boolean[][] visit;
	static LinkedList<int[]> q = new LinkedList<int[]>();

	public static void main(String[] args) throws IOException {
		n = Integer.parseInt(br.readLine());
		mat = new boolean[n][n];
		land = new int[n][n];
		int[] tmp = new int[4];
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < n; j++) {
				land[i][j] = 0;
				mat[i][j] = st.nextToken().equals("1");
				if (mat[i][j]) {
					tmp[0] = i;
					tmp[1] = j;
				}
			}
		}

		int num = 1;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (!mat[i][j] || land[i][j] > 0)
					continue;
				q.clear();
				land[i][j] = num;
				q.add(new int[] { i, j });
				while (q.size() > 0) {
					int[] now = q.remove();
					int x = now[0];
					int y = now[1];
					for (int d = 0; d < 4; d++) {
						int nx = x + dx[d];
						int ny = y + dy[d];
						if (nx < 0 || ny < 0 || nx >= n || ny >= n || land[nx][ny] > 0 || !mat[nx][ny])
							continue;
						land[nx][ny] = num;
						q.add(new int[] { nx, ny });
					}
				}
				num++;
			}
		}

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (land[i][j] == 0)
					continue;
				visit = new boolean[n][n];
				int sl = land[i][j];
				q.clear();
				q.add(new int[] { i, j, 0 });
				w: while (q.size() > 0) {
					int[] now = q.remove();
					int x = now[0];
					int y = now[1];
					int w = now[2];
					for (int d = 0; d < 4; d++) {
						int nx = x + dx[d];
						int ny = y + dy[d];
						if (nx < 0 || ny < 0 || nx >= n || ny >= n || visit[nx][ny] || land[nx][ny] == sl)
							continue;
						visit[nx][ny] = true;
						if (land[nx][ny] > 0) {
							result = Math.min(result, w);
							break w;
						} else {
							q.add(new int[] { nx, ny, w + 1 });
						}
					}
				}
			}
		}

		sb.append(result);

		// -----------------------------------------------------

		System.out.println(sb);
	}
}
