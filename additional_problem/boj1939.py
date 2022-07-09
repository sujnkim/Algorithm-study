"""
[boj] 1939: 중량 제한
문제 링크: https://www.acmicpc.net/problem/1939
INPUT: 
    * 첫째 줄에 섬 개수N, 다리 개수M
    * M개의 줄에 다리 정보를 나타내는 A, B, C
    * A-B 섬 사이에 중량 제한이 C인 다리가 존재한다는 의미
    * 모든 다리는 양방향이다, 다리가 여러개일 수 있다.
    * 마지막 줄에 공장이 위치한 섬의 번호를 나타내는 두 정수
OUTPUT: 한 번의 이동에서 옮길 수 있는 물품 중량의 최대값
"""
import sys
from collections import deque

#input
input = sys.stdin.readline

n, m = map(int, input().split())

# 중량 데이터 저장: 인접 리스트
bridges = [ [] for _ in range(n+1) ]
for _ in range(m):
    a, b, c = map(int, input().split())
    bridges[a].append((b, c))
    bridges[b].append((a, c))    #양방향

x, y = map(int, input().split())


#solve
"""
x->y로 가는 방법: bfs로 구현
물품 중량의 범위 = 1 ~ 10억 (매우 큰 범위)
물품 중량을 기준으로 이분 탐색을 수행해야 할 듯
"""
def bfs(x, y, mid):
    visited = [0] * (n+1)    #방문기록 저장
    
    que = deque()
    que.append(x)
    visited[x] = 1

    while que:
        now = que.popleft()

        if now == y:    #도착한 경우
            return True

        for next_node, w in bridges[now]:
            if visited[next_node]==0 and w >= mid:
                visited[next_node] = 1
                que.append(next_node)

    return False    #도착하지 못한 경우
           

start = 1
end = 1000000000

result = 0
while start <= end:
    mid = (start + end) // 2

    if bfs(x, y, mid) == True:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

#output
print(result)