"""
[ch17.shortest] 17-38: 정확한 순위 | 난이도2 | k대회
INPUT:
    * 첫째 줄에 학생 수n(2<=n<=500), 성적 비교 횟수 m(2<=m<=10,000)
    * 다음 m개의 줄에 학생 성적을 비교한 결과를 나타내는 양의 정수 a, b
    * a학생의 성적이 b학생보다 낮다는 의미
OUTPUT: 성적 순위를 정확히 알 수 있는 학생이 몇 명인지 출력
"""
"""
성적이 낮은 학생이 높은 학생을 가리키는 방향 그래프로 표현
=> A에서 B에 도달이 가능한 경우, 성적을 비교할 수 있음
=> 도달할 수 없는 경우, 성적을 비교할 수 없음

학생 수 n이 500이하이므로, 플로이드-워셜 알고리즘을 이용할 수 있음
모든 노드에 대해 다른 노드와 서로 도달 가능한 지 체크하여 문제 해결
=> 특정 노드의 카운트 값이 n이면, 정확한 순위를 알 수 있음
"""
import sys

#input
imput = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

graph = [ [INF]*(n+1) for _ in range(n+1) ]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

    
#solve
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


#output
total = 0

for i in range(1, n+1):
    cnt = 0
    for j in range(1, n+1):
        if graph[i][j]!=INF or graph[j][i]!=INF:
            cnt += 1
    if cnt == n:
        total += 1

print(total)