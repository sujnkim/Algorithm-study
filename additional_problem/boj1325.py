"""
[boj] 1325: 효율적인 해킹
문제링크: https://www.acmicpc.net/problem/1325
INPUT: 
    * 첫째 줄에 컴퓨터개수n, 관계 개수m
    * m개의 줄에 신뢰관계 a, b (a가 b를 신뢰함)
OUTPUT: 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터 번호를 오름차순으로 출력

문제풀이:
a가 b를 신뢰한다 = b를 해킹하면 a도 해킹할 수 있다.
즉 b -> a 단방향으로 연결된 그래프처럼 생각할 수 있음.

bfs를 이용하여 시작점에서부터 몇 개의 노드에 도달할 수 있는 지 계산
새로운 노드를 큐에 append할 때마다 cnt를 증가시킨 후 마지막에 return

max_value값을 이용하여 더 큰 값이 나올 경우
결과 리스트를 초기화하는 방식으로 구현
마지막에 결과 리스트를 출력해주면 됨

python3로 제출하면 시간 초과 발생. pypy3로 제출.
"""
import sys
from collections import deque

#input
inputdata = sys.stdin.readline
n, m = map(int, input().split())

#인접 리스트 생성
graph = [ [] for _ in range(n+1) ]
for _ in range(m):
    a, b = map(int, input().split())  #a가 b를 신뢰
    graph[b].append(a)                #b를 해킹하면 a도 해킹됨


# bfs 너비 우선 탐색 알고리즘
def bfs(start, graph, visited):
    que = deque()
    que.append(start)
    visited[start] = True
    cnt = 1    #해킹 가능한 컴퓨터 개수
    
    while que:
        now = que.popleft()

        for next_node in graph[now]:
            if visited[next_node] == False:
                visited[next_node] = True
                que.append(next_node)
                cnt += 1

    return cnt

    
#solve
max_list = []    #정답을 저장할 리스트
max_value = -1   # 가장 많이 해킹 가능한 경우의 개수

for start in range(1, n+1):    #모든 컴퓨터에 대하여
    visited = [False]*(n+1)
    cnt = bfs(start, graph, visited)

    if cnt > max_value:
        max_list.clear()       #정답 리스트 초기화
        max_list.append(start)
        max_value = cnt
    elif cnt == max_value:
        max_list.append(start)

#output
for k in max_list:
    print(k, end=' ')