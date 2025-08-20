import java.util.*;

public class Functions{
    static void add(int n, int m){
        int sum = n+m;
        System.out.println(sum);
    }
    static void mul(int c, int d){
        int pro = c*d;
        System.out.println(pro);
    }
    static void fact(int num){
        int fact = 1;
        if(num == 1 || num == 0){
            System.out.println(fact);
        }
        else if(num < 0){
            System.out.println("Invalid Choice");
        }
        else{
            for (int i = 1; i < num+1; i++){
                fact *= i;
            }
            System.out.println(fact);
        }
    }
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        add(5,6);
        mul(10,100);
        fact(-1);
    }
}