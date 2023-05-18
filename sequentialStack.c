#include <stdio.h>
#include <stdlib.h>

#define STACK_SIZE 3 //the stack capacity
#define STACK_INCREMENT 2  //expend capacity

/**
 * define the struct of stack data
 */
typedef struct {
  int data;
}Data;

/**
 * define the struct of stack
 */
typedef struct {
  Data *base;
  Data *top;
  int stackSize;
}Stack;


/**
 * init the Sequential stack
 * @param S the stack initialized
 * @return 0 success / -1 malloc failure
 */
int initStack(Stack *S){
    S->base = (Data*)malloc(STACK_SIZE * sizeof(Data));
    if(!S->base) return -1;
    S->top = S->base;
    S->stackSize = STACK_SIZE;
    return 0;
}

/**
 * destroy the stack
 * @param S the stack destroyed
 * @return 0  stack is empty / 1 success
 */
int destroyStack(Stack *S){
  if(!S->base) return 0;
  free(S->base);
  S->base = S->top = NULL;
  S->stackSize = 0;
  return 1;
}

/**
 * push element in the stack
 * @param s be push stack
 * @param d be push data
 * @return 0 success / -1 failure
 */
int pushStack(Stack *s, Data *d){
  if(s->top - s->base >= s->stackSize){
    s->base = (Data *)realloc(s->base, (s->stackSize + STACK_INCREMENT)*sizeof(Data));
    if(s->base == NULL) return -1;
    printf("expend the stack %d\n",STACK_INCREMENT);
    s->top = s->base + s->stackSize;
    s->stackSize += STACK_INCREMENT;
  }
  *s->top ++ = *d;
  return 0;
}

/**
 * display element in the stack
 */
void displayData(Data *d){
  if(!d) return;
  printf("data : %5d\n", d->data);
}

/**
 * ergodic the stack
 * @return 0  stack is empty / 1 success
 */
int displayStack(Stack *s){
    if(s->top == s->base) return 0;
    Data *p = s->base;
    while(p != s->top){
        displayData(p);
        p++;
    }
    return 1;
}

/**
 * testcase
 * @param s a stack
 * @param n the data number be test
 */
void test(Stack *s, int n){
  Data d;
  for(int i = 0; i < n; i ++){
    printf("please input stack data\n");
    scanf("%d", &d.data);
    pushStack(s, &d);
  }
}

/**
 * pop data
 * @param s a stack
 * @param d the data be pop
 * @return 0  stack is empty / 1 success
 */
int pop(Stack *s,Data *d){
    if(s->top == s->base) return 0;
    *d = *(-- s->top);
    return 1;
}

/**
 * check the stack
 * @param s a stack
 * @return stackSize;
 */
int empty(Stack *s){
    if(s->top == s->base) return 0;
    return s->top - s->base;
}
int main(){

    Stack S;
    initStack(&S);

    test(&S,5);

    displayStack(&S);

    printf("after pop the element in the stack\n");

    Data d;
    pop(&S,&d);

    displayStack(&S);
    printf("the pop element\n");
    displayData(&d);

    printf("element number in the stack %d\n",empty(&S));

    destroyStack(&S);
  return 0;
}
