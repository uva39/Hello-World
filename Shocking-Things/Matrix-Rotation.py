# 행렬을 쉽게 90도 회전하는 파이썬 잡기술

def counterclock(A:list) -> list:
    "반시계 방향으로 행렬 90도 회전시키기"
    temp = [list(row) for row in list(zip(*A))]
    return temp
def clock(A:list) -> list:
    "시계방향으로 행렬 90도 회전시키기"
    temp = [list(row) for row in list(zip(*A[::-1]))]
    return temp

# 테스트
if __name__ == '__main__':
    # (n * n) size의 정사각행렬 생성
    n = 4
    A = [[i*n + j + 1 for j in range(n)] for i in range(n)]
    print(*A, sep='\n')
    print()
    print(*clock(A), sep='\n')
    print()
    print(*counterclock(A), sep='\n')
    print()