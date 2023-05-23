#include <stdio.h>
#include <stdlib.h>


typedef struct Node{
    int data;
    struct Node* next;
}DLIST;

DLIST* createList();
int nodeInsert(DLIST *pHead,int pData,int cData);
int nodeDelete(DLIST *pHead,int data);
int reverselist(DLIST *pHead);
int destoryList(DLIST *pHead);
int printList(DLIST *pHead);

DLIST* createList()
{
    DLIST *pHead, *pM, *pCur;
    int data;
    pHead = (DLIST*)malloc(sizeof(DLIST));
    if(pHead == NULL)
    {
        return NULL;
    }
    pHead->data = 0;
    pHead->next = NULL;

    printf("\nplease input node data:");
    scanf("%d",&data);

    pCur = pHead;
    while(data != -1)
    {
        pM = (DLIST*)malloc(sizeof(DLIST));
        if(pM == NULL)
        {
            return NULL;
        }
        pM->data = data;
        pCur->next = pM;
        pM->next = pHead;
        pCur = pM;

        printf("\nplease input node data:");
        scanf("%d",&data);
    }
    return pHead;
}

int nodeInsert(DLIST *pHead,int pData,int cData)
{
    DLIST *pM,*pPre,*pCur;
    if(pHead == NULL)
    {
        return -1;
    }
    pM = (DLIST*)malloc(sizeof(DLIST));
    if(pM == NULL)
    {
        return -1;
    }
    pM->data = cData;
    pM->next = NULL;

    pPre = pHead;
    pCur = pHead->next;

    while(pCur != pHead)
    {
        if(pCur->data == pData)
        {
            pM->next = pCur;
            pPre->next = pM;
            break;

        }
        pPre = pCur;
        pCur = pCur->next;
    }

    if(pCur == pHead)
    {
        printf("no like %d pdata\n",pData);
    }

    return 0;
}

int nodeDelete(DLIST *pHead,int data)
{
    DLIST *pCur,*pPre;
    if(pHead == NULL)
    {
        return -1;
    }
    pPre = pHead;
    pCur = pHead->next;
    while(pCur != pHead)
    {
        if(pCur->data == data)
        {
            break;
        }
        pPre = pCur;
        pCur = pCur->next;
    }

    if(pCur == pHead)
    {
        printf("no like :%d node\n",data);
        return -1;
    }

    pPre->next = pCur->next;
    if(pCur != NULL)
    {
        free(pCur);
    }

    return 0;
}

int reverseList(DLIST *pHead)
{
    DLIST *pTemp,*pPre,*pCur;
    if(pHead == NULL)
    {
        return -1;
    }
    pPre = pHead->next;
    pCur = pHead->next->next;

    while(pCur != pHead)
    {
        pTemp = pCur->next;
        pCur->next = pPre;
        pPre = pCur;
        pCur = pTemp;
    }
    pHead->next->next = pHead;
    pHead->next = pPre;

    return 0;
}

int destoryList(DLIST *pHead)
{
    DLIST *temp =NULL;
    if(pHead == NULL)
    {
        return -1;
    }
    temp = pHead->next;
    while(temp != pHead)
    {
        temp = pHead->next;
        free(pHead);
        pHead = temp;
    }
    printf("DLIST is destory\n");
    return 0;
}

int printDList(DLIST *pHead)
{
    DLIST *temp = NULL;
    if(pHead == NULL)
    {
        return -1;
    }
    temp = pHead->next;
    printf("\nBegin\t");
    while(temp != pHead)
    {
        printf("%d ",temp->data);
        temp = temp->next;
    }
    printf("\tEnd ");
    return 0;
}

int main()
{
    int ret = 0;
    DLIST *pHead = NULL;
    pHead = createList();
    ret = nodeInsert(pHead,56,999);
    ret = printDList(pHead);
    ret = nodeInsert(pHead,999,998);
    ret = printDList(pHead);
    ret = nodeInsert(pHead,998,997);
    ret = nodeDelete(pHead,999);
    ret = printDList(pHead);
    ret = reverseList(pHead);
    ret = printDList(pHead);
    ret = destoryList(pHead);
}
