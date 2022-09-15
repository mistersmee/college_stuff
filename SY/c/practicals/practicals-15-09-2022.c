#include <stdio.h>
#include <stdlib.h>
// Check if number is prime or not

int
main()
{
	int num, flag = 0, i;
	printf("Enter a number to check if prime or not:");
	scanf("%d", &num);

	if (num == 1 || num == 0) {
		printf("1 and 0 are neither prime nor composite.");
		exit(0);
	}

	for (i = 2; i < num; i++) {
		if (num % i == 0) {
			flag++;
			break;
		}
	}
	
	if (flag != 0) {
		printf("The number is composite.");
	} else {
		printf("The number is prime.");
	}

	return 0;
}
