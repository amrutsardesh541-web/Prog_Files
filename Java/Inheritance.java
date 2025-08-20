class Shape {
    public void area(){
        System.out.println("display area");
    }
}

class Triangle extends Shape {
    public void area(int l, int h){
        System.out.println(0.5*l*h);
    }
}

class EquilateralTriangle extends Triangle{
    public void area(int l, int h){
      System.out.println(0.5*l*h);
    }
}

class Circle extends Shape{
    public void area(int r){
        System.out.println(3.142*r*r);
    }
}

public class Inheritance {
    public static void main(String[] args){
        
     EquilateralTriangle e1 = new EquilateralTriangle();
     e1.area(4,3);

     Circle c1 = new Circle();
     c1.area(4);
}
}