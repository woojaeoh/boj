import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		
		Scanner sc= new Scanner(System.in);

		int n= sc.nextInt();	//연산 횟수 
		
		String s= sc.next();
//		char c[]=s.toCharArray();	//문자열을 문자로 변환하는 함수이다,
		
		int sum =0;
		
		for(int i=0; i<n; i++) {
			sum+=s.charAt(i)-'0';
		}
		System.out.println(sum);
	
	}
}
