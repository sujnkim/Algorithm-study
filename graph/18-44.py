"""
[ch18.graph] 18-44: 행성 터널 | 난이도2 | COCI
문제 링크: https://www.acmicpc.net/problem/2887
INPUT: 행성 개수n, 행성 좌표(x, y, z)
    * 첫째 줄에 n (1<=n<=100,000)
    * 다음 n개의 줄에 각 행성의 x, y, z 좌표
OUTPUT: 모든 행성을 터널로 연결하는데 필요한 최소 비용 출력
"""
"""
[풀이 구상]
모든 행성이 서로 연결되도록, 필요한 최소 비용 구하기
=> 최소 신장 트리, 크루스칼 알고리즘 사용

cost 공식
: min( abs(xa-xb), abs(ya-yb), abs(za-zb) )

main idea>
입력값이 n일 때, 가능한 간선의 개수는 n(n-1)/2 임.
n이 최대 100,000이므로 전부 계산하면 시간이 초과될 것
=> x, y, z 각 축을 기준으로 정렬하여 고려할 간선 개수를 줄이자
=> 각 축에 대해 n-1개의 간선만 고려하면 됨
=> 총 고려할 간선 개수 = 3*(n-1)

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

n = int(input())

# parent 리스트 초기화
parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

x = []
y = []
z = []

for i in range(n):
    data = map(int, input().split())
    x.append((data[0], i))
    y.append((data[1], i))
    z.append((data[2], i))

# x, y, z축을 기준으로 각각 정렬
x.sort()
y.sort()
z.sort()

edges = []

#cost 계산
for i in range(n-1):
    # cost, 행성a, 행성b
    edges.append((x[i+1][0] - x[i][0], x[i][1], x[i+1][1]))
    edges.append((y[i+1][0] - y[i][0], y[i][1], y[i+1][1]))
    edges.append((z[i+1][0] - z[i][0], z[i][1], z[i+1][1]))    

#solve
result = 0
edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost


#output
print(result)
