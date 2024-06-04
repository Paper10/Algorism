import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();
	static StringTokenizer st;
	static final int MAX = 2000000000;
	static final long LMAX = Long.MAX_VALUE;
	static final int[] dx = { 1, -1, 0, 0, 0};
	static final int[] dy = { 0, 0, 1, -1, 0};

	static int far(int x1, int x2, int y1, int y2) {
		int xx = Math.abs(x1 - x2);
		int yy = Math.abs(y1 - y2);
		return xx + yy;
	}

	public static void main(String[] args) throws NumberFormatException, IOException {
		int n = Integer.parseInt(br.readLine());
		long[] a = new long[5];
		int[][] ap = new int[5][2];
		long[] b = new long[5];
		int[][] bp = new int[5][2];
		st = new StringTokenizer(br.readLine());
		int x1 = Integer.parseInt(st.nextToken());
		int y1 = Integer.parseInt(st.nextToken());
		for (int i = 0; i < 5; i++) {
			ap[i][0] = x1;
			ap[i][1] = y1;
			b[i] = LMAX;
		}

		for (int T = 0; T < n; T++) {
			st = new StringTokenizer(br.readLine());
			int x2 = Integer.parseInt(st.nextToken());
			int y2 = Integer.parseInt(st.nextToken());
			for (int i = 0; i < 5; i++) {
				bp[i][0] = x2 + dx[i];
				bp[i][1] = y2 + dy[i];
				for (int j = 0; j < 5; j++)
					b[i] = Math.min(b[i], a[j] + far(ap[j][0], bp[i][0], ap[j][1], bp[i][1]));
			}

			for (int i = 0; i < 5; i++) {
				a[i] = b[i];
				ap[i][0] = bp[i][0];
				ap[i][1] = bp[i][1];
				b[i] = LMAX;
			}

		}

		long res = LMAX;
		for (int i = 0; i < 5; i++)
			res = Math.min(res, a[i]);
		sb.append(res);

		System.out.println(sb);
	}
}
