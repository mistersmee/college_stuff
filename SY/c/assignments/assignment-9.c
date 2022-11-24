#include <stdio.h>

int
main() 
{
    int key, i = 0, num;
    printf("Enter the number of elements you want in array:");
    scanf("%d", &num);
    int arr[num];
    for (i = 0; i < num; i++) {
        printf("Enter the numbers in array:");
        scanf("%d", &arr[i]);
    }    
    
    printf("Enter the key you want to search:");
    scanf("%d", &key);

    for (i = 0; i < num; i++) {
        if (arr[i] == key) {
            break;
        }
    }
    if (arr[i] == key) {
        printf("\n%d Key found at %d position.", arr[i], i + 1);
    } else {
        printf("\nKey not found in array.");
    }
}