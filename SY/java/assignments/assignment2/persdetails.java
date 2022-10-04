package assignment2;
import java.util.Scanner;

public class persdetails {

	public static void main(String args[]) {
		Scanner persdet = new Scanner(System.in);

		System.out.println("Enter your name:");
		String name = persdet.nextLine();
		System.out.println("Enter your gender[M/F]:");
		String gender = persdet.nextLine();
		System.out.println("Enter your age:");
		int age = persdet.nextInt();
		System.out.println("Enter your phone number:");
		int phone = persdet.nextInt();
		System.out.println("Enter your CET score:");
		float cetscore = persdet.nextFloat();

		if (age < 25) {
			System.out.println("Student can get 25% discount on Bus pass.");
		} else if (age < 25 && gender == "F") {
			System.out.println("Student can get 30% discount on Bus pass.");
		}

		System.out.println("Name is: " + name);
		System.out.println("Gender is: " + gender);
		System.out.println("Age is: " + age);
		System.out.println("Phone No. is: " + phone);
		System.out.println("CET score is: " + cetscore);

		persdet.close();

	}
}
