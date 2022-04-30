"""
신장 트리Spanning Tree
: 하나의 그래프가 있을 때, 모든 노드를 포함하며 사이클이 존재하지 않는 부분 그래프(트리의 성립 조건)
트리 자료구조 => v개의 노드, v-1개의 간선으로 구성됨

크루스칼 알고리즘Kruskal Algorithm
: 최소 비용으로 신장 트리를 찾는 알고리즘, 최소 신장 트리 알고리즘 중 한 가지
가장 적은 비용으로 모든 노드를 연결, 그리디 알고리즘으로 분류됨

모든 간선에 대하여 정렬 수행 => 가장 거리가 짧은 간선부터 집합에 포함

1. 간선 데이터를 비용에 따라 오름차순으로 정렬
2. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인
    1) 사이클이 발생하지 않는 경우, 최소 신장 트리에 포함
    2) 사이클이 발생하는 경우, 최소 신장 트리에 포함시키지 않음
3. 모든 간선에 대하여 과정 2를 반복

"""

# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

        
# 노드 개수, 간선 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v+1)

# 모든 간선을 담을 리스트, 최종 비용을 담을 변수
edges = []
result = 0

# 부모 노드를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

# 모든 간선에 대한 정보 입력
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge

    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)


"""
간선 개수가 e개일 때, 시간복잡도 = O(ElogE)
크루스칼 알고리즘에서 시간이 가장 오래 걸리는 부분이 간선을 정렬하는 작업
=> 정렬할 때 시간 복잡도가 O(ElogE)임
=> 크루스칼 내부에서 사용되는 서로소 집합 알고리즘 시간 복잡도는 이보다 작으므로 무시
"""