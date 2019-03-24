#include <stdio.h>

void main(){
    int peso_exc = 0;
    float peso, excesso, multa = 0;
    printf("informe a quant de peixe: KG ");
    scanf("%f", &peso);
    peso_exc = (int)(peso - 50);
    printf("peso excedente: KG %d.", peso_exc);
    printf("multa por peso excedente: R$%d.", peso_exc * 4);
}
