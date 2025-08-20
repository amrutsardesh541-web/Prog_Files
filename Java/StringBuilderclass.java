public class StringBuilderclass{
    public static void main(String args[]){
        StringBuilder sb = new StringBuilder("Last");
        System.out.println(sb);
        // Print char at idx 0
        System.out.println(sb.charAt(0));
        // Set new char at idx 0
        sb.setCharAt(0, 'F');
        System.out.println(sb);
        // Insert Character at idx -1
        sb.insert(1, 'a');
        System.out.println(sb);
        // Delete any character or substing from string
        sb.delete(1,2);
        System.out.println(sb);
        // Append to the string
        sb.append('e');
        sb.append('r');
        System.out.println(sb);

        // Reverse the string
        StringBuilder sb1 = new StringBuilder("Hello");
        for(int i = 0; i < sb1.length()/2; i++){
            int first = i;
            int last = sb1.length()-1-i;
            char frontChar = sb1.charAt(first);
            char backChar = sb1.charAt(last);
            sb1.setCharAt(first, backChar);
            sb1.setCharAt(last, frontChar);
                        
        }
        System.out.println(sb1);
    }
}