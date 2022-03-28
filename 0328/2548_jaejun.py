package algorithm.baekjoon.BruteForcing;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class S2548 {
	static int[] numbers;
	static boolean[] isCalculated;
	static int N, answer = Integer.MAX_VALUE;
	static int nowMin = Integer.MAX_VALUE;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());

		numbers = new int[N];
		isCalculated = new boolean[10001];
		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) {
			numbers[i] = Integer.parseInt(st.nextToken());
		}

		for (int number : numbers) {
			if (!isCalculated[number]) {
				int result = getDiff(number);
				getAnswer(result, number);
			}
		}

		System.out.println(answer);
	}

	private static void getAnswer(int result, int number) {
		if (result < nowMin) {
			nowMin = result;
			answer = number;
		} else if (result == nowMin) {
			answer = Math.min(answer, number);
		}
	}

	private static int getDiff(int standard) {
		int ret = 0;
		for (int number : numbers) {
			ret += Math.abs(number - standard);
		}
		return ret;
	}
}

