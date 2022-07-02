"""
[BOJ] 2644: 촌수계산
문제링크: https://www.acmicpc.net/problem/2644
INPUT:
    * 첫째 줄에 사람의 수 n(1<=n<=100)
    * 둘째 줄에 촌수를 계산할 사람 두 명의 번호
    * 셋째 줄에 관계의 개수 m
    * m개의 줄에 관계를 나타내는 번호 x, y(x가 y의 부모)
OUTPUT: 입력받은 두 사람의 촌수를 나타내는 정수
    * 친척관계가 없어 촌수를 계산할 수 없으면 -1 출력

문제해결:
bfs를 이용하여 두 사람 사이의 거리를 계산
"""
import sys
from collections import deque

#input
inputdata = sys.stdin.readline

n = int(inputdata())
x, y = map(int, inputdata().split())

graph = [ [] for _ in range(n+1) ]

m = int(inputdata())
for _ in range(m):
    i, j = map(int, inputdata().split())
    graph[i].append(j)
    graph[j].append(i)


#solve
distance = [-1]*(n+1)

que = deque()

que.append(x)
distance[x] = 0

while que:
    now = que.popleft()

    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now]+1
            que.append(next_node)
    
#output
print(distance[y])