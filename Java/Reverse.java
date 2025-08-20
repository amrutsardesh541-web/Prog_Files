import java.util.*;

public class Reverse {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number you wish to reverse ");   
        int num = sc.nextInt();
        int reverse = 0;
        while(num>0){
            int last = num%10;
            
            reverse = reverse*10+last;
            num /= 10;
        }     
        System.out.println("Reversed digit is "+reverse);
    
    }
    
}