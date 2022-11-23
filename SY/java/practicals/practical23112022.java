// Java program to demonstrate that
// In both static and non-static methods,
// static methods are directly accessed.

import java.io.*;

public class practical23112022 {

    static int num = 100;
	static int salary = 50000;
    static String str = "GeeksForGeeks";

    // This is Static method
    static void display()
    {
        System.out.println("static number is " + num);
        System.out.println("static string is " + str);
    }

    // non-static method
    void nonstatic() {
    // our static method can accessed 
    // in non static method
        System.out.println("I am in non-static method");
		display();
		System.out.println("End of non-static method");
    }

	void GetSalary() {
		System.out.println("Salary is " + salary);
	}
    // main method
    public static void main(String args[]) {
        hello obj = new hello();

        // This is object to call non static function
        //obj.nonstatic();

        // static method can called 
        // directly without an object
        //display();
		hello James = new hello();
        hello Emma = new hello();

        ++salary;

        James.GetSalary();
        Emma.GetSalary();
    }
}
