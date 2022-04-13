"""
idea: 못생긴 수에 2,3,5를 곱하면 못생긴 수가 된다
가장 작은 못생긴 수부터 오름차순으로 확인하며 2,3,5를 곱한 수를 저장
"""

n = int(input())

#못생긴 수를 저장할 리스트
ugly = [0] * n
ugly[0] = 1        # 첫 번째 못생긴 수는 1

i2 = i3 = i5 = 0

# 다음에 확인할 못생긴 수
next2, next3, next5 = 2, 3, 5 

# 1부터 n까지 못생긴 수 찾기
for l in range(1, n):
    # 가능한 결과 중 가장 작은 수 선택
    ugly[l] = min(next2, next3, next5)

    # 다음 못생긴 수 계산
    if ugly[1] == next2:
        i2 += 1
        next2 = ugly[i2] * 2
    if ugly[3] == next3:
        i3 += 1
        next3 = ugly[i3] * 3
    if ugly[5] == next5:
        i5 += 1
        next5 = ugly[i5] * 5


print(ugly[n-1])