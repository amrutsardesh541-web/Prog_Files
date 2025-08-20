import java.util.*;
public class StringDS {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        /*
        System.out.print("Enter your good name ");
        String name = sc.nextLine();
        System.out.println();
        System.out.println("Hello "+name+" I welcome you to the world of programing");
        */

        // Concatenation
        String first = "Thala";
        String last = "Dhoni";
        String full = first +" "+ last;
        System.out.println(full);

        // Length
        System.out.println(full.length());

        // charAt
        for(int i =0; i < full.length(); i++){
            System.out.print(full.charAt(i)+" ");
        }
        System.out.println();

        // compareTo
        String a = "Hi";
        String b = "Thala Dhoni";
        System.out.println(b.compareTo(last));
        System.out.println(a.compareTo(full));

        // Substrings
        String sentence = "Thala For a reason";
        String name = sentence.substring(12, 18);
        System.out.println(name);

        


    }
}