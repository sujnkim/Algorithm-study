"""
[BOJ] 7569: 토마토
문제링크: https://www.acmicpc.net/problem/7569
INPUT:
    * 첫째 줄에 상자 가로M, 세로N, 쌓는 수H
    * 다음 H개의 줄에 한 상자에 들어있는 토마토 정보
    * M개씩 N쌍이 한 줄로 입력됨
    * 1:익은 토마토 / 0:익지 않은 토마토 / -1:없음
OUTPUT: 토마토가 모두 익을때까지 최소 몇일이 걸리는 지 계산
    * 처음부터 모두 익어있으면 0 출력
    * 모두 익지 못하는 상황이면 -1 출력

문제풀이: bfs를 이용하여 주변의 토마토를 익힌다.
(주위의 토마토를 하루에 1개씩 익혀나감 = 거리가 1인 최단거리 문제와 유사)

bfs를 실행한 뒤, 조작한 data리스트에서 (가장 큰 값-1)이 모두 익을 때까지
걸리는 최소 일수이다.

처음부터 모두 익어있는 경우를 판단하기 위해 ripen변수를 사용
값을 입력받을 때 0이 있으면 false로 저장하여 bfs를 수행한다

bfs를 실행한 수 리스트에 0이 존재하는 경우, 모두 익지 못하는 상황이므로
-1를 출력하도록 if문을 구성한다

"""
import sys
from collections import deque

#input
input = sys.stdin.readline

m, n, h = map(int, input().split())    #가로, 세로, 높이

ripen = True    #처음부터 모두 익어있는 경우 판단 변수

data = [ [] for _ in range(h) ]
tomatoes = []    # (height, row, col, time)
for height in range(h):
    for i in range(n):
        temp = list(map(int, input().split()))
        data[height].append(temp)
        
        #토마토 정보만 저장
        for j in range(m):
            if temp[j] == 1:
                tomatoes.append((height, i, j))
            if temp[j] == 0:
                ripen = False

#solve
  
#높이, 세로(행), 가로(열) 변화: 6방향
dir = [(-1,0,0),(0,-1,0),(0,0,1),(0,1,0),(0,0,-1),(1,0,0)]

def bfs():
    que = deque(tomatoes)
    
    while que:
        height, x, y = que.popleft()
    
        for i in range(6):
            dh, dx, dy = dir[i]
    
            nh = height + dh
            nx = x + dx
            ny = y + dy
    
            if 0<=nh<h and 0<=nx<n and 0<=ny<m \
            and data[nh][nx][ny] == 0:
                data[nh][nx][ny] = data[height][x][y] + 1
                que.append((nh, nx, ny))

                
#output
result = 0   

if ripen == True:    #처음부터 모두 익어있는 경우
    print(0)
else:
    bfs()

    for height in range(h):
        for i in range(n):
            for j in range(m):
                #모두 익지 못하는 경우
                if data[height][i][j] == 0:   
                    print(-1)
                    exit(0)
                result = max(result, data[height][i][j])
   
    print(result-1)