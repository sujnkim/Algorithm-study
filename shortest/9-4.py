"""
[ch09.shortest] 미래도시 | 난이도2 | M기업 코테
INPUT: 전체 회사 개수N, 경로 개수M, 경로 정보
    * 첫째 줄에 공백으로 구분된 n, m (1<=n,m<=100)
    * 둘째 줄부터 m+1번째 줄에 연결된 두 회사의 번호
    * m+2번째 줄에 공백으로 구분된 x, k (1<=k<=100)
OUTPUT: 방문판매원이 1번에서 출발하여 K번 회사를 거쳐 X번 회사로 가는 최소 이동 시간
        만약 도달할 수 없다면 -1 출력
"""
"""
[풀이]
문제에서 N의 범위가 100이하로 매우 작음
=> 구현이 간단한 플로이드 워셜 알고리즘을 이용하는 것이 유리

1번 -> k번 걸리는 시간 + k번 회사 -> x번 회사 걸리는 시간
graph[1][k] + graph[k][x]
"""

INF = int(1e9)    # 무한을 의미하는 값: 10억

#input
n, m = map(int, input().split())    # 노드, 간선 개수

# 그래프 정보를 담을 2차원 리스트: 무한으로 초기화
graph = [ [INF]*(n+1) for _ in range(n+1)]

# 자신->자신 거리 = 0으로 초기화
for i in range(1, n+1):
    graph[i][i] = 0

# 간선에 대한 정보로 리스트 초기화
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# x, k번 회사 입력
x, k = map(int, input().split())


#solve
for t in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][t] + graph[t][b])

result = graph[1][k] + graph[k][x]

#output
if result >= INF:
    print('-1')
else:
    print(result)