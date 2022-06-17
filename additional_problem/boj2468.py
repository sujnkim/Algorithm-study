"""
[BOJ] 2468: 안전 영역
문제링크: https://www.acmicpc.net/problem/2468
INPUT: 
    * 첫째 줄에 2차원 배열의 행과 열의 개수를 나타내는 n (2<=n<=100)
    * 둘째 줄부터 n개의 줄에 지역 높이 정보
    * 높이 정보는 1이상 100이하의 정수
OUTPUT: 첫째 줄에 장마철에 물에 잠기지 않는 안전한 영역 최대 개수를 출력


[풀이 구상]
물에 잠기는 높이 = h라고 하자
h값에 따라 안전영역(잠기지 않는 지점)의 개수가 달라진다
즉, h값을 변화시키면서 안전 영역 개수를 계산하여 최대값으로 갱신해나가면 된다
    * h값은 입력 데이터의 1씩 증가시키며 확인
    * h=가장 큰 값인 경우: 모두 잠기기 때문에 확인할 필요가 없음

안전 영역 개수를 계산하는 과정에서 bfs알고리즘을 사용 할 것
    * 사실 처음에 dfs를 이용하여 풀려고 했으나... 시간초과/메모리초과가 나서
    * bfs로 다시 풀었다... 아마 재귀함수를 사용해서 그런듯하다
    * bfs는 큐 자료구조를 사용하여 구현함

"""
import sys
from collections import deque

#input
input = sys.stdin.readline

n = int(input())

data = []
max_height = 0        #최대빗물높이
for i in range(n):
    data.append(list(map(int, input().split())))
    max_height = max(max_height, max(data[i]))

    
#solve

dx = [-1, 0, 1, 0]  
dy = [0, 1, 0, -1]

def bfs(x, y, height, visited):
    que = deque()
    que.append((x, y))
    visited[x][y] = 1

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<n \
                and data[nx][ny] > h and visited[nx][ny]==0:
                    visited[nx][ny] = 1
                    que.append((nx, ny))


result = 0

for h in range(max_height):

    # 방문지역 표시를 위한 이차원 리스트
    visited = [ [0]*n for _ in range(n)]
    cnt = 0
    
    for i in range(n):
        for j in range(n):

            # h보다 높은 지역이고 방문하지 않았다면
            if data[i][j] > h and visited[i][j] == 0:
                bfs(i, j, h, visited)
                cnt += 1

    result = max(result, cnt)

    
#output
print(result)