import java.util.*;

abstract class Person {
    int Id;
    String Name;
    abstract public int getManagerID();
    abstract void displayE();
    abstract void displayM();
}

abstract class Employee extends Person {

    String Post;
	int Salary;
	int ManagerID;
   	boolean IsManager;

	public Employee() {
       	IsManager = false;
   	}

   	public int getManagerID() {
   	    return ManagerID;
   	}

   	void displayE() {
		IsManager = false;
		System.out.println("*EMPLOYEE*");
		System.out.println("ID = "+ Id);
       	System.out.println("Name = "+ Name);
        System.out.println("Post = " + Post);
        System.out.println("Salary = " + Salary);
        System.out.println("ManagerID  = " + ManagerID);
        System.out.println("IsManager = " + IsManager);
	}
}

class Manager extends Employee {

    String Department;

	public Manager() {
        ManagerID = 0;
        IsManager = true;
	}

    public int getManagerID() {
    	return ManagerID;
    }

    void displayM() {
		System.out.println("*MANAGER*");
        System.out.println("Id = " + Id);
		System.out.println("Name = " + Name);
        System.out.println("Post = " + Post);
        System.out.println("Salary = " + Salary);
        System.out.println("ManagerID  = " + ManagerID);
        System.out.println("IsManager = " + IsManager);
        System.out.println("Department = " + Department);
    }
}

public class Assignment9 {

	public static void main(String[] args) {

		Person p[] = new Person[10];
		Scanner s = new Scanner(System.in);
		int c = 0;
		while(true) {
			int choice = s.nextInt();

			switch(choice) {

				case 1:


				Manager m_obj = new Manager();
				p[c] = m_obj;

				m_obj.Id = c;
				System.out.println("Enter Name : ");
				m_obj.Name = s.next();
				System.out.println("Enter Post : ");
				m_obj.Post = s.next();
				System.out.println("Enter Salary : ");
				m_obj.Salary = s.nextInt();
				System.out.println("Enter Department : ");
				m_obj.Department = s.nextLine();
				c++;
				break;

				case 2:

					Employee obj = new Manager();
					p[c] = obj;

					obj.Id = c;
					System.out.println("Enter Name : ");
					obj.Name = s.next();
					System.out.println("Enter Post : ");
					obj.Post = s.nextLine();
					System.out.println("Enter Salary : ");
					obj.Salary = s.nextInt();
					System.out.println("Enter ManagerID : ");
					obj.ManagerID = s.nextInt();
					c++;
				break;

				case 3:
					System.out.println("1. Display All Employee\n2. Display Manager\n3. Display Employes by MangerID");
                    int ch = s.nextInt();

                    switch(ch)
        			{
            			case 1:
            				for(int i=0;i<c;i++)
                            {
								if(p[i].getManagerID()==0) {
									p[i].displayM();
								}
								else {
									p[i].displayE();
								}
						    }
                    	break;

                        case 2:
                        	for(int i=0;i<c;i++)
                        	{
                            	if(p[i].getManagerID() == 0)
                            	{
                                	p[i].displayM();
                            	}
                        	}
                        break;

                        case 3:
                			System.out.println("Enter ManagerID : ");
            				int id_m = s.nextInt();
							int cnt=0;
                			for(int i=0;i<c;i++)
                        	{
								if(p[i].getManagerID()== id_m)
                				{
            						p[i].displayE();
									cnt++;
                            	}
                        	}

							if(cnt==0) {
								System.out.println("not a Manager");
							}

                		break;

						default :
							System.out.println("Invalid Choice");
					}
				break;

				default :
					System.out.println("Invalid Choice");

			}
			s.close();
		}
	}
}
