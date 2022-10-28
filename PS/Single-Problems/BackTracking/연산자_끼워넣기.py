import sys
input = sys.stdin.readline

n = int(input())
nums = [*map(int, input().split())]
a, b, c, d = map(int, input().split())
oper = '+'*a + '-'*b + '*'*c + '/'*d
print(oper)
using = []
ans = []
def backtracking(k, n = n):
    if k == n:
        ans.append(using)
        return
    for i in range(n-1):
        if oper[i] not in using:
            using.append(oper[i])
            backtracking(k+1)
            using.pop()# 백트래킹 (Python3 통과, PyPy3도 통과)
import sys

input = sys.stdin.readline
N = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))  # +, -, *, //

maximum = -1e9
minimum = 1e9


def dfs(depth, total, plus, minus, multiply, divide):
    global maximum, minimum
    if depth == N:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    if plus:
        dfs(depth + 1, total + num[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - num[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * num[depth], plus, minus, multiply - 1, divide)
    if divide:
        dfs(depth + 1, int(total / num[depth]), plus, minus, multiply, divide - 1)


dfs(1, num[0], op[0], op[1], op[2], op[3])
print(maximum)
print(minimum)


backtracking(0)
print(ans)
