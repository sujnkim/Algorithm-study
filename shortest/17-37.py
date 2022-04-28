"""
[ch17.shortest] 17-37: 플로이드 | 난이도1.5 | 핵심유형
문제링크: https://www.acmicpc.net/problem/11404
INPUT:
    첫째 줄에 도시의 개수 n (1<=n<=100)
    둘째 줄에 버스의 개수 m (1<=m<=100,000)
    셋째 줄~m+2줄에 버스의 정보: 시작도시a, 도착도시b, 비용c
OUTPUT: i에서 j로 가는 데 필요한 최소 비용을 저장한 n개의 줄
        갈 수 없는 경우 0 출력
"""
"""
[풀이구상]
i -> j로 가는 모든 최소 비용를 구해야 하고, 노드 개수가 최대 100개이므로
시간 복잡도가 O(n^3)인 플로이드-워셜 알고리즘을 사용해도 될 것 같다

입력에서 시작-도착 도시를 연결하는 노선이 하나가 아닐 수 있다고 했는데,
최소 비용를 구하는 문제이므로 더 작은 비용 입력값이 주어질 경우에 변경하도록 하면 될 것 같다
"""
import sys

INF = int(1e9)
 
input = sys.stdin.readline

#input
n = int(input())
m = int(input())

# 그래프 정보 저장 이차원 리스트 초기화
graph = [ [INF]*(n+1) for _ in range(n+1) ]

# i -> i인 경우 비용은 0
for a in range(1, n+1):
    for b in range(1, n+1):
        if a==b:
            graph[a][b] = 0

# 그래프 정보 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    # 새로 입력 받은 비용이 더 작은 경우에만
    if c < graph[a][b]:
        graph[a][b] = c


# solve
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


#output
for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print(0, end=' ')
        else:    
            print(graph[i][j], end=' ')
    print()
