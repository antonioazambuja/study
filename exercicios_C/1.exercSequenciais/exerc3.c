#include <stdio.h>
#include <ctype.h>

void main(){
    float a = 0, b = 0;
    printf("Numero 1: ");
    scanf("%f", &a);
    printf("Numero 2: ");
    scanf("%f", &b);
    printf("Soma: %.2f", a + b);
}
