#include <stdio.h>
int test(int arr[], int size);
int main(){
    int arr[3] = {1,2,3};
    int ret = test(arr, 3);
    printf("sum is %d\n", ret);
}
int test(int arr[], int size){
    int sum = 0;
    for (int i=0; i<size; i++){
        sum += arr[i];
    }
    return sum;
}
