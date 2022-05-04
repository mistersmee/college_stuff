#include<stdio.h>

int
main()
{
    // Basic hello world
    printf("Hello world!");

    // Basic addition of two numbers
    int a = 5, b = 6;
    int add, sub, div, mult;
    add = a + b;

    printf("\nThe addition of %d and %d is: %d", a, b, add);

    //Basic subtraction
    sub = b - a;
    printf("\nThe subtraction of %d and %d is: %d", b, a, sub);

    //Basic division
    div = b / a;
    printf("\nThe division of %d and %d is: %d", b, a, div);

    //Basic multiplication
    mult = b * a;
    printf("\nThe multiplication of %d and %d is: %d", a, b, mult);

    //Area of circle
    float pi = 3.14, areac, r = 10;
    areac = pi * r * r;

    printf("\nThe area of circle with radius %f is: %f", r, areac);

    //Area of triangle
    int base = 100, h = 50, areat;
    areat = 0.5 * base * h;

    printf("\nThe area of triangle with base %d and height %d is: %d", base, h, areat);

    //Area of square
    int side = 10, areas;
    areas = side * side;

    printf("\nThe area of square with side %d is: %d", side, areas);

    //Area of rectangle

    int length = 10, breadth = 10, arear;
    arear = length * breadth;

    printf("\nThe area of rectangle with length %d and breadth %d is: %d", length, breadth, arear);

    //Perimeter of circle
    float peric = 2 * pi * r;

    printf("\nThe perimeter of circle with radius %f is: %f", r, peric);

    //Perimeter of triangle
    int side1 = 10, side2 = 10, side3 = 10, perit;
    perit = side1 + side2 + side3;

    printf("\nThe perimeter of triangle with sides %d, %d, %d is: %d", side1, side2, side3, perit);

    //Perimeter of square
    int peris = side * 4;

    printf("\nThe perimeter of square with side %d is: %d", side, peris);

    //Perimeter of rectangle
    int perir = 2 * (length + breadth);

    printf("\nThe perimeter of rectangle with length %d and breadth %d is: %d", length, breadth, perir);

    return 0;
}
