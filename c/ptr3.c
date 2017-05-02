#include <stdio.h>
int main(){
    int list[3] = {1, 2, 3};
    int *ptr;
    ptr = list;
    for (int i=0;i<3;i++){
        printf("address: list[%d] = %p\n", i, ptr);
        ptr ++;
    }
}
