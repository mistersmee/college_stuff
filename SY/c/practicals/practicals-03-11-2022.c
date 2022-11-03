#include <stdio.h>
#include <stdlib.h>

struct node {
	int data;
	struct node *next;
};

struct node *head;

void begininsert();
void lastinsert();
void randominsert();
void begindelete();
void lastdelete();
void randomdelete();
void display();


int
main()
{
	int choice;
	while (choice != 8) {
		printf("\nThe operations for linked list are:");
		printf("\n\t 1. Insert data at the beginning.");
		printf("\n\t 2. Insert data at the end.");
		printf("\n\t 3. Insert data at a specified location.");
		printf("\n\t 4. Delete data at the beginning.");
		printf("\n\t 5. Delete data at the end.");
		printf("\n\t 6. Delete data at a specified location.");
		printf("\n\t 7. Display linked list.");
		printf("\n\t 8. Quit.");
		printf("\n\nEnter your choice:");
		scanf("%d", &choice);
		switch(choice) {
			case 1: 
				begininsert();
				break;
			case 2:
				lastinsert();
				break;
			case 3:
				randominsert();
				break;
			case 4:
				begindelete();
				break;
			case 5:
				lastdelete();
				break;
			case 6:
				randomdelete();
				break;
			case 7:
				display();
				break;
			case 8:
				return 0;
		}
	}
}

void
begininsert() 
{
	struct node *ptr;
	int data;
	ptr = malloc(sizeof(struct node));
	printf("Enter the element you want to enter:");
	scanf("%d", &ptr->data);
	ptr->next = head;
	head = ptr;
}

void
lastinsert()
{
	struct node *ptr, *last;
	if (head == NULL) {
		ptr = malloc(sizeof(struct node));
		printf("Enter the element you want to enter:");
		scanf("%d", &ptr->data);
		ptr->next = NULL;
		head = ptr;
	} else {
		ptr = head;
		while (ptr->next != NULL) {
			ptr = ptr->next;
		}
		last = malloc(sizeof(struct node));
		printf("Enter the element you want to enter:");
		scanf("%d", &last->data);
		last->next = NULL;
		ptr->next = last;
	}
}

void
randominsert()
{
	struct node *ptr, *trgt;
	int i, loc;
	
	printf("Enter the location you want to insert data at:");
	scanf("%d", &loc);
	
	ptr = head;
	for (i = 0; i < loc; i++) {
		ptr = ptr->next;
		if (ptr == NULL) {
			printf("List overflow, there are less than %d elements in the list.", loc);
			return;
		}
	}
	trgt = malloc(sizeof(struct node));
	printf("Enter the element you want to enter:");
	scanf("%d", &trgt->data);
	trgt->next = ptr->next;
	ptr->next = trgt;
}

void
begindelete()
{
	struct node *ptr;
	if (head == NULL) {
		printf("List empty, underflow.");
	} else {
		ptr = head;
		head = head->next;
		free(ptr);
	}
}

void
lastdelete()
{
	struct node *ptr, *del;
	if (head == NULL) {
		printf("List empty, overflow.");
	} else if (head->next == NULL) {
		head = NULL;
		free(head);
	} else {
		ptr = head;
		while (ptr->next != NULL) {
			del = ptr;
			ptr = ptr->next;
		}
		del->next = NULL;
		free(ptr);
	}
}


void
randomdelete()
{
	struct node *ptr, *trgt;
	int i, loc;
	
	printf("Enter the location you want to insert data at:");
	scanf("%d", &loc);
	
	ptr = head;
	for (i = 0; i < loc; i++) {
		trgt = ptr;
		ptr = ptr->next;
		if (ptr == NULL) {
			printf("List overflow, there are less than %d elements in the list.", loc);
			return;
		}
	}
	trgt->next = ptr->next;
	free(ptr);
}

void
display()
{
	struct node *ptr;
	ptr = head;
	while (ptr != NULL) {
		printf("\n%d", ptr->data);
		ptr = ptr->next;
	}
}
