from math import gcd

n = int(input())
arr = [*map(int, input().split())]
prefix = [gcd(i, j) for i in range(1, n+1) for j in range(1, n+1)]
for i in range(n):
    for j in range(n):
        if arr[i] == arr[j]:
            continue
        if arr[i] % arr[j] == 0 and gcd(i+1, j+1) == 1:
            print(j+1, i+1)
            exit()