"""
[boj] 2805: 나무 자르기
문제링크: https://www.acmicpc.net/problem/2805
INPUT:
    * 나무 수n, 집으로 가져가는 나무 길이m
    * 나무의 높이가 한 줄에 주어짐
OUTPUT: 적어도 m미터의 나무를 집에 가져가기 위해 설정할 수 있는
        절단기 높이의 최대값

cf. 이코테 책의 떡볶이 떡 만들기와 사실상 동일한 문제였음...
"""
import sys

#input
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

#solve
start = 0
end = max(trees)

result = 0
while start <= end:
    mid = (start+end) // 2

    #가져가는 나무길이 계산
    total = 0
    for t in trees:
        if t > mid:
            total += (t-mid)

    if total >= m:    #충분히 자름
        result = mid
        start = mid + 1
    else:             #양이 모자름(더 잘라야 함)
        end = mid - 1

#output
print(result)