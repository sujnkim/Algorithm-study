"""
볼링공 고르기
"""

#input
n, m = map(int, input().split())
data = list(map(int, input().split()))


#solve
data.sort()

result = 0
cnt = [0] * (m+1)

for d in data:
    cnt[d] += 1

for i in range(1, m+1):
    n -= cnt[i]
    result += cnt[i] * n


#output
print(result)