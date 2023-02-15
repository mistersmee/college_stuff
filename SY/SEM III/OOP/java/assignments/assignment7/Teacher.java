public class Teacher{
	//instance variables
	int id;
	String name;
	String department;
	float sal;

	//setter method to store id
	void setID(int id){
		this.id=id;
	}
	//getter method to retrieve id
	int getId(){
		return id;
	}

	void setName (String name) {
		this.name = name;
	}

	String getName() {
		return name;
	}

	void setDept (String dept) {
		this.department = dept;
	}

	String getDept() {
		return department;
	}

	void setSal (float sal) {
		this.sal = sal;
	}

	float getSal() {
		return sal;
	}

	public static void main(String args[]){
		// create object to store Teacher Information
		Teacher t = new Teacher();

		// Store data into objects using setter method
		t.setID(107);

		t.setName("Smee");
		t.setDept("AIML");
		t.setSal(99999999.9f);

		// retrieve data using getter methods and display
		System.out.println("ID= "+t.getId());
		System.out.println("Name= "+t.getName());
		System.out.println("Dept= "+t.getDept());
		System.out.println("Salary= "+t.getSal());
	}
}
