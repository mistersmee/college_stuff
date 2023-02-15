import java.util.Scanner;

public class practical02112022 {
    public static void q1() {

        String str = "My College Name is KIT KIT is in Kolhapur";
        String findstr = "KIT";
        int lastindex = 0;
        int count = 0;

        System.out.println("The length of string str is: " + str.length());

        while (lastindex != -1) {
            lastindex = str.indexOf(findstr, lastindex);

            if (lastindex != -1) {
                count++;
                lastindex += findstr.length();
            }
        }
        System.out.println("The count of substring KIT is: " + count);

        System.out.println("The string str in uppercase is: " + str.toUpperCase());

        System.out.println("The string str in lowercase is: " + str.toLowerCase());
    }

    public static void q2() {
        Scanner inputobj = new Scanner(System.in);

        System.out.println("Enter your first name: ");
        String fname = inputobj.nextLine();

        System.out.println("Enter your last name: ");
        String lname = inputobj.nextLine();

        System.out.println("Enter your gender [M/F]: ");
        String gender = inputobj.nextLine();

        System.out.println(gender);

        if (gender.equals("M")) {
            System.out.println("Your full name is: Mr. " + fname + " " + lname);
        } else {
            System.out.println("Your full name is: Miss " + fname + " " + lname);
        }
        inputobj.close();
    }

    public static void q3() {
        String str1 = "This is Exercise 1";
        String str2 = "This is Exercise 2";

        int equal = str1.compareTo(str2);
        if (equal == 0) {
            System.out.println("The strings are lexicographically equal.");
        } else {
            System.out.println("The strings are not lexicographically equal.");
        }
    }

    public static void q4() {
        String str1 = "This is exercise 1";
        String str2 = "This is Exercise 1";

        int equal = str1.compareToIgnoreCase(str2);
        if (equal == 0) {
            System.out.println("The strings are lexicographically equal.");
        } else {
            System.out.println("The strings are not lexicographically equal.");
        }
    }

    public static void q5() {
        String str = "PHP Exercises and Python Exercises.";
        String substr = "Exercises";
        int exists = str.indexOf(substr);

        if (exists != -1) {
            System.out.println("The substring 'Exercises' exists.");

            int lastindex = 0;
            int count = 0;

            while (lastindex != -1) {
                lastindex = str.indexOf(substr, lastindex);

                if (lastindex != -1) {
                    count++;
                    lastindex += substr.length();
                }
            }
            System.out.println("The count of substring 'Exercises' is: " + count);
        } else {
            System.out.println("The substring 'Exercises' doesn't exist.");
        }

    }

    public static void main(String args[]) {
        q1();
        q2();
        q3();
        q4();
        q5();
    }
}
