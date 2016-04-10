//Will Bowditch
//Define the binary search tree
#include "bst.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

BSTnode *createNode(void *item){
	BSTnode *node = (BSTnode*)malloc(sizeof(BSTnode));
	node->item = item;
	node->left = NULL;
	node->right = NULL;
	return node;
}

BSTnode *find(BSTnode *n, void *item, int compare(void *,void *)){

	if(compare(n->item,item) == 0){
		return  n;
	}
	if(compare(n->item,item) > 0){ //if the current node is less than the value we're looking for, we go right
		if(n->right == NULL){
			return n;
		}
		else{
			return find(n->right,item,compare);
		}
	}
	else{
		if(n->left == NULL){
			return n;
		}
		else{
			return find(n->left,item,compare);
		}
	}
}


void insert(BSTnode *n, void *item, int compare(void *,void *)){

	if(compare(n->item,item)>0){
		if(n->right == NULL){
			BSTnode *new_node = createNode(item);
			n->right = new_node;
		}
		else{
			insert(n->right, item,compare);
		}
	}
	else if(compare(n->item,item)<0){
		if(n->left == NULL){
			BSTnode *new_node = createNode(item);
			n->left = new_node;
		}
		else{
			insert(n->left, item,compare);
		}
	}

}
