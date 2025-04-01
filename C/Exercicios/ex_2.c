/*Contador de numeros pares, até o numero de imput */

#include <stdio.h>


int main(){

    int contador=0, limite;

    printf("Digite o limite para saber os numeros pares de 0 ate ele: ");
    scanf("%d",&limite);

    while (contador < limite)
    {
        contador++;
        if(contador % 2==0){
            printf("\n%d",contador);
        }
    }
    
printf("\nFim");
}