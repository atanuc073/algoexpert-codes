/******************************************************************************

                            Online Java Compiler.
                Code, Compile, Run and Debug java program online.
Write your code in this editor and press "Run" button to execute it.

*******************************************************************************/

public class SelectionSort
{
	public static void main(String[] args) {
		System.out.println("Hello World");
		int a[] = {2, 1, 4, 3};
	    selectionSort(a);
	    
	    for(int i = 0; i <a.length; i++){
	        System.out.print(a[i] + " ");
	    }
	}
	
	public static void selectionSort(int[] arr){
	    int n=arr.length;
	    
	    for(int i=0;i<n;i++){
	        int min_ind=i;
	        for(int j=i;j<n;j++){
	            if(arr[j]<arr[min_ind]){
	                min_ind=j;
	            }
	            
	        }
	        int temp=arr[min_ind];
	        arr[min_ind]=arr[i];
	        arr[i]=temp;
	    }
	}
}
