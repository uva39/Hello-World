# 1등 solution
# ord chr 각 나오면 적극 활용하기
# A~Z, a~z, 0~9를 개수를 저장하며 입력받는 경우 사용할 수 있음
import sys
input = sys.stdin.readline

s = input()[:-1]
a = [0] * 200
f = [1] * 200
for _ in range(int(input())):
    a[ord(input()[0])] += 1
ans = 1
for c in s:
    c = ord(c)
    ans = ans * a[c] // f[c]
    a[c] -= 1
    f[c] += 1
print(ans)

# my solution

import sys
def main():
    f = sys.stdin.readline # fast I/O
    g = lambda: f().rstrip() # fast I/O
    i1 = lambda : int(f()) # a integer
    i2 = lambda : list(map(int, f().split())) # a row of integers

    dps = g()
    names = [g() for _ in range(i1())]
    d = {k:0 for k in set(dps)}
    for k in names:
        try: d[k[0]] += 1
        except: pass

    ans = 1
    if len(d) == 3: # 3
        for v in d.values():
            ans *= v
    elif len(d) == 1: # 1
        M = max(d.values())
        ans = M * (M-1) * (M-2) // 6
    else: # 2
        for k in d:
            if dps.count(k) == 2:
                ans *= d[k] * (d[k]-1) // 2
            else:
                ans *= d[k]
    print(ans)
main()