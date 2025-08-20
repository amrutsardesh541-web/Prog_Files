public class MergeSort {
    public static void conquer(int arr[], int start, int mid, int end){
        int merged[] = new int[end - start + 1];
        int idx1 = start; // start of first divide array
        int idx2 = mid+1; // start of second divided array
        int x = 0;
        while(idx1 <= mid && idx2 <= end){
            if(arr[idx1] <= arr[idx2]){
                merged[x] = arr[idx1];
                x++;
                idx1++;
            }
            else{
                merged[x] = arr[idx2];
                x++;
                idx2++;
            }
        }

        while(idx1 <= mid){
            merged[x] = arr[idx1];
            x++;
            idx1++;
        }

        while(idx2 <= mid+1){
           merged[x] = arr[idx2];
           x++;
           idx2++; 
        }

        for(int i = 0, j = start; i<merged.length; i++, j++){
            arr[j] = merged[i];
        }

    }

    
    public static void mergeSort(int arr[], int start, int end){
        if (start >= end){
            return;
        }
        int mid = start + (end - start)/2;
        mergeSort(arr, start, mid);
        mergeSort(arr, mid+1, end);
        conquer(arr, start, mid, end);
    }

    public static void main(String args[]){
        int arr[] = {5,8,10,68,30,41,49,53,2,25,24,9,4,50,54,62,6,48,42,12,17,60,65,54,45,29,57,21,69,33,44,30,32};
        int size = arr.length;
        int start = 0;
        int end = size-1;
        //int mid = start + (end - start)/2;
        mergeSort(arr, start, end);

        // print sorted array
        for(int i = 0; i<arr.length; i++){
            System.out.print(arr[i]+" ");
        }
    }
    
}