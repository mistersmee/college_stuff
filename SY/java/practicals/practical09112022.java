public class practical09112022 {
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

    public static void main(String args[]) {

        Person[] arr = new Person[3];

        arr[0] = new Person(21, "James");
        arr[1] = new Person(22, "Emma");
        arr[2] = new Person(77, "John");

        for (int i = 0; i < 3; i++) {
            System.out.println("Person " + i + " data: ");
            arr[i].display();
        }
    }
}
