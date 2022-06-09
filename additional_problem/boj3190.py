"""
[boj] 3190: 뱀
문제 링크: https://www.acmicpc.net/problem/3190

INPUT:
* 첫째 줄에 보드의 크기 n (2<=n<=100)
* 둘째 줄에 사과의 개수 k (0<=k<=100)
* 다음 k개의 줄에 사과의 위치 행, 열
* 다음 줄에 뱀의 방향 변환 횟수 l (1<=l<=100)
* 다음 l개의 줄에 방향 변환 정보 정수 x, d
    * 시작 후 x초 뒤에 왼쪽(L), 오른쪽(D)로 90도 회전

OUTPUT:
* 게임이 몇 초에 끝나는지 출력

요구사항:
* 시작 위치는 (1,1), 뱀의 길이는 1, 처음에는 오른쪽을 향함
* 이동 규칙
    * 몸길이를 늘려 머리를 다음 칸에 위치
    * 이동한 칸에 사과가 있다면, 사과는 없어지고 꼬리는 움직이지 않음(몸 길이 1 증가)
    * 이동한 칸에 사과가 없다면, 꼬리가 위치한 칸을 비워줌(몸길이 변화 없음)
* 벽 또는 자기 자신의 몸과 부딪히면 게임이 종료
"""
import sys
from collections import deque


#input
input = sys.stdin.readline

n = int(input())    #맵 크기
k = int(input())    #사과 개수

#사과 위치 저장
apple = [ [0]*(n+1) for _ in range(n+1) ]
for _ in range(k):
    x, y = map(int, input().split())
    apple[x][y] = 1


l = int(input())    #방향 변환 횟수
change_time = []
move = []
for _ in range(l):
    t, d = input().split()
    change_time.append(int(t))
    move.append((int(t), d))


#solve

#방향정보: 북, 동, 남, 서(오른쪽 +)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 시작 정보 초기화
x, y = 1, 1
dir = 1
snake = deque([(x, y)])
time = 0


while True:

    # 방향 변환
    if time in change_time:
        ndir = move[change_time.index(time)][1]
        #print(time, ndir)
        if ndir == 'L':
            dir = (dir+4-1) % 4
        elif ndir == 'D':
            dir = (dir+4+1) % 4

    # 다음 칸 위치
    nx = x + dx[dir]
    ny = y + dy[dir]
    time += 1

    # 종료 조건 확인
    if nx<=0 or ny<=0 or nx>n or ny>n:
        break
    if (nx,ny) in snake:
        break

    snake.append((nx,ny))

    if apple[nx][ny] == 1:    #사과가 있다면->사과제거
        apple[nx][ny] = 0
    else:                   #사과가 없다면->꼬리제거
        snake.popleft()

    #print(snake)
    x, y = nx, ny
            


#output
print(time)
