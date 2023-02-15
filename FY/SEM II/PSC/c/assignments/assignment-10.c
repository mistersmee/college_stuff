#include <stdio.h>

struct q1struct
{
	int a;
	char b;
};

struct q2nest1
{
	char b;
};

struct q2neststruct
{
	int a;
	struct q2nest1 s2;
};

struct q3struct
{
	int a;
	int b;
	char c;
};

struct q4struct
{
	int a;
	int b;
};

struct q5cric
{
	char cricname[20];
	int cricruns;
	int cricwickets;
};

struct name
{
	char first_name[10];
	char middle_name[10];
	char last_name[10];
};

struct address
{
	int flat_number;
	int lane_number;
	int pin_code;
	char city[10];
};

struct dob
{
	int dd;
	int mm;
	int yyyy;
};

struct q6_1
{
	int regno;
	struct name n1;
	struct dob d1;
	int age;
	struct address a1;
};

struct q6_2
{
	int bookid;
	char bookname[20];
	char author[20];
	int price;
	int edition;
	char publisher[20];
	int year;
};

struct q6_3
{
	int employeeid;
	struct name n2;
	struct address a2;
	struct dob d2;
};

struct dist
{
	int ft;
	int in;
};

int
q1()
{
	struct q1struct s1;

	printf("Enter a number:");
	scanf("%d", &s1.a);
	printf("\nEnter a character:");
	getchar();
	scanf("%c", &s1.b);

	printf("\nThe value of `a` in structure `s1` is: %d", s1.a);
	printf("\nThe value of `b` in structure `s1` is: %c", s1.b);

	return 0;
}

int
q2()
{
	struct q2neststruct s1;
	struct q2nest1 s2;

	printf("\nEnter a number:");
	scanf("%d", &s1.a);
	printf("\nEnter a character:");
	getchar();
	scanf("%c", &s1.s2.b);

	printf("\nThe value of `a` in structure `s1` is: %d", s1.a);
	printf("\nThe value of `b` in nested structure `s2` of `s1` is: %c", s1.s2.b);

	return 0;
}

int
q3()
{
	struct q3struct s1[5];
	int i;

	for (i = 0; i < 5; i++) {
		printf("\nEnter a number for structure s1[%d]:", i+1);
		getchar();
		scanf("%d", &s1[i].a);
		printf("\nEnter another number for structure s1[%d]:", i+1);
		getchar();
		scanf("%d", &s1[i].b);
		printf("\nEnter a character for structure s1[%d]:", i+1);
		getchar();
		scanf("%c", &s1[i].c);
	}
	for (i = 0; i < 5; i++) {
		printf("\nThe number in `a` in structure s1[%d] is: %d", i+1, s1[i].a);
		printf("\nThe number in `b` in structure s1[%d] is: %d", i+1, s1[i].b);
		printf("\nThe character in `c` in structure s1[%d] is: %c", i+1, s1[i].c);
	}

	return 0;
}

struct q4struct q4func()
{
	struct q4struct s1;

	printf("\nEnter a number: ");
	getchar();
	scanf ("%d", &s1.a);

	printf("\nEnter another number: ");
	getchar();
	scanf("%d", &s1.b);

	return s1;
}

int
q4()
{
	struct q4struct s;

	s = q4func();

	printf("\nThe number in `a` in structure `s` is: %d", s.a);
	printf("\nThe number in `b` in structure `s` is: %d", s.b);

	return 0;
}

int
q5()
{
	struct q5cric c1;
	printf("\nEnter the cricketer's name:");
	getchar();
	fgets(c1.cricname, 20, stdin);
	printf("\nEnter the cricketer's runs scored:");
	scanf("%d", &c1.cricruns);
	printf("\nEnter the cricketer's wickets taken:");
	scanf("%d", &c1.cricwickets);

	printf("\nThe cricketer's record:");
	printf("\n\tName: %s", c1.cricname);
	printf("\n\tRuns: %d", c1.cricruns);
	printf("\n\tWickets: %d", c1.cricwickets);

	return 0;
}

int
q6()
{
	struct q6_1 s1;
	struct q6_2 b1;
	struct q6_3 e1;
	struct name n1, n2;
	struct address a1, a2;
	struct dob d1, d2;

	// 6.1
	printf("\nEnter the student's registration number:");
	getchar();
	scanf("%d", &s1.regno);
	printf("\nEnter the student's full name [first<CR>middle<CR>last]:");
	getchar();
	scanf("%s%s%s", s1.n1.first_name, s1.n1.middle_name, s1.n1.last_name);
	printf("\nEnter the student's date of birth [dd<CR>mm<CR>yyyy]:");
	getchar();
	scanf("%d%d%d", &s1.d1.dd, &s1.d1.mm, &s1.d1.yyyy);
	printf("\nEnter the student's age:");
	getchar();
	scanf("%d", &s1.age);
	printf("\nEnter the student's address' flat number:");
	getchar();
	scanf("%d", &s1.a1.flat_number);
	printf("\nEnter the student's address' lane number:");
	getchar();
	scanf("%d", &s1.a1.lane_number);
	printf("\nEnter the student's address' pin code:");
	getchar();
	scanf("%d", &s1.a1.pin_code);
	printf("\nEnter the student's address' city:");
	getchar();
	scanf("%s", &s1.a1.city);

	// 6.2
	printf("\nEnter the book ID:");
	getchar();
	scanf("%d", &b1.bookid);
	printf("\nEnter the book name:");
	getchar();
	scanf("%s", b1.bookname);
	printf("\nEnter the author name:");
	getchar();
	scanf("%s", b1.author);
	printf("\nEnter the book price:");
	getchar();
	scanf("%d", &b1.price);
	printf("\nEnter the book edition:");
	getchar();
	scanf("%d", &b1.edition);
	printf("\nEnter the book publisher:");
	getchar();
	scanf("%s", b1.publisher);
	printf("\nEnter the book year:");
	getchar();
	scanf("%d", &b1.year);
	// 6.3
	printf("\nEnter the employee ID:");
	getchar();
	scanf("%d", &e1.employeeid);
	printf("\nEnter the employee's full name [first<CR>middle<CR>last]:");
	getchar();
	scanf("%s%s%s", e1.n2.first_name, e1.n2.middle_name, e1.n2.last_name);
	printf("\nEnter the employee's date of birth [dd<CR>mm<CR>yyyy]:");
	getchar();
	scanf("%d%d%d", &e1.d2.dd, &e1.d2.mm, &e1.d2.yyyy);
	printf("\nEnter the employee's address' flat number:");
	getchar();
	scanf("%d", &e1.a2.flat_number);
	printf("\nEnter the employee's address' lane number:");
	getchar();
	scanf("%d", &e1.a2.lane_number);
	printf("\nEnter the employee's address' pin code:");
	getchar();
	scanf("%d", &e1.a2.pin_code);
	printf("\nEnter the employee's address' city:");
	getchar();
	scanf("%s", &e1.a2.city);

	return 0;
}

void
add (struct dist d1, struct dist d2, struct dist *result)
{
	result->ft = d1.ft + d2.ft;
	result->in = d1.in + d2.in;
}

int
q7()
{
	struct dist d1, d2, result;

	printf("\nEnter distance 1 feet part:");
	getchar();
	scanf("%d", &d1.ft);
	printf("\nEnter distance 1 inch part:");
	getchar();
	scanf("%d", &d1.in);
	printf("\nEnter distance 2 feet part:");
	getchar();
	scanf("%d", &d2.ft);
	printf("\nEnter distance 2 inch part:");
	getchar();
	scanf("%d", &d2.in);

	add(d1, d2, &result);
	printf("\nThe addition result feet part: %d", result.ft);
	printf("\nThe addition result inch part: %d", result.in);

	return 0;
}

int
main()
{
	q1();
	q2();
	q3();
	q4();
	q5();
	q6();
	q7();

	return 0;
}
