#include <stdio.h>
#include <stdlib.h>

/**
 * define the struct of tree data
 */
typedef struct {
    int data;
}Data;

/**
 * define the struct of tree node
 */
typedef struct node{
  Data d;
  char ch;
  struct node *lchild,*rchild;
}NODE;

/**
 * inputValue
 * @param d the pointer of the tree data
 */
void inputValue(Data *d){
  if(!d) return;
  printf("please intput data：\n");
  scanf("%d",&d->data);
}

/**
 * creatNode the tree
 * @param d d the pointer of the tree data
 * @return node success  / -1 malloc failure
 */
NODE *creatNode(Data *d){
  if(!d) return NULL;
  NODE *node = (NODE*)malloc(sizeof(NODE));
  if(!node) exit(-1);
  node->d = *d;
  printf("node flag is：");
  fflush(stdin);
  scanf("%c",&node->ch);
  node->lchild = node->rchild = NULL;

  return node;
}

/**
 * CreatTree
 * @param tree the pointer of the tree node
 * @return return the created tree
 */
NODE *creatTree(NODE *tree){
  int tag = 0;
  printf("Is there a left or right subtree? If so, enter 1; otherwise, enter 0；");
  scanf("%d",&tag);
  if(tag != 0){
    Data d;
    inputValue(&d);
    tree = creatNode(&d);
    tree->lchild = creatTree(tree->lchild);
    tree->rchild = creatTree(tree->rchild);
  }
  return tree;
}

/**
 * destroyTree
 * @param tree the pointer of the tree node
 */
void destroyTree(NODE *tree){
  if(tree != NULL){
    destroyTree(tree->lchild);
    destroyTree(tree->rchild);
    free(tree);
  }
}

/**
 * outputValue
 * @param d the pointer of the Data
 */
void outputValue(Data *d){
  if(!d) return;
  printf("data%-5d\n",d->data);
}

/**
 * preOrderTree
 * @param tree the pointer of the tree node
 */
void preOrderTree(NODE *tree){
  if(tree != NULL){
    outputValue(&tree->d);
    printf("%c\n",tree->ch);
    preOrderTree(tree->lchild);
    preOrderTree(tree->rchild);
  }
}

/**
 * inOrderTree
 * @param tree the pointer of the tree node
 */
void inOrderTree(NODE *tree){
  if(tree != NULL){
    inOrderTree(tree->lchild);
    outputValue(&tree->d);
    printf("%c\n", tree->ch);
    inOrderTree(tree->rchild);
  }
}

/**
 * postOrderTree
 * @param tree the pointer of the tree node
 */
void postOrderTree(NODE *tree){
  if(tree != NULL){
     postOrderTree(tree->lchild);
     postOrderTree(tree->rchild);
     outputValue(&tree->d);
     printf("%c\n", tree->ch);
  }
}

/**
 * numNode
 * @param tree the pointer of the tree node
 * @param num the out argument
 */
void numNode(NODE *tree,int *num){
  if(tree != NULL){
    numNode(tree->lchild,num);
    numNode(tree->rchild,num);
    (*num)++;
  }
}

int main(){
  NODE *tree = creatTree(tree);

  printf("\n");
  inOrderTree(tree);
  printf("\n");

  int num = 0;
  numNode(tree, &num);
  printf("%d\n", num);

  destroyTree(tree);

  return 0;

}
