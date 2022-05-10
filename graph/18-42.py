"""
[ch18.graph] 18-42: 탑승구 | 난이도2 | CCC
INPUT: 탑승구 수g, 비행기 수p, 탑승구 정보gi
    * 첫째 줄에 g (1<=g<=100,000)
    * 둘째 줄에 p (1<=p<=100,000)
    * p개의 줄에 각 비행기가 도킹할 수 있는 탑승구 정보, 1에서 gi번째 까지 중 도킹 가능
OUTPUT: 도킹할 수 있는 비행기의 최대 개수를 출력
"""
"""
[풀이 구상]
서로소 집합 알고리즘 이용

가능한 큰 번호의 탑승구로 도킹을 수행한다고 가정
도킹은 합집합 연산 => 해당 집합을 왼쪽의 집합과 union
집합의 루트가 0인 경우, 더 이상 도킹이 불가능 한 것으로 판단
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

g = int(input())
p = int(input())

parent = [0] * (g+1)
for i in range(1, g+1):
    parent[i] = i


#solve
result = 0
for _ in range(p):
    root = find_parent(parent, int(input()))
    if root == 0:
        break
    union_parent(parent, root, root-1)
    result += 1

    
#output
print(result)