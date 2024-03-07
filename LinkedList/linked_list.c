#include <stdio.h>
#include <stdlib.h>

typedef struct  
{
    int data;
    void *next;

} Node;

Node *head = NULL;


// add to list

Node *addNode(int data){
    Node *new = malloc(sizeof(Node));
    if (head == NULL){
        if (new==NULL) return NULL;
        new->data = data;
        head = new;
        new->next = NULL;
    }else{
        if (new==NULL) return NULL;
        new->data = data;
        new->next = head;
        head = new;


    }
}
//remove a node from list
int removeNode(int data){
    Node *current = head;
    Node *prev = head;
    while (current!=NULL){
        if (current->data == data){
             // if current node is head 
            if (current == head ) head = current->next;
            else {
                prev ->next = current->next; 
            }
            return 1;
        }
        prev = current;
        current= current->next;
    }
    return 0 ;

}
// insert a node in a list
void insertNode(int data, int place){
    Node *insert = malloc(sizeof(Node));
    Node *current = head;
    insert->data = data;
    int count = 1;
    while (current!=NULL && place !=0){
        if (count == place-1){
            int * temp =current->next;
            current->next = insert;
            insert->next =  temp;
            break;
        }else 
        {
        current= current->next;}
        count ++;

    }
    if (place!=0){
        printf("not a good position ");
    }
}
// print the list 
void printlist(){
    Node *current = head ;
    while (current!=NULL){
        printf(" %d -> ",current->data);
        current = current->next;
    }
    printf("\n");
}

// ui
void printMenu(){
    printf("Following things which u can do\n");
    printf("\t 1. ADD something\n");
    printf("\t 2. REMOVE something\n");
    printf("\t 3. INSERT something\n");
    printf("\t 4. PRINT list\n");
    printf("\t 5. QUIT\n");
}

int main(){


    int option =-1;
    while (option!=5){
        printMenu();
        int num = scanf("%d",&option);
        if (num ==1 && option>=1 && option<=5){
            switch (option)
            {
            case 1:
                printf("What to add?\n");
                scanf("%d",&option);
                
                Node *new = addNode(option);
                break;
            case 2:
                // rem
                printf("Which no. to remove\n");
                scanf("%d",&option);
                int succes= removeNode(option);
                if (!succes) printf( "element not found");

                break;

            case 3:
                // insert
                printf (" what to insert and where to insert\n");
                scanf("%d",&option);
                int place ;
                scanf("%d",&place);
                insertNode(option,place);

                break;
            
            case 4:
                printlist();
            case 5:
                break;
            default:
                printf("Invalid option\n");
            }
        }
    }
    return 0;
}