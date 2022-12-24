import package1.Java.math.Addition;
import package1.Java.math.Subtraction;
import package1.Java.math.Multiplication;
import package1.Java.math.Division;
import package1.Java.math.special.Armstrong;
import package1.Java.math.special.EvenOdd;
import package1.Java.math.special.Factorial;
import package1.Java.math.special.Fibonacci;


import java.util.Scanner;

public class Assignment11 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        char keep_going = 'y';
        while(keep_going == 'y'){
            System.out.println("Choose one option: ");
            System.out.println("\t1. Add two numbers\n\t2. Subtract two numbers\n\t3. Multiply two numbers\n\t" +
                    "4. Divide two numbers\n\t5. Calculate factorial of a number\n\t" +
                    "6. Check if number is even or odd\n\t7. Print Armstrong numbers till a number\n\t" +
                    "8. Print n fibonacci numbers\n\t9. Exit");
            System.out.println("Enter your choice: ");
            int choice = sc.nextInt();
            switch (choice){
                case 1:
                    ad();
                    break;
                case 2:
                    su();
                    break;
                case 3:
                    mu();
                    break;
                case 4:
                    di();
                    break;
                case 5:
                    fa();
                    break;
                case 6:
                    ieoo();
                    break;
                case 7:
                    arm();
                    break;
                case 8:
                    fi();
                    break;
                case 9:
                    keep_going = 'a';
                    break;
            }
        }

    }

    public static void ad(){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter two number to add");
        int a = sc.nextInt();
        int b = sc.nextInt();
        Addition obj = new Addition();
        System.out.println("The addition is: "+obj.add(a,b));
    }
    public static void su(){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter two number to subtract");
        int a = sc.nextInt();
        int b = sc.nextInt();
        Subtraction obj = new Subtraction();
        System.out.println("The subtraction is: "+obj.subt(a,b));
    }
    public static void mu(){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter two number to multiply");
        int a = sc.nextInt();
        int b = sc.nextInt();
        Multiplication obj = new Multiplication();
        System.out.println("The multiplication is: "+obj.mult(a,b));
    }
    public static void di(){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter two number to divide");
        float a = sc.nextFloat();
        float b = sc.nextFloat();
        Division obj = new Division();
        System.out.println("The division is: "+obj.div(a,b));
    }

    public static void fa(){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter number to calculate factorial: ");
        int a = sc.nextInt();
        Factorial obj = new Factorial();
        System.out.println("Factorial is: "+obj.fact(a));
    }

    public static void ieoo(){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter number to check whether Even or Odd: ");
        int a = sc.nextInt();
        EvenOdd obj = new EvenOdd();
        if(obj.isEven(a)){
            System.out.println("The number is even.");
        }else{
            System.out.println("The number is odd.");
        }
    }

    public static void arm(){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a number to print armstrong numbers till: ");
        int a = sc.nextInt();
        Armstrong obj = new Armstrong();
        for(int i=0;i<=a;i++){
            if(obj.isArmstrong(i)){
                System.out.print(i+" ");
            }
        }
        System.out.println();
    }

    public static void fi(){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number of fibonacci terms: ");
        int a = sc.nextInt();
        Fibonacci obj = new Fibonacci();
        for(int i=0;i<a;i++){
            System.out.print(obj.fib(i)+" ");
        }
        System.out.println();
    }
}
