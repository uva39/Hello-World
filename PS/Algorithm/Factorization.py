import sys
sys.setrecursionlimit(4000) # 분할정복 시 재귀깊이 늘리기
from math import gcd
input = sys.stdin.readline

# 필요 시 (2, 7, 61)보다 더 많은 소수 사용
checking_primes = (2, 7, 61)

def Miller_Rabin(n:int, _a:int) -> bool:
    "밀러-라빈 구현부"
    d = (n-1) // 2
    while d % 2 == 0:
        if pow(_a, d, n) == n-1:
            return True
        d //= 2
    t = pow(_a, d, n)
    return True if t in (n-1, 1) else False

# 밀러-라빈 최적화를 위한 에라토스테네스의 체 set
eras = [True] * 101
for i in range(2, 11):
    if eras[i]:
        for j in range(i*2, 101, i):
            eras[j] = False
eras = set([i for i in range(101) if eras[i]][2:])

def isPrime(n:int) -> bool:
    if n <= 1:
        return False
    if n <= 100:
        return True if n in eras else False
    for i in checking_primes:
        if not Miller_Rabin(n, i):
            return False
    return True

def pollard_rho(n, x):
    def g(x, n):
        return (x*x + 1) % n

    if isPrime(n):
        return n
    else:
        # 소수가 아니지만, [1, 100] 사이의 소수를 나누는 경우는 최적화를 위해 바로 처리함
        for i in eras:
            if n % i == 0:
                return i
    p = y = x
    d = 1
    while d == 1:
        x = g(x, n)
        y = g(g(y, n), n)
        d = gcd(abs(x-y), n)
    if d == n:
        return pollard_rho(n, p+1)
    else:
        if isPrime(d):
            return d
        else:
            return pollard_rho(d, 2)

if __name__ == '__main__':
    n = int(input())
    ans = []
    while n != 1:
        k = pollard_rho(n, 2)
        ans.append(int(k))
        n //= k
    ans.sort()
    print(*ans, sep='\n')