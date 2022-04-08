"""
[ch16.dp] 16-34: 병사 배치하기 | 난이도1.5 | 핵심 유형
문제링크: https://www.acmicpc.net/problem/18353
INPUT: 병사 수n, 각 병사의 전투력
    * 첫째 줄에 n ( 1<=n<=2000)
    * 둘째 줄에 공백으로 구분된 전투력 (10000000보다 작거나 같음)
OUTPUT: 남아있는 병사가 최대가 되도록 하기 위해 열외시켜야 할 병사의 수
"""

#input
n = int(input())
data = list(map(int, input().split()))

"""
[풀이]
병사를 열외시켜서 전투력 기준 내림차순으로 만들 것
이때, 열외 시키는 병사 수를 최소로 만들어야 함

'가장 긴 증가하는 부분 수열 (LIS;Longest Increasing Subsequence)'
: 하나의 수열이 주어졌을 때 값들이 증가하는 형태의 가장 긴 부분 수열을 찾는 문제

dp[i] = array[i]를 마지막 원소로 가지는 부분 수열의 최대 길이
"""

#solve
data.reverse()    #순서를 뒤집어 lis문제로 변환
dp = [1] * (n)

#가장 긴 증가하는 부분 수열 LIS 알고리즘 수행
for i in range(1,n):
    for j in range(0, i):
        if data[j] < data[i]:
            dp[i] = max(dp[i], dp[j]+1)


#output            
# 열외시킬 병사 최소 수 출력
print(n-max(dp))
