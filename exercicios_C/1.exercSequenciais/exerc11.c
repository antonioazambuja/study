#include <stdio.h>
#include <math.h>

void main(){
    int a, b = 0;
    float c, result_a, result_b, result_c = 0;
    printf("informe o primeiro numero inteiro: ");
    scanf("%d", &a);
    printf("informe o segundo numero inteiro: ");
    scanf("%d", &b);
    printf("informe o numero decimal: ");
    scanf("%f", &c);
    result_a = (a * 2) * ((float)b / 2);
    result_b = (a * 3) + c;
    printf("o produto do dobro do primeiro com metade do segundo: %0.1f.\n", result_a);
    printf("a soma do triplo do primeiro com o terceiro: %0.1f.\n", (float)result_b);
    printf("o terceiro elevado ao cubo: %0.2f.", pow(c,3));
}
