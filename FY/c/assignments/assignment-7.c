#include <stdio.h>

int
q1()
{
    int votes[6] = { 0, 0, 0, 0, 0, 0 }, cand = 0, i;
    char keepgoing = 'y';
    while (keepgoing == 'y') {
	printf("Enter your candidate:");
	scanf("%d", &cand);
	switch (cand)
	{
	  case 1:
	      printf("\nEnter the candidate 1 votes:");
	      scanf("%d", &votes[0]);
	      votes[0] += votes[0];
	      break;
	  case 2:
	      printf("\nEnter the candidate 2 votes:");
	      scanf("%d", &votes[1]);
	      votes[1] += votes[1];
	      break;
	  case 3:
	      printf("\nEnter the candidate 3 votes:");
	      scanf("%d", &votes[2]);
	      votes[2] += votes[2];
	      break;
	  case 4:
	      printf("\nEnter the candidate 4 votes:");
	      scanf("%d", &votes[3]);
	      votes[3] += votes[3];
	      break;
	  case 5:
	      printf("\nEnter the candidate 5 votes:");
	      scanf("%d", &votes[4]);
	      votes[4] += votes[4];
	      break;
	  default:
	      printf("\nBallot spoilt.");
	      printf("\nEnter the spoilt ballot votes:");
	      scanf("%d", &votes[5]);
	      votes[5] += votes[5];
	}
	printf("\nDo you want to enter more votes?:");
	getchar();
	scanf("%c", &keepgoing);
    }
    printf("The votes are:");
    for (i = 0; i < 6; i++) {
	if (i == 5) {
	    printf("\nThe spoilt ballot votes are: %d", votes[5]);
	    break;
	}
	printf("\n The votes for candidate %d are: %d", i+1, votes[i]);
    }
    return 0;
}

int
q2()
{

  int a[3][3], i, j;
  float determinant = 0;

  printf("Enter the 9 elements of matrix: ");
  for(i = 0; i < 3; i++) {
      for(j = 0; j < 3; j++) {
	   scanf("%d",&a[i][j]);
      }
  }

  printf("\nThe matrix is:\n");
  for(i = 0; i < 3; i++) {
      printf("\n");
      for(j = 0; j < 3; j++) {
	   printf("%d\t",a[i][j]);
      }
  }

  for( i = 0; i < 3; i++) {
      determinant = determinant + (a[0][i]*(a[1][(i+1)%3]*a[2][(i+2)%3] - a[1][(i+2)%3]*a[2][(i+1)%3]));
  }

   printf("\nInverse of matrix is: \n\n");
   for( i = 0; i < 3; i++) {
      for(j = 0; j < 3; j++) {
	   printf("%.2f\t",((a[(i+1)%3][(j+1)%3] * a[(i+2)%3][(j+2)%3]) - (a[(i+1)%3][(j+2)%3]*a[(i+2)%3][(j+1)%3]))/ determinant);
      }
      printf("\n");
   }

   return 0;
}

int
q3()
{
    int mat[3][3], i, j, rsum = 0, csum = 0, diagsum = 0;
    printf("Enter a 3x3 Matrix:");
    for(i=0;i<3;i++)
    {
	for(j=0;j<3;j++)
	{
	    scanf("%d",&mat[i][j]);
	}
    }
    printf("The matrix is: \n");
    for (i=0;i<3;i++)
    {
	for(j=0;j<3;j++)
	{
	    printf("%d ",mat[i][j]);
	}
	printf("\n");
    }
    //checking sum of row elements
    for(i=0;i<3;i++)
    {
	for(j=0;j<3;j++)
	{
	    rsum = rsum + mat[i][j];
	}
    }
    //Checking sum of column elements
    for(j=0;j<3;j++)
    {
	for(i=0;i<3;i++)
	{
	    csum = csum + mat[i][j];
	}
    }
    //Checking sum of diagonal elements
    for(i=0;i<3;i++)
    {
	for(j=0;j<3;j++)
	{
	    if(i==j)
	    {
		diagsum = diagsum + mat[i][j];
	    }
	}
    }
    if(rsum==csum && csum==(3*diagsum))
    {
	printf("The matrix is magic square");
    }
    else
    {
	printf("Not magic square");
    }
    return 0;
}

int
main()
{
    q1();
    q2();
    q3();

    return 0;
}
