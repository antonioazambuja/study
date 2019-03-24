#include <stdio.h>
#include <math.h>

void main(){
    float metros, litros, menor = 0;
    int galao, latas, galao_mist, lata_mist, litros_mist, mist = 0;
    printf("informe o tamanho em metros: ");
    scanf("%f", &metros);
    litros = metros / 6;
    latas = ceil(litros / 18);
    galao = ceil(litros / 3.6);
    if (latas <= 0)
        printf("1 lata, custando R$80.00.\n");
    else
        printf("%d latas, custando R$%d.\n", latas, latas * 80);
    if (galao <= 0)
        printf("1 galao, custando R$25.00.\n");
    else
        printf("%d galoes, custando R$%d.\n", galao, galao * 25);
    if(latas <= galao)
        menor = latas * 80;
    else
        menor = galao * 25;
    do{
        mist += 25;
        galao_mist += 1;
        mist += 80;
        lata_mist += 1;
    }while(mist < menor);
    //mist = (galao_mist * 20) + (lata_mist * 80);
    printf("Valor de tintas com %d galoes e %d latas misturadas com preco de %d.", galao_mist, lata_mist, mist);
}
