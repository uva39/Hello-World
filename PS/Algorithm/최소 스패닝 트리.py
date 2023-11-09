'''
https://gmlwjd9405.github.io/2018/08/28/algorithm-mst.html
최소 스패닝 트리(Minimum Spanning Tree, MST)는 가중치가 할당된 연결 그래프에서 
선택된 가중치의 합이 최소가 되는 "스패닝 트리"를 말합니다.
"스패닝 트리"란 그래프의 모든 정점을 포함하면서 사이클이 없는 연결 부분 그래프입니다.

수학적으로, 최소 스패닝 트리는 다음과 같은 특성을 가집니다:

연결 그래프(Connected Graph): 그래프의 모든 정점들이 간선을 통해 서로 연결되어 있어야 합니다.
사이클이 없음(Acyclic): 스패닝 트리는 사이클을 포함할 수 없습니다. 사이클이 있으면 트리가 아니게 됩니다.
n-1개의 간선(Edges): n개의 정점을 가진 스패닝 트리는 반드시 n-1개의 간선을 가져야 합니다.
최소 가중치(Minimum Weight): 선택된 스패닝 트리의 모든 간선의 가중치 합이 최소여야 합니다.

다음은 가중치 그래프가 주어질 때 최소 스패닝 트리를 구하는 두 가지 알고리즘입니다.
'''

# 크루스칼: O(elog₂e) -> 희소 그래프에서 유리
# 프림: O(v^2) -> 밀집 그래프에서 유리

# https://www.acmicpc.net/problem/1197
import sys

v, e = map(int, sys.stdin.readline().split())
graph = [[] for i in range(v+1)] # 0번 idx는 버림

for i in range(e):
    a, b, c = map(int, sys.stdin.readline().split()) # a 시작 b 끝 c 가중치
    graph[a].append([b, c]) # 양방향으로 시작점.append([종점, 가중치])
    graph[b].append([a, c])

# MST를 구하는 두 방법


def find(parent, i): # Union-Find 알고리즘의 그 Find
    if parent[i] != i:
        find(parent, parent[i])
    return parent[i]

def kruskal(graph, v):
    result = []  # 결과로 생성된 MST

    # Step 1: 가중치를 기준으로 간선 정렬
    edges = [(c, a, b) for a, row in enumerate(graph) for b, c in row]
    edges.sort(key=lambda x: x[0])

    parent = [i for i in range(v + 1)]
    rank = [0] * (v + 1) # 랭크를 기준으로 내림차순으로 쓸고 내려가면 MST로 순회함

    i, e = 0, 0  # edges, while에 쓸 index
    while e < v - 1: # MST의 간선은 v-1개니까 0 <= 간선 < v-1으로 반복
        # Step 2: Greedy하게 최소 가중치 간선을 잡고 i++
        c, a, b = edges[i]
        i += 1
        x = find(parent, a)
        y = find(parent, b)

        # Step 3: Union-Find로 서로 부모가 같은지 비교해보고 다르면 ㄱㄱ
        if x != y:
            e += 1
            result.append((a, b, c)) # 가장 가중치가 낮은 간선을 append
            # a랑 b를 Union해주기
            if rank[x] < rank[y]:
                parent[x] = y
            elif rank[x] > rank[y]:
                parent[y] = x
            else:
                parent[y] = x
                rank[x] += 1

    return sum(weight for _, _, weight in result), result


import heapq

def prim(graph, v):
    visited = [False] * (v + 1)
    edges = [(0, 1)]
    heapq.heapify(edges)
    # (weight 0, vertex 1)
    # 시작점은 아무거나(여기선 1번 정점) 잡고 이걸 인접한 최소 가중치 간선으로 이으며 확장할 거임
    # 최소힙을 써서 최소 가중치를 가진 간선을 찾음

    mst_weight = 0
    mst_edges = []

    while edges:
        weight, u = heapq.heappop(edges)
        if not visited[u]:
            visited[u] = True
            mst_weight += weight

            for v, w in graph[u]:
                if not visited[v]:
                    heapq.heappush(edges, (w, v))
                    mst_edges.append((u, v, w))

    return mst_weight, mst_edges

print(kruskal(graph, v)[0])