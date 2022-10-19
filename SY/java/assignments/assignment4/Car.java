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

/*
 *  Q4:
 *
 *     The output of the question 4 is:
 *		    Object hashcode is: 1995265320
 *		    The amount of cars the customer has is: 0
 *			The model year of the car is: 0
 *			The revision of the car is: 0
 *			The serial number of the car is: 0
 *			The length of the car is: 0.0
 *			The model of the car is:
 *			The name of the car is: null
 *
*/