#include <stdio.h>

void main(){
    float val, horas = 0;
    printf("informe o valor da sua hora: ");
    scanf("%f", &val);
    printf("informe o numero de horas: ");
    scanf("%f", &horas);
    printf("O seu salario e: R$ %.2f", val * horas);
}
