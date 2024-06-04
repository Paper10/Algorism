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
	static LinkedList<int[]> q = new LinkedList<int[]>();
	static char[][] mat;
	static int[][][] visit;

	static void right(int x, int y, int h, int w) {
		if (h == 0) {
			if (y == n - 2)
				return;
			if (mat[x][y + 2] == '1')
				return;
		}
		if (h == 1) {
			if (y == n - 1)
				return;
			if (mat[x][y + 1] == '1' || mat[x + 1][y + 1] == '1' || mat[x - 1][y + 1] == '1')
				return;
		}
		if (visit[x][y + 1][h] <= w + 1)
			return;
		visit[x][y + 1][h] = w + 1;
		q.add(new int[] { x, y + 1, h, w + 1 });
		// System.out.println(x + " " + y + " " + h + " " + w + " " + "r");
	}

	static void left(int x, int y, int h, int w) {
		if (h == 0) {
			if (y == 1)
				return;
			if (mat[x][y - 2] == '1')
				return;
		}
		if (h == 1) {
			if (y == 0)
				return;
			if (mat[x][y - 1] == '1' || mat[x + 1][y - 1] == '1' || mat[x - 1][y - 1] == '1')
				return;
		}
		if (visit[x][y - 1][h] <= w + 1)
			return;
		visit[x][y - 1][h] = w + 1;
		q.add(new int[] { x, y - 1, h, w + 1 });
	}
	
	static void up(int x, int y, int h, int w) {
		if (h == 0) {
			if (x == 0)
				return;
			if (mat[x - 1][y] == '1' || mat[x - 1][y + 1] == '1' || mat[x - 1][y - 1] == '1')
				return;
		}
		if (h == 1) {
			if (x == 1)
				return;
			if (mat[x - 2][y] == '1')
				return;
		}
		if (visit[x - 1][y][h] <= w + 1)
			return;
		visit[x - 1][y][h] = w + 1;
		q.add(new int[] { x - 1, y, h, w + 1 });
	}

	static void down(int x, int y, int h, int w) {
		
		if (h == 0) {
			if (x == n - 1)
				return;
			if (mat[x + 1][y] == '1' || mat[x + 1][y + 1] == '1' || mat[x + 1][y - 1] == '1')
				return;
		}
		if (h == 1) {
			if (x == n - 2)
				return;
			if (mat[x + 2][y] == '1')
				return;
		}
		if (visit[x + 1][y][h] <= w + 1)
			return;
		visit[x + 1][y][h] = w + 1;
		q.add(new int[] { x + 1, y, h, w + 1 });
	}
	
	static void turn(int x, int y, int h, int w) {
		for (int i = x - 1; i <= x + 1; i++) {
			for (int j = y - 1; j <= y + 1; j++) {
				if (i < 0 || j < 0 || i >= n || j >= n || mat[i][j] == '1')
					return;
			}
		}
		if (visit[x][y][(h + 1) % 2] <= w + 1)
			return;
		visit[x][y][(h + 1) % 2] = w + 1;
		q.add(new int[] { x, y, (h + 1) % 2, w + 1 });
	}

	public static void main(String[] args) throws IOException {
		n = Integer.parseInt(br.readLine());
		mat = new char[n][n];
		visit = new int[n][n][2];
		int[] st = null;
		int[] et = null;
		for (int i = 0; i < n; i++) {
			char[] t = br.readLine().toCharArray();
			for (int j = 0; j < n; j++) {
				visit[i][j][0] = MAX;
				visit[i][j][1] = MAX;
				mat[i][j] = t[j];
				if (mat[i][j] == 'B') {
					if (i >= 2 && mat[i - 1][j] == 'B' && mat[i - 2][j] == 'B')
						st = new int[] { i - 1, j, 1 };
					if (j >= 2 && mat[i][j - 1] == 'B' && mat[i][j - 2] == 'B')
						st = new int[] { i, j - 1, 0 };
				}
				if (mat[i][j] == 'E') {
					if (i >= 2 && mat[i - 1][j] == 'E' && mat[i - 2][j] == 'E')
						et = new int[] { i - 1, j, 1 };
					if (j >= 2 && mat[i][j - 1] == 'E' && mat[i][j - 2] == 'E')
						et = new int[] { i, j - 1, 0 };
				}
			}
		}

		q.clear();
		q.add(new int[] { st[0], st[1], st[2], 0 });
		visit[st[0]][st[1]][st[2]] = 0;
		while (q.size() > 0) {
			int[] now = q.remove();
			int x = now[0];
			int y = now[1];
			int h = now[2];
			int w = now[3];
			if (x == et[0] && y == et[1] && h == et[2]) {
				result = Math.min(result, w);
				continue;
			}
			right(x, y, h, w);
			left(x, y, h, w);
			up(x, y, h, w);
			down(x, y, h, w);
			turn(x, y, h, w);
		}
		System.out.println(result == MAX ? 0 : result);
	}

}

