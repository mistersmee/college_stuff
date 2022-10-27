#include <stdio.h>

# define max 5

int queue[max];
int front = -1;
int rear = -1;

void
enqueue(int element)
{
	if(front == -1 && rear == -1) {
		front = 0;
		rear = 0;
		queue[rear] = element;
	} else if((rear + 1) % max == front) {
		printf("Queue is overflow.");
	} else {
		rear=(rear + 1) % max;
		queue[rear] = element;
	}
}


int
dequeue()
{
	if(front == -1 && rear == -1) {
		printf("\nQueue is underflow.");
	} else if(front == rear) {
		printf("\nThe dequeued element is %d", queue[front]);
		front = -1;
		rear = -1;
	} else {
		printf("\nThe dequeued element is %d", queue[front]);
		front=(front + 1) % max;
	}
}

void 
display() {
        int i;
        if(front == -1 && rear == -1) {
                printf("\n Queue is empty.");
        } else {
                printf("\n Elements in the queue are: ");
                for (i = front; i != rear; i = (i + 1) % max) {
                        printf("%d ", queue[i]);
                }
                printf("%d ", queue[i]);
        }
}

int
main()
{
	int choice = 1, x;

	 do {
		printf("\nPress 1: Insert an element.");
		printf("\nPress 2: Delete an element.");
		printf("\nPress 3: Display the queue.");
		printf("\nPress 4: Exit.");
		printf("\nEnter your choice:");
		scanf("%d", &choice);

		switch(choice) {
			case 1:
				printf("Enter the element which is to be inserted:");
				scanf("%d", &x);
				enqueue(x);
				break;
			case 2:
				dequeue();
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
	} while(choice != 4);
	return 0;
}
