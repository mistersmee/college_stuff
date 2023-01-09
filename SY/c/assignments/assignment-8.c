#include <stdio.h>
#include <stdlib.h>

// Implementation of Queue using linked list

struct node {
    int data;
    struct node *next;
};

struct node *front = NULL;
struct node *rear = NULL;


void enqueue(int value) {
    struct node * ptr;
    ptr = malloc(sizeof(struct node));
    ptr->data = value;
    ptr->next = NULL;
    if ((front == NULL) && (rear == NULL)) {
        front = rear = ptr;
    } else {
        rear->next = ptr;
        rear = ptr;
    }
    printf("\nNode is Inserted.");
}

int dequeue() {
    if (front == NULL) {
        printf("\nUnderflow.");
        return -1;
    } else {
        struct node *temp = front;
        int temp_data = front->data;
        front = front->next;
        free(temp);
        return temp_data;
    }
}

void display() {
    struct node * temp;
    if ((front == NULL) && (rear == NULL)) {
        printf("\nQueue is Empty.");
    } else {
        printf("\nThe queue is:");
        temp = front;
        while (temp) {
            printf(" %d ", temp->data);
            temp = temp->next;
        }
    }
}

int main() {
    int choice, value;
    printf("\nImplementation of Queue using Linked List:");
    while (choice != 4) {
        printf("\n1.Enqueue\n2.Dequeue\n3.Display\n4.Exit\n");
        printf("\nEnter your choice:");
        scanf("%d", &choice);
        switch (choice) {
            case 1:
                printf("\nEnter the value to insert:");
                scanf("%d", &value);
                enqueue(value);
                break;
            case 2:
                printf("\nDequeued element is :%d", dequeue());
                break;
            case 3:
                display();
                break;
            case 4:
                exit(0);
                break;
            default:
                printf("Please choose only between 1-4.");
        }
    }
    return 0;
}
