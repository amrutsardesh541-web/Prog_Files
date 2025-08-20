public class backtracking {
/*    
    public static void printperm(String str, String perm, int idx){
        if(str.length()==0){
            System.out.println(perm);
            return;
        }
        for(int i = 0; i < str.length(); i++){
            char currchar = str.charAt(i);
            String newstr = str.substring(0, i) + str.substring(i+1);
            printperm(newstr, perm+currchar, idx+1);
        }
    
    public static void main(String[] args){
        String permutation = "";
        String name = "abc";
        printperm(name, permutation, 0);
    }
*/
    public static void printperm(String str, String perm, int idx){
        if (str.length() == 0){
            System.out.println(perm);
        }
        for(int i = 0; i < str.length(); i++){
            char currChar = str.charAt(i);
            String newstr = str.substring(0, i) + str.substring(i+1);
            printperm(newstr, perm+currChar, idx+1);
        }
    }

    public static void main(String[] args){
        String name = "riya";
        String permutation = "";
        printperm(name, permutation, 0);
    }
}