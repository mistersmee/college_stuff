#include<stdio.h>

/*
 * 1. Write a sample C program to illustrate Function in C.
 *
 */

int add(int x,int y);
void hello();

int
q1()
{
    int a,b;
    printf("Enter two numbers to see the addition: ");
    scanf("%d %d",&a,&b);
    printf("The sum is: %d\n",add(a,b));
    hello();

    return 0;
}

int
add(int x, int y)
{
    return x + y;
}

void
hello()
{
    printf("Hello\n");
}


/*
 *
 *   2. Write a C program to illustrate following function types
 *	     1. With argument with return type
 *	     2. Without argument without return type
 *	     3. Without argument with return type
 *	     4. With argument without return type
 *
 */

int sum(int x,int y);  //With argument and return value
void sub(int x,int y); //With argument without return value
void hello2();		//Without argument without return value
int mult();	       //Without argument with return value

int
q2()
{
    int a,b;
    printf("Enter two numbers: ");
    scanf("%d %d",&a,&b);
    printf("The sum is: %d\n",sum(a,b));
    sub(a,b);
    hello();
    printf("%d\n",mult());

    return 0;
}

int
sum (int x,int y)
{
    return x +y;
}

void
hello2()
{
    printf("Hello Im a function without argument and return value\n");
}

int
mult()
{
    int p,q;
    printf("This is multiplication function, enter two numbers to multiply: ");
    scanf("%d %d",&p,&q);
    return p*q;
}
void
sub (int x,int y)
{
    int s = x -y;
    printf("The subtraction is: %d\n",x-y);
}


//  3. Write C program that uses recursive function to print Fibonacci series.

int
fibbonacci (int n)
{
   if(n == 0)
   {
      return 0;
   }
   else if(n == 1)
   {
      return 1;
   }
   else
   {
      return (fibbonacci(n-1) + fibbonacci(n-2));
   }
}

int
q3 ()
{
   int n,i;
   printf("Enter the number of fibonacci terms: ");
   scanf("%d",&n);
   printf("Fibbonacci of %d: " , n);

   for(i = 0;i<n;i++) {
      printf("%d ",fibbonacci(i));
   }

   return 0;
}

//  4. Write a C program to perform factorial of given number using recursion.

long int factorial(int n);

int
q4()
{
    int num;
    printf("Enter number: ");
    scanf("%d",&num);
    printf("The factorial is: %ld\n",factorial(num));
    return 0;
}

long int
factorial(int n)
{
    if(n>=1)
    {
	return n*factorial(n-1);
    }
    else
    {
	return 1;
    }
}

//  5. Write a C program to perform sum of 1 to 10 numbers using recursion.

long int sigma(int n);

int
q5 ()
{
    int num=10;
    printf("The sum of numbers from 1 to 10 is: %ld\n",sigma(num));
    return 0;
}

long int
sigma (int n)
{
    if(n>=1)
    {
	return n+ sigma(n-1);
    }
    else
    {
	return 0;
    }
}

//  6. Write C program that convert a lowercase character to uppercase using a user defined function.

char uppercase(char c);
int
q6()
{
    char ch;
    printf("Enter a character: ");
    scanf("%c",&ch);
    printf("The uppercase is: %c", uppercase(ch));

    return 0;
}

char
uppercase(char c)
{
    return c - 32;
}

//  7. Write a program in C to swap two numbers using function. (Perform call by value and call by reference).


//Swapping using Call by Value

void swapv(int , int);

int
q7a()
{
    int a = 10;
    int b = 20;
    printf("Before swapping the values in main a = %d, b = %d\n",a,b);
    swapv(a,b);
    printf("After swapping values in main a = %d, b = %d\n",a,b);

    return 0;
}

void
swapv (int a, int b)
{
    int temp;
    temp = a;
    a=b;
    b=temp;
    printf("After swapping values in function a = %d, b = %d\n",a,b); // Formal parameters, a = 20, b = 10
}

//Call by Reference


void swapr(int *, int *);

int
q7b()
{
    int a = 10;
    int b = 20;
    printf("Before swapping the values in main a = %d, b = %d\n",a,b);
    swapr(&a,&b);
    printf("After swapping values in main a = %d, b = %d\n",a,b);

    return 0;
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
main()
{
    q1();
    q2();
    q3();
    q4();
    q5();
    q6();
    q7a();
    q7b();

    return 0;
}
