#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define LIST_INII_SIZE 5  //SqList capacity
#define LIST_INCREMENT 2  //extend capacity

/**
 * define the struct of SqList data
 */
typedef struct {
    int data;
}Data;

/**
 * define the struct of SqList
 */
typedef struct {
    Data *d;
    int length;
    int listsize;
}SqList;

/**
 * init the Sequential SqList
 * @param L the SqList initialized
 * @return 0 success / -1 exit
 */
int initSqList(SqList *L){

  L->d = (Data *)malloc(LIST_INII_SIZE * sizeof(Data));
  if(!L->d) exit(-1);
  L->length = 0;
  L->listsize = LIST_INII_SIZE;

  return 1;
}

/**
 * destroy the SqList
 * @param L the SqList destroyed
 * @return 0  SqList is empty / 1 success
 */
int destorySqList(SqList *L){
  if(L->d == NULL) return 0;
  free(L->d);
  L->length = 0;
  L->listsize = 0;

  return 1;
}

/**
 * display data in the SqList
 * @param L the SqList display
 */
void displaySqList(SqList* L){
  int i = 0;
  for(int i = 0; i < L->length; i++){
    printf("data%5d \n",L->d[i].data);
  }
}

/**
 * findDataSqList in the SqList
 * @param L the SqList find
 * @param d be find Data
 * @return 0  not find / 1 success
 */
int findDataSqList(SqList *L,Data *d){
  int i = 0;
  while(i < L->length){
    if((L->d[i].data) == d->data) return 1;
    i++;
  }
  return 0;
}

/**
 * displayValue in the SqList
 * @param d be display Data
 */
void displayValue(Data *d){
  if(!d) return;
  printf("data=%5d \n",d->data);
}

/**
 * extendSqList in the SqList
 * @param L be extend SqList
 * @return 0 success / -1 exit
 */
int extendSqList(SqList *L){
  Data *p = (Data*)realloc(L->d,(L->listsize + LIST_INCREMENT)*sizeof(Data));
  if(!p) exit(-1);
  L->d = p;
  L->listsize += LIST_INCREMENT;
   return 0;
}

/**
 * copyValue in the SqList
 * @param d1 copyed Data
 * @param d2 copy Data
 */
void copyValue(Data *d1,Data *d2){
  d1->data = d2->data;
}

/**
 * insertLastSqList in the SqList
 * @param L be insert SqList
 * @param dv be insert Data
 */
void insertLastSqList(SqList *L,Data *dv){
  if(L->length >= L->listsize) extendSqList(L);
  copyValue(&L->d[L->length],dv);
  L->length++;
}

/**
 * insertLocSqList in the SqList
 * @param L be insert SqList
 * @param i be insert position
 * @param dv be insert Data
 * @return 0  SqList is empty / 1 success
 */
int insertLocSqList(SqList *L,int i, Data *dv){
  if(i < 0 || i > L->length-1) return 0;
  if(L->length >= L->listsize) extendSqList(L);
  for(int j = L->length; j > i; j--){
    copyValue(&L->d[j],&L->d[j-1]);
  }

  copyValue(&L->d[i],dv);

  L->length++;
  return 1;
}

/**
 * deleteLocSqList in the SqList
 * @param L be delete SqList
 * @param i be delee position
 * @return 0  SqList is empty / 1 success
 */
int deleteLocSqList(SqList *L,int i){
    if(i < 0 || i > L->length-1) return 0;
    for(int j = i; j < L->length; j++){
        copyValue(&L->d[j-1],&L->d[j]);
  }
  L->length--;
  return 1;;
}

int main(){

  SqList L;
  Data d;

  initSqList(&L);
  for(int i = 0; i < L.listsize; i++){
    printf("input data\n");
    scanf("%d", &L.d[i].data);
    L.length ++;
  }

  displaySqList(&L);
  printf("display result\n");
  Data dp = {10};
  findDataSqList(&L, &dp);
  displayValue(&dp);
  printf("After insert the SqList\n");
  insertLastSqList(&L, &dp);
  displaySqList(&L);
  printf("Specify the insertion element position \n");
  insertLocSqList(&L, 3, &dp);
  displaySqList(&L);
  printf("deleteLocSqList element position \n");
  deleteLocSqList(&L,4);
  displaySqList(&L);

  destorySqList(&L);
  return 0;
}
