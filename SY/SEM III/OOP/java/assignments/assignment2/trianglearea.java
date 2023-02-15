package assignment2;
import java.util.Scanner;

public class trianglearea {

	public static void tarea() {
		Scanner triarea = new Scanner(System.in);

		System.out.println("Enter the base of triangle:");
		float base = triarea.nextFloat();
		System.out.println("Enter the height of triangle:");
		float height = triarea.nextFloat();

		float area = 0.5f * base * height;

		System.out.println("The area of triangle with base " + base + " and height " + height + " is: " + area);

		triarea.close();
	}
	public static void main(String args[]) {
		tarea();
	}
}
