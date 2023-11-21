#include <stdio.h>

int main() {
    int AngkaPertama, AngkaKedua, i, j, x, y;
    scanf("%d %d", &AngkaPertama, &AngkaKedua);
    x = AngkaPertama;
    y = AngkaKedua;

    if (AngkaPertama > AngkaKedua) {
        for(i = AngkaPertama, j = AngkaKedua; i >= AngkaKedua, j <= AngkaPertama; i--, j++) {
                while(AngkaPertama >= AngkaKedua){
                printf("%d %d - ", AngkaPertama, AngkaKedua);
                AngkaPertama--;
                AngkaKedua++;
                continue;
            }
            printf("%d %d - ", AngkaPertama, AngkaKedua);
            AngkaPertama--;
            AngkaKedua++;
            if(AngkaPertama == y){
                    printf("%d %d", AngkaPertama, AngkaKedua);
            }
        }
    }
    else {
        for(i = AngkaPertama, j = AngkaKedua; i <= AngkaKedua, j >= AngkaPertama; i++, j--) {
                while(AngkaPertama <= AngkaKedua){
                printf("%d %d - ", AngkaPertama, AngkaKedua);
                AngkaPertama++;
                AngkaKedua--;
                continue;
            }
            printf("%d %d - ", AngkaPertama, AngkaKedua);
            AngkaPertama++;
            AngkaKedua--;
            if(AngkaKedua == x){
                    printf("%d %d", AngkaPertama, AngkaKedua);
            }
        }
    }
    return 0;
}