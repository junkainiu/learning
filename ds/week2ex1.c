List Merge(List L1, List L2){
    List L,s,l1,l2;
    L=(List)malloc(sizeof(List));
    L->Next=NULL;
    l1 = L1->Next;
    l2 = L2->Next;
    s = L;
    while(l1&&l2){
        if (l1->Data <= l2->Data) {
            s->Next = l1;
            s = s->Next;
            l1 = l1->Next;
        } else {
            s->Next = l2;
            s = s->Next;
            l2 = l2->Next;
        }
    }
    if(l1){
        s->Next = l1;
    }

    if(l2){
        s->Next = l2;
    }
    L1->Next = NULL;
    L2->Next = NULL;
    return L;
}
