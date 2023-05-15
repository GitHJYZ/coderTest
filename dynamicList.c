#include <stdio.h>
#include <stdlib.h>

/**
 * define the struct of list node
 */
typedef struct Node{
    int data;
    struct Node* next;
}DLIST;

DLIST* CreateLIST();
int nodeInsert(DLIST *pHead,int pData,int cData);
int nodeDelete(DLIST *pHead,int data);
int reverseList(DLIST *pHead);
int destoryList(DLIST *pHead);
int printList(DLIST *pHead);

/**
 * creat a link list
 * @return the head pointer of link list's head
 */
DLIST* CreateLIST()
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
    while(data !=-1)
    {
        pM = (DLIST*)malloc(sizeof(DLIST));
        if(pM == NULL)
        {
            return NULL;
        }
        pM->data = data;
        pCur->next = pM;
        pM->next = NULL;
        pCur = pM;

        printf("\nplease input node data:");
        scanf("%d",&data);
    }
    return pHead;
}

/**
 * insert item in link between pData cData
 * @param pHead the head pointer of link list
 * @param pData the data you want to insert before
 * @param cData the data you want to insert after
 * @return 0 success / -1 failure
 */
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

    while(pCur)
    {
        if(pCur->data == pData)
        {
            break;
        }
        pPre = pCur;
        pCur = pCur->next;
    }

    pM->next = pCur;
    pPre->next = pM;

    return 0;
}

/**
 * delete item in link list
 * @param pHead the head pointer of link list
 * @param data  the data you want to delete
 * @return 0 success / -1 failure
 */
int nodeDelete(DLIST *pHead,int data)
{
    DLIST *pCur,*pPre;
    if(pHead == NULL)
    {
        return -1;
    }
    pPre = pHead;
    pCur = pHead->next;
    while(pCur)
    {
        if(pCur->data == data)
        {
            break;
        }
        pPre = pCur;
        pCur = pCur->next;
    }
    //É¾³ý²Ù×÷
    if(pCur == NULL)
    {
        printf("no like £º%d node\n",data);
        return -1;
    }

    pPre->next = pCur->next;

    if(pCur != NULL)
    {
        free(pCur);
    }
    return 0;
}

/**
 * reverse item in link list
 * @param pHead the head pointer of link list
 * @return 0 success / -1 failure
 */
int reverseList(DLIST *pHead)
{
    DLIST *pTemp,*pPre,*pCur;
    if(pHead == NULL)
    {
        return -1;
    }

    pPre = pHead->next;
    pCur = pHead->next->next;

    while(pCur)
    {
        pTemp = pCur->next;
        pCur->next = pPre;
        pPre = pCur;
        pCur = pTemp;
    }

    pHead->next->next = NULL;
    pHead->next = pPre;

    return 0;
}

/**
 * destory link list
 * @param pHead the head pointer of link list
 * @return 0 success / -1 failure
 */
int destoryList(DLIST *pHead)
{
    DLIST *temp = NULL;
    if(pHead == NULL)
    {
        return -1;
    }
    while(pHead)
    {
        temp = pHead->next;
        free(pHead);
        pHead = temp;
    }
    printf("DLIST is destory\n");
    return 0;
}

/**
 * print all items in a link list
 * @param pHead the head pointer of link list
 * @return 0 success / -1 failure
 */

int printDList(DLIST* pHead)
{
    DLIST* temp = NULL;
    if(pHead == NULL)
    {
        return -1;
    }
    temp = pHead->next;
    printf("\nBegin\t");
    //while(temp != pHead)
    while(temp)
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
    pHead = CreateLIST();
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

    return 0;
}
