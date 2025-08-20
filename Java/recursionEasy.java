public class recursionEasy {
    // Print n numbers till 1
    public static void printNum(int n){
        if(n==0){
            System.out.println("Bismillah");
            return;
        }
        System.out.println(n);
        printNum(n-1);
    }

    // Print n numbers from 1
    public static void printNumb(int lb, int ub){
        
        if(lb > ub){
            System.out.println("Liftoff");
            return;
        }
        System.out.println(lb);
        printNumb(lb+1,ub);
    }

    // Print sum of first n natural numbers
    public static void printSum(int lb, int ub, int sum){
        if(lb == ub){
            sum += lb;
            System.out.println(sum);
            return;
        }
        sum += lb;
        printSum(lb+1, ub, sum);
        
    }

    // Print Factorial of a number n
    public static int printFact(int n){
        if(n == 1 || n== 0){
            return 1;
        }
        else {
            return (n*printFact(n-1));
        }
    }


    // Tower of Hanoi : 3 tower side by side ___src___help___dest___
    public static void towerOfHanoi(int disk, String src, String helper, String dest){
        if(disk == 1){
            System.out.println("Transfer disk "+disk+" from "+src+" to "+dest);
            return;
        }
        // transfer n-1 disk from src to helper(here as a dest) using dest(here as a helper)
        towerOfHanoi(disk - 1, src, dest, helper);
        // 1st disk transfered from source to destination
        System.out.println("Transfer disk "+disk+" from "+src+" to "+dest);
        // Transfer n-1 disk from helper(here source) to dest using src(here helper)
        towerOfHanoi(disk-1, helper, src, dest);
    }

    // Reverse the string
    public static void reverse(String str, int idx){
        if(idx == 0){
            System.out.println(str.charAt(idx));
            return;
        }
        System.out.println(str.charAt(idx));
        reverse(str, idx-1);
    }

    // Find the first and last occurence of an element in the string
    

    public static void main(String args[]){
        //printNum(10);
        //printNumb(1,10);
        //printSum(1,10,0);
        //printFact(5);
        //towerOfHanoi(3, "S tower", "H tower", "D tower");
        reverse("abcd", 3);

    }
}
