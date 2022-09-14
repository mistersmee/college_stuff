#include <stdio.h>

/*
 *  1. Write a sample C program to illustrate decision making and branching statements used in C language
 *    ( If ,if else,if else ladder,nested if else, Switch case )
 *
*/

void ispositive(int n);       //If statement
void isComposite(int n);        //If Else statement
void grade(int n);              //If Else ladder
void whichLargest(int x,int y,int z);          //Nested If Else
void whichDay(int n);           //Switch Case

int 
q1()
{
    int a,b,c;
    printf("Enter a number to check if positive: ");
    scanf("%d",&a);
    ispositive(a);
    printf("Enter a number to check whether it's composite: ");
    scanf("%d",&a);
    isComposite(a);
    printf("Enter marks from 0 to 50 to check grade earned: ");
    scanf("%d",&a);
    grade(a);
    printf("Enter 3 numbers to check which is largest: ");
    scanf("%d %d %d",&a,&b,&c);
    whichLargest(a,b,c);
    printf("Enter the week number to get the day: ");
    scanf("%d",&a);
    whichDay(a);

    return 0;
}

void 
ispositive(int n)
{
    if(n>0)
    {
        printf("The number is positive\n");
    }
}

void 
isComposite(int n)
{
    if(n%2 == 0)
    {
        printf("It is composite\n");
    }
    else
    {
        printf("Not composite\n");
    }
}

void
grade(int n)
{
    if(n>= 40)
    {
        printf("A Grade\n");
    }
    else if(n>=30)
    {
        printf("B Grade\n");
    }
    else if(n>=20)
    {
        printf("C Grade\n");
    }
    else
    {
        printf("Fail\n");
    }
}

void
whichLargest(int x,int y,int z)
{
    if(x>=y)
    {
        if(x>=z)
        {
            printf("%d is the largest number.\n",x);
        }
        else
        {
            printf("%d is the largest number.\n",z);
        }
    }
    else
    {
        if(y>=z)
        {
            printf("%d is the largest number.\n",y);
        }
        else
        {
            printf("%d is the largest number.\n",z);
        }
    }
}

void
whichDay(int n)
{
    switch(n)
    {
        case 1:
            printf("Monday\n");
        break;
        case 2:
            printf("Tuesday\n");
        break;
        case 3:
            printf("Wednesday\n");
        break;
        case 4:
            printf("Thursday\n");
        break;
        case 5:
            printf("Friday\n");
        break;
        case 6:
            printf("Saturday\n");
        break;
        case 7:
            printf("Sunday\n");
        break;
        default:
            printf("Invalid input! Please enter week number between 1-7.\n");
    }
}


/*
 *
 *   2. An electric power distribution company charges its domestic consumers as follows.
 *        Consumption Units Rate of Charge
 *          001 – 200 Rs.0.50 per unit
 *          201 – 400 Rs.100 plus Rs.0.65 per unit excess of 200
 *          401 – 600 Rs.230 plus Rs.0.80 per unit excess of 400
 *          601 and above Rs.390 plus Rs.1.00 per unit excess of 600
 *      Write a C Program that reads the customer number and power consumed and prints the
 *      amount to be paid by the customer.
 *
*/

int
q2()
{
    int cno, pwr;
    float amt, surplus;

    printf("Enter the customer number:");
    scanf("%d", &cno);

    printf("\nEnter the units consumed:");
    scanf("%d", &pwr);


    if (pwr == 0) {
        printf("Units consumed cannot be 0.");
        amt = 0;
    }
    else if (pwr > 0 && pwr <= 200) {
        amt = 0.50 * pwr;
    } else if (pwr >= 201 && pwr <= 400) {
        surplus = 0.65 * (pwr - 200);
        amt = 100 + surplus;
    } else if (pwr >= 401 && pwr <= 600) {
        surplus = 0.80 * (pwr - 400);
        amt = 230 + surplus;
    } else if ( pwr >= 601 ) {
        surplus = 1 * (pwr - 600);
        amt = 390 + surplus;
    }

    printf("\n The amount to be paid by customer %d is: %.4f", cno, amt);

    return 0;

}

int
main()
{
    q1();
    q2();
    return 0;
}