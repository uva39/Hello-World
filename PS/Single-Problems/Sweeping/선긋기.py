# BOJ 2170 선긋기 (https://www.acmicpc.net/problem/2170)
# 2021. 10. 19. 10:00:00    골드5
import sys
input = sys.stdin.readline

n = int(input())
a = sorted(tuple(map(int, input().split())) for _ in range(n))
s, e = a[0]
ans = 0

for i in range(1, n):
    if e < a[i][0]:
        ans += e-s
        s, e = a[i]
    else:
        e = max(e, a[i][1])
ans += e-s
print(ans)