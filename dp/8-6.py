"""
[ch08.dp] 8-6: 개미전사 | 난이도2 | 실전문제
INPUT: 식량창고n, 각 식량창고의 식량개수k
    * 첫째 줄에 n (3<=n<=100)
    * 둘째 줄에 공백으로 구분된 식량개수 k (0<=k<=1000)
OUTPUT: 얻을 수 있는 식량의 최대값
"""
#input
n = int(input())
data = list(map(int, input().split()))

"""
[풀이]
서로 인접한 칸을 선택할 수 없음
-> 최소한 한 칸 이상 떨어진 칸들을 선택하여 합이 최대가 되도록 만드는 문제

현재 ith 칸을 계산하려고 한다
1) (i-1)th 칸을 선택한 경우 -> 현재 칸의 값을 합할 수 없음 = dp[i-1]
2) (i-2)th 칸을 선택한 경우 -> 현재 칸의 값을 합할 수 있음 = dp[i-2] + data[i]
두 경우 중 max값을 dp[i]값으로 update
즉, dp[i] = max( dp[i-1], dp[i-2]+data[i] )
"""

#solve
dp = [0] * 101

dp[0] = data[0]
dp[1] = max(data[0], data[1])

for i in range(2, n):
    dp[i] = max(dp[i-1], dp[i-2]+data[i])

#output
print(dp[n-1])