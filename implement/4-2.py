"""
[ch4.구현] 4-2: 시각 | 난이도1 | 예제
INPUT: 정수n (0<=n<=23)
OUTPUT: 00시 00분 00초부터 n시 59분 59초 모든 시각에서 3이 하나라도 포함되는 모든 경우의 수
"""
import time

# input
n = int(input())

"""
[풀이 구상]
1. 내 풀이: 경우의 수 계산
00시 00분 00초 ~ n시 59분 59초 범위의 모든 경우의 수를 전체라고 하자
전체 - 3이 하나도 없는 경우의 수 = 3이 하나라도 포함된 경우의 수

2. 책 풀이: 완전 탐색Brute Force (가능한 모든 경우의 수를 검사하는 탐색 방법)
하루는 86,400(24*60*60)초이므로 모든 경우의 수가 100,100을 넘지 않는다.
따라서 문자열 연산을 이용하여 3이 포함되어 있는지 확인해도 제한 시간 2초 내에 해결 가능하다.

+ 일반적으로 확인 해야 할 전체 데이터 개수가 100만개 이하일 때 완전 탐색을 사용하면 적절하다고...
"""

# solve1---------------------------
start = time.time()
result1 = 0

total = (n+1)*6*10*6*10
if n>=3:
    no = n*5*9*5*9
else:
    no = (n+1)*5*9*5*9
result1 = total - no

#output
print(result1)

#time check
end = time.time()
print(f"{end-start:.5f} sec")

# solve2---------------------------
start = time.time()
result2 = 0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            # 매 시각 문자열 내에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i)+str(j)+str(k):
                result2 += 1
#output
print(result2)

#time check
end = time.time()
print(f"{end-start:.5f} sec")

"""
[느낀점]
대부분의 문제의 제한시간이 1~2초이므로 이중for문 이상을 쓰면 안된다고
단순하게 생각했었는데, 그게 아니라 주어진 데이터의 범위에 따라 
사용할 수 있는 알고리즘의 복잡도 수준이 달라진다는 것을 잘 알 수 있는 문제였다. 
"""