import java.util.Scanner;
import java.lang.Math.*;

public class AlternateAssignment2Demo {
    public static void main(String args[]){
        AreaTriangle tri = new AreaTriangle();
        AreaCircle cir = new AreaCircle();

        tri.Triangle();
        cir.Circle();

    }

}

class AreaTriangle {
     void Triangle(){
        Scanner myObj = new Scanner(System.in);

        System.out.println("Enter the base of the triangle: ");
        float b = myObj.nextFloat();

        System.out.println("Enter the height of the triange: ");
        float h = myObj.nextFloat();

        float area = (float)1/2*(b*h);

        System.out.println("The area of triangle is: "+ area);
        myObj.close();
     }
}

class AreaCircle{
    void Circle(){
        Scanner myObj = new Scanner(System.in);

        System.out.println("Enter the radius of circle: ");
        float r = myObj.nextFloat();

        float area = r*r*(float)Math.PI;

        System.out.println("The area is: " + area);
        myObj.close();
    }
}
