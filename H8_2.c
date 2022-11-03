#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>
#define MAX 100000

void selection_sort(int* arr, const int length);
void bubble_sort(int* arr, const int length);

int main(){
    int a[MAX] = {};
    int b[MAX] = {}; // a의 복사
    int pointer = 0;
    do{
        scanf("%d", &a[pointer]);
        b[pointer] = a[pointer]; // 복사
        pointer++;
    }while (getchar() != '\n');

    printf("정렬 이전의 값: ");
    for (int i = 0; i < pointer; i++)
        printf("%d, ", a[i]);
    printf("\n");

    selection_sort(a, pointer);
    bubble_sort(b, pointer);

    printf("선택정렬: ");
    for (int i = 0; i < pointer; i++) // a
        printf("%d, ", a[i]);
    printf("\n");
    printf("버블정렬: ");
    for (int i = 0; i < pointer; i++) // b
        printf("%d, ", b[i]);
    printf("\n");

    return 0;
}

void selection_sort(int* arr, const int length){
    int minidx, i, j, temp;
    for (i = 0; i < length; i++){
        minidx = i;
        // 최소값의 인덱스 구하기
        for (j = i+1; j < length; j++){
            if (arr[j] < arr[i])
                minidx = j;
        }
        // swap
        temp = arr[minidx];
        arr[minidx] = arr[i];
        arr[i] = temp;
    }
}

void bubble_sort(int* arr, const int length){
    int i, j, temp;
    for (i = 0; i < length - 1; i++){
        for (j = 0; j < length - 1 - i; j++){
            if (arr[j] > arr[j+1]){
                // 2중 for문으로 전체 원소에 대해서 반복한 다음,
                // 순서가 올바르지 않다면 swap
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}