"""
[ch18.graph] 18-41: 여행 계획 | 난이도2 | 핵심 유형
INPUT: n개의 여행지를 m개의 여행 계획으로 방문
    * 첫째 줄에 n, m (1<=n,m<=500)
    * n개의 줄에 걸쳐 nxn 행렬(1이면 서로 연결, 0이면 연결x)
    * 마지막 줄에 여행 계획에 포함된 m개의 여행지 번호가 주어짐
OUTPUT: 여행 계획이 가능하면 YES, 불가능하다면 NO 출력
"""

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
n, m = map(int, input().split())

# 서로소 집합 연산을 위한 parent 리스트 초기화
parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

# 연결된 노드 정보 입력 -> union 연산 수행
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1:
            union_parent(parent, i+1, j+1)


# 여행 계획 가능 여부 판단
result = True
trip = list(map(int, input().split()))

# 모든 여행지가 같은 집합에 속하는 지 확인
for i in range(m-1):
    if find_parent(parent, trip[i]) == find_parent(parent, trip[i+1]):
        continue
    else:
        result = False
        break

# output
if result == True:
    print('YES')
else:
    print('NO')