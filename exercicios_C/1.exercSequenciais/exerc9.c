#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void main(){
    float temp = 0;
    printf("informe a temperatura em graus Farenheit: ");
    scanf("%f", &temp);
    printf("temperatura em graus Celsius: %.2f", (5 * (temp - 32) / 9));
}
