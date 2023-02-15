#include <stdio.h>

// Linear Queue using array

int choice, item, rear = -1, front = -1, i;

int queue[5], max = 5;


void enq();
void deq();
void display();

int
main()
{

	printf("Linear queue operations using array:");
	printf("\n\t 1. Enqueue");
	printf("\n\t 2. Dequeue");
	printf("\n\t 3. Display");
	printf("\n\t 4. Exit");
	do {
		printf("\nEnter your choice:");
		scanf("%d", &choice);
		switch(choice)
		{
			case 1:
				enq();
				break;
			case 2:
				deq();
				break;
			case 3:
				display();
				break;
			case 4:
				printf("Exiting.");
				break;
			default:
				printf("Enter a valid choice[1/2/3/4]:");
				break;
		}
	} while (choice != 4);
}

void
enq()
{
	if (rear == max - 1) {
		printf("Queue overflow.");
	} else if ( front == -1 && rear == -1) {
		front = 0;
		rear = 0;
	} else {
		printf("Enter the element you want to insert:");
		scanf("%d", &item);

		queue[rear] = item;
		printf("Item inserted.");
		rear++;
	}
}

void
deq()
{
    if (front == -1 || front > rear)
    {
        printf("Queue Underflow \n");
        return;
    } else {
        printf("Element deleted from queue is : %d\n", queue[front]);
        queue[front] = 0;
	front = front + 1;
    }
}

void display() {
	printf("The queue is:");
	for (i = 0; i < rear; i++) {
		printf(" %d ", queue[i]);
	}
}
