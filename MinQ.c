#include <stdio.h>

int main() {
    // Inserir os valores desejados e o real
    double x[] = {1, 2, 3, 4, 5};   // Valor encontrado
    double y[] = {2.2, 2.8, 3.6, 4.5, 5.1}; // Valor desejado
    int n = 5;   // Números de amostras

    double alfa, ro;
    double sumx = 0, sumy = 0, sumxy = 0, sumxx = 0;

    for (int i = 0; i < n; i++) {
        sumx += x[i];
        sumy += y[i];
        sumxy += x[i] * y[i];
        sumxx += x[i] * x[i];
    }

    alfa = ( n * sumxy - sumx * sumy )/( n * sumxx - sumx * sumx );
    ro = ( sumy * sumxx - sumxy * sumx )/( n * sumxx - sumx * sumx );

    printf("O valor de ro = %.4f \n O valor de alfa = %.4f\n",ro, alfa);

    return 0;
}