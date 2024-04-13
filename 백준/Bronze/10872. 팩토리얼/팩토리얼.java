import java.util.Scanner;

public class Main {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		
		//3 입력-> 2랑 1곱하기
		int score=1;
		
		for(int i=1; i<=n; i++) {
		score*=i;
		}
		System.out.println(score);
	}

}
