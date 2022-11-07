import sys
input = sys.stdin.readline
# BOJ 14500

def dfs(x, y, depth, total):
    global ans
    if depth == 4:
        ans = max(ans, total)
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, depth + 1, total + graph[nx][ny])
            visited[nx][ny] = False

def Tmino(r, c, k):
    if k == 1:
        return graph[r][c] + graph[r][c + 1] + graph[r][c + 2] + graph[r - 1][c + 1]
    elif k == 2:
        return graph[r][c] + graph[r][c + 1] + graph[r][c + 2] + graph[r + 1][c + 1]
    elif k == 3:
        return graph[r][c] + graph[r + 1][c] + graph[r + 2][c] + graph[r + 1][c + 1]
    else:
        return graph[r][c] + graph[r - 1][c + 1] + graph[r][c + 1] + graph[r + 1][c + 1]

n, m = map(int, input().split())
graph = [[*map(int, input().split())] for _ in range(n)]
visited = [[False]*m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = 0

for x in range(n):
    for y in range(m):
        visited[x][y] = True
        dfs(x, y, 1, graph[x][y])
        visited[x][y] = False

        # T-mino 처리
        if x - 1 >= 0 and y + 2 < m:
            ans = max(ans, Tmino(x, y, 1))
        if x + 1 < n and y + 2 < m:
            ans = max(ans, Tmino(x, y, 2))
        if x + 2 < n and y + 1 < m:
            ans = max(ans, Tmino(x, y, 3))
        if x + 1 < n and x - 1 >= 0 and y + 1 < m:
            ans = max(ans, Tmino(x, y, 4))
print(ans)