#include <stdio.h>

void main(){
    int i = 0;
    float num, soma = 0;
    float vetor[4] = {0};
    for(i = 0; i < 4; i++){
        printf("INFORME A NOTA: ");
        scanf("%f", &vetor[i]);
        soma += vetor[i];
    }
    printf("Media das notas: %.2f", soma / i);
}
