#include <stdio.h>

struct dog
{
    char name[10];
    char breed[10];
    int age;
    char color[10];
};

void swapr(int *, int *);
void getSeconds(unsigned long *par);

void getSeconds(unsigned long *par) {
   /* get the current number of seconds */
   *par = time( NULL );
   return;
}

void
swapr (int *a, int *b)
{
    int temp;
    temp = *a;
    *a=*b;
    *b=temp;
    printf("After swapping values in function a = %d, b = %d\n",*a,*b);
}

int
q1()
{
    //Initialize pointer, store and display elements using simple pointer
    int a = 5;
    int *b;
    b = &a;

    printf("Value of `a` is: %d", a);
    printf("\nAddress of `a` is: %u", &a);
    printf("\nPointer to 'a', 'b': %d", *(&a));
    printf("\nValue in variable `b`: %u", b);
    printf("\n Address of `b`: %u", &b);
    printf("\n`b` points to `a` so *b = %d", *b);

    //Pointer to array

    int a1[10];
    int (*c)[10];
    int i;

    c = &a1;

    for (i = 0; i < 10; i++) {
	printf("\nEnter value in array a1[%d]:", i);
	scanf("%d", &a1[i]);
    }

    for (i = 0; i < 10; i++) {
	printf("\nArray a1[%d] stored at %u having value %d", i, c, (*c)[i]);
    }

    //Pointer to structure
    struct dog spike = {"spike", "Bulldog", 5, "white"};
    struct dog *ptr_dog;
    ptr_dog = &spike;

    printf("\nDog's name: %s\n", ptr_dog->name);
    printf("\nDog's breed: %s\n", ptr_dog->breed);
    printf("\nDog's age: %d\n", ptr_dog->age);
    printf("\nDog's color: %s\n", ptr_dog->color);

    //Pointer to function
   unsigned long sec;
   getSeconds( &sec );

   /* print the actual value */
   printf("Number of seconds: %ld\n", sec );

   //Pointer to string
   char str[10] = "Aseem";
   char (*ptr)[10];

   ptr = &str;

   printf("\nThe string `str` stored at %u is: %s", ptr, *ptr);

   return 0;
}


int
q2()
{
    int a = 10;
    int b = 20;
    printf("\nBefore swapping the values in main a = %d, b = %d\n",a,b);
    swapr(&a,&b);
    printf("\nAfter swapping values in main a = %d, b = %d\n",a,b);

    return 0;
}


int
main()
{
    q1();
    q2();
    return 0;
}
