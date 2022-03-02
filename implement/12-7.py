"""
[ch12.구현] 12-7: 럭키 스트레이트 | 난이도1 | 핵심유형
INPUT: 점수n
    * 첫째 줄에 정수로 주어지는 점수n(10<=n<=99,999,999)
    * n의 자리수는 항상 짝수
OUTPUT: 럭키스트레이트를 사용할 수 있다면 "LUCKY", 사용할 수 없다면 "READY" 출력
"""
import time

#input
n = input()

"""
[풀이 구상]
주어진 n의 자릿수를 기준으로 왼쪽/오른쪽 두 부분으로 나누어
왼쪽 각 자릿수의 합 = 오른쪽 각 자릿수의 합인 경우
럭키스트레이트
"""
#solve
start = time.time()

strlen = len(n)//2
left, right = 0, 0

# 왼쪽 부분의 합
for i in range(strlen):
    left += int(n[i])

# 오른쪽 부분의 합
for i in range(strlen):
    right += int(n[i+strlen])

# output
# 왼쪽, 오른쪽 합 비교 후 답 출력
if  left == right:
    print("LUCKY")
else:
    print("READY")

#timecheck
end = time.time()
print(f"{end-start:.5f} sec")

"""
[느낀점]
+ 책의 예시 답안에서는 왼쪽 부분을 전부 더한 값에서 오른쪽 부분을 빼서
마지막 결과가 0이면 lucky를 출력하는 방식으로 설명하였다.
-> 처음에 나도 이 방식을 떠올리긴 했지만, left와 right를 직접 비교하는 것이
코드를 봤을 때 더 직관적으로 이해할 수 있을 거라고 생각해서 따로 더한 후 비교하였음
"""