# 타임소트(Tim Sort): O(N) - O(NlgN) - O(NlgN) - Stable

# 파이썬의 기본 내장 정렬함수가 사용하는 알고리즘
# 삽입 정렬과 병합 정렬을 합치고, 여기에 다양한 잡기술을 섞은 정렬 방식
# 삽입 정렬과 병합 정렬 모두 Stable하기에 타임 소트도 Stable
# Big-O 표기법과 별개로 많이 빠름
def tim(arr):
    arr.sort()


# 선택정렬(Selection Sort): O(N^2) - O(N^2) - O(N^2) - Unstable

# 1. 바꿀 데이터의 인덱스를 i라 하고, 0(맨 앞)으로 초기화한다.
# 2. O(n)의 시간복잡도로 배열에서 가장 작은 데이터를 찾은 뒤, arr[i]와 맞바꾼다.
# 3. 그 다음으로 작은 데이터를 선택해, arr[i+1]과 맞바꾼다.
# 4. i가 배열의 마지막에 도착할 때까지 반복한다.

def selection(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                min_idx = j
        arr[min_idx], arr[i] = arr[i], arr[min_idx]


# 삽입 정렬(Insertion Sort): O(n) - O(n^2) - O(n^2) - Stable

# 정렬 과정에서 데이터가 들어가기에 적절한 위치를 찾은 뒤, 그 위치에 데이터를 삽입한다.
# 필요할 때만 위치를 바꾸기 때문에, "거의 정렬된 데이터"에서 매우 효율적이다.

# 1. 첫번째 데이터는 그 자체로 정렬되어있다고 가정한다.
# 2. 두번째 데이터부터 정렬된 데이터의 끝부터 처음까지 비교하면서 필요할 경우 삽입한다.
# 3. 마지막 데이터를 비교할 때까지 반복한다.

def insertion(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1): # j in (i, i-1, ... , 2, 1)
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:
                break


# 버블 정렬(Bubble Sort): O(n) - O(n^2) - O(n^2) - Stable

# 서로 인접한 두 원소의 대소 관계를 비교해가며 정렬한다.
# 버블 정렬을 양방향으로 번갈아 수행한 것이 칵테일 정렬이다.

# 1. 서로 인접한 두 원소를 비교한 후, 더 큰 원소를 뒤로 보낸다.
# 2. 이걸 1 cycle동안 반복하면, 가장 큰 원소가 뒤로 가게 된다.
# 3. 따라서 이를 n회 반복하면, 데이터가 정렬된다.

def bubble(x):
    t = len(x)-1
    for i in range(t):
        for j in range(t-i):
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]


# 칵테일 정렬(Cocktail Shaker Sort): O(n) - O(n^2) - O(n^2) - Stable

# 버블 정렬과 Big-O Notation은 같아도, 실제론 더 빠르게 동작한다.
# 최댓값으로 push하는 것만 반복했다면 버블 정렬이지만, 칵테일 정렬에선 최대, 최소로 원소들을 전부 push한다.
# 칵테일 정렬의 아이디어 자체는 다른 정렬들에도 충분히 적용할 수 있어서 범용성이 높음

def cocktail(arr):
    a, b = 0, len(arr)
    swap = True  # 정방향 True / 역방향 False
    swapped = True  # 바뀌었는지
    while swapped:
        swapped = False

        if swap:  # 정방향
            for i in range(a, b):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swapped = True
            b = b - 1
            swap = False
        else:  # 역방향
            for i in range(b - 1, a - 1, -1):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swapped = True
            a = a + 1
            swap = True



# 퀵 정렬(Quick Sort): O(N) - O(NlgN) - O(N^2)

# O(NlgN) 알고리즘 중에서 대부분에 데이터에 대해 다른 O(NlgN) 알고리즘보다 빠르게 동작하고, 가장 보편적인 정렬 방법이다.
# 병합정렬(Merge Sort)과 퀵정렬 모두 분할정복(Divide and Conquer)방식과 재귀적인 알고리즘을 사용한다.
# 리스트 슬라이싱을 사용하여 구현할 경우엔, 함수가 간단해지긴 하지만 슬라이싱이 새로운 리스트를 생성하기 때문에 공간복잡도 면에서 마이너스다.
# 게다가, 퀵정렬은 슬라이싱 없이 구현할 경우엔 추가 메모리를 필요로 하지 않아서 O(1)의 공간복잡도를 갖는다.
# 단점으로는, 데이터가 이미 정렬된 상태에 가까울 수록 시간복잡도가 O(N^2)에 가까워진다는 점이 있다.

def quick(arr):
    def sort(low, high):
        if high <= low:
            return
        mid = partition(low, high)
        sort(low, mid - 1)
        sort(mid, high)

    def partition(low, high):
        pivot = arr[(low + high) // 2]
        while low <= high:
            while arr[low] < pivot:
                low += 1
            while arr[high] > pivot:
                high -= 1
            if low <= high:
                # while loop 2개를 돌며 arr[low] > arr[pivot] > arr[high]이 되었기에 서로 바꿔줘야 함.
                arr[low], arr[high] = arr[high], arr[low]
                low, high = low + 1, high - 1
        return low
    return sort(0, len(arr) - 1)


# 병합정렬(Merge Sort): O(NlgN) - O(NlgN) - O(NlgN) - Stable

# 퀵정렬과 마찬가지로 분할 정복 (Devide and Conquer) 이용
# 리스트 슬라이싱을 사용하여 구현하면 간단하지만, 슬라이싱이 새로운 리스트를 생성하기 때문에 공간복잡도가 안좋다

def merge_sort(arr):
    def sort(low, high):
        if high - low < 2:
            return
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)

    def merge(low, mid, high):
        temp = []
        l, h = low, mid

        while l < mid and h < high:
            if arr[l] < arr[h]:
                temp.append(arr[l])
                l += 1
            else:
                temp.append(arr[h])
                h += 1

        while l < mid:
            temp.append(arr[l])
            l += 1
        while h < high:
            temp.append(arr[h])
            h += 1

        for i in range(low, high):
            arr[i] = temp[i - low]
    return sort(0, len(arr))


# 힙 정렬(heap sort) - O(NlgN) - O(NlgN) - O(NlgN)

# 정렬할 값의 개수가 적을 때엔 오히려 삽입정렬 등의 O(N^2) 알고리즘 보다도 성능이 떨어진다.
# heapq 모듈을 사용하지 않는 경우엔 이진 검색 트리를 직접 구현해야 하는데,
# 이진 검색 트리를 실용적으로 구현하기 위해선 잡기술이 너무 많이 필요하다.
# 우선순위 큐 (Priority Queue) 구현 용도로만 쓰기

import heapq
def heap(arr):
    l = len(arr)
    H = []
    for i in range(l):
        heapq.heappush(H, arr[i])
    for i in range(l):
        arr[i] = heapq.heappop(H)


# 셸 정렬(Shell Sort): O(NlgN) - gap에 따라 다름 - O(N^1.25)

# 셸 정렬은 Cell과는 아무 상관 없다. Donald L.Shell이라는 사람이 제안한 방법일 뿐이다(...)
# 삽입 정렬에선 자신의 index에서 멀리 떨어진 index로 이동할 때에 속도 저하가 크게 발생한다
# 이를 보완해서 정렬할 array를 일정한 gap을 두고 나눈다
# 정렬할 배열의 요소를 일정한 gap을 기준으로 나눠 각 그룹 별로 삽입 정렬을 수행하고, 그 그룹을 합치면서 정렬을 반복하여 요소의 총 이동 횟수를 줄인다.
# 이때 gap을 점점 줄여가며 정렬하는데, 1st cycle : 5 / 2nd cycle : 3 / 3rd cycle : 1 이런 식으로 줄여나간다.
# ex: [0~99], gap = 5일땐, range(0, 100, 5) range(1, 100, 5) range(2, 100, 5) ...  range(4, 100, 5)를 각각 정렬

def shell(arr):
    gap = len(arr)//3 + 1 # gap은 3씩 나눠가는 방식으로 정함
    while gap > 0:
        for i in range(gap, len(arr)):
            while i >= gap and arr[i - gap] > arr[i]:
                arr[i], arr[i - gap] = arr[i - gap], arr[i] # mini 삽입정렬 part.
                i -= gap
        gap = 0 if gap == 1 else gap//3 + 1
        # while문이 끝났을 때 gap이 1이면 종료, 아니면 gap을 바꿔서 반복


# 기수정렬(Radix Sort): O(k/d * n) - O(k/d * n) - O(k/d * n) - Stable

# LSD : Least Signigicant Digit, MSD : Most Significant Digit 로 구분된다. 일반적으론 LSD기수정렬을 의미한다.
# 기수 정렬은 비교연산을 하지 않고, 따라서 모든 비교연산을 쓴 정렬은 시간복잡도렬 O(NlgN)보다 낮아질 수 없다는 법칙을 벗어날 수 있다.
# 따라서 O(N)만큼 빨라질 수 있지만, 정렬할 때에 큰 메모리가 필요하고, 정수나 문자열이 아닌 경우 O(NlgN) 알고리즘보다 느려질 수 있다.

# 기수정렬의 정렬방법은 가장 작은 자리수부터 차례로 Counting Sort를 수행하는 것이라고 볼 수도 있다.

from collections import deque
def radix(arr):
    # 이건 10진수를 정렬할 때의 경우고, 알파벳 정렬엔 훨씬 더 많이 필요. (대문자도 들어가면 버킷이 26*2 = 52개???)
    buckets = [deque() for _ in range(10)]

    max_val = max(arr) # O(N)
    Q = deque(arr) # O(N)
    d = 1
    # 1, 10, 100, ..., 최대원소의 자리까지 나아가며 정렬함.
    while max_val >= d:
        while Q:
            num = Q.popleft()
            buckets[(num//d)%10].append(num)
            # ex: num = 584, d = 1, 10, 100일때 num//d = 584, 58, 5 (num//d)%10 = 4, 8, 5
            # 즉, d가 1, 10, 100일 때 (num//d)%10은 1의 자리 수, 10의 자리 수, 100의 자리 수이다.

        # while문이 끝나고 buckets안의 bucket에 d의 자리 수에 대한 Counting Sort가 완료됨
        # 이제 Q는 비었고, 원소들은 전부 bucket으로 부분 정렬되어 이동됨
        for bucket in buckets:
            while bucket:
                # 모든 bucket에 대해, 각각의 bucket가 비도록 원소를 추출해서 Q에 담음
                Q.append(bucket.popleft())

        d *= 10 # 자리수를 바꿔서 반복

    for i in range(len(Q)): # 원래의 배열에 복사
        arr[i] = Q.popleft()

if __name__ == '__main__':
    arr = [*map(int(), input().split())]
    # TEST CODE