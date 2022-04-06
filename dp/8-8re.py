import time

#input
n, m = map(int, input().split())
data = []
dp = [10001] * (10001)    # 10001 -> 해당 값을 만들 수 없음
dp[0] = 0                # 화폐 0개일 때 -> 0원을 만들 수 있음

for _ in range(n):
    temp = int(input())
    data.append(temp)
    dp[temp] = 1

#solve
start = time.time()

"""
# 8-8.py의 경우
# 각 화폐의 경우마다
for i in range(n):
    # j = data[i] ... m
    # dp[j]의 값을 update
    for j in range(data[i], m+1):
        # dp[j-화폐]를 만들 수 있다면
        if dp[j-data[i]] != 10001:
            # dp[j]와 dp[j-화폐]+1을 비교해서 작은 값으로 update
            dp[j] = min(dp[j], dp[j-data[i]]+1)
"""

# m=10000 * n=100
# data[0] ~ m까지 앞에서부터 채워나감
for i in range(data[0], m+1):
    for d in data:
        # d값이 커서 리스트 범위를 벗어나는 경우
        if i-d < 0:
            continue
        else:
            dp[i] = min(dp[i-d]+1, dp[i])

#print(dp)

#output
if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])

end = time.time()
print(f"{end-start:.5f} sec")