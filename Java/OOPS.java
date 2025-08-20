import bank.Account;

class Pen {
    // Blueprint of pen
    String Color;
    String type; // ball point pen or gel pen
    
    public void write(){
        System.out.println("A pen which is "+Color+" and of type "+type+" is writing.");
    }

    public void printColor(){
        System.out.println(this.Color);
    }
}

class Student {
    String name;
    int age;

    public void printInfo(){
        System.out.println(this.name);
        System.out.println(this.age);
    }

    // Non Parameterised Constructor
    Student(){
        System.out.println("Constructor called");

    }

    // Parameterised Constructor
    Student(String name, int age){
        System.out.println("Constructor called");
        this.name = name;
        this.age = age;
    }        

    // copy constructor
    Student(Student s3){
        this.name = s3.name;
        this.age = s3.age;
    }
}




public class OOPS{
    public static void main(String[] args){
        // Creating object
        /*
        Pen pen1 = new Pen();
        pen1.Color = "blue";
        pen1.type = "gel";

        pen1.write();

        Pen Rorito = new Pen();
        Rorito.Color = "black";

        Rorito.printColor();
        pen1.printColor();
        */
        /*
        Student s1 = new Student(); // Constructor
        s1.name = "Anant";
        s1.age = 24;
        s1.printInfo();
        */
        /*
        Student s1 = new Student();
        s1.name = "Rakesh";
        s1.age = 24;
        s1.printInfo();

        Student s2 = new Student("Suresh", 24);
        s2.printInfo();

        Student s3 = new Student(s2);
        s3.printInfo();
        */

        Account acc = new Account();
        acc.name = "Vijendra Singh Shekhawat";
        

    }
}