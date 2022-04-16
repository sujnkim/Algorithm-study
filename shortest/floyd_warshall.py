# 플로이드 워셜 알고리즘 소스코드

INF = int(1e9)    #무한을 의미하는 값:10억

# 노드, 간선 개수
n, m = 4, 7

# 그래프 간선 정보
data = [
    [1, 2, 4],
    [1, 4, 6],
    [2, 1, 3],
    [2, 3, 7],
    [3, 1, 5],
    [3, 4, 4],
    [4, 3, 2]
]

# 2차원 리스트에 그래프 정보 저장
graph = [ [INF]*(n+1) for _ in range(n+1) ]

# a->a로 가는 값: 0으로 초기화
for a in range(1, n+1):
    graph[a][a] = 0

# 각 간선 정보로 graph 초기화
for i in range(m):
    a, b, val = data[i]
    graph[a][b] = val


# 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행 결과 출력
for a in range(1, n+1):
    for b in range(1, n+1):
        #갈 수 없는 경우: INFINITY 출력
        if graph[a][b] == INF:
            print("INFINITY", end=" ")
        else:
            print(graph[a][b], end=" ")
    print()