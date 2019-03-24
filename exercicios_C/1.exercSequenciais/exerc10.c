#include <stdio.h>
#include <math.h>

void main(){
    float temp = 0;
    printf("informe a temperatura em graus Celsius: ");
    scanf("%f", &temp);
    printf("temperatura em graus Farenheit: %.2f", (temp * 9/5) + 32);
}
