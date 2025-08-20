import java.util.*;

public class Conditions {
    public static void main(String args[]){
        // conditionals in Java
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number you want to check ");
        int n = sc.nextInt();
        if (n==0) {
            System.out.println("Number is zero");
        }
        else if(n%2!=0){
            System.out.println("Number is odd");
        }
        else{
            System.out.println("Number is even");
        }
        sc.close();
    }
}