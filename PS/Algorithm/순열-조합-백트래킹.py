from itertools import *

n = 5
r = 3
arr = list(range(1, n+1))

# 파이썬 내장 모듈을 통한 순열, 조합, 중복순열, 중복조합
if __name__ == '__main__':
    print(f"{n} 순열 {r}")
    print(*permutations(arr, r))

    print(f"{n} 조합 {r}")
    print(*combinations(arr, r))

    print(f"{n} 중복순열 {r}") # 중복순열 = 집합에서의 데카르트 곱이다.
    print(*product(arr, repeat=r))

    print(f"{n} 중복조합 {r}")
    print(*combinations_with_replacement(arr, r))


# 제너레이터를 이용해서 조합 구현
# itertools보다 훨씬 느림( -> 직접 구현은 비추)
def nCr(arr, r):
    # 백트래킹 + 제너레이터로 조합 만들기
     for i in range(len(arr)):
        if r == 1:  # 종료 조건
            yield [arr[i]]
        else:
            for next in nCr(arr[i+1:], r-1):
                yield [arr[i]] + next
print(*nCr(arr, r))


def nHr(arr, r):
    # 백트래킹 + 제너레이터로 중복조합 만들기
    for i in range(len(arr)):
        if r == 1: # 종료 조건
            yield [arr[i]]
        else:
            for next in nHr(arr[i:], r-1):
                yield [arr[i]] + next
print(*nHr(arr, r))