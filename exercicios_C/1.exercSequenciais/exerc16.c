#include <stdio.h>
#include <math.h>

void main(){
    int latas, litros = 0;
    float preco, metros = 0;

    printf("informe o tamanho em metros: ");
    scanf("%f", &metros);
    litros = metros / 3;
    latas = ceil(litros / 18);
    printf("qtd de latas necessarias: %d latas.\n", latas);
    preco = latas * 80.00;
    printf("preco total: R$%0.2f.\n", preco);
}
