"""
[ch05.DFSBFS] 5-11: 미로 탈출 | 난이도1.5 | 실전문제
INPUT: 미로 크기 nxm, 미로의 정보
    * 첫째 줄에 공백으로 구분된 두 정수 n, m (4<=n,m<=200)
    * 다음 n개의 줄에 각각 m개의 정수(0 or 1)로 공백 없이 주어지는 미로의 정보
    * 시작 칸과 마지막 칸은 항상 1임
OUTPUT: 최소 이동 칸 개수 출력
"""
from collections import deque

#input
n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

"""
[풀이 구상]
동빈이는 (1,1)에서 (N,M)으로 한 칸 씩 이동
괴물이 있는 곳:0/괴물이 없는 곳:1 일 때, 1인 곳만 지나 움직이면 됨

BFS: 시작 지점에서 가까운 노드부터 차례대로 그래프의 모든 노드를 탐색.
-> deque라이브러리 append, popleft
1) (1,1)에서 BFS 수행 시작 -> (1,1)의 값은 항상 1
2) 상,하,좌,우로 탐색을 진행 -> 주변 노드를 방문하게 되고 새롭게 방문하는 노드의 값은 2가 됨
3) BFS를 계속 수행하면 최단 경로의 값이 1씩 증가하는 형태로 변경
cf. 단순히 가장 오른쪽 아래 위치로 이동하는 문제이므로 시작 지점의 값이 3으로 변경되지는 않음
"""

#solve

#이동 방향 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#BFS
def bfs(x, y):
    
    queue = deque()    #큐 생성
    queue.append((x,y))

    # 큐가 빌 때까지
    while queue:
        x, y = queue.popleft()

        # 네 방향 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위를 벗어나는 경우
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue

            # 괴물이 있는 경우
            if graph[nx][ny] == 0:
                continue

            # 괴물이 없는 경우
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))               # 큐 추가

    return graph[n-1][m-1]


#output
print(bfs(0,0))