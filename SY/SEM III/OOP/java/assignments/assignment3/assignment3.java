import java.util.Scanner;

public class assignment3 {
	public static void posneg() {
		Scanner inputnum = new Scanner(System.in);

		System.out.println("Enter a number:");
		int num = inputnum.nextInt();

		if (num > 0) {
			System.out.println("The number is positive.");
		} else if (num < 0) {
			System.out.println("The number is negative.");
		} else {
			System.out.println("The number is zero.");
		}
		inputnum.close();
	}

	public static void dowhilenum() {
		int i = 1;

		do {
			System.out.println(i);
			i++;
		} while (i <= 10);
		System.out.println();
	}

	public static void whilenum() {
		int i = 3;

		while (i <= 8) {
			System.out.println(i);
			i++;
		}
		System.out.println();
	}

	public static void whilenum2() {
		int i = 2;

		while (i <= 9) {
			System.out.println(i);
			i++;
		}
		System.out.println();
	}

	public static void numprint() {
		int i = 1, max = 5;
		int temp = max;

		while (i <= max) {
			System.out.println(i + " " + temp--);
			i++;
		}
		System.out.println();
	}

//	public class NestedForDemo {
	public static void NestedForDemo() {
		// add code to complete this class
		int i = 1, j = 1;
		for (i = 1; i <= 3; i++) {
				System.out.println("i"); // how many times this line will be executed?
			for (j = 1; j <= 4; j++) {
				System.out.println("j"); // how many times this line will be executed?
			}
		}
		System.out.println("The first print statement in the outer loop will be executed 3 times.");
		System.out.println("The second print statement in the inner loop will be executed 4 x 3 = 12 times.");
	}

	public static void starprint() {
		int i, j;
		for(i = 0; i< 4; i++) {
			System.out.print(" ");
			for(j = 0; j <= i; j++) {
				System.out.print("* ");
			}
			System.out.println();
		}
	}

	public static void leapyear() {
		Scanner inputnum2 = new Scanner(System.in);

		System.out.println("Enter a year:");
		int year = inputnum2.nextInt();
		if (year % 4 == 0) {
			if (year % 100 == 0) {
				if (year % 400 == 0) {
						System.out.println(year + " is a leap year.");
				} else {
						System.out.println(year + " is not a leap year.");
				}
			} else {
					System.out.println(year + " is a leap year.");
			}
		} else {
				System.out.println(year + " is not a leap year.");
		}
		inputnum2.close();
	}

	public static int fibbonacci(int n) {
		if (n == 0) {
			return 0;
		} else if (n == 1) {
				return 1;
		} else {
			return (fibbonacci(n-1) + fibbonacci(n-2));
		}
	}

	public static void fibnum() {
		Scanner inputnum3 = new Scanner(System.in);

		int i;

		System.out.println("Enter the number of fibonacci terms: ");
		int n = inputnum3.nextInt();

		System.out.println("Fibbonacci of " + n + ": ");

		for(i = 0; i <= n; i++) {
			System.out.print(" " + fibbonacci(i));
		}
		inputnum3.close();
	}

	public static void switchnum() {
		Scanner inputnum4 = new Scanner(System.in);

		System.out.println("Enter a number:");
		int num = inputnum4.nextInt();

		switch (num) {
			case 1:
				System.out.println("One.");
				break;
			case 2:
				System.out.println("Two.");
				break;
			case 3:
				System.out.println("Three.");
				break;
			case 4:
				System.out.println("Four.");
				break;
			case 5:
				System.out.println("Five.");
				break;
			default:
				System.out.println("Number not in range, please enter numbers between 1 to 5 only.");
		}
		inputnum4.close();
	}

	public static void main(String args[]) {
		posneg();
		dowhilenum();
		whilenum();
		whilenum2();
		numprint();
		NestedForDemo();
		starprint();
		leapyear();
		fibnum();
		switchnum();
	}
}
