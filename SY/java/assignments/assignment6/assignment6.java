public class assignment6 {

    public class IntArrayDemo {
        public static void q1() {
            int[] collegecode;
            collegecode = new int[3];

            collegecode[0] = 601;
            collegecode[1] = 602;
            collegecode[2] = 603;

            for (int i = 0; i < collegecode.length; i++) {
                System.out.println("College Code " + i
                                   + " : " + collegecode[i]);
            }
        }
    }

    public class StringArrayDemo {
        public static void q2() {
            String[] colleges;
            colleges = new String[3];

            colleges[0] = "KIT";
            colleges[1] = "DY";
            colleges[2] = "SIT";

            for (int i = 0; i < colleges.length; i++) {
                System.out.println("College " + i
                                   + " : " + colleges[i]);
            }
        }
    }

    public static class Person {
        public int age;
        public String name;

        Person() {
            age = 19;
            name = "smee";
        }

        Person(int age, String name) {
            this.age = age;
            this.name = name;
        }

        public void display() {
            System.out.println("Person age is: " + age + " "
                    + "and Person name is: "
                    + name);
            System.out.println();
        }
    }

    public static void q3() {

        Person James = new Person(21, "James");
        Person Emma = new Person(22, "Emma");
        Person John = new Person(77, "John");

        Person[] arr = new Person[3];

        arr[0] = James;
        arr[1] = Emma;
        arr[2] = John;

        for (int i = 0; i < 3; i++) {
            System.out.println("Person " + i + " data: ");
            arr[i].display();
        }
    }

    public static void main(String args[]) {
        IntArrayDemo.q1();
        StringArrayDemo.q2();
        q3();
    }
}
