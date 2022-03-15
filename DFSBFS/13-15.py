"""
[ch13.DFSBFS] 13-15: 특정 거리의 도시 찾기 | 난이도1.5 | 핵심 유형
INPUT: 도시개수n, 도로개수m, 거리정보k, 출발도시번호x
    * 첫째 줄: 공백으로 구분된 n, m, k, x
    * 둘째 줄이후 m개의 줄 : 공백으로 구분된 자연수, 단방향 도로가 존재함을 의미
OUTPUT: x에서 출발해서 도달할 수 있는 도시 중 최단 거리가 k인 모든 도시 번호
    * 한 줄에 하나씩 출력
    * 최단거리가 k인 도시가 존재하지 않을 경우 -1 반환
"""
from collections import deque

#input
n, m, k, x = map(int, input().split())

# graph : 연결 리스트 사용
graph = [ [] for _ in range(n+1) ]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

#print(graph)
    
"""
[풀이 구상]
모든 거리 길이가 1... 실전4 미로 문제처럼 풀면 되지 않을까 ?

현재 노드에 연결된 노드들을 탐색하며 가까운 것들부터 확인해나가자 -> bfs
bfs를 구현하려면 큐가 필요하므로 deque 라이브러리를 사용

if 이미 방문한 곳이 아닐 경우에만,
( 한 번 방문한 곳은 dist가 0이 아니게 되므로 dist[i] == 0인 경우만)
* 큐에 삽입
* 현재 노드에 연결된 노드의 최단거리 = 현재 노드의 최단거리 + 1

최단거리를 전부 저장한 후, dist가 k인 경우만 출력
만약, dist가 k인 노드가 없을 경우 -1 출력

"""
#solve
def bfs(start):

    dist = [0]*(n+1)   #최단거리 저장 리스트

    # 큐 생성 및 시작 노드 삽입
    queue = deque()
    queue.append(start)

    while queue:
        #print(queue)
        now = queue.popleft()

        for d in graph[now]:

            # 처음 방문하는 경우에만
            if dist[d] == 0:
                queue.append(d)
                dist[d] = dist[now] + 1
            else:
                continue

    #print
    check = 0         # dist가 k인 노드가 있는지 확인하기 위한 변수
    for i in range(len(dist)):
        if dist[i]==k:
            print(i)
            check = 1

    # 최단거리가 k인 노드가 존재하지 않을 경우
    if check == 0 :
        print(-1)

    return


# output
bfs(x)

"""
[느낀점]
+ 그래프에서 모든 간선의 비용이 동일할 때에는 bfs를 이용하여 최단거리 찾을 수 있음
-> 모든 거리의 길이가 1이므로 너비 우선 탐색 사용

+ 노드개수 최대 300,000개 & 간선의 개수 최대 1,000,000개
-> 시간복잡도 O(N+M)으로 동작하는 소스코드를 작성하면 됨
-> 특정 도시 x를 시작점으로 bfs를 수행하여 모든 도시의 최단거리 계산
    & 최단거리를 하나씩 확인하며 k인 경우에 해당 도시 번호 출력

+ 1차원 리스트, 2차원 리스트 만들 때 헷갈렸다...
-> 위의 문제에서 result 일차원 리스트를 생성할 때 [0]*(n+1)이 아니라
[ 0*(n+1) ]이라고 생각해서 IndexError가 발생했었음
-> 일차원리스트 초기화: [0]*(n) ... n by 1
-> 이차원리스트 초기화: [ [0]*(n) for _ in range(n) ] ... n by n
"""