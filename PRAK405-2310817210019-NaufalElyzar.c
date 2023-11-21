#include <stdio.h>

int main(){
    int x, y, a,b,c;
    a = 0;b = 0;c = 0;
    scanf("%d", &x);
    scanf("%d", &y);
    for(int i = 0; i < x; i++){
        for(int j = i; j >= 0; j--){
            printf("(%d * %d)", j+1, y);
            if(j > 0){printf(" + ");}}
        a = (i+1)* y;
        b = b + a;
        printf(" = %d\n",b);
        c = c + b;
    }
    printf("%d\n", c);
    return 0;
}