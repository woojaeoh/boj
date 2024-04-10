import java.util.Scanner;

public class Main {

	static boolean isPrime(int num) {
		
		if(num==1){
			return false;
		}
		
		for(int i=2; i<num; i++) {
			if(num%i==0) {
				return false;
			}
		}
		
		
		return true;
	}
	
	
	public static void main(String[] args) {
		//100이하숫자중 소수 출력
		
	
		Scanner sc= new Scanner(System.in);
		int N = sc.nextInt();
		
		int count=0; //소수의 개수
		
		
		for(int i =0; i<N; i++) {
			int num =sc.nextInt();
			
			if(isPrime(num)) {
				count++;
			}
			
		}
		
			System.out.println(count);
			
	}
}
		
	
