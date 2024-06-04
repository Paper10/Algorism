import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

class Box implements Comparable<Box> {
	int id;
	int space;
	int height;
	int weight;

	public Box(int id, int space, int height, int weight) {
		this.id = id;
		this.space = space;
		this.height = height;
		this.weight = weight;
	}

	@Override
	public int compareTo(Box o) {
		return o.space - space;
	}

	@Override
	public String toString() {
		return "Box [id=" + id + ", space=" + space + ", height=" + height + ", weight=" + weight + "]";
	}
}

class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();
	static StringTokenizer st;
	static int MAX = 2000000000;

	public static void main(String[] args) throws NumberFormatException, IOException {
		int n = Integer.parseInt(br.readLine());
		Box[] bs = new Box[n];
		int[] mh = new int[n];
		for (int i = 1; i <= n; i++) {
			st = new StringTokenizer(br.readLine());
			int s = Integer.parseInt(st.nextToken());
			int h = Integer.parseInt(st.nextToken());
			int w = Integer.parseInt(st.nextToken());
			bs[i - 1] = new Box(i, s, h, w);
			mh[i - 1] = -1;
		}
		Arrays.sort(bs);
//		for(Box b:bs)
//			System.out.println(b);

		int maxh = bs[0].height;
		mh[0] = maxh;

		for (int i = 1; i < n; i++) {
			mh[i] = bs[i].height;
			for (int j = 0; j < i; j++) {
				if (bs[i].weight < bs[j].weight)
					mh[i] = Math.max(mh[i], mh[j] + bs[i].height);
				maxh = Math.max(maxh, mh[i]);
			}
		}

		String res = "";
		int cnt = 0;
		for (int i = n - 1; i >= 0; i--) {
			if (mh[i] == maxh) {
				res += bs[i].id + "\n";
				cnt++;
				maxh -= bs[i].height;
			}
		}
		System.out.println(cnt + "\n" + res);

	}
}