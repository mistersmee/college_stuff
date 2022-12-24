interface TwoWheel {
	int wheels = 2;
}


interface FourWheel {
	int wheels = 4;
}


abstract class Vehicle {
	abstract int noOfWheels();
	abstract int CubicCapacity();
}


class Bike extends Vehicle implements TwoWheel{
	public int noOfWheels() {
		int wheels = 4;
	}
	public int CubicCapacity() {

	}
}


class Car extends Vehicle implements FourWheel{

}
