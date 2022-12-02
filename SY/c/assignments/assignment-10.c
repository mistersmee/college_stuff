#include <stdio.h>

int
main()
{
    int key, i = 0, mid, low, high, num, flag = 0;

    printf("Enter the number of elements you want in array:");
    scanf("%d", &num);
    int arr[num];

    for (i = 0; i < num; i++) {
        printf("Enter the numbers in array:");
        scanf("%d", &arr[i]);
    }

    printf("Enter the key you want to search:");
    scanf("%d", &key);

    low = 0;
    high = num - 1;
    while (low <= high) {
        mid = low + (high - low) / 2;
        if (arr[mid] == key) {
            flag = 1;
            break;
        } else if (arr[mid] < key) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    if (flag != 0) {
        printf("%d Element found at %d position.", arr[mid], mid + 1);
    } else {
        printf("Element not found.");
    }
}
