public class numberConversion {
    static void decimalTobinary(int num){
        int binaryNum[] = new int[100];
        int i = 0;
        while (num > 0) {
            binaryNum[i] = num%2;
            num /= 2;
            i++;
        }

        for(int j = i-1; j >=0; j--){
            System.out.print(binaryNum[j]+", ");
        }
        
    }
    public static void main(String args[]){
        decimalTobinary(7);
    }
}