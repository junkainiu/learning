#include <stdio.h>
#include <time.h>
void getSecond(unsigned long *ptr);
int main(){
    unsigned long sec;
    getSecond(&sec);
    printf("the value of sec is %ld\n", sec);
}

void getSecond(unsigned long *ptr){
    *ptr = time(NULL);
}
