#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#define MAX 100000

// 함수 원형
void add_element(int value, int set[], int* cp);
void delete_element(int value, int set[], int* cp);
int has_element(int value, int set[], const int *cp);
void print_set(int set[], const int *cp);

// 전역변수
int set[MAX];
int cp = 0;

int main(){
    char command;
    int value;

    while (1){
        printf("Enter commands : ");
        command = getchar();
        if (command == 'q') return 0; // q [정수]가 아니라, q만 입력했을 때 꺼짐

        scanf("%d", &value);
        while (getchar() != '\n') {}; // 입력버퍼 비우기

        if (command == 'a') add_element(value, set, &cp);
        else if (command == 'd') delete_element(value, set, &cp);
        else printf("wrong command. try again.\n");
    }
}

void add_element(int value, int set[], int* cp){
    if (has_element(value, set, cp))
        printf("%d is already in the set.\n", value);
    else
        set[(*cp)++] = value;
    print_set(set, cp);
    return;
}

void delete_element(int value, int set[], int* cp){
    int i = has_element(value, set, cp);
    if (i){
        // 받아온 인덱스는 +1된 거라서, 다시 1 빼줌
        for (i--; i < *cp; i++){
            set[i] = set[i+1];
        }
        (*cp)--;
    }
    else
        printf("%d is not in the set.\n", value);
    print_set(set, cp);
    return;
}

int has_element(int value, int set[], const int *cp){
    for (int i = 0; i < *cp; i++){
        if (set[i] == value)
            return i+1; // 인덱스 정보 반환. 인덱스가 0인 경우 대비해서 +1
    }
    return 0;
}

void print_set(int set[], const int *cp){
    for (int i = 0; i < *cp; i++)
        printf("%d ", set[i]);
    printf("\n");
    return;
}