# 행렬을 쉽게 90도 회전하는 파이썬 잡기술

def trace_flip(A:list) -> list:
    """
    Trace를 기준으로 대칭이 되게 행렬 뒤집기 
    (Trace는 보존되고, 그 외는 대칭이 되게 뒤집힘)
    """
    temp = [list(row) for row in list(zip(*A))]
    return temp

def clock(A:list) -> list:
    "시계방향으로 행렬 90도 회전시키기"
    temp = [list(row) for row in list(zip(*A[::-1]))]
    return temp

if __name__ == '__main__':
    # (n * n) size의 정사각행렬 생성
    n = 4
    A = [[i*n + j + 1 for j in range(n)] for i in range(n)]

    f = clock
    g = trace_flip

    print("\n원본 행렬")
    print(*A, sep='\n')
    print("\n\n시계방향으로 90도 회전한 행렬")
    print(*f(A), sep='\n')
    print("\n\n180도 뒤집은 행렬")
    print(*f(f(A)), sep='\n')
    print("\n\n270도 뒤집은 행렬")
    print(*f(f(f(A))), sep='\n')
    print("\n\n360도 뒤집은 행렬")
    print(*f(f(f(f(A)))), sep='\n')
    print("\n\nTrace를 기준으로 대칭이 되게 뒤집은 행렬")
    print(*g(A), sep='\n')
    print("\n\n2번 뒤집은 행렬")
    print(*g(g(A)), sep='\n')