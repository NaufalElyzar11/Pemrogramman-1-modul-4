#include <stdio.h>

int genap(int angka){
    for(int i = angka; i >= 1; --i) {
        if (i % 2 == 0) {
            printf("%d ", i);
        }
    }
    printf("\n");
}

int ganjil(int angka){
    for(int i = 1; i <= angka; ++i) {
        if (i % 2 != 0) {
            printf("%d ", i);
        }
    }
    printf("\n");
}

int main(){
    int angka;
    scanf("%d", &angka);
    ganjil(angka);
    genap(angka);
}