"""
[boj] 2343: 기타 레슨
문제 링크: https://www.acmicpc.net/problem/2343
INPUT:
    * 첫째 줄에 강의 개수N, 블루레이 개수M
    * 둘째 줄에 강의 길이가 순서대로 주어짐
OUTPUT: 가능한 블루레이 크기 중 최소값
"""
import sys

#input
input = sys.stdin.readline

n, m = map(int, input().split())
videos = list(map(int, input().split()))


#solve
result = 0
start = max(videos)    #모든 레슨이 담길 수 있어야 함
end = sum(videos)      # 1개의 블루레이에 담기는 경우

while start <= end:
    mid = (start + end) // 2
    print(start, end)
    print('mid:', mid)

    #블루레이 개수 계산
    cnt = 0
    minutes = 0
    for v in videos:
        if minutes + v > mid:
            cnt += 1
            minutes = 0
        minutes += v
        
    if minutes > 0:
        cnt += 1

    # 블루레이 개수가 많을 경우: 길이를 늘임
    if cnt > m:
        start = mid + 1
    else:
        result = mid
        end = mid - 1

    print('result:', result)
    print()
     
#output
print(result)