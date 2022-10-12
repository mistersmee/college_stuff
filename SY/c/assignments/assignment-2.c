#include <stdio.h>
#include <math.h>

int
towerofh(int n, char from_to, char aux_to, char dest_to)
{
	     if (n == 0) {
		return 0;
	      } else if (n == 1){
		     printf("\nThe ring no. %d is moving from tower %c to tower %c", n, from_to, dest_to);
	      } else {
		towerofh(n-1, from_to,	dest_to, aux_to);
		printf("\nThe ring no. %d is moving from tower %c to tower %c", n, from_to, dest_to);
		towerofh(n-1, aux_to, from_to, dest_to);
	      }

	     return 0;
}

int
ackermann(int m, int n)
{
	if (m == 0) {
	   return  n + 1;
	} else if (m != 0 && n == 0) {
	   return ackermann(m-1, 1);
	} else if (m != 0 && n != 0) {
	   return ackermann(m-1, ackermann( m, n - 1));
	}

	return 0;
}

int
main()
{
	// Tower of Hanoi
	int num;
	long long num_moves;

	printf("Enter how many rings you want to have:");
	scanf("%d", &num);


	towerofh(num, 'A', 'B', 'C');

	num_moves =  pow(2, num) - 1;
	printf("\n\nThe number of moves required for %d rings is: %lld", num, num_moves);

	// Ackermann's Function
	int m, n;
	printf("\n\nEnter number for Ackermann's functions' m:");
	scanf("%d", &m);

	printf("\nEnter number for Ackermann's functions' n:");
	scanf("%d", &n);

	printf("\n\nThe result of Ackermann's function is: %d", ackermann(m, n));

	return 0;
}
