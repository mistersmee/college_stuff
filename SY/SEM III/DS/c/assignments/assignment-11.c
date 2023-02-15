#include <stdio.h>
#include <stdlib.h>

// Implementation of bubble sort

int
main()
{
	int arr[100], i, j, k, num, temp;

	printf("Enter the number of elements for array:");
	scanf("%d", &num);

	for (i = 0; i < num; i++) {
		printf("Enter the elements in array:");
		scanf("%d", &arr[i]);
	}

	for (i = 0; i < num - 1; i++) {
		for (j = 0; j < num - i - 1; j++) {
			if (arr[j] > arr[j + 1]) {
				temp = arr[j + 1];
				arr[j + 1] = arr[j];
				arr[j] = temp;
			}
			printf("\nThe iteration number %d, sort number %d array looks like:", i, j);
			for (k = 0; k < num; k++) {
				printf(" %d ", arr[k]);
			}
		}
	}
	printf("\nThe final sorted array becomes:");
	for (i = 0; i < num; i++) {
		printf(" %d ", arr[i]);
	}
}
