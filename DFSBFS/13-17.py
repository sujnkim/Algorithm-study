"""
[ch13.DFSBFS] 13-17: 경쟁적 전염 | 난이도2 | 핵심 유형
INPUT: 시험관 크기n, 바이러스 종류k
    * 첫째 줄에 공백으로 구분된 n, k (1<=n<=200, 1<=k<=1000)
    * 둘째 줄 부터 n개의 줄에 시험관 정보 제공
    * n+1번째 줄에 공백으로 구분된 s, x, y (0<=s<=10000, 1<=x,y<=n)

OUTPUT: s초 후 (x,y)에 존재하는 바이러스 종류 출력
    * 만약 해당 위치에 바이러스가 존재하지 않는다면 0 출력
"""
from collections import deque

#input
n, k = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
s, x, y = map(int, input().split())


"""
[풀이 구상]
바이러스가 가까운 곳부터 퍼지니까... bfs를 써야 하지 않을까

현재 큐에 들어있는 노드, 바이러스 번호가 낮은 순으로 pop
-> 바이러스 번호 기준으로 소팅? 우선순위 큐를 써야하는 걸까
-> 처음에 큐에 담을 때에만 번호가 낮은 순으로 담으면 될 것 같음
-> 3중 루프... 200*200*1000 = 40000000... ? 시간초과 안 나려나


if pop한 노드의 상하좌우에 있는 노드에 바이러스가 없을 경우
    * pop한 노드의 바이러스를 저장
    * 큐에 삽입
-> 이 과정을 s초 만큼 수행

"""
# 방향 : 상, 우, 하, 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


#solve
def solution(x, y):
    nowsec = 0
    queue = deque()

    # 매 초 번호가 낮은 바이러스부터 증식함
    # 바이러스 값(1~k)이 낮은 것부터 큐에 삽입
    for v in range(1, k+1):
        for i in range(n):
            for j in range(n):
                if graph[i][j] == v:
                    queue.append((i, j))
                else: continue
    #print(queue)
                    
    while queue:
        #print(queue)
        qx, qy = queue.popleft()

        # 시간이 s초가 지나면 종료
        # 바이러스 값이 1일때마다 시간을 1증가
        if graph[qx][qy]==1:
            nowsec += 1
        if nowsec == s+1:
            break

        # 주변 칸 탐색(사방)
        for i in range(4):
            nx = qx + dx[i]
            ny = qy + dy[i]

            # 범위를 벗어날 경우
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue

            # 바이러스가 없을 경우, 큐에 삽입
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[qx][qy]
                queue.append((nx, ny))
            else:
                continue

    #print(graph)
    return graph[x-1][y-1]

#output
print(solution(x,y))