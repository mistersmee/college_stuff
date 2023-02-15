public class Person {
    String name;
    int age;
    Person() {
        name = "James";
        age = 23;
    }
    Person(String s, int i) {
        name = s;
        age = i;
    }

    public void talk() {
        System.out.println("Hello I am " + name);
        System.out.println("My age is: " + age);
    }

    public static void main(String args[]) {
        	Person James = new Person();
        	James.talk();

            Person Emma = new Person("Emma", 25);
            Emma.talk();
    }
}

/*  Q1:
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
