public class practical24092022 {
	public static void main (String[] args) {
		helloworld();
		addition();
		printest();
		datatypes();
	}
	public static void helloworld() {
		System.out.println("Hello World!");
	}
	public static void printest() {
		System.out.println("This is a test.");
		System.out.print("This is also a test.");
		System.out.println("This is more of a test.");
	}
	public static void addition() {
		int a = 2;
		int b = 3;
		int c = a + b;
		System.out.println("The addition of " + a + " and " + b + " is: " + c);
	}
	public static void datatypes() {
		int num = 5;
		float floatnum = 5.9423f;
		double doublenum = 5.9423d;
		char letter = 'D';
		String sentence = "Aseem";
		boolean trueorfalse = true;
		System.out.println(num);
		System.out.println(floatnum);
		System.out.println(doublenum);
		System.out.println(letter);
		System.out.println(sentence);
		System.out.println(trueorfalse);
	}
}
