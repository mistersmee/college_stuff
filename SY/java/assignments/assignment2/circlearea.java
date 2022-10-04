package assignment2;
import java.util.Scanner;

public class circlearea {

	public static void carea() {
		Scanner circarea = new Scanner(System.in);

		System.out.println("Enter the radius of circle:");
		float rad = circarea.nextFloat();

		float area = 3.142f * rad * rad;

		System.out.println("The area of circle with radius " + rad + " is: " + area);
		circarea.close();
	}
	public static void main(String args[]) {
		carea();
	}
}
