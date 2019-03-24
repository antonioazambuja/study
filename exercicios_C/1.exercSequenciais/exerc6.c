#include <stdio.h>
#include <math.h>
#define PI 3.1415

void main(){
    float raio = 0;
    printf("informe o raio: ");
    scanf("%f", &raio);
    printf("area: %f", pow(raio,2) * PI);
}
