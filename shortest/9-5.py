"""
[ch09.shortest] 전보 | 난이도3 | 유명알고리즘대회
INPUT: 도시 개수N, 통로 개수M, 메시지 보내려는 도시C, 통로 정보
    * 첫째 줄에 공백으로 구분된 N, M, C
    * 1<=N<=30000, 1<=M<=200000, 1<=C<=N
    * 둘째 줄부터 M+1번째 줄에 통로에 대한 정보 X, Y, Z
    * X->Y로 보내는데 걸리는 시간이 Z
OUTPUT: 도시 C에서 보낸 편지를 받는 도시 총 개수, 총 걸리는 시간을 공백으로 구분하여 출력
"""
"""
[풀이]
한 도시 c에서 다른 도시로 가는 최단거리 구하는 문제
=> 다익스트라 알고리즘 사용
"""
import heapq
import sys

INF = int(1e9)

#input
input = sys.stdin.readline
n, m, c = map(int, input().split())    # 도시 개수, 통로 개수, 도시 c

# 연결 노드 정보를 담을 리스트
graph = [ [] for i in range(n+1) ]

# 최단거리 리스트
shortdist = [INF]*(n+1)

# 통로 정보를 입력받아 그래프 초기화
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y,z))

#solve
# 다익스트라 알고리즘
def dijkstra(start):
    q = []

    #시작노드에 대해 큐 삽입, 거리 0 설정
    heapq.heappush(q, (0, start))
    shortdist[start] = 0

    while q:
        # 큐에서 팝
        dist, now = heapq.heappop(q)
        if shortdist[now] < dist:
            continue

        # 현재 노드와 인접한 다른 노드 확인
        for i in graph[now]:
            cost = dist + i[1]
            if cost < shortdist[i[0]]:
                shortdist[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(c)

#output
cnt = 0
max_dist = 0

for d in shortdist:
    if d!= INF:
        cnt = cnt + 1
        max_dist = max(max_dist, d)

print(cnt-1, max_dist)
