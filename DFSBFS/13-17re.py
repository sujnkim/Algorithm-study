"""
책의 예시 답안을 참고하여 수정한 코드
+ 리스트에 데이터를 append한 후 소팅하여 큐를 생성
    -> 루프를 돌면서 큐에 append할 필요가 없었음
+ 데이터를 append할 때 (바이러스번호, 현재시간, 행위치, 열위치) 이렇게 구성함
    -> 따로 시간변수를 설정하여 계산할 필요가 없었음
"""

from collections import deque

#input
n, k = map(int, input().split())

graph = []            # 전체 시험관 리스트
data = []            #바이러스 정보를 담을 리스트
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            # (바이러스번호, 시간, 행 위치, 열 위치)
            data.append((graph[i][j], 0, i, j))
            
s, x, y = map(int, input().split())


#solve
# 방향 : 상, 우, 하, 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def solution(x, y):
    
    # 바이러스 번호가 낮은 순으로 정렬 -> 큐에 삽입
    data.sort()
    queue = deque(data)

    while queue:
        #print(queue)
        virus, sec, qx, qy = queue.popleft()

        # 시간이 s만큼 경과한 경우 종료
        if sec == s:
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
                graph[nx][ny] = virus
                queue.append((virus, sec+1, nx, ny))
            else:
                continue

    print(graph)
    return graph[x-1][y-1]

#output
print(solution(x,y))
