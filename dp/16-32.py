"""
[ch16.dp] 16-32: 정수 삼각형 | 난이도1.5 | IOI 1994년
문제링크: https://www.acmicpc.net/problem/1932
INPUT: 삼각형의 크기n, 정수 삼각형 데이터
    * 첫째 줄에 n (1<=n<=500)
    * 둘째 줄부터 n+1번째 줄 까지 정수 삼각형
OUTPUT: 합이 최대가 되는 경로에 있는 수의 합
"""

#input
n = int(input())

"""
[풀이]
dp[i][j] = data[i][j] + max(dp[i-1][j-1], dp[i-1][j])
특정 위치에 도달하기 위해서는 1)왼쪽 위, 2)바로 위 2가지 위치에서 내려올 수 있음
"""

"""
#solve1

data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

#solve
dp = [ [0]*(n+1) for _ in range(n+1) ]
for i in range(1, n+1):
    for j in range(1, i+1):
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + data[i-1][j-1]

#output
print(max(dp[n]))
"""

#solve2
dp = [0] * (n+1)
for i in range(n):
    data = list(map(int, input().split()))

    for j in range(i+1, 0, -1):
        dp[j] = max(dp[j], dp[j-1]) + data[j-1]

#output
print(max(dp))
