public class Use{
	public static void main(String args[]){
		//create object of Student
		Student s = new Student();
		s.setId(12);
		s.setName("Smee");
		s.setMarks(100);
		//retrieve data using getter methods and display
		System.out.println("Id ="+s.getId());
		System.out.println("Name ="+s.getName());
		System.out.println("Marks ="+s.getMarks());
	}
}