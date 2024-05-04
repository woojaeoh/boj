import java.util.Scanner;

public class Main {

	static void quicksort(int arr[],int left, int right) {
		if(left<right) {
		int p = partition(arr, left,right);
		
		quicksort(arr,left, p-1);
		quicksort(arr,p+1,right);
		}
	}
	
	static int partition(int arr[],int left,int right) {
		int pivot=arr[right]; //제일 오른쪽 값을 pivot으로 설정.
		int i= left -1;
		
		for(int j= left; j<=right-1; j++) {
			if(arr[j]<=pivot) {
				i++;
				swap(arr,i,j);
			}
		}
		swap(arr,i+1,right);
		return i+1;
	}
	
	static void swap(int arr[],int i, int j) {
		int tmp=arr[i];
		arr[i]=arr[j];
		arr[j]=tmp;
		
	}
	
	public static void main(String[] args) {
		//quick sort 이용
		//pivot 이용 해서 pivot 과 크기 비교해서
		Scanner sc= new Scanner(System.in);
		int n= sc.nextInt();
	
		int arr[]= new int[n];
		for(int i=0; i<n; i++) {
			arr[i]=sc.nextInt();
		}
		
		quicksort(arr,0,arr.length-1);
	
		for(int i=0; i<n; i++) {
		System.out.println(arr[i]);
		
		}
	}

}
