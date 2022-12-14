import java.util.Scanner;

public class Assignment9 {
    class Person {
        int Id;
        String Name;
    }
    
    class Employee extends Person{
        String Post;
        int Salary;
        int ManagerID;
        boolean IsManager;
    }
    
    class Manager extends Employee{
        String Department;
    }

    public void main(String args[]) {
        Scanner sc = new Scanner(System.in);

        char keepgoing = 'y';
        int i, j = 0;

        System.out.println("HR Management system:");
        System.out.println("Choose what you want to do:");
        System.out.println("\t1.Create Manager\n\t2.Create Employee\n\t3.Display\n\t4. Exit");
        
        while (keepgoing == 'y') {
            System.out.println("Enter your choice:");
            int choice = sc.nextInt();
            switch(choice) {
                case 1:
                    
            }
        }
    }
}
