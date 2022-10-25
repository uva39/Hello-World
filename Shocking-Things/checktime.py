import time
import sys
from functools import wraps

# decorator을 사용해서 함수의 실행시간을 측정함
# 어떤 알고리즘이 더 빠른지 벤치마킹 테스트를 할 때 사용함

def multi_elapsed(n):
    def elapsed(f):
        @wraps(f)
        def wrap(*args, **kwargs):
            start_r = time.perf_counter()
            start_p = time.process_time()
            # 함수 실행
            ret = [0]*n
            for i in range(n):
                ret[i] = f(*args, **kwargs)

                if n >= 100:
                    if i % (n//100) == 0:
                        sys.stdout.write(f'\r{f.__name__} : {i // (n//100) + 1}% 진행됨 ')
            end_r = time.perf_counter()
            end_p = time.process_time()
            elapsed_r = end_r - start_r
            elapsed_p = end_p - start_p

            print(f'\n{f.__name__} elapsed: {elapsed_r:.6g}sec (real) / {elapsed_p:.6g}sec (cpu)')
            return ret
        return wrap
    return elapsed

@multi_elapsed(1000)
def comp_flat(l):
    return [item for sublist in m for item in sublist]

@multi_elapsed(1000)
def sum_flat(l):
    return sum(l,[])

if __name__ == '__main__':
    n = 20
    m = [[i*n + j for j in range(n)] for i in range(n)]
    sum_flat(m)
    comp_flat(m)