#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void main(){
    float area = 0;

    printf("informe o comprimento de um lado do quadrado: ");
    scanf("%f", &area);
    area *= 4;
    printf("dobro da area: %.2f metros.", area * 2);
}
