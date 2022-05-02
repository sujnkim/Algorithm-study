"""
[ch10.graph] 10-7: 팀 결성 | 난이도2 | 핵심 유형
INPUT: 번호n개, 연산 개수m개
    * 첫째 줄에 n, m (1<=n,m<=100,000)
    * 다음 m개의 줄에 연산이 주어짐
    * 팀 합치기 연산: 0 a b, a가 속한 팀과 b가 속한 팀을 합침
    * 같은 팀 여부 확인 연산: 1 a b, a와 b가 같은 팀에 속하는지 확인
OUTPUT: m개의 연산을 수행할 때, 같은 팀 여부 확인 연산에 대한 연산 결과를 출력
        * 같은 팀 여부 확인 연산에 대해 한 줄에 하나씩 YES 또는 NO 출력
"""

"""
서로소 집합 알고리즘 문제
같은 팀 여부 확인 연산 = find
팀 합치기 연산 = union 연산

n, m의 범위가 최대 100,000임
=> 경로 압축 방식으로 시간 복잡도를 최적화시켜야 함
"""

# 특정 원소가 속한 집합 찾기: find
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합 합치기: union
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


#input
n, m = map(int, input().split())
parent = [0]*(n+1)

for i in range(n+1):
    parent[i] = i

#solve
for i in range(m):
    oper, a, b = map(int, input().split())
    if oper == 0:
        union_parent(parent, a, b)
    elif oper == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print('YES')
        else:
            print('NO')
