#include <stdio.h>
#include <stdlib.h>

struct node {
	int data;
	struct node *next;
};

struct node *top = NULL;

void push(int x);
void pop();
void display();

int
main()
{
	int choice, n;
	
	do {
		printf("\nOperations on stack:");
		printf("\n\t1. Push");
		printf("\n\t2. Pop");
		printf("\n\t3. Display");
		printf("\n\t4. Quit");

		printf("\nEnter your choice of operation [1/2/3/4]:");
		scanf("%d", &choice);

		switch(choice) {
			case 1:
				printf("\nEnter a number:");
				scanf("%d", &n);
				push(n);
				break;
			case 2:
				pop();
				break;
			case 3:
				display();
				break;
			case 4:
				break;
			default:
				printf("\nPlease type only 1-4.");
				break;
		}
	} while (choice != 4);

	return 0;
}

void push (int x)  
{  
    struct node *ptr = malloc(sizeof(struct node));   
    
	if(ptr == NULL) {  
        printf("\nStack is empty.");   
    } else {    
        if(top == NULL) {         
            ptr->data = x;  
            ptr->next = NULL;  
            top = ptr;  
        } else {  
            ptr->data = x;  
            ptr->next = top;  
            top = ptr;  
        }  
        printf("\nItem pushed.");  
    }
}  
  
void pop()  
{  
    int item;  
    struct node *ptr;  
    if (top == NULL)  
    {  
        printf("\nUnderflow.");  
    }  
    else  
    {  
        item = top->data;  
        ptr = top;  
        top = top->next;  
        printf("\nItem: %d popped.", item);
		free(ptr);  
    }  
}  

void display()  
{  
    int i;  
    struct node *ptr;  
    
	ptr = top;
	  
    if(ptr == NULL) {  
        printf("\nStack is empty.");  
    } else {  
        printf("\nPrinting Stack elements:");  
        while(ptr != NULL) {  
            printf("\n%d",ptr->data);  
            ptr = ptr->next;  
        }
    }  
}  
