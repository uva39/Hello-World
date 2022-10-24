# 필요 시 (2, 7, 61)보다 더 많은 소수 사용
checking_primes = (2, 7, 61)

# 에라스토테네스의 체. n 크기 늘려도 됨
size = 100
eras = [True]*(size + 1)
for i in range(2, int((size + 2)**0.5)+1):
    if eras[i]:
        for j in range(i*2, size + 1, i):
            eras[j] = False
eras = set([i for i in range(2, size) if eras[i]])

def miller_rabin(n:int, _a:int) -> bool:
    "밀러-라빈 구현부"
    d = (n-1) // 2
    while d % 2 == 0:
        if pow(_a, d, n) == n-1:
            return True
        d //= 2
    t = pow(_a, d, n)
    return True if t in (n-1, 1) else False

def isPrime(n):
    if n <= 1:
        return False
    if n <= size:
        return True if n in eras[n] else False
    for a in checking_primes:
        if not miller_rabin(n, a):
            return False
    return True

# Test1: 24815323469403931728221172233738523533528335161133543380459461440894543366372904768334987264000000000000000000479
# Test2: 9876543217
if __name__ == '__main__':
    while True:
        try:
            num = int(input())
            print(isPrime(num))
        except:
            break