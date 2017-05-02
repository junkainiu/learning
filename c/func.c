#include <stdio.h>

int max(int num1, int num2);

int main()
{
    int a = 300;
    int b = 200;
    int ret;
    ret = max(a, b);
    printf("Max value is : %d\n", ret);
    return 0;
}
int max(int num1, int num2){
    if (num1 > num2){
        return num1;
    } else {
        return num2;
    }
}
