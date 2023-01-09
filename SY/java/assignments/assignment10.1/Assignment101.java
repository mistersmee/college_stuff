import java.util.Scanner;
interface TwoWheel {
	int wheels = 2;
}


interface FourWheel {
	int wheels = 4;
}


abstract class Vehicle {
	abstract int noOfWheels();
	abstract void CubicCapacity();
	abstract int DispCC();
}


class Bike extends Vehicle implements TwoWheel{
	int cc;
	int wheels = 2;

	public int noOfWheels() {
		return this.wheels;
	}

	public void CubicCapacity() {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the cc of vehicle:");
		this.cc = sc.nextInt();
	}
	public int DispCC() {
		return this.cc;
	}
}


class Car extends Vehicle implements FourWheel{
	int cc;
	int wheels = 4;

	public int noOfWheels() {
		return this.wheels;
	}

	public void CubicCapacity() {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the cc of vehicle:");
		this.cc = sc.nextInt();
	}
	public int DispCC() {
		return this.cc;
	}
}

public class Assignment101 {
	public static void main(String args[]) {
		Bike b[] = new Bike[10];
		Car ca[] = new Car[10];
		Scanner s = new Scanner(System.in);
		int c = 0;
		System.out.println("Options: \n\t1.Create Bike\n\t2.Create Car\n\t3.Display all Bikes\n\t4. Display all cars\n\t5. Exit");
		while(true) {
			System.out.println("Enter your choice:");
			int choice = s.nextInt();
			switch(choice) {
				case 1:
					Bike bobj = new Bike();
					b[c] = bobj;
					bobj.CubicCapacity();
					c++;
					break;
				case 2:
					Car cobj = new Car();
					ca[c] = cobj;
					cobj.CubicCapacity();
					c++;
					break;
				case 3:
					System.out.println("The bikes are:");
					for (int i = 0; i < c; i++) {
							System.out.println("Bike no. " + c);
							System.out.println("No. of wheels: " + b[c].noOfWheels());
							System.out.println("Cubic capacity: " + b[c].DispCC());
					}
					break;
				case 4:
					System.out.println("The cars are:");
					for (int i = 0; i < c; i++) {
						System.out.println("Car no. " + c);
						System.out.println("No. of wheels: " + ca[c].noOfWheels());
						System.out.println("Cubic capacity: " + ca[c].DispCC());
					}
					break;
				case 5:
					break;
				default:
					System.out.println("Invalid choice.");
			}
		}
	}
}
