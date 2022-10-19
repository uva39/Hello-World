import sys
sys.setrecursionlimit(2500) # 분할정복 시에 재귀 깊이를 늘려주면 좋음
p = 1000000007

def matrix_mult(A:list, B:list) -> list:
    temp = [[0]*2 for _ in range(2)] 
    for i in range(2):
        for j in range(2):
            for k in range(2):
                temp[i][j] += (A[i][k] * B[k][j])
                temp[i][j] %= p
    return temp

def matrix_pow(n:int, M:list) -> list:
    if n == 1:
        return M
    if n % 2 == 0:
        temp = matrix_pow(n//2, M)
        return matrix_mult(temp, temp)
    else:
        temp = matrix_pow(n-1, M)
        return matrix_mult(temp, M)

def fibo(n:int) -> int:
    a = ((1, 1), (1, 0))
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return matrix_pow(n-1, a)[0][0]

dp = [0, 1, 1]
for i in range(3, 100):
    dp.append((dp[i-1] + dp[i-2]) % p)

def f(n):
    if n < len(dp):
        return dp[n]
    k = n//2
    # TODO: 어떻게 O(lg(N))으로 줄일 수 없을지? f의 호출을 줄이는 식으로??
    a, b, c, d = f(k+1)%p, f(n-k)%p, f(k)%p, f(n-k-1)%p
    return (a*b%p + c*d%p) % p

if __name__ == '__main__':
    while True:
        try:
            n = int(input())
            print(f"fibo({n}) = {fibo(n)}")
            print(f"new fibo({n}) = {f(n)}")
        except:
            break