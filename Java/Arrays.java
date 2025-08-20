import java.util.*;
public class Arrays {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int[] marks = new int[3];
        marks[0] = 60;
        marks[1] = 63;
        marks[2] = 65;
        /*
        One Way to print array elements
        System.out.println(marks[0]);
        System.out.println(marks[0]);
        System.out.println(marks[0]);
        */
        /* printing array using loops */
        for(int i = 0; i < 3; i++){
            System.out.print(marks[i]+" ");
        }
        System.out.println();
        /*
        int mks[] = {1,5,3,9};
        */
        /*
        System.out.print("Enter size of the array ");
        int size = sc.nextInt();
        int[] nums = new int[size];
        for(int i = 0; i < size; i++){
            nums[i] = sc.nextInt();
        }
        
        for(int j = 0; j < size; j++){
            System.out.print(nums[j]+" ");
        }
        */
        System.out.println();
        System.out.println();
        // Ques : Create an array and apply linear search on it.
        int[] arr = new int[5];
        for(int i = 0; i < arr.length; i++){
            System.out.print("Enter elements at "+i+" ");
            arr[i] = sc.nextInt();
            System.out.println();
        }
        
        System.out.println("Enter the key you would like to search ");
        int key = sc.nextInt();
        for(int i = 0; i < arr.length; i++){
            if(key == arr[i]){
                System.out.println("The key was found at index "+i);
            }
        }
    }
}
