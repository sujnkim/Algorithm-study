"""
서로소 집합을 활용한 사이클 판별

서로소 집합은 무방향 그래프 내에서 사이클을 판별할 때 사용됨
    cf. 방향 그래프에서 사이클 여부는 DFS를 이용

간선을 하나씩 확인하며 두 노드가 포함되어 있는 집합을 합치는 과정을 반복

1. 각 간선을 확인하며 두 노드의 루트를 확인
    1) 루트 노드가 다르다면 두 노드에 대해 union 수행
    2) 루트 노드가 같다면 사이클이 발생한 것
2. 그래프에 포함된 모든 간선에 대해 과정 1 반복

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

# 노드의 개수와 간선 개수(union 횟수) 입력받기
v, e = map(int, input().split())
parent = [0] * (v+1)

# 부모 테이블에서, 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

    
# 사이클 발생 여부 변수
cycle = False

for i in range(e):
    a, b = map(int, input().split())

    # 사이클이 발생한 경우 => 종료
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    # 발생하지 않은 경우 => 합집합 수행
    else:
        union_parent(parent, a, b)

if cycle == True:
    print("사이클이 발생하였습니다.")
else:
    print("사이클이 발생하지 않았습니다.")
