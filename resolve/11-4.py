"""
만들 수 없는 금액
"""

#input
n = int(input())
data = list(map(int, input().split()))

#solve
data.sort()

# 만들 수 있는 지 확인할 수
target = 1

for d in data:

    # target보다 단위가 클 경우, target은 만들 수 없음
    if target < d:
        break

    # target보다 단위가 작거나 같을 경우
    # 이전의 결과와 d를 조합하여 만들 수 있음
    # target을 더 큰 수로 변경(갱신)
    target += d

print(target)