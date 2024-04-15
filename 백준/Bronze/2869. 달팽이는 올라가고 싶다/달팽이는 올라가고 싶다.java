import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		
		int a,b,v;
		
		Scanner sc= new Scanner(System.in);
		a =sc.nextInt();
		b =sc.nextInt();
		v = sc.nextInt();

		sc.close();
		
		int day = (v-b)/(a-b);

		
		if( (v-b)%(a-b)!=0) {
			day++;
		}
		
		System.out.println(day);

		
}
}