 #include <stdio.h>
int
main()
{
	int i, j, csum = 0, rsum = 0;
	int a[5][5];
	for ( i = 0; i < 5; i++ ) {
		for ( j = 0; j < 5; j++) {
			printf("Enter numbers to store in 2D array [%d][%d]:", i, j);
			scanf("%d", & a[i][j]);
		}
	}
	printf("rsum = ");
	for ( i = 0; i < 5; i++ ) {
		for ( j = 0; j < 5; j++) {
			rsum = rsum + a[i][j];
		}
		printf(" %d ", rsum);
		rsum = 0;
	}
	printf("\ncsum = ");
	for ( j = 0; j < 5; j++) {
		for (i = 0; i < 5; i++) {
			csum = csum + a[i][j];
		}
		printf(" %d ", csum);
		csum = 0;
	}
	printf("\n");
}
