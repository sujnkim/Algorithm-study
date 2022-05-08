"""
[ch10.graph] 10-9: 커리큘럼 | 난이도3 | 핵심 유형
INPUT: 강의 개수n, 걸리는 시간
    * 첫째 줄에 강의 개수 n(1<=n<=500)
    * 다음 n개의 줄에 강의 시간, 먼저 들어야하는 강의 번호가 주어짐
    * 강의 번호는 1~n까지 구성, 각 줄은 -1로 끝남
OUTPUT: n개의 강의에 대하여 수강하기까지 걸리는 최소 시간을 한 줄에 하나씩 출력
"""

"""
선수과목 => 위상정렬Topology sort 문제

각 노드와 인접한 노드를 확인하여
현재보다 강의 시간이 더 긴 경우를 찾아 값을 저장

"""
from collections import deque
import copy

#input
n = int(input())

# 진입차수 초기화
indegree = [0] * (n+1)

# 수강 시간 초기화
time = [0] * (n+1)

# 방향 그래프 정보 초기화
graph = [ [] for i in range(n+1) ]

# 선수과목 정보 입력
for i in range(1, n+1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for x in data[1:-1]:
        indegree[i] += 1
        graph[x].append(i)


#solve
def topology_sort():
    result = copy.deepcopy(time)
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()

        for i in graph[now]:
            result[i] = max(result[i], result[now]+time[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in range(1, n+1):
        print(result[i])
        
#output
topology_sort()