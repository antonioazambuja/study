#include <stdio.h>

void main(){
    float altura = 0;
    printf("informe a a altura: ");
    scanf("%f", &altura);
    printf("peso ideal: %0.2f KG.", (72.7 * altura) - 58);
}
