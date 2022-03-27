"""
[ch14.sorting] 14-26: 카들 정렬하기 | 난이도2 | 핵심유형
문제링크 : https://www.acmicpc.net/problem/1715
INPUT: n개의 숫자 카드 묶음의 크기
    * 첫째 줄에 n (1<=n<=100000)
    * n개의 줄에 숫자 카드 묶음의 각 크기
OUTPUT: 최소 비교 횟수
"""

"""
[풀이 구상]
가장 작은 카드 묶음 2개씩 합쳐나가기
-> 가장 작은 것 2개를 더함
-> 더한 값을 다시 자료에 넣음
항상 작은 값부터 정렬이 되어 있어야 하므로 우선순위 큐를 사용

우선순위큐
heapq 라이브러리: 리스트를 최소힙처럼 다룰 수 있게 만들어줌
heapq.heappush(), heapq.heappop()으로 푸시팝
"""
import heapq

#input
n = int(input())
data = []
for _ in range(n):
    heapq.heappush( data, int(input()) )

#solve
result = 0
for i in range(n-1):
    first = heapq.heappop(data)
    second = heapq.heappop(data)
    result += first + second
    heapq.heappush(data, first+second)
    #print(data)


print(result)


"""
[느낀점]
+ 책에 쓰여진 예시를 반대로 이해해서... 처음에 잘못 풀었다

+ 책 설명 추가)
매 상황에서 무조건 가장 작은 크기의 두 카드 묶음을 합치면 된다는 점에서
그리디 문제로도 볼 수 있음

"""