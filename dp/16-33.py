"""
[ch16.dp] 16-33: 퇴사 | 난이도2 | 삼성전자sw역량
문제링크: https://www.acmicpc.net/problem/14501
INPUT: 남은 일수 n, 각 상담 완료까지 걸리는 시간 ti, 받을 수 있는 금액 pi
    * 첫째 줄에 n (1<=n<=15)
    * 둘째 줄부터 n개의 줄에 공백으로 구분된 ti, pi (1<=ti<=5, 1<=pi<=1000)
OUTPUT: 얻을 수 있는 최대 이익
"""

#input
n = int(input())    #남은 일수
t = []                # 각 상담에 걸리는 시간
p = []                # 각 상담 완료 시 받는 돈
for _ in range(n):
    # 걸리는 시간t, 받는 돈p
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)


"""
[풀이]
상담 하는 데 필요한 기간은 1일보다 클 수 있음 -> 모든 상담 불가
퇴사하는 날 전에 상담이 끝나야 함

idea: 뒤쪽 날짜부터 거꾸로 확인하는 방식으로 접근

dp[i] = i번째 날부터 마지막 날까지 낼 수 있는 최대 이익
점화식 dp[i] = ( p[i] + dp[ i+t[i] ], max_value )

ex) i=1일 때, 걸리는 시간 t[1]=3, 받는 돈 p[1]
1일 차에 상담을 진행하는 경우 받는 돈
= 1일차 상담금액 p[1] + (1+t[1]=4)일 부터의 최대 상담 금액
"""

# solve
dp = [0] * (n+1)
max_value = 0        # 현재까지 최대 상담 금액

# n-1 ... 0
for i in range(n-1, -1, -1):

    # 상담이 기간 내에 완료될 경우
    if t[i] + i <= n:
        dp[i] = max(p[i]+dp[i+t[i]], max_value)
        max_value = dp[i]

    # 상담이 기간을 벗어나는 경우
    else:
        dp[i] = max_value    


#output
print(max_value)