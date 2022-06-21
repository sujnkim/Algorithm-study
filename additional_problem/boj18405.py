"""
[BOJ] 18405: 경쟁적 전염
문제링크: https://www.acmicpc.net/problem/18405
INPUT:
    * 첫째 줄에 자연수 n, k
    * 둘째 줄부터 n개의 줄에 시험관 정보
    * n+2번째 줄에 s, x, y

OUTPUT: s초 뒤 (x,y)에 존재하는 바이러스 종류 출력
    * 존재하지 않는다면 0 출력

문제풀이:
바이러스가 가까운 곳에서부터 1칸씩 사방으로 퍼져나감
현재 위치를 꺼내서 사방을 확인한 후 비어있다면
다시 큐에 집어넣는 행위를 반복... bfs

"""
import sys
from collections import deque

#input
imput = sys.stdin.readline

n, k = map(int, input().split())

virus = []    #바이러스 정보를 담을 리스트
data = []     #전체 맵 정보
for i in range(n):
    data.append(list(map(int, input().split())))

    #바이러스 위치 확인
    for j in range(n):
        if data[i][j] != 0:
            # (바이러스번호, 현재시간, 행위치, 열위치)
            virus.append((data[i][j], 0, i, j))

s, tx, ty = map(int, input().split())


#solve

virus.sort()    #바이러스번호기준 오름차순 정렬
que = deque(virus)    #큐에 담기

#방향 리스트
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

time = 0
while que:

    # 큐에서 꺼내기
    vnum, time, x, y = que.popleft()

    #시간이 목표 시간인 경우, 종료
    if time==s:
        break

    # 바이러스 퍼뜨리기(4방향)
    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]

        #바이러스가 새롭게 퍼진 경우, 큐에 추가
        if 0<=nx<n and 0<=ny<n and data[nx][ny]==0:
            data[nx][ny] = vnum
            que.append((vnum, time+1, nx, ny))

    
#output
print(data[tx-1][ty-1])