public class practical28092022 {
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
	public static void main (String args[]) {
		int i = 9, j = 3;
		practical28092022 calc = new practical28092022();
		calc.Addition(i, j);
		calc.Subtraction(i, j);
		calc.Multiplication(i, j);
		int divresult = calc.Division(i, j);
		System.out.println("The division of " + i + " and " + j + " is: " + divresult);
	}               
}
