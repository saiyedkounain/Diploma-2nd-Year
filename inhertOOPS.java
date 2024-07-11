
class Shape {
    String name;
    public void displayName(String name){
        this.name = name;
        System.out.println("The shape is: "+this.name);
    }
}
class Triangle extends Shape {
    String name;
    int l;
    int h;

    public void displayArea(int l,int h){

        System.out.println("The lenght is "+this.l+" The height is "+ this.h);
        System.out.println("Area of "+this.name+ " is "+ 0.5*l*h);
    }
    Triangle(String name,int l, int h){
        this.name = name;
        this.l = l;
        this.h = h;
    }

}
class Square extends Shape {
    int side;
    public void displayArea(String name,int size){
        System.out.println("The area of shape "+this.name+" is "+ side*side);

    }
    Square (String name,int side){
        this.name = name;
        this.side = side;

    }

}
class Circle extends Shape {
    String name;
    int r;
    Circle(String name, int r){
        this.name = name;
        this.r = r;
    }
    public void displayArea(String name, int r){
        System.out.println("The radius of shape "+this.name+" is "+ (3.14)*r*r);
    }
}
class Student {
    String name;j
    static String college;
    public void displayInfo(String name, String college){
        System.out.println(name+" studies at "+ college);
    }
    Student(String name, String college){
        this.name =name;
        this.college = college;
    }
}
public class inhertOOPS {
    public static void main(String[] args) {
        Triangle tri = new Triangle("Triangle",10,5);
        tri.displayArea(tri.l, tri.h);
        
        Square sk = new Square("Square",7);
        sk.displayArea(sk.name,sk.side);

        Circle cs = new Circle("Circle",7);
        cs.displayArea(cs.name,cs.r);
        Student rs = new Student("Saiyed K", "CPC Polytecnic");
        rs.displayInfo(rs.name,rs.college);
}
    
}