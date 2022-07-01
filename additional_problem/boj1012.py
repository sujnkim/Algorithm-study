"""
[BOJ] 1012: 유기농 배추
문제링크: https://www.acmicpc.net/problem/1012
INPUT:
    * 첫째 줄에 테스트 케이스 개수 t
    * 둘째 줄에 배추밭 가로길이m, 세로길이n, 배추개수k
    * k개의 줄에 배추 위치 x, y
OUTPUT: 필요한 최소 배추흰지렁이 마리 수 출력

풀이:
주어진 배추밭 데이터에서 인접한 배추무리가 몇 개인지 계산하는 문제.
dfs/bfs를 이용하여 풀 수 있다.
"""
import sys
from collections import deque


#start
inputdata = sys.stdin.readline
for tc in range(int(inputdata())):
    
    #input
    m, n, k = map(int, inputdata().split())    #가로, 세로, 배추개수
    data = [ [0]*m for _ in range(n) ]         #배추밭 정보
    for _ in range(k):
        x, y = map(int, inputdata().split())
        data[y][x] = 1
        
    #solve
    result = 0
    visited = [ [0]*m for _ in range(n) ]    #방문기록 저장

    #방향리스트
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    #너비 우선 탐색 알고리즘
    def bfs(x, y, visited):
        que = deque()
        que.append((x, y))
        visited[x][y] = 1

        while que:
            x, y = que.popleft()

            for dir in range(4):
                nx = x + dx[dir]
                ny = y + dy[dir]

                if 0<=nx<n and 0<=ny<m \
                    and visited[nx][ny]==0 and data[nx][ny]==1:
                    visited[nx][ny] = 1
                    que.append((nx, ny))
                
    #배추밭 탐색
    for i in range(n):
        for j in range(m):
            if visited[i][j]==0 and data[i][j]==1:
                bfs(i, j, visited)
                result += 1
        

    #output
    print(result)
