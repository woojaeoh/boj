import java.util.Scanner;

public class Main{

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		char ascii = sc.next().charAt(0);
		
		System.out.println((int)ascii);
		
		sc.close();
		
	}

}
