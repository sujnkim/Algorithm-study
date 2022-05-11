"""
[ch18.graph] 18-45: 최종 순위 | 난이도3 | NWERC 2010
문제 링크: https://www.acmicpc.net/problem/3665
INPUT:
    * 첫째 줄에 테스트 케이스 개수 (100개 이하)
    * 팀의 개수 n ( 2<=n<=500)
    * n개의 정수 ti = 작년에 i등을 한 팀 번호 (1<=ti<=n)
    * 상대적으로 등수가 바뀐 쌍의 개수 m (0<=m<=25000)
    * 두 정수 ai, bi를 포함하는 m개의 줄 (1<=ai<bi<=n)
OUTPUT: n개의 정수(올해의 순위)를 한 줄에 출력
        확실한 순위를 알 수 없다면 "?"출력
        순위를 정할 수 없는 경우 "IMPOSSIBLE" 출력
"""
"""
[풀이 구상]
상대적인 순위로 전체 순위를 파악 -> 위상 정렬 문제

작년의 순위 정보로 '자기보다 낮은 등수를 가진 팀을 가리키도록' 방향 그래프 생성
cf. 만약 이를 이용해 위상 정렬을 수행한다면 문제에서 제시된 순위 정보와 동일한 결과가 나올 것

상대적 순위가 바뀌는 경우, 해당 간선의 방향을 반대로 변경 => 위상 정렬 수행
1) 사이클이 발생: 노드가 N개 나오기 전에 큐기 비는 경우
    -> "IMPOSSIBLE"
2) 위상 정렬 결과가 여러 개인 경우: 2개 이상의 노드가 큐에 한 번에 들어가는 경우
    -> "?"

"""
from collections import deque

#input
n = int(input())

indegree  = [0] * (n+1)

# 노드 인접 간선 정보를 위한 인접 행렬 초기화
graph = [ [False]*(n+1) for i in range(n+1) ]

# 작년 순위 정보
last = list(map(int, input().split()))
for i in range(n):
    for j in range(i+1, n):
        graph[last[i]][last[j]] = True
        indegree[last[j]] += 1
        

# 올해 변경된 순위 정보
m = int(input())
for i in range(m):
    a, b = map(int, input().split())

    if graph[a][b]:
        graph[a][b] = False
        graph[b][a] = True
        indegree[b] -= 1
        indegree[a] += 1
    else:
        graph[a][b] = True
        graph[b][a] = False
        indegree[a] -= 1
        indegree[b] += 1
        

#solve
result = []
q = deque()

for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)

certain = True    # 결과가 하나인지 여부
cycle = False    # 사이클이 존재하는지 여부

for i in range(n):
    if len(q) == 0:
        cycle = True
        break
    if len(q) >= 2:
        certain = False
        break

    now = q.popleft()
    result.append(now)

    for j in range(1, n+1):
        if graph[now][j]:
            indegree[j] -= 1
            if indegree[j] == 0:
                q.append(j)
            

#output
if cycle:
    print("IMPOSSIBLE")
elif not certain:
    print("?")
else:
    for i in result:
        print(i, end=' ')
    print()