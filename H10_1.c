#include <stdio.h>
#include <stdlib.h>

int** readTable(int* row, int *col);
int rowMinimum(int* rowPtr, int col);
int rowMaximum(int* rowPtr, int col);
float rowAverage(int* rowPtr, int col);

int main(){
    printf("=== The Statistics of a Table ===\n");
    printf("%4s %6s %6s %15s", "Row", "Min", "Max", "Average\n");

    FILE* f;
    f = fopen("in.txt", "r");
    if (f == NULL) {
        printf("input file open error !\n");
        return 1;
    }
    int row, col;
    fscanf(f, "%d %d", &row, &col);
    int** table = readTable(&row, &col);
    for (int i = 0; i < row; i++){
        printf("%4d %6d %6d %15.2f", i, rowMinimum(table[i], col),
        rowMaximum(table[i], col), rowAverage(table[i], col));
    }
    for (int i = 0; i < row; i++){
        free(table[i]);
    }
    free(table);
    fclose(f);
    return 0;
}

int** readTable(int* row, int* col){
    int** table = (int**)malloc(*row * sizeof(int*));
    for (int i = 0; i < *row; i++){
        table[i] = (int*)malloc(*col * sizeof(int));
    }
    for (int i = 0; i < *row; i++){
        for (int j = 0; j < *col; j++){
            fscanf(f, "%d", &table[i][j]); // error
        }
    }
    return table;
}

int rowMinimum(int* rowPtr, int col){
    int min = rowPtr[0];
    for (int i = 1; i < col; i++){
        if (rowPtr[i] < min) min = rowPtr[i];
    }
    return min;
}

int rowMaximum(int* rowPtr, int col){
    int max = rowPtr[0];
    for (int i = 1; i < col; i++){
        if (rowPtr[i] > max) max = rowPtr[i];
    }
    return max;
}

float rowAverage(int* rowPtr, int col){
    float sum = 0;
    for (int i = 0; i < col; i++){
        sum += rowPtr[i];
    }
    return sum / col;
}