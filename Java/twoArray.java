import java.util.*;

import javax.sound.midi.Soundbank;
public class twoArray {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int mat[][] = new int[3][2];
        // Take input from user 
        for(int i = 0; i < 3; i++){
            for(int j = 0; j < 2; j++){
                System.out.print("Enter element at"+i+" th row and "+j+" th column ");
                mat[i][j] = sc.nextInt();
                System.out.println();
            }
        }

        // Display the matrix 
        for(int i = 0; i < 3; i++){
            System.out.print("[ ");
            for(int j = 0; j < 2; j++){
                System.out.print(mat[i][j]+" ");
            }
            System.out.println("]");
        }

        // Apply liner search on the matrix by taking key from the user
        System.out.println("Enter the key ");
        int key = sc.nextInt();
        for(int i = 0; i < 3; i++){
            for(int j = 0; j < 2; j++){
                if(key == mat[i][j]){
                    System.out.println("ELement found at "+i+" th row and "+j+" th column");

                }
            }
            }
            
        }

    }

