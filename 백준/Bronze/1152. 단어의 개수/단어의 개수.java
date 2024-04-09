import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		// 입력받는 문자의 개수 세기, 띄어쓰기로 구분.
		//1. 문자열 배열 객체 생성 후, 띄어쓰기로 다른 배열에 담기
		//	띄어쓰기 개수 +1
		
		int count=0;
		
		Scanner sc = new Scanner(System.in);
		String string  =sc.nextLine();
		sc.close();
		
		string=string.trim(); //양 끝 공백문자 제거? 필요한가 
		
		String words[]=string.split(" ");
		
		if(string.isEmpty()) {
			System.out.println(0);
		}
		else {
			
			for(int i=0; i<words.length; i++)
			{
				if(words[i]!="") {
					count++;
				}
			}
			System.out.println(count);
				
		}
		
		
	}

}
