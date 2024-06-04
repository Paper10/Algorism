import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();
	static StringTokenizer st;

	static ArrayList<Integer> arr = new ArrayList<>();
	static ArrayList<Integer> cycle = new ArrayList<>();
	static boolean[] visit;
	static int result;

	static void team(int now) {
		visit[now] = true;
		cycle.add(now);
		int next = arr.get(now);
		if (visit[next]) {
			if (cycle.contains(next))
				result += cycle.size() - cycle.indexOf(next);
		} else
			team(next);

	}

	public static void main(String[] args) throws IOException {
		int N = Integer.parseInt(br.readLine());
		for (int T = 0; T < N; T++) {
			int n = Integer.parseInt(br.readLine());
			arr.clear();
			arr.add(0);
			st = new StringTokenizer(br.readLine());
			for (int i = 1; i <= n; i++)
				arr.add(Integer.parseInt(st.nextToken()));
			visit = new boolean[n + 1];
			result = 0;

			for (int i = 1; i <= n; i++) {
				if (!visit[i]) {
					cycle.clear();
					team(i);
				}
			}

			sb.append(n - result).append("\n");

		}

		// --------------------------
		System.out.println(sb);
	}

}
