public class Use{
	public static void main(String args[]){
		//create object of Student
	//	Student s = new Student();
	//	s.setId(12);
	//	s.setName("Smee");
	//	s.setMarks(100);
		Studentv2 s2 = new Studentv2();
		s2.setId(15);
		s2.setName("Smee");
		s2.setMarks(1000);
		//retrieve data using getter methods and display
		System.out.println("Id ="+s2.getId());
		System.out.println("Name ="+s2.getName());
		System.out.println("Marks ="+s2.getMarks());
	}
}
