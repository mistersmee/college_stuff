#include<stdio.h>

int
evenodd()
{
	int num, i;
	printf("Enter a number:");
	scanf("%d", &num);
	for ( i = 0; i <= num; i += 2) {
		if (i == num) {
			printf("\nThe number is even.");
		} else {
			printf("\nThe number is odd.");
		}
	}
}

int
floyd()
{
   int i, j, n, p, q;
   
   printf("\nInput number of rows:");
   scanf("%d", &n);
   
   for ( i = 1 ; i <= n ; i++) {
    	if( i % 2 == 0) { 
	   		p = 1;
	   		q = 0;
		} else { 
	    	p = 0;
			q = 1;
		}
    	for ( j = 1; j <= i; j++) {
	 		if( j % 2 == 0) {
	    		printf("%d",p);
	 		} else {
	    		printf("%d",q);
	 		}
		}
		printf("\n");
   }
}

int
main()
{
	evenodd();
	floyd();
}
