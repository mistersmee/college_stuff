public class Assignment8 {
    static class Fruit {
        void eat() {
            System.out.println("Eating fruits...");
        }
    }
    static class Banana extends Fruit {
        void beat() {
            System.out.println("Eating a banana.");
        }
    }
    static class Apple extends Banana {
        void aeat() {
            System.out.println("And also an apple.");
        }
    }
    static class Grapes extends Fruit {
        void geat() {
            System.out.println("And a grape.");
        }
    }

    public static void main(String args[]) {
        // Single inheritance
        Banana fruity = new Banana();
        System.out.println("\nSingle inheritance example:");
        fruity.eat();
        fruity.beat();

        // Multilevel inheritance
        Apple fruity2 = new Apple();
        System.out.println("\n Multilevel inheritance example:");
        fruity2.eat();
        fruity2.beat();
        fruity2.aeat();
        

        // Heirarchical inheritance
        Grapes fruity3 = new Grapes();
        System.out.println("\n Heirarchical inheritance example:");
        fruity3.eat();
        fruity3.geat();
    }
}
