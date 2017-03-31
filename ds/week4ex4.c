BinTree Delete(BinTree BST, ElementType X){
    BinTree b;
    if(!BST){
        printf("Not Found\n");
    }
    else if(X > BST->Data){
        BST->Right = Delete(BST->Right, X);
    } else if(X < BST->Data){
        BST->Left = Delete(BST->Left, X);
    } else if(X == BST->Data){
        if (BST->Left && BST->Right){
            b = FindMin(BST->Right);
            BST->Data = b->Data;
            BST->Right = Delete(BST->Right, b->Data);
        }else{
            if(!BST->Right){
                BST = BST->Left;
            }else{
                BST = BST->Right;
            }
        }
    }
    return BST;
}

BinTree Insert(BinTree BST, ElementType X){
    BinTree b, s;
    b = (BinTree)malloc(sizeof(BinTree));
    b->Data = X;
    s = BST;
    if (!s) {
        return b;
    }
    while (s){
        if (X > s->Data){
            if (s->Right) {
                s = s->Right;
            } else{
                s->Right = b;
                break;
            }
        } else if(X < s->Data){
            if (s->Left) {
                s = s->Left;
            } else {
                s->Left = b;
                break;
            }
        }
    }
    return BST;
}

Position Find(BinTree BST, ElementType X){
    BinTree b;
    b = BST;
    if (!b){
        return NULL;
    }
    if (b->Data == X) {
        return b;
    } else if(b->Data > X) {
        return Find(b->Left, X);
    } else {
        return Find(b->Right, X);
    }
}

Position FindMin(BinTree BST) {
    BinTree b;
    b = BST;
    if(BST){
        while(b->Left){
            b = b->Left;
        }
    }
    return b;
}

Position FindMax(BinTree BST) {
    BinTree b;
    b = BST;
    if(BST){
        while(b->Right){
            b = b->Right;
        }
    }
    return b;
}
