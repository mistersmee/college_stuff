#include <stdio.h>

int
q36()
{
	int size, i, *my_array;

	printf("\n Please type the size of array:");

	scanf("%d", &size);

	my_array=(int*)malloc(size * sizeof(int));

	printf("\n Enter the values of Array:  ");

	for ( i = 0; i < size; i++ ) {
		scanf("%d", &my_array[i]);
	}
	printf("\n The values in the array are: ");
	for ( i = 0; i < size; i++ ){
		printf("%d  ", my_array[i]);
	}
	printf("\n");
	return 0;
}

int
q37()
{
	int arr[5] = {1,2,3,4,5};
	int sum = 0, i;
	for (i = 0; i < 5; i++) {
		sum += arr[i];
	}
	printf("The sum of all array elements is: %d", sum);
	return 0;
}

int
q38()
{
	int size, i;
	char *my_array;

	printf("\n Please type the size of string:");

	scanf("%d", &size);

	my_array = (char*)malloc(size * sizeof(char));

	printf("\n Enter a string:");
	scanf("%s", my_array);
	printf("\n The string is: %s", my_array);
	return 0;
}


int
q39()
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
