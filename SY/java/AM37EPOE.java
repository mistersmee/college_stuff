import java.util.Scanner;

class parentArea {
	int base;
	int height;
	double area;
	
	public void getInput() {
		Scanner sc = new Scanner(System.in);
	
		System.out.println("Enter the length of triangle base (in cm):");
		this.base = sc.nextInt();
		
		System.out.println("Enter the length of triangle height (in cm):");
		this.height = sc.nextInt();
		
		sc.close();
	}
	
	public void display() {
		System.out.println("Program to calculate area of triangle:");
	}
}

class areaTriangle extends parentArea {
	public void triarea() {
		area = 0.5 * base * height;
		System.out.println("The area of triangle with base " + base + " and height " + height + " is: " + area +  " cm²");
	}
}

public class AM37EPOE {
	public static void main (String args[]) {
			areaTriangle tri = new areaTriangle();
			
			tri.display();
			tri.getInput();
			tri.triarea();
	}
}