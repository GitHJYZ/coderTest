#include <stdio.h>
#include <stdlib.h>

/**
 * define the struct of list node
 */
typedef struct Nod{
    int data;
    struct Nod* pre;
    struct Nod* next;

}Node;

Node* initList();
int headInsert(Node* L,int data);
int tailInsert(Node* L,int data);
int findNode(Node* L,int data);
int deleteNode(Node* L,int data);
int destoryList(Node* L);
int printList(Node* L);

/**
 * init a link list
 * @return the head pointer of link list's head
 */
Node* initList()
{
    Node* L = (Node*)malloc(sizeof(Node));
    L->data = 0;
    L->pre = NULL;
    L->next = NULL;

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
    Node* node = (Node*)malloc(sizeof(Node));
    if(node == NULL){
        return -1;
    }
    node->data = data;
    if(L->data == 0){
        node->pre = L;
        node->next = L->next;
        L->next = node;
    }else{
        node->pre = L;
        node->next = L->next;
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
    while(temp->next != NULL){
        temp = temp->next;
    }

    Node* node = (Node*)malloc(sizeof(Node));
    if(node == NULL){
        return -1;
    }
    node->data = data;

    node->pre = temp;
    node->next = NULL;
    temp->next = node;

    return 0;
}

/**
 * find item in link list
 * @param L the head pointer of link list
 * @param data  the data you want to insert
 * @return 0 success / -1 failure
 */
int findNode(Node* L,int data)
{
    int node_count = 0;
    Node* node = NULL;
    if(L == NULL){
        return -1;
    }
    node = L->next;
     while(node != NULL){
        if(node->data == data){
            node_count++;
        }
        node = node->next;
    }
    if(node_count != 0){
        printf("this node have %d is %d\n",node_count,data);
    }else {
        printf("these is no node like this\n");
        return -1;
    }
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
    int node_count = 0;
    Node* node = NULL;
    if(L == NULL){
        return -1;
    }
    node = L->next;
    while(node != NULL){
        if((node->data == data) && (node->next != NULL)){
            node->pre->next = node->next;
            node->next->pre = node->pre;
            node_count++;
            free(node);
        }else if((node->data == data) && (node->next == NULL)){
            node->pre->next = NULL;
            node_count++;
            free(node);
        }
        node = node->next;
    }

    if(node_count == 0){
        printf("the node is absent\n");
        return -1;
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
    while(node != NULL){
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

    Node* node = NULL;
    if(L == NULL){
        printf("list is NULL\n");
        return 0;
    }
    int node_count = 1;
    node = L->next;
    while(node != NULL){
        printf("%d : %d ->",node_count,node->data);
        node = node->next;
        node_count++;
    }
    printf("NULL\n");
    return 0;
}

int  main()
{
    Node* L = initList();

    headInsert(L,78);
    headInsert(L,69);
    headInsert(L,87);
    headInsert(L,58);
    headInsert(L,11);
    headInsert(L,11);
    headInsert(L,11);

    tailInsert(L,151);
    tailInsert(L,151);
    tailInsert(L,151);
    tailInsert(L,589);
    tailInsert(L,121);
    tailInsert(L,654);
    tailInsert(L,569);

    printList(L);
    deleteNode(L,11);
    deleteNode(L,151);
    printList(L);
    findNode(L,151);
    deleteNode(L,569);
    deleteNode(L,11);
    printList(L);
    destoryList(L);
    return 0;
}
