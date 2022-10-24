# 적록색약 - bfs, dfs : https://www.acmicpc.net/problem/10026

import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y, graph):
    global n
    q = deque([[x, y]])
    visited[x][y] = True

    dx = [-1, 1, 0, 0]
    dy = [ 0, 0, 1,-1]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not (0 <= nx < n and 0 <= ny < n):
                continue
            if graph[x][y] == graph[nx][ny] and not visited[nx][ny]:
                q.append([nx, ny])
                visited[nx][ny] = True

n = int(input())
g = [input().rstrip() for _ in range(n)]
h = [row.replace('G', 'R') for row in g]
normal, odd = 0, 0

visited = [[False]*n for _ in range(n)]
for x in range(n):
    for y in range(n):
        if not visited[x][y]:
            bfs(x, y, g)
            normal += 1

visited = [[False]*n for _ in range(n)]
for x in range(n):
    for y in range(n):
        if not visited[x][y]:
            bfs(x, y, h)
            odd += 1
print(normal, odd)