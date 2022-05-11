#include <stdio.h>

int 
rnum()
{
	// Reverse number
    int num, rem, rnum = 0, i = 0;
    
	printf("Enter a number:");
    scanf("%d", &num);
    
	while (num > 0){
        rem = num % 10;
        rnum =  (rnum * 10) + rem;
        num = num / 10;
    }
    
	printf("%d",rnum);
}

int 
pal()
{
	// Palindrome
    int num, ornum, rem, rnum = 0, i = 0;
    
	printf("\nEnter a number:");
    scanf("%d", &num);
    
	ornum = num;
    
	while (num > 0){
        rem = num % 10;
        rnum =  (rnum * 10) + rem;
        num = num / 10;
    }
    
	printf("%d",rnum);
	
	if (rnum == ornum) {
		printf("\nThe number %d is a palindrome.", ornum);
	} else {
		printf("\nThe number %d is not a palindrome.", ornum);
	}
}

int
sum()
{
	// Sum of digits of a number
    int num, orgnum, rem, sum = 0, i = 0;
    
	printf("\nEnter a number:");
    scanf("%d", &num);
    
	orgnum = num;
    
	while (num > 0){
        rem = num % 10;
        sum =  sum + rem;
        num = num / 10;
    }
    
	printf("\nThe sum of the digits of the number %d is: %d", orgnum, sum);
}

int 
prime()
{
	int num, flag = 0, i = 2, r;
	
	printf("\nEnter a number:");
	scanf("%d", &num);
	
	do
	{
		r = num % i;
		if (r == 0) {
			flag = 1;
		}
		i++;
	} while (i < num);
	
	if (flag == 1) {
		printf("\nThe number %d is not prime.", num);
	} else {
		printf("\nThe number %d is prime.", num);
	}
}

int
main()
{
	rnum();
	pal();
	sum();
	prime();
}