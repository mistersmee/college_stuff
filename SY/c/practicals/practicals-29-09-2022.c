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

	// Stack
	int MAX, TOP;

	printf("\nEnter stack max size:");
	scanf("%d", &MAX);

	int stack[MAX];

	// Push in stack
	for (TOP = 0; TOP <= MAX; TOP++) {
		if (TOP == MAX) {
			printf("\n!! Stack Overflow !!");
			break;
		} else {
			printf("Enter item you want to insert:");
			scanf("%d", &stack[TOP]);
		}
	}

	printf("\nThe stack is:");

	for (TOP = 0; TOP < MAX; TOP++) {
		printf("\n %d", stack[TOP]);
	}

	// Pop Operation
	for (TOP = MAX - 1; TOP >= 0; TOP--) {
		if (TOP == 0) {
			printf("\n!! Stack Underflow !!");
			stack[TOP] = 0;
			break;
		} else {
			printf("\nSelecting TOP element for popping from stack:");
			printf("\nElement no. %d: %d", TOP, stack[TOP]);
			stack[TOP] = 0;
		}
	}

	printf("\nThe stack becomes:");

	for (TOP = 0; TOP < MAX; TOP++) {
		printf("\n %d", stack[TOP]);
	}

	return 0;
}
