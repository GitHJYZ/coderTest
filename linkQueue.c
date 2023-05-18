#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

/**
 * define the struct of queue data
 */
typedef struct node{
    int data;
    struct node* next;
}Node;

/**
 * define the struct of queue
 */
typedef struct {
    Node *front;
    Node *tail;
}LinkQueue;

/**
 * check the queue
 */
bool emptyQueue(LinkQueue *q){
    if(!q) return q->front == NULL;
}

/**
 * init the linkQueue
 * @param q the queue initialized
 * @return 0 success / -1 malloc failure
 */
int initQueue(LinkQueue *q){
    emptyQueue(q);
    q->front = (Node *)malloc(sizeof(Node));
    q->tail = q->front;
    if(!q->tail) return -1;
    q->front->next = NULL;
    return 0;
}

/**
 * destroy the linkQueue
 * @param q the queue destroy
 * @return 0 success
 */
int destroyQueue(LinkQueue *q){
    emptyQueue(q);
    while(q->front){
        q->tail = q->front->next;
        free(q->front);
        q->front = q->tail;
    }
    printf("LinkQueue was destroyed\n");
    return 0;
}

/**
 * destroy the linkQueue
 * @param q the queue push
 * @return 0 success
 */
int pushQueue(LinkQueue *q, Node *node){
    emptyQueue(q);
    q->tail->next = node;
    q->tail = node;
    return 0;
}

/**
 * pop the linkQueue
 * @param q the queue pop
 * @return 0 success
 */
int popQueue(LinkQueue *q){
    emptyQueue(q);
	if (q->front->next == NULL){
		free(q->front);
		q->front = q->tail = NULL;
	}
	else{
		Node *t = q->front->next;
		free(q->front);
		q->front = t;
	}
	return 0;
}

/**
 * print the linkQueue node
 * @param d the queue node
 */
void outputValue(Node *d){
    if(!d) return;
    printf("%d\n", d->data);
}

/**
 * ergodic the LinkQueue
 * @return 0 success
 */
int displayQueue(LinkQueue *q){
    emptyQueue(q);
    Node *p = q->front->next;
    while(p){
        outputValue(p);
        p = p->next;
    }
    return 0;
}
/**
 * the linkQueue node
 * @param d the queue node
 */
void inputValue(Node *d){
    if(!d) return;
    printf("please input data\n");
    scanf("%d", &d->data);
}

/**
 * creat the linkQueue node
 * @param d the queue node
 * @return the queue node
 */
Node* creatNode(Node *d){
    Node *node = (Node*)malloc(sizeof(Node));
    if(!node) return NULL;
    node->data = d->data;
    node->next = NULL;
    return node;
}

/**
 * testcase
 */
void test(LinkQueue *q){
    Node d;
    Node *n;
    emptyQueue(q);
    for(int i = 1; i < 5; i ++){
        inputValue(&d);
        n = creatNode(&d);
        pushQueue(q, n);
    }
}

int main(){

    LinkQueue q;

    initQueue(&q);

    test(&q);

    printf("after push\n");
    displayQueue(&q);

    popQueue(&q);
    popQueue(&q);

    printf("after pop\n");
    displayQueue(&q);

    destroyQueue(&q);

    return 0;
}
