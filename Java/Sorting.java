import java.util.*;
public class Sorting {
    public static void main(String args[]) {
        // Bubble sort 
        // Sorting Array in ascending order 
        int arr[] = {5,8,10,68,30,41,49,53,2,25,24,9,4,50,54,62,6,48,42,12,17,60,65,45,29,57,21,69,33,44,32,58,66,13,22,27,26,28,19,1,23};
        for(int i = 0; i < arr.length-1; i++){
            for(int j = 0; j < arr.length-i-1; j++) {
                if(arr[j+1] < arr[j]) {
                    // Swap c=a, a=b, b=c
                    int temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                }
            }
        }
        System.out.println("Bubble sort");
        // Array sorted in ascending order
        for(int i = 0; i < arr.length; i++){
            System.out.print(arr[i]+" ");
        }
        System.out.println();
        //System.out.println();

        // Sorting Array in descending order 
        for(int i = 0; i < arr.length-1; i++){
            for(int j = 0; j < arr.length-i-1; j++) {
                if(arr[j+1] > arr[j]) {
                    // Swap c=a, a=b, b=c
                    int temp = arr[j+1];
                    arr[j+1] = arr[j];
                    arr[j] = temp;
                }
            }
        }

        // Array sorted in descending order
        for(int i = 0; i < arr.length; i++){
            System.out.print(arr[i]+" ");
        }
        System.out.println();
        System.out.println("Selection sort");

        // Selection Sort Case : 1 Descending order
        for(int i = 0; i < arr.length-1; i++){
            int smallest = i;
            for(int j = i+1; j < arr.length; j++){
                if(arr[smallest] > arr[j]){
                    smallest = j;
                }
                int temp = arr[smallest];
                arr[smallest] = arr[j];
                arr[j] = temp;
            }
        }

        // Array sorted using selection sort
        
        for(int i = 0; i < arr.length; i++){
            System.out.print(arr[i]+" ");
        }

        // Selection Sort Case : 2 Ascending Order
        for(int i = 0; i < arr.length-1; i++){
            int smallest = i;
            for(int j = i+1; j < arr.length; j++){
                if(arr[j] > arr[smallest]){
                    j = smallest;
                }
                int temp = arr[j];
                arr[j] = arr[smallest];
                arr[smallest] = temp;
            }
        }

        // Array sorted using selection sort
        System.out.println();
        for(int i = 0; i < arr.length; i++){
            System.out.print(arr[i]+" ");
        }
        
        System.out.println();
        System.out.println("Insertion Sort");
        // Insertion Sort
        for(int i = 1; i<arr.length; i++){
            int current = arr[i]; // for starting from 2nd element of array and now cosider that element as current
            int j = i-1; // j is part of sorted array
            while(j >= 0 && current < arr[j]){
                arr[j+1] = arr[j];
                j--;
            }

            arr[j+1] = current;
        }
        // placement of the element
        for(int i = 0; i < arr.length; i++){
            System.out.print(arr[i]+" ");
        }
    }
}