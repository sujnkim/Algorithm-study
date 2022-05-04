"""
[ch10.graph] 10-8: 도시 분할 계획 | 난이도2 | 기초 문제집
문제링크: https://www.acmicpc.net/problem/1647
INPUT: n개의 집, m개의 길
    * 첫째 줄에 n, m (2<=n<=100,000) (1<=m<=1,000,000)
    * 다음 m개의 줄에 길의 정보 a, b, c
    * a와 b를 연결하는 길의 비용이 c (1<=c<=1,000)
OUTPUT: 첫째 줄에 길을 없애고 남은 유지비 합의 최솟값 출력
"""
"""
마을의 n개의 집은 m개의 길로 열결, 길은 양방향

마을을 2개로 분할하려고 함
분리된 각 마을 안의 집은 서로 연결되어야 함, 마을에는 집이 하나 이상
분리된 두 마을 사이에 있는 길은 필요가 없으므로 없앨 수 있음
분리된 마을 내에서도 임의의 두 집 사이의 경로가 항상 존재하게 하면서 길을 없앨 수 있음
=> 조건을 만족하도록 길을 없애 나머지 길의 유지비의 합을 최소로 만들기

[풀이]
크루스칼 알고리즘: 최소 신장 트리 알고리즘
최소한의 비용으로 모든 노드를 포함하며 사이클이 존재하지 않는 부분 그래프를 만들 수 있음

마을을 2개로 분리해야 하므로, 최소 신장 트리를 2부분으로 나누자
최소 신장 트리의 간선 중 비용이 가장 큰 간선을 제거하면 될 것
"""

#특정 원소가 포함된 집합 찾기: find
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

#두 원소가 속한 집합 합치기: union
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

    
#input
v, e = map(int, input().split())

#부모 테이블 초기화
parent = [0] * (v+1)
for i in range(1, v+1):
    parent[i] = i

edges = []
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

    
#solve
edges.sort()

result = 0
max_val = 0        #최소 신장 트리에서 가장 비용이 큰 간선

for edge in edges:
    cost, a, b = edge

    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        max_val = cost

#output
print(result-max_val)