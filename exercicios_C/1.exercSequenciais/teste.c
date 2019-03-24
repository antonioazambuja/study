#include <stdio.h>
#include <string.h>

int main(){
    /*
    int i, tam = 0;
    char a[2];
    scanf("%s", &a);
    for(i = 0; i < strlen(a); i++){
        fflush(stdin);
        printf("posicao %d: %d\n", i, (int)a[i]);
    }
    */
    char s[2];
    scanf("%2[^\n]", &s);
    printf("%d", atoi(s));
}
