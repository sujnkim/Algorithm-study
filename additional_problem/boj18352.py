"""
[BOJ] 18352: 특정 거리의 도시 찾기
문제 링크: https://www.acmicpc.net/problem/18352
INPUT:
* 첫째 줄에 도시의 개수N, 도로의 개수M, 거리 정보K, 출발 도시 번호X
    * 2<=N<=300,000 / 1<=M<=1,000,000
    * 1<=K<=300,000 / 1<=X<=N
* 둘째 줄부터 M개의 줄에 공백으로 구분된 두 개의 자연수 A, B
    * A번 도시에서 B번 도시로 이동하는 단방향 도로가 존재한다는 의미
    * 1 <= A,B <= N

OUTPUT:
* X에서 출발하여 도달할 수 있는 도시 중, 최단 거리가 K인 모든 도시의 번호를
한 줄에 하나씩 오름차순으로 출력
* 최단 거리가 K인 도시가 존재하지 않는다면 -1 출력

추가 정보
* 모든 도로의 거리는 1
* 출발 도시X에서 X로 가는 최단 거리는 항상 0


문제 풀이
* 출발 도시X에서 다른 도시들로 가는 최단 거리를 계산
    * bfs 알고리즘: 큐 사용
* 최단 거리가 K인 도시를 모두 출력
"""
from collections import deque
import sys

#input
input = sys.stdin.readline
n, m, k, x = map(int, input().split())

data = [ [] for _ in range(n+1) ]
for _ in range(m):
    a, b = map(int, input().split())
    data[a].append(b)


# bfs함수
def bfs(data, start, dist):
    que = deque()
    que.append(start)
    dist[start] = 0

    while que:
        now = que.popleft()

        for next_city in data[now]:
            if dist[next_city] == -1:
                dist[next_city] = dist[now] + 1
                que.append(next_city)


#solve
                
dist = [-1]*(n+1)

bfs(data, x, dist)


#output
if k not in dist:
    print(-1)
else:
    for i in range(1, n+1):
        if dist[i] == k:
            print(i)