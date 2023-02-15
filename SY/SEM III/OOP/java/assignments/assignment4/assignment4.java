/*
 *  Q1:
 *
 *   The output of Question 1 is:
 *        Hello I am null
 *        My age is: 0
 *
*/

/*
 *  Q2:
 *
 *    Because we have assigned default values to the Person class and thereby its attributes,
 *    the values for all of its objects will be the default values, if we do not assign new values.
 *    So, even if the object is named Emma, the value of name and age will still be James and 23.
 *
*/

/*
 *  Q3:
 *
 *    Now, since we have allowed changing the attributes' using parameters, we can change the values,
 *    while still keeping the default, for when we don't want to change them. We can change the parameters
 *    by passing the changes as arguments to the object declaration statement.
 *
 */

/*
 *  Q4:
 *
 *     The output of the question 4 is:
 *          Object hashcode is: 1995265320
 *          The amount of cars the customer has is: 0
 *          The model year of the car is: 0
 *          The revision of the car is: 0
 *          The serial number of the car is: 0
 *          The length of the car is: 0.0
 *          The model of the car is:
 *          The name of the car is: null
 *
*/

public class assignment4 {
    public class Person {
        String name;
        int age;
        Person() {
            name = "James";
            age = 23;
        }

    public void talk() {
        System.out.println("Hello I am " + name);
        System.out.println("My age is: " + age);
        }
    }

    public class DemoPerson {
        public static void main(String args[]) {
        	Person James = new Person();
        	James.talk();

            Person Emma = new Person();
            Emma.talk();
        }
    }

    public class Car {
        byte customercarnumber;
        short modelyear;
        int carrevision;
        long carserialno;
        float carlength;
        char carmodel;
        String carname;

        public void showCarDetails() {
            System.out.println("The amount of cars the customer has is: " + customercarnumber);
            System.out.println("The model year of the car is: " + modelyear);
            System.out.println("The revision of the car is: " + carrevision);
            System.out.println("The serial number of the car is: " + carserialno);
            System.out.println("The length of the car is: " + carlength);
            System.out.println("The model of the car is: " + carmodel);
            System.out.println("The name of the car is: " + carname);
        }

        public static void main(String args[]) {
            Car Maruti = new Car();
            System.out.println("Object hashcode is: " + Maruti.hashCode() );
            Maruti.showCarDetails();
        }
    }
}
