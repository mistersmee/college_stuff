#include<stdio.h>

int
evenodd()
{
	int num;
	printf("Enter a number:");
	scanf("%d", &num);
		if (num & 1) {
				printf("\nThe number is odd.");
		} else {
			printf("\nThe number is even.");
		}

		return 0;
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

    return 0;
}

int
main()
{
	evenodd();
	floyd();
}
