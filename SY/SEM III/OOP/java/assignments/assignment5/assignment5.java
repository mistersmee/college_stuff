import java.util.Scanner;

public class assignment5 {

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

    public static void q6() {
        String str = "Reverse words in a given string", revstr = "";
        char ch;

        System.out.println("The original string is: " + str);
        for (int i = 0; i < str.length(); i++) {
            ch = str.charAt(i);
            revstr = ch + revstr;
        }
        System.out.println("The reversed string is: " + revstr);
    }

    public static void q7() {
        String str = "The given string is: abrambabasc";
        String strnew = str.replace("b", "");
        strnew = strnew.replace("ac", "");

        System.out.println("The original string is: " + str);
        System.out.println("After removing `b` and `ac`,  the string becomes: " + strnew);
    }

    public static void q8() {
        String string1 = "w3resource";
        int count;

        char string[] = string1.toCharArray();


        System.out.println("The string is: " + string1);
        System.out.println("Duplicate characters in a given string: ");

        for(int i = 0; i < string.length; i++) {
            count = 1;
            for(int j = i + 1; j < string.length; j++) {
                if(string[i] == string[j] && string[i] != ' ') {
                    count++;
                    string[j] = '0';
                }
            }
            if (count > 1 && string[i] != '0') {
                System.out.println("Number of times duplicate character `" + string[i] + "` occurred: " + count);
            }
        }
    }

    public static void q9 () {
       String str = "bbthhfccuukkllrr";
       StringBuilder strnew = new StringBuilder();
        for (int i = 0; i < str.length(); i++) {
            if (str.indexOf(str.charAt(i), str.indexOf(str.charAt(i)) + 1) == -1) {
                strnew.append(str.charAt(i));
            }
        }
        System.out.println("The original string is: " + str);
        System.out.println("The string after removing all instances of duplicate characters becomes: " + strnew);
    }

    public static void q10() {
        String str = "Hello this is a book on java.";
        String[] arrOfStr = str.split(" ");
        for (String a : arrOfStr) {
            System.out.println(a);
        }
    }

    public static void main(String args[]) {
        q1();
        q2();
        q3();
        q4();
        q5();
        q6();
        q7();
        q8();
        q9();
        q10();
    }
}
