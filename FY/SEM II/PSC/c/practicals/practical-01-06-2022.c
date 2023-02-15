#include <stdio.h>

void add();
int subtract();
void mult(int a, int b);
int div(int a, int b);
int factorial(int n);
void swap(int a, int b);
void change(int *num);

void
add()
{
    int a, b, c;

    printf("\nEnter a number:");
    scanf("%d", &a);
    printf("\nEnter another number:");
    scanf("%d", &b);

    c = a + b;
    printf("\nThe addition is: %d", c);
}

int
subtract()
{
    int a, b, c;

    printf("\nEnter a number:");
    scanf("%d", &a);
    printf("\nEnter another number:");
    scanf("%d", &b);

    c = a - b;

    return c;
}

void
mult(int a, int b)
{
    int c = a * b;

    printf("\nThe multiplication is: %d", c);
}

int
div(int a, int b)
{
    int c = a / b;

    return c;
}

int
factorial(int n)
{
  if (n == 0) {
    return 1;
  } else {
    return(n * factorial(n-1));
  }
}

void
swap (int a, int b)
{
    int temp;
    temp = a;
    a = b;
    b = temp;
    printf("\nAfter swapping values in function a = %d, b = %d\n",a,b);
}

void
change(int *num)
{
    printf("\nBefore adding value inside function num = %d \n",*num);
    (*num) += 100;
    printf("\nAfter adding value inside function num = %d \n", *num);
}

int main()
{
    int multa, multb, diva, divb, subc, divc;

    add();

    subc = subtract();
    printf("\nThe subtraction is: %d", subc);

    printf("\nEnter a number for multiplication:");
    scanf("%d", &multa);
    printf("\nEnter another number:");
    scanf("%d", &multb);
    mult(multa, multb);

    printf("\nEnter a number for division:");
    scanf("%d", &diva);
    printf("\nEnter another number:");
    scanf("%d", &divb);
    divc = div(diva, divb);
    printf("\nThe division is: %d", divc);

    int number;
    int fact;
    printf("\nEnter a number: ");
    scanf("%d", &number);

    fact = factorial(number);
    printf("\nFactorial of %d is %d\n", number, fact);

    int a = 10;
    int b = 20;
    printf("\nBefore swapping the values in main a = %d, b = %d\n",a,b);
    swap(a,b);
    printf("\nAfter swapping values in main a = %d, b = %d\n", a, b);

    int x = 100;
    printf("\nBefore function call x = %d \n", x);
    change(&x);
    printf("\nAfter function call x = %d \n", x);

    int array[10], i;

    for (i = 0; i < 10; i++) {
	printf("\nEnter a number [%d]:", i);
	scanf("%d", &array[i]);
    }

    printf("The array is:");

    for (i = 0; i < 10; i++) {
	printf(" [%d] ", array[i]);

    }

    int array2[5][3], j, k;

    for (j = 0; j < 5; j++) {
	for (k = 0; k < 3; k++) {
	    printf("\nEnter the number in array [%d][%d]:", j, k);
	    scanf("%d", &array2[j][k]);
	}
    }

    printf("\nThe array is:");

    for (j = 0; j < 5; j++) {
	printf("\nThe row [%d] is:", j);
	for (k = 0; k < 3; k++) {
	    printf(" | %d |", array2[j][k]);
	}
	printf("\n");
    }


    return 0;
}
