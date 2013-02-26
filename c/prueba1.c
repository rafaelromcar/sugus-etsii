#include <stdio.h>

int suma(int a, int b);
void intercambio(int* a, int* b);

int main(){

	printf("Hola Mundo!\n");
	printf("%d\n", suma(3,4));
	
	int* punt1;
	int* punt2;
	int var1=5;
	int var2=7;
	
	printf("Var1: %d, var2: %d.\n", var1, var2);
	
	punt1=&var1;
	punt2=&var2;

	printf("Punt1: %d, punt2: %d.\n", *punt1, *punt2);
	printf("Cambiamos  con la función intercambio");

	intercambio(*punt1, *punt2);
	printf("Punt1: %d, punt2: %d.\n", *punt1, *punt2);

	
}

int suma(int a, int b){

	int res= a+b;
	return res;
}

void intercambio(int* a, int* b){
	int aux = *a;
	*a=*b;
	*b=aux;
}

