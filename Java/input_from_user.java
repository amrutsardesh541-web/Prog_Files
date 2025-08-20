import java.util.*;

public class input_from_user {
    public static void main(String args[]){
    Scanner sc = new Scanner(System.in);
    // Calculate Area of rectangle by taking lenght and breadth from user
    System.out.print("Enter the length of the rectangle : ");
    int l = sc.nextInt();
    System.out.print("Enter the breadth of the rectangle : ");
    int b = sc.nextInt();
    int area = l*b;
    System.out.println("The area of the rectangle is : "+area+" sq.m");
    }
}