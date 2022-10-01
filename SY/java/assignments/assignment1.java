import java.util.Scanner;

public class assignment1 {

	void Addition (int a, int b) {
		int c = a + b;
		System.out.println("The addition of " + a + " and " + b + " is: " + c);
	}

	void Subtraction (int a, int b) {
		int c = a - b;
		System.out.println("The subtraction of " + a + " and " + b + " is: " + c);
	}

	void Multiplication (int a, int b) {
		int c = a * b;
		System.out.println("The multiplication of " + a + " and " + b + " is: " + c);
	}
	int Division (int a, int b) {
		int c = a / b;
		return c;
	}

	public static void q1a() {
		System.out.println("Hello World!");
	}

	public static void q2() {
		String name  = "smee";
		String dept = "AIML";
		char division = 'C';
		int rollno = 37;
    int prn = 2122000421;
		float cgpi = 8.68f;

	  System.out.println("Name is: " + name);
    System.out.println("Department is: " + dept);
    System.out.println("Division is: " + division);
    System.out.println("Roll No. is: " + rollno);
    System.out.println("PRN is: " + prn);
    System.out.println("CGPI is: " + cgpi);
  }

  public static void q3 () {
		int i = 9, j = 3;
		assignment1 calc = new assignment1();
		calc.Addition(i, j);
		calc.Subtraction(i, j);
		calc.Multiplication(i, j);
		int divresult = calc.Division(i, j);
		System.out.println("The division of " + i + " and " + j + " is: " + divresult);
	}

  public static void q4() {

    Scanner myObj = new Scanner(System.in);

    System.out.println("Enter Name:");
    String name = myObj.nextLine();
    System.out.println("Enter Department:");
    String dept = myObj.nextLine();
    System.out.println("Enter Division:");
    String divisn = myObj.nextLine();
    System.out.println("Enter Roll No:");
    int rollno = myObj.nextInt();
    System.out.println("Enter PRN:");
    int prn = myObj.nextInt();
    System.out.println("Enter CGPI:");
    float cgpi = myObj.nextFloat();

    System.out.println("Name is: " + name);
    System.out.println("Department is: " + dept);
    System.out.println("Division is: " + divisn);
    System.out.println("Roll No. is: " + rollno);
    System.out.println("PRN is: " + prn);
    System.out.println("CGPI is: " + cgpi);

    myObj.close();
  }

  public static void main(String args[]) {
    q1a();
    q2();
    q3();
    q4();
  }
}
