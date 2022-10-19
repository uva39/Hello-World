import time

# decorator을 사용해서 함수의 실행시간을 측정함
# 어떤 알고리즘이 더 빠른지 벤치마킹 테스트를 할 때 사용함

def elapsed(f):
    def wrap(*args):
        start_r = time.perf_counter()
        start_p = time.process_time()
        # 함수 실행
        ret = f(*args)
        end_r = time.perf_counter()
        end_p = time.process_time()
        elapsed_r = end_r - start_r
        elapsed_p = end_p - start_p

        print(f'{f.__name__} elapsed: {elapsed_r:.6g}sec (real) / {elapsed_p:.6g}sec (cpu)')
        return ret
   # 함수 객체를 return
    return wrap

@elapsed
def comp_flat(l):
    return [item for sublist in m for item in sublist]

@elapsed
def sum_flat(l):
    return sum(l,[])

if __name__ == "__main__":
    n = 500
    m = [[i*n + j for j in range(n)] for i in range(n)]
    sum_flat(m)
    comp_flat(m)