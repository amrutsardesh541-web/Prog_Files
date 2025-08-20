import java.util.*;

public class loops{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        // for loops
        for(int i =1; i < 6; i++){
            System.out.print(i+" ");
            System.out.println(" ");
        }
        // while loops
        int j = 6;
        while(j < 11){
            System.out.print(j+" ");
            j++;
            System.out.println(" ");
            //System.out.println(" ");
        }

        // do-while loops
        int k = 11;
        do{
            System.out.println(k+" ");
            k++;
        }while(k<16);
    }
}