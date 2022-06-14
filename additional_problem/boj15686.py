"""
[BOJ] 15686: 치킨 배달
문제링크: https://www.acmicpc.net/problem/15686
INPUT:
* 첫째 줄에 도시 크기 n(2<=n<=50), 선택할 치킨집 개수 m(1<=m<=13)
* 둘째 줄부터 n개의 줄에 도시의 정보
    * 0: 빈칸, 1: 집, 2: 치킨집
    * 1<= 치킨집 개수<=2n

OUTPUT:
* 폐업시키지 않을 치킨집을 최대 m개 골랐을 때, 도시의 치킨 거리 최솟값 출력
"""
from itertools import combinations
import sys

#input
input = sys.stdin.readline
n, m = map(int, input().split())

chicken = []
house = []

# 집, 치킨집 좌표 저장 리스트
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 2:
            chicken.append((i,j))
        if data[j] == 1:
            house.append((i,j))

            
#solve
result = 1e9    # 도시 치킨 거리의 최소값

# m개의 치킨집 조합에 대해 도시 치킨 거리 계산
for selected in combinations(chicken, m):

    city_dist = 0

    # 각 집에 대하여 치킨 거리 계산
    for r1, c1 in house:
        chicken_dist = 1e9
        for r2, c2 in selected:     
            chicken_dist = min(chicken_dist, abs(r1-r2)+abs(c1-c2) )
    
        city_dist += chicken_dist

    result = min(result, city_dist)
    

#output
print(result)