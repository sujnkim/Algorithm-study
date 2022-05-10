"""
[ch18.graph] 18-43: 어두운 길 | 난이도2 | University of Ulm
INPUT: 집의 수n, 도로의 수m, 각 도로에 대한 정보(x, y, z)
    * 첫째 줄에 n, m (1<=n<=200000, n-1<=m<=200000)
    * 다음 m개의 줄에 x, y, z (0<=x,y<=n)
OUTPUT: 일부 가로등을 비활성화하여 절약할 수 있는 최대 금액 출력
"""
"""
[풀이 구상]
n개의 집을 m개의 도로로 연결
임의의 두 집에 대하여 가로등이 켜진 도로만으로 오갈 수 있도록 만들기 => 모두 연결되어야 함
최대한 적은 비용으로 연결 => 최소 신장 트리 형성... 크루스칼 알고리즘

1. cost를 기준으로 소팅
2. cost가 적은 것부터 확인
    if, 사이클이 발생 => 절약하는 비용, result에 추가
    else, 집합에 추가(union)

"""
import sys

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


#input
input = sys.stdin.readline
n, m = map(int, input().split())

# 서로소 집합을 위한 parent 리스트 초기화
parent = [0]*(n)
for i in range(n):
    parent[i] = i

# 도로 정보 입력
edges = []
for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

    
#solve
# 크루스칼 알고리즘 구현
edges.sort()
result = 0

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
    else:
        result += cost


#output
print(result)
