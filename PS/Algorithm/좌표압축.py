def compress(arr):
    d = {}
    for i, x in enumerate(sorted(arr)):
        d[x] = i
    return list(map(lambda x: d[x], arr))

if __name__ == '__main__':
    n = int(input())
    coord = [[*map(int, input().split())] for _ in range(n)]
    x = compress([x for x, y in coord])
    y = compress([y for x, y in coord])
    for i in range(n):
        print(x[i], y[i])