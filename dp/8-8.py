"""
[ch08.dp] 8-8: 효율적인 화폐 구성 | 난이도2 | 실전문제
INPUT: 화폐종류n, 화폐가치합m, 각 화폐 가치
    * 첫째 줄에 공백으로 구분된 n, m (1<=n<=100, 1<=m<=10000)
    * 둘째 줄부터 각 화폐 가치 (10000보다 작거나 같은 자연수)
OUTPUT: m원을 만들기 위한 최소한의 화폐 개수
    * 만들 수 없다면 -1 출력
"""

#input
n, m = map(int, input().split())
data = []
for _ in range(n):
    data.append(int(input()))

"""
[풀이]
그리디파트에서 풀었던 거스름돈 문제와 유사
but, 화폐 단위에서 큰 단위가 작은 단위의 배수가 아니라는 점!!
-> 그리디 때처럼 가장 큰 화폐부터 처리하는 방법으로 풀 수 없음

dp 방식으로
적은 금액부터 큰 금액까지 확인하며 만들 수 있는 최소한의 화폐개수를 찾기
"""

#solve
dp = [10001] * (m+1)    # 10001 -> 해당 값을 만들 수 없음
dp[0] = 0                # 화폐 0개일 때 -> 0원을 만들 수 있음

# 각 화폐의 경우마다
for i in range(n):
    # j = data[i] ... m
    # dp[j]의 값을 update
    for j in range(data[i], m+1):
        # dp[j-화폐]를 만들 수 있다면
        if dp[j-data[i]] != 10001:
            # dp[j]와 dp[j-화폐]+1을 비교해서 작은 값으로 update
            dp[j] = min(dp[j], dp[j-data[i]]+1)

#output
if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])