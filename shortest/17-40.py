"""
[ch17.shortest] 17-40: 숨바꼭질 | 난이도2 | USACO
INPUT:
    첫째 줄에 공백으로 구분된 헛간 개수 n(2<=n<=20,000), 통로 개수 m(1<=m<=50,000)
    이후 m개의 줄에 서로 연결된 헛간 번호(1<=A,B<=n)
OUTPUT: 숨어야하는 헛간 번호(최단 거리가 가장 먼 헛간), 헛간까지 거리, 같은 거리를 갖는 헛간 개수
"""
"""
[풀이]
n, m의 값이 크기 때문에 O(n^3)인 플루이드 워셜은 쓸 수 없을 것
=> 다익스트라 알고리즘으로 각 헛간까지 최단 거리를 구해야 함
시작 위치는 항상 1번 헛간이므로, 1번 노드에서 출발해서 다른 n-1개의 노드에 도착하는 최단거리를 구함
개선된 다익스트라는 힙을 사용하여 계산함 => heapq 라이브러리

최단 거리 배열을 돌면서 거리가 가장 먼 헛간 index, 값, 같은 거리를 갖는 헛간 개수 출력

입력으로 받는 개수가 크기 때문에 readline 함수를 사용하자
"""
import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

#input
n, m = map(int, input().split())

# 최단 거리 테이블 무한으로 초기화
distance = [INF] * (n+1)

# 그래프 정보를 담을 이차원 리스트
graph = [ [] for _ in range(n+1) ]
for _ in range(m):
    a, b = map(int, input().split())
    # 양방향 통로, 거리는 1
    graph[a].append((b,1))
    graph[b].append((a,1))    

    
# 다익스트라 알고리즘 수행
def dijkstra(start):
    q = []

    # 시작 노드 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            # i[0]: 노드 번호, i[1]: 거리
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

start = 1
dijkstra(start)

# output
max_idx = 0
max_val = 0
result = []

for i in range(1, n+1):
    # 최단거리가 더 큰 경우가 있을 때 => max정보 초기화
    if max_val < distance[i]:
        max_idx = i
        max_val = distance[i]
        result = [max_idx]
    
    # 최단 거리가 같을 때 => 결과 리스트에 추가
    elif max_val == distance[i]:
        result.append(i)

print(max_idx, max_val, len(result))