#include <stdio.h>
int main(){
    char *names[] = {
        "Ab",
        "Bb",
        "Cb",
        "Db"
    };
    for (int i=0;i<4;i++){
        printf ("value of name[%d] is %s\n", i, names[i]);
    }
    return 0;
}
