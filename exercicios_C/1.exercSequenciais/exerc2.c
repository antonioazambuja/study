# include <stdio.h>
#include <ctype.h>

void main(){
    int num;
    do{
        fflush(stdin);
        printf("\nInforme o numero: ");
        scanf("%i", &num);
        if(isdigit(num) == 1)
            printf("entrada incorreta");
        else
            printf("\nNumero informado: %d", num);
    }while(isdigit(num) == 1);
}
