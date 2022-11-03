#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

// 함수 원형
void func(int a, int b, int* add, int* sub, int* div, int* mod);

int main(){
    int a, b;
    int add, sub, div, mod;
    printf("Enter two integers : ");
    scanf("%d %d", &a, &b);
    func(a, b, &add, &sub, &div, &mod);
    printf("%d + %d = %d\n", a, b, add);
    printf("%d - %d = %d\n", a, b, sub);
    printf("%d / %d = %d\n", a, b, div);
    printf("%d %% %d = %d\n", a, b, mod);
}

void func(int a, int b, int* add, int* sub, int* div, int* mod){
    *add = a + b;
    *sub = a - b;
    *div = a / b;
    *mod = a % b;
    return;
}