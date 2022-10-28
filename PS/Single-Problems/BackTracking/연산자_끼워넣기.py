import sys
input = sys.stdin.readline

n = int(input())
num = [*map(int, input().split())]
op = [*map(int, input().split())]  # +, -, *, //

maximum = -int(1e9)
minimum = int(1e9)

def dfs(depth, total, plus, minus, multiply, divide):
    global maximum, minimum
    if depth == n:
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

# 다른 풀이

# 순열 (Python3 시간초과 / PyPy3는 통과)
import sys
from itertools import permutations

input = sys.stdin.readline
N = int(input())
num = list(map(int, input().split()))
op_num = list(map(int, input().split()))  # +, -, *, /
op_list = ['+', '-', '*', '/']
op = []

for k in range(len(op_num)):
    for i in range(op_num[k]):
        op.append(op_list[k])

maximum = -1e9
minimum = 1e9


def solve():
    global maximum, minimum
    for case in permutations(op, N - 1):
        total = num[0]
        for r in range(1, N):
            if case[r - 1] == '+':
                total += num[r]
            elif case[r - 1] == '-':
                total -= num[r]
            elif case[r - 1] == '*':
                total *= num[r]
            elif case[r - 1] == '/':
                total = int(total / num[r])

        if total > maximum:
            maximum = total
        if total < minimum:
            minimum = total


solve()
print(maximum)
print(minimum)