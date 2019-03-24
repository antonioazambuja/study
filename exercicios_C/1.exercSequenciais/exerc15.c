#include <stdio.h>

void main(){
    float sal, sal_bruto, inss, sind, ir = 0;
    int horas = 0;

    printf("informe o salario: ");
    scanf("%f", &sal);
    printf("informe o numero de horas: ");
    scanf("%d", &horas);
    // descontos salarial
    ir = sal * 0.11;
    inss = sal * 0.08;
    sind = sal * 0.05;
    sal_bruto = sal * horas;
    printf("salario bruto mensal: R$%0.2f.\n", sal_bruto);
    printf("ir: R$%0.2f.\n", ir);
    printf("inss: R$%0.2f.\n", inss);
    printf("sindicato: R$%0.2f.\n", sind);
    printf("salario liquido mensal: R$%0.2f.", sal_bruto - ir - inss - sind);
}
