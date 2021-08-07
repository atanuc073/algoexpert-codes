

public class BubbleSort
{
	public static void main(String[] args) {
		System.out.println("Hello World");
		int a[] = {2, 1, 4, 3};
	    bubbleSort(a);
	    
	    for(int i = 0; i < a.length; i++){
	        System.out.print(a[i] + " ");
	    }
	}
	public static void bubbleSort(int[] arr){
	    int n=arr.length;
	    for(int i=0;i<n;i++){
	        
	        for(int j=0;j<(n-i-1);j++){
	            if(arr[j]>arr[j+1]){
	                int temp =arr[j];
	                arr[j]=arr[j+1];
	                arr[j+1]=temp;
	            }
	            
	        }
	    }
	}
}
