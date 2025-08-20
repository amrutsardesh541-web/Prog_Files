import java.util.*;

public class Switches{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        System.out.println("Select your language \n 1 for English \n2. Hindi \n3. French");
        int button = sc.nextInt();
        switch (button) {
            case 1:
                System.out.println("Hello");
                break;
            case 2:
                System.out.println("Namaste");
                break;
            case 3:
                System.out.println("Bonjour");
                break;            
            default:
                System.out.println("Entered invalid choice");
                break;
        }
    }
}