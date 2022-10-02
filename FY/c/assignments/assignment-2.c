#include <stdio.h>
/*
 *   1. Write a C program to read the values of x and y and print the results of the following expressions in one line:
 *	 i. (x + y) / (x - y)
 *	 ii. (x + y)(x - y)
 *
 */

int
q1()
{
    int x,y,a,b;
    printf("Enter numbers: ");
    scanf("%d %d",&x,&y);
    a =  (x+y) / (x - y);
    b = (x+y)*(x-y);
    printf("%d %d",a,b);

    return 0;
}

/*
 *   2. Write a C program to perform operation of all operators used in C.
 *
 */

int
q2()
{

    // Arithmetic

    int a = 9,b = 4, c;

    c = a+b;
    printf("a+b = %d \n",c);
    c = a-b;
    printf("a-b = %d \n",c);
    c = a*b;
    printf("a*b = %d \n",c);
    c = a/b;
    printf("a/b = %d \n",c);
    c = a%b;
    printf("Remainder when a divided by b = %d \n",c);

    // Increment/Decrement

    int e = 10, f = 100;
    float g = 10.5, d = 100.5;

    printf("++a = %d \n", ++e);
    printf("--b = %d \n", --f);
    printf("++c = %f \n", ++g);
    printf("--d = %f \n", --d);

    // Assignment

    int a1 = 5, c1;

    c1 = a1;	  // c is 5
    printf("c = %d\n", c);
    c1 += a1;	  // c is 10
    printf("c = %d\n", c);
    c1 -= a1;	  // c is 5
    printf("c = %d\n", c);
    c1 *= a1;	  // c is 25
    printf("c = %d\n", c);
    c1 /= a1;	  // c is 5
    printf("c = %d\n", c);
    c1 %= a1;	  // c = 0
    printf("c = %d\n", c);

    // Relational

    int a2 = 5, b2 = 5, c2 = 10;

    printf("%d == %d is %d \n", a2, b2, a2 == b2);
    printf("%d == %d is %d \n", a2, c2, a2 == c2);
    printf("%d > %d is %d \n", a2, b2, a2 > b2);
    printf("%d > %d is %d \n", a2, c2, a2 > c2);
    printf("%d < %d is %d \n", a2, b2, a2 < b2);
    printf("%d < %d is %d \n", a2, c2, a2 < c2);
    printf("%d != %d is %d \n", a2, b2, a2 != b2);
    printf("%d != %d is %d \n", a2, c2, a2 != c2);
    printf("%d >= %d is %d \n", a2, b2, a2 >= b2);
    printf("%d >= %d is %d \n", a2, c2, a2 >= c2);
    printf("%d <= %d is %d \n", a2, b2, a2 <= b2);
    printf("%d <= %d is %d \n", a2, c2, a2 <= c2);

    // Logical
    int a3 = 5, b3 = 5, c3 = 10, result;

    result = (a3 == b3) && (c3 > b3);
    printf("(a3 == b3) && (c3 > b3) is %d \n", result);

    result = (a3 == b3) && (c3 < b3);
    printf("(a3 == b3) && (c3 < b3) is %d \n", result);

    result = (a3 == b3) || (c3 < b3);
    printf("(a3 == b3) || (c3 < b3) is %d \n", result);

    result = (a3 != b3) || (c3 < b3);
    printf("(a3 != b3) || (c3 < b3) is %d \n", result);

    result = !(a3 != b3);
    printf("!(a3 != b3) is %d \n", result);

    result = !(a3 == b3);
    printf("!(a3 == b3) is %d \n", result);

    // Conditional
    int a4 = 10;
    int b4 = 15;
    int x = ( a > b )? a : b;
    printf("%d", x);

    // Bitwise

    // AND
    int a5 = 12, b5 = 25;
    printf("Output = %d", a5 & b5);

    // OR
    int a6 = 12, b6 = 25;
    printf("Output = %d", a6 | b6);

    // XOR
    int a7 = 12, b7 = 25;
    printf("Output = %d", a6 ^ b6);

    // Complement
    printf("Output = %d\n",~35);
    printf("Output = %d\n",~-12);

    // Shift

    int num=212, i;
    for (i=0; i<=2; ++i)
	printf("Right shift by %d: %d\n", i, num>>i);

     printf("\n");

     for (i=0; i<=2; ++i)
	printf("Left shift by %d: %d\n", i, num<<i);

    // Special Operators
    // sizeof

    int a8;
    float b8;
    double c8;
    char d8;
    printf("Size of int=%lu bytes\n",sizeof(a8));
    printf("Size of float=%lu bytes\n",sizeof(b8));
    printf("Size of double=%lu bytes\n",sizeof(c8));
    printf("Size of char=%lu byte\n",sizeof(d8));


    return 0;
}

int
main()
{
    q1();
    q2();

    return 0;
}
