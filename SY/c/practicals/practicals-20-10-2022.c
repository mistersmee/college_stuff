#include <stdio.h>

int choice, item, rear = -1, front = -1, i;

int queue[5], max = 5;


void enq();
void deq();
void displaylq();

int
lqueue()
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
				displaylq();
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
    if (front == - 1 || front > rear)
    {
        printf("Queue Underflow \n");
        return ;
    } else {
        printf("Element deleted from queue is : %d\n", queue[front]);
        front = front + 1;
    }
}

void
displaylq() {
	printf("The queue is:");
	for (i = 0; i < rear; i++) {
		printf(" %d ", queue[i]);
	}
}


// Circular queue

# define max 5

int cqueue[max];
int cfront = -1, crear = -1;

void
enqueue(int element)
{
	if(cfront == -1 && crear == -1) {
		cfront = 0;
		crear = 0;
		cqueue[crear] = element;
	} else if((crear + 1) % max == cfront) {
		printf("Queue is overflow.");
	} else {
		crear=(crear + 1) % max;
		cqueue[crear] = element;
	}
}


int
dequeue()
{
	if(cfront == -1 && crear == -1) {
		printf("\nQueue is underflow.");
	} else if(cfront == crear) {
		printf("\nThe dequeued element is %d", cqueue[cfront]);
		cfront = -1;
		crear = -1;
	} else {
		printf("\nThe dequeued element is %d", cqueue[cfront]);
		cfront=(cfront + 1) % max;
	}
}

void
display()
{
	int i = cfront;
	if(cfront == -1 && crear == -1) {
		printf("\n Queue is empty.");
	} else {
		printf("\nElements in a Queue are:");
		while(i <= crear) {
			printf(" %d ", cqueue[i]);
			i++;
		}
	}
}

int
c_queue()
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

int
main()
{
	lqueue();
	c_queue();
}
