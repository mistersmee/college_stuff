#include <stdio.h>
#include <stdlib.h>

//1) Write a program for handling dynamic array memory using malloc()/calloc()/realloc() and free () functions.
int q1()
{
    int i,n;
    printf("Enter number of integers: ");
    scanf("%d",&n);
    int *ptr=(int*) malloc(n* sizeof(int));

    if(ptr==NULL)
    {
	printf("Memory not available");
	exit(0);
    }
    for(i=0;i<n;i++)
    {
	printf("Enter an integer: ");
	scanf("%d",ptr+i);
    }
    for(i=0;i<n;i++)
    {
	printf("Integer is: %d\n",*(ptr+i));
    }
    return 0;
}

//2) Write a program for perform union for any of the information creation with using array and pointer into it.

union abc
{
    int integer;
    float decimal;

    char name[20];
};

int q2()
{
    union abc u={18,38,"geeksforgeeks"};
    union abc *p=&u;
    printf("\nunion data: \n integer: %d\n" "decimal: %.2f\n name: %s\n",p->integer,p->decimal,p->name);
    printf("Sizeof union: %ld\n", sizeof(u));


    return 0;
}

//3) WAP to perform implementation of enum keyword in your program.


enum ABC{x,y,z};

int q3()
{
    int a;

    a= x+y+z;
    printf("Sum: %d",a);

    return 0;
}

int
main()
{
    q1();
    q2();
    q3();

    return 0;
}
