# 이미 생성된 딕셔너리를 이어붙이는 방법

x = {'Alice':18}
y = {'Bob':27, 'Ann':22}
z = {**x, **y}
print(z)
z = x | y # 동일 기능
print(z)