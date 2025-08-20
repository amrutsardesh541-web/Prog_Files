import bank.Bank;

public class Access_package {
    public static void main(String[] args) {
        Account acc = new Account();
        acc.name = "Raj";
        //acc.IFSC = 67890;  // This is allowed because IFSC is protected
        acc.setBalance(500);  // Use setter to modify the private balance

        acc.bankInfo();
        System.out.println("Balance: " + acc.getBalance());
    }
}
