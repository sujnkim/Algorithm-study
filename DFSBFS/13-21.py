"""
[ch13.DFSBFS] 13-21: 인구이동 | 난이도2 | 삼성전자sw역량테스트
문제링크: https://www.acmicpc.net/problem/16234
INPUT: 땅 크기n, 인구차 l,r
    * 첫째 줄에 공백으로 구분된 n, l, r
    * 둘째 줄부터 n개의 줄에 각 나라의 인구수
OUTPUT: 각 나라의 인구수가 주어졌을 때, 인구이동이 몇 번 발생하는지
"""
from collections import deque

# input

# 땅의 크기n, 인구차이 l,r
n, l, r = map(int, input().split())

data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

"""
[풀이 구상]
사실... 처음에 문제 이해 못했었다ㅎㅎ
1. 인구 차이가 l~r 사이인 경우 국경선 열고 연합으로 간주
2. 연합 내의 인구 계산식: (연합 인구수)/(연합을 이루는 칸 개수)
3. 연합 해체, 국경선 닫음

1~3 과정을 통해 각 나라의 인구수가 재조정 되었음
즉, 다시 1~3 과정을 거치면서 연합 내의 인구수가 평준화되었기 때문에
차이가 l보다 작게 나와 국경을 열지 못하게 될 것...
-> 1~3 과정을 총 몇 번 수행할 수 있는지를 묻는 문제
즉, 국경선을 연 국가가 없을 때까지 몇 번 과정을 수행했는가

-----
가까운 국가부터 확인하면서 한 집단으로 간주하므로 bfs가 적합할 것 같다 -> 큐
이중for로 전체 맵을 돌면서 현재위치의 4방향 확인
확인한 국가가 기준에 적합할 경우 큐에 append 하자
연합 내의 인구를 새롭게 계산해야 하므로 총 연합 인구수를 더하는 것도 필요

"""
#solve

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y, index):

    # (x,y)와 연결된 나라 정보를 담는 리스트
    # 인구 이동할 때 연합 내 국가의 위치가 필요하기 때문에 생성
    united = []
    united.append((x,y))

    # 큐 생성
    que = deque()
    que.append((x,y))

    union[x][y] = index    #현재 연합에 번호 할당
    psum = data[x][y]        # 연합 총 인구 수
    country = 1            # 연합 내 국가 수

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<n and union[nx][ny]==-1 :

                # 차이가 범위 내(l,r)내에 존재할 경우
                if l <=abs(data[x][y]-data[nx][ny])<=r:
                    que.append((nx,ny))
                    union[nx][ny] = index
                    psum += data[nx][ny]
                    country += 1
                    united.append((nx,ny))

    # 인구 이동
    for i, j in united:
        data[i][j] = psum // country
                
    
total_cnt = 0
while True:

    union = [ [-1]*n for _ in range(n) ]    #방문한 곳 표시
    index = 0    # 현재 존재하는 연합의 개수
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                bfs(i, j, index)
                index += 1

    # 모든 인구 이동이 끝난 경우
    # 현재 존재하는 연합이 n*n개 일때 = 인구이동이 없을 때
    if index == n*n:
        break
    total_cnt += 1

print(total_cnt)

"""
[느낀점]
+ if문에서 이상,이하 두 조건 모두 확인할 때
-> a<=x and x<=b 이 아니라 한 번에 a<=x<=b라고 써도 된다

+ 문제를 이해한 뒤에 구현할 때 왜 이렇게 헤맸는지 모르겠다...
-> 다시 연습해봐야 할 듯
"""