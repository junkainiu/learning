#include <stdio.h>
int main(){
    typedef struct Books{
        int a;
        int b;
    }Book;
    Book book;
    book.a = 1;
    book.b = 2;
    printf("Books.a is %d\n", book.a);
}
