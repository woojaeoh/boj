import java.math.*;
import java.util.Scanner;

public class Main {

	
	//하노이탑-> 맨 마지막꺼를 3으로 옴기고 n-1개를 다시 옴기고,
	
	static void hanoi(int n, int a, int b, int c) {
		
		if(n==1) { 
		System.out.println(a +" "+ c);
		}
		
		else {
			hanoi(n-1, a, c, b); //2, 1,3,2-> 1,1,2,3 (1에서 3으로)->1에서2로->1,3,1,2(3에서 2로)-> 1,1,3,2(1에서 2로)->
			System.out.println(a + " "+ c);
			hanoi(n-1, b, a, c );//
		}
	}

	public static void main(String[] args) {
		
		Scanner sc= new Scanner(System.in);
		int N = sc.nextInt(); //원판의 개수는 N개
		

		BigInteger k = new BigInteger( "2" ).pow( N ).subtract( BigInteger.ONE );//
		//2의 100승-1은 8바이트넘어감.-> BigInteger사용
		
		System.out.println(k);
		
		if(N<=20) {
			hanoi(N,1,2,3); //1에 N개의 원판이 있고 2를거쳐 3으로 옴기기
		}
		
		
	}
	

}
