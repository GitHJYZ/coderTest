#include <stdio.h>
#include <stdlib.h>

/**
 * define the struct of list node
 */
typedef struct Nod{
    int data;
    struct Nod* pre;
    struct Nod* next;
} Node;

Node* initList();
int headInsert(Node* L,int data);
int tailInsert(Node* L,int data);
int deleteNode(Node* L,int data);
int destoryList(Node* L);
int printList(Node* L);

/**
 * init a link list
 * @return the head pointer of link list's head
 */
Node* initList()
{
    Node *L = (Node*)malloc(sizeof(Node));
    L->data = 0;
    L->pre = L;
    L->next = L;
    return L;
}

/**
 * insert item in link list's head
 * @param L the head pointer of link list
 * @param data  the data you want to insert
 * @return 0 success / -1 failure
 */
int headInsert(Node* L,int data)
{
    Node *node = (Node*)malloc(sizeof(Node));
    if(node ==NULL)
    {
        return -1;
    }
    node->data = data;
    if(L->data == 0){
        node->next = L->next;
        node->pre = L;
        L->pre = node;
        L->next = node;
    }else{
        node->next = L->next;
        node->pre = L;
        L->next->pre = node;
        L->next = node;
    }
    return 0;
}

/**
 * insert item in link list's tail
 * @param L the head pointer of link list
 * @param data  the data you want to insert
 * @return 0 success / -1 failure
 */
int tailInsert(Node* L,int data)
{
    Node* temp = L;
    while(temp->next != L){
        temp = temp->next;
    }
    Node *node = (Node*)malloc(sizeof(Node));
    if(node ==NULL)
    {
        return -1;
    }
    node->data = data;
    node->pre = temp;
    node->next = L;
    temp->next = node;
    L->pre = node;
    return 0;
}

/**
 * delete item in link list
 * @param L the head pointer of link list
 * @param data  the data you want to delete
 * @return 0 success / -1 failure
 */
int deleteNode(Node* L,int data)
{
    Node* node = NULL;
    if(L == NULL){
        return -1;
    }
    node = L->next;
    while(node != L){
        if(node->data == data){
            node->pre->next = node->next;
            node->next->pre = node->pre;
            free(node);
        }
        node = node->next;
    }
    return 0;
}
/**
 * destory link list
 * @param L the head pointer of link list
 * @return 0 success / -1 failure
 */
int destoryList(Node* L)
{
    if(L == NULL)
    {
        printf("List is NULL\n");
        return 0;
    }
    Node* node = NULL;
    node = L->next;
    while(node != L){
        free(node);
        node = node->next;
    }
    printf("List is destoryed\n");
    return 0;
}

/**
 * print all items in a link list
 * @param L the head pointer of link list
 * @return 0 success / -1 failure
 */
int printList(Node* L)
{
    int node_count = 1;
    Node* node = NULL;
    if(L == NULL)
    {
        return -1;
    }
    node = L->next;
    while(node != L){

        printf("%d : %d ->",node_count,node->data);
        node = node->next;
        node_count++;
    }
    printf("NULL\n");
    return 0;
}
int main()
{
    Node* L = initList();
    headInsert(L,89);
    headInsert(L,67);
    headInsert(L,78);
    headInsert(L,94);
    headInsert(L,87);

    tailInsert(L,13);
    tailInsert(L,56);
    tailInsert(L,59);
    tailInsert(L,99);
    tailInsert(L,133);

    deleteNode(L,133);
    deleteNode(L,67);

    printList(L);
    destoryList(L);

    return 0;
}
