"""
[boj] 2110: 공유기 설치
문제링크: https://www.acmicpc.net/problem/2110
INPUT:
    * 집 개수n, 공유기 개수c
    * 둘째 줄부터 n개의 줄에 집의 좌표를 나타내는 x(1<=x<=1,000,000,000)
OUTPUT: 첫째 줄에 가장 인접한 두 공유기 사이의 최대 거리

문제 풀이:
집 좌표의 범위가 매우 넓기 때문에 하나씩 확인하는 방법으로 풀 경우 시간 초과가 발생한다.
따라서 이분 탐색을 이용하여 '공유기 사이의 거리(최소한 떨어져 있어야 하는 거리)'를 조절하며 확인하는 방식으로 해결.
"""
import sys

#input
input = sys.stdin.readline

n, c = map(int, input().split())
houses = []
for _ in range(n):
    houses.append(int(input()))

#solve
houses.sort()    #집 좌표를 정렬(계산을 위해)

result = 0
start = 1
end = houses[n-1] - houses[0]

while start <= end:
    mid = (start + end) // 2

    #공유기 개수 계산
    check = houses[0]    #공유기 설치 좌표
    cnt = 1
    for house in houses:
        if house >= check + mid:
            cnt += 1
            check = house

    #이분탐색 변수 갱신
    if cnt >= c:
        result = mid
        start = mid + 1    #거리 증가=>공유기 개수 감소
    else:
        end = mid - 1      #거리 감소=>공유기 개수 증가    

#output
print(result)