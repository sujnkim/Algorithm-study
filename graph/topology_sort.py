"""
위상 정렬Topology Sort:
정렬 알고리즘의 일종, 순서가 정해져 있는 일련의 작업을 차례대로 수행해야 할 때 사용할 수 있는 알고리즘
방향 그래프의 모든 노드를 '방향성에 거스르지 않도록 순서대로 나열'하는 것\

진입 차수Indegree:
특정 노드로 들어오는 간선의 개수

1. 진입차수가 0인 노드를 큐에 삽입
2. 큐가 빌 때까지 다음을 반복
    1) 큐에서 원소를 꺼내, 해당 노드에서 출발하는 간선을 그래프에서 제거
    2) 새롭게 진입 차수가 0이 된 노드를 큐에 삽입

모든 원소를 방문하기 전에 큐가 비는 경우 = 사이클이 존재

큐에서 빠져나간 노드를 순서대로 출력 = 위상 정렬 수행 결과
위상 정렬의 답안은 여럭 가지가 될 수 있음
"""
from collections import deque

#노드 개수, 간선 개수 입력
v, e = map(int, input().split())

#모든 노드의 진입차수 0으로 초기화
indegree = [0] * (v+1)

#각 노드에 연결된 간선 정보를 담기 위한 연결 리스트
graph = [ [] for _ in range(v+1) ]

# 방향 그래프 간선 정보 입력받기
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

    
# 위상 정렬 함수
def topology_sort():
    result = []
    q = deque()

    # 처음 시작할 때, 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    # 결과 출력
    for i in result:
        print(i, end = ' ')


topology_sort()


""" 
위상 정렬 시간 복잡도 = O(V+E)
차례대로 모든 노드를 확인하면서, 해당 노드에서 출발하는 간선을 차례대로 제거
결과적으로 모든 간선과 노드를 확인한다는 측면
"""