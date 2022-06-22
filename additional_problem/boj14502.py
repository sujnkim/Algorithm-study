"""
[boj] 14502: 연구소
문제 링크: https://www.acmicpc.net/problem/14502
INPUT:
    * 첫째 줄에 지도의 가로크기n, 세로크기m
    * 둘째 줄부터 n개의 줄에 지도이 모양
        * 0:빈칸, 1:벽, 2:바이러스
    * 빈칸의 개수는 3개 이상
OUTPUT:
    * 안전 영역의 최대 개수
"""
import sys
from collections import deque

#input
inputdata = sys.stdin.readline

n, m = map(int, inputdata().split())

virus = []
data = []
for i in range(n):
    data.append(list(map(int, inputdata().split())))
    for j in range(m):
        if data[i][j]==2:
            virus.append((i, j))


#solve
temp = [ [0]*m for _ in range(n) ]    #조작에 사용할 임시 리스트

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0


# (x, y)를 기준으로 바이러스를 퍼뜨림
def spread_virus(x, y):
    que = deque()
    que.append((x, y))

    while que:
        x, y = que.popleft()
        
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
    
            if 0<=nx<n and 0<=ny<m and temp[nx][ny]==0:
                temp[nx][ny] = 2
                que.append((nx, ny))

            
#안전지역 개수 계산
def check_zero():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j]==0:
                cnt += 1
    return cnt

    
def put_wall(cnt):
    global result
    
    #벽이 3개 설치되었을 때
    if cnt==3:
        
        #temp에 원래 데이터를 복사
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]

        #바이러스 퍼뜨리기
        for vx, vy in virus:
            spread_virus(vx, vy)

        #안전지역 개수 최대값으로 갱신
        result = max(result, check_zero())
        return
        

    #벽이 아직 3개가 아닐 때
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:

                #벽 생성
                data[i][j] = 1
                cnt += 1
                
                put_wall(cnt)

                #벽 삭제
                data[i][j] = 0
                cnt -= 1

        
#output
put_wall(0)
print(result)