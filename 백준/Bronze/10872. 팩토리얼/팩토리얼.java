import java.util.Scanner;

//팩토리얼
public class Main {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();

		if(n==0) {
			System.out.println("1");
		}
		else {
		factorial(n);
		int factorial=factorial(n);
		System.out.println(factorial);
		}
		
	}

	static int factorial(int n) {
		
		if(n==1) {
			return 1;
		}
		else {
			return n*factorial(n-1);
		}
	}
	
}
