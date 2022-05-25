"""
[BOJ] 10610: 30
문제링크: https://www.acmicpc.net/problem/10610
INPUT: 양수 N
    * 최대 10^5개의 숫자로 구성, 0으로 시작하지 않음
OUTPUT: 만들고 싶어하는 수를 출력, 존재하지 않는다면 -1 출력
    * 양수N에 포함된 숫자를 섞어 30의 배수가 되는 가장 큰 수
"""

#input
n = input()

data = []
data_sum = 0
for i in range(len(n)):
    now = int(n[i])
    data_sum += now
    data.append(now)

    
#solve
result = -1

# 가장 큰 수를 구하는 것이므로 내림차순 정렬
data.sort(reverse=True)

# 마지막 숫자가 0이 아니면 => 30의 배수가 아님
# 모든 숫자의 3의 배수가 아니면 => 30의 배수가 아님
if data[len(n)-1] == 0:
    if data_sum % 3 == 0:
        result = data

#output
if result == -1:
    print(result)
else:
    for d in result:
        print(d, end='')