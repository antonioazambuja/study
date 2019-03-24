#include <stdio.h>
#include <stdlib.h>

void main(){
    int i = 0;
    float metros = 0;
    printf("INFORME O TAMANHO EM METROS: ");
    scanf("%f", &metros);
    printf("Valor em centimetros %.2f cm.", metros * 100);
}
