import java.util.*;
public class Pattern{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        /* 
        // Solid rectangle or square
        System.out.print("Enter rows ");
        int row = sc.nextInt();
        System.out.print("Enter columns ");
        int col = sc.nextInt();
        for(int i = 0; i < row; i++){
            for(int j = 0; j < col; j++){
                System.out.print("* ");
            }
            System.out.print("\n");
        }

        // Hollow rectangle or square 
        for(int i = 0; i < row; i++){
            for(int j = 0; j < col; j++){
                if(i==0 || i==row-1 || j==0 || j==col-1){
                    System.out.print(" * ");
                }
                else{
                    System.out.print("   ");
                }
            }
            System.out.println();
        }
        */

        // Half Pyramid
        System.out.print("Enter no of rows ");
        int r = sc.nextInt();
        for(int i = 1; i <= r; i++){
            for(int j = 1; j <= i; j++){
            System.out.print("*");
            }
        System.out.println();
        }

        // Inverted half pyramid
        for(int i = r; i >= 1; i--){
            for(int j = 1; j <= i ; j++){
                System.out.print("*");
            }
            System.out.println();
        }
        
    }
}