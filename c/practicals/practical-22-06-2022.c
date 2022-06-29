#include <stdio.h>

struct address
{
	char apt[10];
	char city[10];
};

struct dob
{
	int dd;
	int mm;
	int yyyy;
};

struct empdetails
{
	int empid;
	char name[10];
	int age;
	int salary;
	struct address a1;
	struct dob d1;

};


int
structure()
{
	struct address a1;
	struct dob d1;
	struct empdetails e1;

	printf("Enter employee id:");
	scanf("%d", &e1.empid);
	printf("Enter employee name:");
	scanf("%s", e1.name);
	printf("Enter employee age:");
	scanf("%d", &e1.age);
	printf("Enter employee salary:");
	scanf("%d", &e1.salary);
	printf("Enter employee address apartment:");
	scanf("%s", e1.a1.apt);
	printf("Enter employee address city:");
	scanf("%s", e1.a1.city);
	printf("Enter employee dob dd mm yyyy:");
	scanf("%d%d%d", &e1.d1.dd, &e1.d1.mm, &e1.d1.yyyy );

	printf("\nThe employee details are:");
	printf("\n\t Employee ID: %d", e1.empid);
	printf("\n\t Employee Name: %s", e1.name);
	printf("\n\t Employee age: %d", e1.age);
	printf("\n\t Employee ID: %d", e1.salary);
	printf("\n\t Employee Address Apartment: %s", e1.a1.apt);
	printf("\n\t Employee Address City: %s", e1.a1.city);
	printf("\n\t Employee DOB: %d-%d-%d", e1.d1.dd, e1.d1.mm, e1.d1.yyyy);

	return 0;
}

int
array()
{
	int array1[3][3], array2[3][3], result[3][3];
	int choice;
	int i, j;

	for (i = 0; i < 3; i++) {
		for (j = 0; j < 3; j++) {
			printf("Enter numbers for array1[%d][%d]:", i, j);
			scanf("%d", &array1[i][j]);
		}
	}

	for (i = 0; i < 3; i++) {
		for (j = 0; j < 3; j++) {
			printf("Enter numbers for array2[%d][%d]:", i, j);
			scanf("%d", &array2[i][j]);
		}
	}

	printf("\nChoose the operation you want to perform: \n\t [1] Addition \n\t [2] Subtraction \n\t [3] Multiplication \n\t [4] Division");
	printf("\nEnter choice here:");
	scanf("%d", &choice);

	switch(choice)
	{
		case 1:
			for ( i = 0; i < 3; i++) {
				for ( j = 0; j < 3; j++) {
					result[i][j] = array1[i][j] + array1[i][j];
				}
			}
			break;
		case 2:
			for ( i = 0; i < 3; i++) {
				for ( j = 0; j < 3; j++) {
					result[i][j] = array1[i][j] - array1[i][j];
				}
			}
			break;
		case 3:
			for ( i = 0; i < 3; i++) {
				for ( j = 0; j < 3; j++) {
					result[i][j] = array1[i][j] * array1[i][j];
				}
			}
			break;
		case 4:
			for ( i = 0; i < 3; i++) {
				for ( j = 0; j < 3; j++) {
					result[i][j] = array1[i][j] / array1[i][j];
				}
			}
			break;
		default:
			printf("Invalid choice, please use 1-4 only.");
	}

	printf("\n The result is:");
	for ( i = 0; i < 3; i++) {
		for ( j = 0; j < 3; j++) {
			printf("|  %d  |",result[i][j]);
		}
		printf("\n\t");
	}

	return 0;
}

int
main()
{
	structure();
	array();

	return 0;
}
@mistersmee
