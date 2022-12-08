#include <stdio.h>
#include <stdlib.h>

int
main() 
{
	int arr[100], i, j, k, temp, positions, num;

	printf("Enter the number of elements for array:");
	scanf("%d", &num);

	for (i = 0; i < num; i++) {
		printf("Enter the elements in array:");
		scanf("%d", &arr[i]);
	}	


	for (i = 0; i < num - 1; i++) {
		positions = i;
		for (j = i + 1; j < num; j++) {
			printf("\nThe iteration number %d, sort number %d array looks like:", i, j);
			for (k = 0; k < num; k++) {
				printf(" %d ", arr[k]);
			}
			if (arr[positions] > arr[j]) {
				positions = j;
				temp = arr[i];
				arr[i] = arr[positions];
				arr[positions] = temp;
			}	
		}
	}

	printf("\nThe final sorted array becomes:");
	for (i = 0; i < num; i++) {
		printf(" %d ", arr[i]);
	}

}