from itertools import \
    permutations, combinations, product, combinations_with_replacement

# 제너레이터를 이용해서 조합 구현
# 리스트 덧셈때문에 itertools보다 훨씬 느림
# 슬라이싱 도배때문에 메모리도 개많이 씀
# 직접 구현은 비추

def nCr(arr, r):
    # 백트래킹 + 제너레이터로 조합 만들기
     for i in range(len(arr)):
        if r == 1:  # 종료 조건
            yield [arr[i]]
        else:
            for next in nCr(arr[i+1:], r-1):
                yield [arr[i]] + next

def nHr(arr, r):
    # 백트래킹 + 제너레이터로 중복조합 만들기
    for i in range(len(arr)):
        if r == 1: # 종료 조건
            yield [arr[i]]
        else:
            for next in nHr(arr[i:], r-1):
                yield [arr[i]] + next

def nPr(arr, r, _prefix=None):
    # 백트래킹 + 제너레이터로 순열 만들기
    # 중복처리를 위해 _prefix 사용
    for i in range(len(arr)):
        if arr[i] == _prefix:
            continue
        if r == 1: # 종료 조건
            yield [arr[i]]
        else:
            _prefix = arr[i]
            for next in nPr(arr, r-1, _prefix):
                yield [arr[i]] + next
def nPIr(arr, r):
    # 백트래킹 + 제너레이터로 순열 만들기
    for i in range(len(arr)):
        if r == 1: # 종료 조건
            yield [arr[i]]
        else:
            for next in nPIr(arr, r-1):
                yield [arr[i]] + next


if __name__ == '__main__':
    n = 4
    r = 2
    arr = list(range(1, n+1))

    # 파이썬 내장 모듈을 통한 순열, 조합, 중복순열, 중복조합
    print(f"{n} 순열 {r}")
    print(*permutations(arr, r))
    print(f"{n} 조합 {r}")
    print(*combinations(arr, r))
    print(f"{n} 중복순열 {r}") # 중복순열 = 집합에서의 데카르트 곱이다.
    print(*product(arr, repeat=r))
    print(f"{n} 중복조합 {r}")
    print(*combinations_with_replacement(arr, r))

    print('\n\n 직접 구현한 제너레이터들')
    print("\n순열")
    print(*nPr(arr, r))
    print("\n조합")
    print(*nCr(arr, r))
    print("\n중복순열")
    print(*nPIr(arr, r))
    print("\n중복조합")
    print(*nHr(arr, r))