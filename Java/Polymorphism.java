class Automobile {
    String name;
    int wheeldrive;

    // Method to print the name
    public void printInfo(String name) {
        System.out.println(name);
    }

    // Method to print the wheeldrive
    public void printInfo(int wheeldrive) {
        System.out.println(wheeldrive);
    }

    // Method to print both name and wheeldrive
    public void printInfo(String name, int wheeldrive) {
        System.out.println(name + ", " + wheeldrive);
    }
}

public class Polymorphism {
    public static void main(String[] args) {
        Automobile Kia = new Automobile();
        Kia.name = "Seltos";
        Kia.wheeldrive = 4;
        Kia.printInfo(Kia.name, Kia.wheeldrive); 
        Kia.printInfo(Kia.name);
        Kia.printInfo(Kia.wheeldrive);
    }
}
