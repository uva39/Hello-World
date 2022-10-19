# 자기 자신을 포함하는 리스트 a, b 생성
a = [1]
b = [1]
a.append(a)
b.append(b)

# a[1]은 a이므로, 이걸 몇 번이고 반복하던지, 계속 a가 나온다.
print(f'{a = }')
print(f'{a[1] = }')
print(f'{a[1][1] = }')
print(f'{a[1][1][1] = }\n')

# a, a[1], a[1][1]...의 데이터의 주소가 모두 같다.
# temp = a에서, 
# temp는 a의 shallow copy이기에 실제로는 a의 레퍼런스 꼴이라는 것을 생각하면 당연하다.
print(f'{a is a[1] = }')
print(f'{a is a[1][1] = }')
print(f'{a[1] is a[1][1] = }\n')


# 파이썬은 리스트끼리 비교를 하면, 각 리스트의 모든 원소들이 서로 같은지 검사한다.
# 이때 중첩된 리스트에서는 재귀를 사용한다.
# 그렇기에 무한대로 리스트가 중첩된 a, b는 비교 연산 수행 시 최대재귀깊이를 초과한다.
try:
    print(f'a == b는, {a == b}')
except RecursionError as e:
    print(f'a == b인지 비교하는 중에 {e}')

# 파이썬에 논리연산이 short-circuit을 사용하듯이,
# a == a를 계산할 때엔 먼저 a의 주소부터 확인하고,
# 만약 같다면 비교를 수행하지 않고 True를 반환하는 것 같다.
try:
    print(f'a == a는, {a == a}')
except RecursionError as e:
    print(f'a == a인지 비교하는 중에 {e}')

# 파이썬 내장 모듈 copy의 deepcopy는 이런 자기참조가 포함된 리스트를 복사해도 안전한데,
# deepcopy가 내부적으로 재귀로 동작하긴 하지만,
# 재귀를 하며 이미 복사한 리스트들을 저장해놓기 때문이다.
 
from copy import deepcopy
try:
    temp = deepcopy(a)
    print(temp)
except RecursionError as e:
    print(e)