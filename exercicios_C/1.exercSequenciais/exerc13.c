#include <stdio.h>
#include <string.h>

void main(){
    char gen = "";
    float altura = 0;
    do{
        fflush(stdin);
        printf("informe o genero: ");
        gen = getchar();
    }while(toupper(gen) != 'H' && toupper(gen) != 'M');
    printf("informe a altura: ");
    scanf("%f", &altura);
    if (toupper(gen) == 'H'){
        printf("peso ideal de homem: %0.2f KG.", (float)(72 * altura) - 58);
    }else
    printf("peso ideal de mulher: %0.2f KG.", (float)(62.1 * altura) - 44.7);
}
