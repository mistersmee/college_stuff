import java.util.Scanner;
import java.util.HashMap;

public class AM37POE {

	static HashMap<Integer, String> map = new HashMap<>();
	static Scanner sc = new Scanner(System.in);

	public static void Search() {
		System.out.println("Enter the student ID you want to search in records:");
		int i = sc.nextInt();

		boolean result = map.containsKey(i);

		if (result == true) {
			System.out.println("Student record: Student ID "+ i + " present.");
			System.out.println("Student name at student ID " + i + " : " + map.get(i));
		} else {
			System.out.println("Student record: Student ID "+ i + " absent.");
		}
	}

	public static void main(String args[]) {
		map.put(1, "Yash");
		map.put(2, "Atharva");
		map.put(3, "Ronit");
		map.put(4, "Niranjan");
		map.put(5, "Aseem");


		System.out.println("Existing student records are: " + map);

		System.out.println("Do you want to add student records? [y/n]:");
		char keepGoing = sc.next().charAt(0);

		while (keepGoing == 'y') {
			System.out.println("Enter a ID number for student record:");
			int Id = sc.nextInt();

			sc.nextLine();

			System.out.println("Enter a name for student record:");
			String inName = sc.nextLine();

			map.put(Id, inName);

			System.out.println("Add more records? [y/n]:");
			keepGoing = sc.next().charAt(0);
		}

		System.out.println("Final student records after adding records are: " + map);


		System.out.println("Do you want to search student records? [y/n]:");
		keepGoing = sc.next().charAt(0);

		while (keepGoing == 'y') {
			System.out.println("Searching records:");
			AM37POE.Search();

			System.out.println("Search for more records? [y/n]:");
			keepGoing = sc.next().charAt(0);
		}

		sc.close();
	}
}
