#include <stdio.h>

int profloss();
int case_check();
int space_check();
int even();
int odd();
int dist();
int switch_demo();
int nestedif();

int
profloss()
{
	float s_price, c_price;

	printf("Enter the cost price:");
	scanf("%f", &c_price);
	printf("Enter the sold price:");
	scanf("%f", &s_price);

	if (s_price > c_price) {
		float profit, prof_perc;

		profit = s_price - c_price;
		prof_perc = ( profit / c_price ) * 100;

		printf("A profit of %.2f and percentage %.2f%% was incurred.", profit, prof_perc);
	} else if (s_price < c_price) {
		float loss, loss_perc;

		loss = c_price - s_price;
		loss_perc = ( loss / c_price) * 100;

		printf("A loss of %.2f and percentage %.2f%% was incurred.", loss, loss_perc);
	} else {
		printf("No profit or loss was incurred.");
	}
	return 0;
}

int
case_check()
{
	char check_char;

	printf("\nEnter a character:");
	scanf("%c", &check_char);

	( check_char >= 'a' && check_char <= 'z' ) ? printf("\nThe given character is lowercase.")
	                    	: printf("\nThe give character is uppercase.");

	return 0;
}

int
space_check()
{
	char spat_char;

	printf("\nEnter another character to check if spatial or not:");
	scanf("%c", &spat_char);

	(spat_char == ' ') ? printf("\nThe given character is spatial.")
					   : printf("\nThe given character is not spatial");

	return 0;
}

int
even()
{
	int i = 0;
	for (;i < 10;) {
		i++;
		i++;
		printf("\n%d", i);
	}

	return 0;
}

int
odd()
{
	int i = 0;

	label:

	if ( i % 2 != 0 ) {
		printf("\n%d", i);
	}

	i++;

	if (i < 20) {
		goto label;
	}

	return 0;
}

int
dist()
{
	int dist;

	printf("Enter the distance between any two cities in km:");
	scanf("%d", &dist);

	int distm;
	distm = dist * 1000;

	int distcm;
	distcm = distm * 100;

	int distft;
	distft = distm * 3.281;

	int distin;
	distin = distm * 39.37;

	printf("The distance in meters is: \t%d m,"
			"\n\t in centimeters is: \t%d cm,"
			"\n\t in feet is: \t%d ft.,"
			"\n\t in inches is: \t%d in.", distm, distcm, distft, distin);

	return 0;
}

int
switch_demo()
{
	int a;
	printf("Enter a number:");
	scanf("%d", &a);
	switch (a) {
		case 1:
			printf("You have entered the first case.");
			break;
		case 2:
			printf("You have entered the second case.");
			break;
		case 3:
			printf("You have entered the third case.");
			break;
		default:
			printf("Invalid number.");
			break;
	}

	return 0;
}

int
nestedif()
{

	int n;

	printf("Enter a number:");
	scanf("%d",&n);

	if (n % 2 == 0){

	    printf("Even ");

	    if (n % 4 == 0) {
	        printf("and divisible by 4");
	    } else {
	        printf("and not divisible by 4");
	    }
	} else {
	    printf("Odd ");

	    if(n % 3 == 0) {
	        printf("and divisible by 3");
	    } else {
	        printf("and not divisible by 3");
	    }

	}

	return 0;
}
int
main()
{
	profloss();
	case_check();
	space_check();
	even();
	odd();
	dist();
	switch_demo();
	nestedif();
}
