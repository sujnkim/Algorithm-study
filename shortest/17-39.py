"""
[ch17.shortest] 17-39: 화성 탐사 | 난이도2 | ACM-ICPC
INPUT:
    * 첫째 줄에 테스트 케이스 t(1<=t<=10)
    * 매 테스트 케이스의 첫째 줄에는 탐사 공간 크기 n(2<=n<=125)
    *                 다음 n개의 줄에 각 칸의 비용(0<=비용<=9)
OUTPUT: 각 테스트 케이스마다 [0][0]의 위치에서 [n-1][n-1]로 이동하는 최소 비용을 한 줄에 하나씩 출력
"""
"""
(0,0)에서 (n-1, n-1)로 이동하는 최단거리를 구하는 문제
상하좌우 인접한 곳으로 1칸 움직일 수 있다 = 상하좌우로 연결된 노드

현재 탐색하는 노드와 인접한 노드는 상하좌우 4개
"""
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# test case
for tc in range(int(input())):
    #input
    n = int(input())

    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))

    # 최단거리 테이블 초기화
    distance = [ [INF]*n for _ in range(n) ]
    
    x, y = 0, 0    # 시작 위치(0, 0)
    q = [(graph[x][y], x, y)]    # (값, x, y)
    distance[x][y] = graph[x][y]

    while q:
        dist, x, y = heapq.heappop(q)

        if distance[x][y] < dist:
            continue

        # 현재 노드와 연결된 노드 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue

            cost = dist + graph[nx][ny]
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))

    print(distance[n-1][n-1])
