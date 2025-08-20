package bank;

class Account {
    public String name;
    protected int IFSC;
    private int balance;

    public void bankInfo() {
        System.out.println(this.name);
        System.out.println(this.IFSC);
    }

    // Getter and Setter for balance
    public int getBalance() {
        return balance;
    }

    public void setBalance(int balance) {
        this.balance = balance;
    }
}

public class Bank {
    Account acc = new Account();

    public void setupAccount() {
        acc.name = "Sanjay";
        acc.IFSC = 12345;  // Setting a default value for IFSC
        acc.setBalance(1000);  // Setting a default balance
    }

    public void printAccountInfo() {
        acc.bankInfo();
    }
}
