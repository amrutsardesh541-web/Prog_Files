import java.util.*;

public class bitManipulation {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int n = 5;
        int pos = 1;
        int bitMask = 1<<pos;
        // Get Bit
        if((bitMask & n) == 0){
            System.out.println("bit was zero");
        }
        else{
            System.out.println("bit was one");
        }

        // Set Bit
        int newNumber = bitMask | n;
        System.out.println(newNumber);

        // Clear Bit
        int notbitMask = ~(bitMask);
        int clearedBit = n & notbitMask;
        System.out.println(clearedBit);

        // Update Bit 
        // Case I : for making bit 1
        System.out.print("Would you like to update bit to 1 ot 0 ");
        int bit = sc.nextInt();
        if(bit == 0){
            // Carry out clear operation
            int not = ~(bitMask);
            int newBit = n & not;
            System.out.println(newBit);
        }
        else {
            // Carry out Set operation
            int newbit1 = bitMask | n;
            System.out.println(newbit1);
        }

    }
    
}
