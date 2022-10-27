#include <stdio.h>
#include <stdlib.h>

struct node {
	int data;
	struct node *next;
};

int
main()
{

//	Initial linked list

	struct node *head;

	head = (struct node *)malloc(sizeof(struct node));
	
	head->data = 10;
	head->next = NULL;

//	Insertion at the beginning
	
	struct node *temp;
	temp = (struct node*)malloc(sizeof(struct node));

	temp->data = 20;
	temp->next = NULL;

//	Insertion at the end


	if (head == NULL) {
		temp = malloc(sizeof(struct node));
		temp->data = 50;
		temp->next = NULL;
		head = temp;
	} else {
		temp = head;
		while (temp->next != NULL) {
			temp = temp->next;
		}

		r = malloc(sizeof(struct node));
		r->data = 60;
		r->next = NULL;
		temp->next = r;
	}
}
