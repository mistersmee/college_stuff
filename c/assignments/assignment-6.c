#include <stdio.h>

int
q1()
{
    int a[3];
    int b[3][3];
    int c[3][3][3];
    int i, j, k;

    // 1D
    for (i = 0; i < 3; i++) {
        printf("Enter the numbers for array a[%d]:", i);
        scanf("%d", &a[i]);
    }
    //2D
    for (i = 0; i < 3; i++) {
        for (j = 0; j < 3; j++) {
            printf("\nEnter the number for array b[%d][%d]", i, j);
            scanf("%d", &b[i][j]);
        }
    }
    //3D
    for (i = 0; i < 3; i++) {
        for (j = 0; j < 3; j++) {
            for (k = 0; k < 3; k++) {
                printf("\nEnter the numbers for array c[%d][%d][%d]", i, j, k);
                scanf("%d", &c[i][j][k]);
            }
        }
    }

    return 0;
}

int
q2()
{
    int a[3];
    int i;

    for (i = 0; i < 3; i++) {
        printf("\nEnter the numbers for array a[%d]:", i);
        scanf("%d", &a[i]);
    }

    for (i = 0; i < 3; i++) {
        printf("\nThe array element a[%d] at memory address [%d] is: %d", i, &a[i], a[i]);
    }

     return 0;
}

int
q3()
{
	int A[3][3], B[3][3], C[3][3];
	int choice;
	int i, j;

	for (i = 0; i < 3; i++) {
		for (j = 0; j < 3; j++) {
			printf("Enter numbers for A[%d][%d]:", i, j);
			scanf("%d", &A[i][j]);
		}
	}

	for (i = 0; i < 3; i++) {
		for (j = 0; j < 3; j++) {
			printf("Enter numbers for B[%d][%d]:", i, j);
			scanf("%d", &B[i][j]);
		}
	}

	printf("\nChoose the operation you want to perform: \n\t [1] Addition \n\t [2] Subtraction \n\t [3] Multiplication \n\t [4] Division");
	printf("\nEnter choice here:");
	scanf("%d", &choice);

	switch(choice)
	{
		case 1:
			for ( i = 0; i < 3; i++) {
				for ( j = 0; j < 3; j++) {
					C[i][j] = A[i][j] + B[i][j];
				}
			}
			break;
		case 2:
			for ( i = 0; i < 3; i++) {
				for ( j = 0; j < 3; j++) {
					C[i][j] = A[i][j] - B[i][j];
				}
			}
			break;
		case 3:
			for ( i = 0; i < 3; i++) {
				for ( j = 0; j < 3; j++) {
					C[i][j] = A[i][j] * B[i][j];
				}
			}
			break;
		case 4:
			for ( i = 0; i < 3; i++) {
				for ( j = 0; j < 3; j++) {
					C[i][j] = A[i][j] / B[i][j];
				}
			}
			break;
		default:
			printf("Invalid choice, please use 1-4 only.");
	}

	printf("\n The resultant matrix C is:");
	for ( i = 0; i < 3; i++) {
		for ( j = 0; j < 3; j++) {
			printf("|  %d  |",C[i][j]);
		}
		printf("\n\t");
	}

	return 0;
}

int
q4()
{
		int a[10], i, min, max;
		for (i = 0; i < 10; i++) {
			printf("Enter the elements in array a[%d]", i);
			scanf("%d", &a[i]);
		}
		min = max = a[0];
		for (i = 0; i < 10; i++) {
			if (min > a[i]) {
				min = a[i];
			}
			if (max < a[i]) {
					max = a[i];
			}
		}
		printf("The largest element in the array is: %d", max);
		printf("\nThe smallest element in the array is: %d", min);

    return 0;
}

int
q5()
{
    int a[10] = { 1, 5, 3, 2, 0, 5, 7, 6, -1, 10  };

    int max = 0;
    int second_max = 0;

    for( int i = 0; i < 10; i++ ) {
        if( a[i] > max ) {
            second_max = max;
            max = a[i];
        } else if( a[i] > second_max ) {
            second_max = a[i];
        }
    }

    printf("max: %d, second_max: %d\n", max, second_max);
		return 0;
}

int
q6()
{
	int a[10] = { 1, 2, 3, 3, 4, 4, 5, 5, 6, 6 };
	int i, j;
	for (i = 0; i < 10; i++) {
		for (j = 0; j < 10; j++) {
			if (a[i] == a[j] && i != j) {
				break;
		}
		if (j == 9) {
			printf("%d ", a[i]);
			}
		}
	}
	return 0;
}

int
q7()
{
    int i, arr[10], revarr[10];
    printf("Enter 10 elements in an array: ");
    for(i = 0; i < 10; i++) {
        scanf("%d",&arr[i]);
    }
    printf("The array is: \n");
    for(i = 0; i < 10; i++) {
        printf(" %d ",arr[i]);
    }
    for(i = 0; i < 10; i++)
    {
        revarr[i] = arr[9-i];
    }
    printf("\nThe reverse array is: \n");
    for(i = 0;i < 10; i++)
    {
        printf(" %d ",revarr[i]);
    }

		return 0;
}

int
q8()
{
    int i, arr[10], pos[10], neg[10], zero[10];
    int poscount = 0, negcount = 0, zerocount = 0;
    printf("Enter 10 integers: ");
    for( i = 0; i < 10; i++) {
        scanf("%d",&arr[i]);
    }
    printf("The array is: ");
    for(i = 0; i < 10; i++) {
        printf(" %d ",arr[i]);
    }
    for(i = 0;i < 10; i++)
    {
        if(arr[i] > 0) {
            pos[poscount] = arr[i];
            poscount++;
        } else if(arr[i] < 0) {
            neg[negcount] = arr[i];
            negcount++;
        } else {
            zero[zerocount] = arr[i];
            zerocount++;
        }
    }
    printf("\nThe array of positive elements is: ");
    for(i = 0; i < poscount; i++) {
        printf(" %d ",pos[i]);
    }
    printf("\nThe array of negative number is: ");
    for (i = 0;i < negcount; i++) {
        printf("%d ",neg[i]);
    }
    printf("\nThe array of zero elements is: ");
    for(i = 0;i < zerocount; i++) {
        printf("%d ",zero[i]);
    }

		return 0;
}

int
main()
{
    q1();
    q2();
    q3();
    q4();
    q5();
    q6();
    q7();
    q8();
    return 0;
}
