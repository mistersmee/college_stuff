#include <stdio.h>

// Queue insertion

int
main()
{
    int rear = -1, MAX, front = -1, i = 0;

    printf("Enter the max size of the queue:");
    scanf("%d", &MAX);

    int queue[MAX];

    for ( i = 0; i <= MAX; i++) {
        if (rear == MAX) {
            printf("\nQueue overflow.");
        } else if (front == -1 && rear == -1) {
            front = 0;
            rear = 0;
        } else {
            printf("Enter the item to be inserted in queue:");
            scanf("%d", &queue[rear]);
            rear++;
        }
    }

    printf("The queue is:");

    for (int i = 0; i < MAX; i++) {
        printf(" %d ", queue[i]);
    }
    return 0;
}
