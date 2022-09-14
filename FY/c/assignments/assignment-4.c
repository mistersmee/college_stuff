#include <stdio.h>
#include <math.h>

/*
 *
 *   1. Write a sample C program to illustrate different loops used in C language
 *        (for , while ,do-while, nested loops with for, while and do-while loop)
 *
 */
int forLoop(int n);
int whileLoop(int n);
int dowhileLoop(int n);
void nestedForLoop(int n);
void nestedWhileLoop(int n);
void nestedDoWhileLoop(int n);

int
q1()
{
    int a,b,c,d,e,f;
    printf("Enter a number to calculate factorial: ");
    scanf("%d",&a);
    printf("The factorial is: %d\n",forLoop(a));
    printf("Enter a number to check the sum of its digits: ");
    scanf("%d",&b);
    printf("The sum of digits is: %d\n", whileLoop(b));
    printf("Enter a number to reverse: ");
    scanf("%d",&c);
    printf("The reverse is: %d\n", dowhileLoop(c));
    printf("Enter number for base of right angle triangle: ");
    scanf("%d",&d);
    nestedForLoop(d);
    printf("Enter number to make square pattern till: ");
    scanf("%d",&e);
    nestedWhileLoop(e);
    printf("Enter number till which to print number pattern: ");
    scanf("%d",&f);
    nestedDoWhileLoop(f);

    return 0;
}

int
forLoop(int n)
{
    int mul = 1;
    for(int i=1;i<=n;i++)
    {
        mul = mul*i;
    }
    return mul;
}

int
whileLoop(int n)
{
    int rem,sum=0;
    while(n>0)
    {
        rem = n%10;
        sum = sum + rem;
        n = n/10;
    }
    return sum;
}

int
dowhileLoop(int n)
{
    int rem,rev=0;
    do
    {
        rem = n%10;
        rev = rev*10 + rem;
        n = n/10;
    }
    while(n>0);
    return rev;
}

void
nestedForLoop(int n)
{
    int i,j;
    for(i=0;i<n;i++)
    {
        for(j=0;j<=i;j++)
        {
            printf("* ");
        }
        printf("\n");
    }
}

void
nestedWhileLoop(int n)
{

    int i=1,j;
    while(i<=n)
    {
        j=1;
        while(j<=n)
        {
            printf("%d ",j);
            j++;
        }
            printf("\n");
            i++;
        }

}

void
nestedDoWhileLoop(int n)
{
    int i=1,j;
    do
    {
        j=1;
        do
        {
            printf("%d ",j);
            j++;
        }while(j<=i);
        printf("\n");
        i++;
    }while(i<=n);
}

/*
 *
 *    2. Write a C program to find the factorial of given number.
 *
 */


int
q2()
{
    int n,i,mul=1;
    printf("Enter number to find it's factorial: ");
    scanf("%d",&n);
    for(i=1;i<=n;i++)
    {
        mul = mul*i;
    }
    printf("The factorial of %d is: %d\n",n,mul);

    return 0;
}


/*
 *    3. Write a C program to find the roots of a quadratic equation.
 *
 */


int
q3()
{
    double a, b, c, discriminant, root1, root2, realPart, imagPart;
    printf("Enter coefficients in format ax^2 + bx + c = 0\n");
    printf("Enter coefficients a, b and c: ");
    scanf("%lf %lf %lf", &a, &b, &c);

    discriminant = b * b - 4 * a * c;

    // condition for real and different roots
    if (discriminant > 0)
    {
        root1 = (-b + sqrt(discriminant)) / (2 * a);
        root2 = (-b - sqrt(discriminant)) / (2 * a);
        printf("root1 = %.2lf and root2 = %.2lf", root1, root2);
    }

        // condition for real and equal roots
    else if (discriminant == 0)
    {
        root1 = root2 = -b / (2 * a);
        printf("root1 = root2 = %.2lf;", root1);
    }

        // if roots are not real
    else
    {
        realPart = -b / (2 * a);
        imagPart = sqrt(-discriminant) / (2 * a);
        printf("root1 = %.2lf+%.2lfi and root2 = %.2f-%.2fi", realPart, imagPart, realPart, imagPart);
    }

    return 0;
}

/*
 *   4. Write a C program to list all the prime numbers between 1 and n, where n is a value
 *       supplied by the user.
 */

int
q4()
{
    int count,i,j,n;
    printf("Enter number till which to find primes: ");
    scanf("%d",&n);
    for(i=1;i<=n;i++)
    {
        count = 0;
        for(j=2;j<i;j++)
        {
            if (i%j==0)
            {
                count++;
                break;
            }
        }
        if(count==0 && i!=1)
        {
            printf("%d ", i);
        }
    }
    return 0;
}

/*
 *   5. Write a program in C to make such a pattern like a pyramid with numbers increased by 1
 *                1 
 *               2 3 
 *              4 5 6 
 *             7 8 9 10
 *
 */

int
q5()
{
    int i,j,n=4,k=1;
    for(i=0;i<n;i++)
    {
        for(j=0;j<(n-i);j++)
        {
            printf(" ");
        }
        for(j=0;j<=i;j++)
        {
            printf("%d ",k++);
        }
        printf("\n");
    }

    return 0;
}

/*
 *  6. Write a C program to read temperature in centigrade and display a suitable message
 *       according to temperature state below : 
 *           Temp &lt; 0 then Freezing weather
 *           Temp 0-10 then Very Cold weather
 *           Temp 10-20 then Cold weather
 *           Temp 20-30 then Normal in Temp
 *           Temp 30-40 then Its Hot
 *           Temp &gt;=40 then Its Very Hot
 *      Test Data :
 *          42
 *      Expected Output :
 *           Its very hot.
 *
 */

void
q6()
{
    int temp;
    printf("Enter the temperature in centigrade: ");
    scanf("%d",&temp);
    if(temp>=40)
    {
        printf("Its very hot");
    }
    else if(temp>=30)
    {
        printf("Its hot");
    }
    else if(temp>=20)
    {
        printf("Normal");
    }
    else if(temp>=10)
    {
        printf("Cold");
    }
    else if(temp>=0)
    {
        printf("Very Cold weather");
    }
    else
    {
        printf("Freezing weather");
    }
}

/*
 *    7. Write a C program to find the eligibility of admission for a professional course based on
 *           the following criteria:
 *               Marks in Maths &gt;=65
 *               Marks in Phy &gt;=55
 *               Marks in Chem&gt;=50
 *           Total in all three subject &gt;=190
 *           or
 *           Total in Math and Physics &gt;=140
 *
 */

void
q7()
{
    int m,p,c;
    printf("Enter marks in Maths, Physics and Chemistry: ");
    scanf("%d %d %d",&m,&p,&c);
    if(m>=65 && p>=55 && c>=50)
    {
        printf("Eligible for admission");
    }
    else if(m+p+c>=190 || m+p>=140)
    {
        printf("Eligible for admission");
    }
    else
    {
        printf("Not eligible for admission");
    }
}

/*
 *  8. Write a c program to count total number of notes in entered amount.
 *
 */

int
q8()
{
    int amount;
    int note500, note100, note50, note20, note10, note5, note2, note1;

    note500 = note100 = note50 = note20 = note10 = note5 = note2 = note1 = 0;


    printf("Enter amount: ");
    scanf("%d", &amount);


    if(amount >= 500)
    {
        note500 = amount/500;
        amount = amount - note500 * 500;
    }
    if(amount >= 100)
    {
        note100 = amount/100;
        amount = amount - note100 * 100;
    }
    if(amount >= 50)
    {
        note50 = amount/50;
        amount = amount - note50 * 50;
    }
    if(amount >= 20)
    {
        note20 = amount/20;
        amount = amount - note20 * 20;
    }
    if(amount >= 10)
    {
        note10 = amount/10;
        amount = amount - note10 * 10;
    }
    if(amount >= 5)
    {
        note5 = amount/5;
        amount = amount - note5 * 5;
    }
    if(amount >= 2)
    {
        note2 = amount /2;
        amount = amount - note2 * 2;
    }
    if(amount >= 1)
    {
        note1 = amount;
    }

    printf("Number of 500 Rs notes = %d\n", note500);
    printf("Number of 100 Rs notes = %d\n", note100);
    printf("Number of 50 Rs notes = %d\n", note50);
    printf("Number of 20 Rs notes = %d\n", note20);
    printf("Number of 10 Rs notes = %d\n", note10);
    printf("Number of 5 Rs coins= %d\n", note5);
    printf("Number of 2 Rs coins = %d\n", note2);
    printf("Number of 1 Rs coins = %d\n", note1);

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
    q8();

    return 0;
}
