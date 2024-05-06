import java.io.*;
import java.util.Arrays;

public class Main {
	public static void main(String[] args) throws IOException{
	
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringBuilder sb = new StringBuilder();
		
		
		int n =Integer.parseInt(br.readLine());
		int arr[]= new int[n];
		for(int i=0; i<n; i++) {
			arr[i]=Integer.parseInt(br.readLine());
		}
		

		Arrays.sort(arr);	//java내장함수 sort ->오름차순 정렬
		
		for(int ans: arr) {
			sb.append(ans).append("\n");
		}
		bw.write(sb.toString());	//stringbuilder객체 sb에 저장된 문자열을 bw파일에 쓴다.. 
									
		
		
		br.close();	//객체 br닫기.
	    bw.flush();	//버퍼에있는 데이터 모두 출력
	    bw.close();	//객체 닫기
	}

}
