#include <stdio.h>
int calc(int balance[], int size);
int main(){
    int balance[] = {10, 20 ,30};
    int ret = calc(balance, 3);
    printf("sum is %d\n", ret);
    for (int i=0;i<3;i++){
        printf("balance[%d] is %d\n", i, balance[i]);
    };
}

int calc(int balance[], int size){
    int sum;
    for (int i=0;i<size; i++){
        balance[i] += i;
        sum += balance[i];
    };
    return sum;
}
