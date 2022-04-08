"""
[ch16.dp] 16-31: 금광 | 난이도1.5 | Flipkart인터뷰
INPUT: 테스트케이스t, 금광 크기 nxm
    * 첫째 줄에 테스트 케이스 개수 t (1<=t<=100)
    * 케이스 첫째 줄에 공백으로 구분된 n, m (1<=n,m<=20)
    * 케이스 둘째 줄에 공백으로 구분된 금 매장 개수 (0 이상 100이하)
OUTPUT: 케이스마다 얻을 수 있는 금의 최대 크기 (줄바꿈)
"""

"""
[풀이 구상]
jth 열에 도달하려면 무조건 (j-1)th 열을 거쳐야 함
즉, 1번째 열부터 n번째 열까지 계산하며 dp를 채워나가면 될 것
최종 답은 m번째 열의 max값

i행 j열에 도달할 수 있는 경우 (3가지)
1) dp[i-1][j-1]
2) dp[i][j-1]
3) dp[i+1][j-1]

dp[i][j] = max(dp[i-1][j-1], dp[i][j-1], dp[i+1][j-1]) + data[i][j]
"""


def solution(n, m, data):

    # 다이나믹 프로그래밍을 위한 2차원 리스트
    dp = [ [0]*(m+2) for _ in range(n+2) ]

    #각 열을 돌면서
    for j in range(1, m+1):
        for i in range(1, n+1):

            # dp[i-1][j-1], dp[i][j-1], dp[i+1][j-1] 중 max
            temp = max(dp[i-1][j-1], dp[i][j-1])
            temp = max(temp, dp[i+1][j-1])
            dp[i][j] = temp + data[i][j]

    result = 0
    for i in range(1, n+1):
        result = max(result, dp[i][m])

    return result
        
"""
# test case 개수
t = int(input())

for _ in range(t):

    # 금광 크기 nxm
    n, m = map(int, input().split())

    # 매장된 금 개수 입력
    temp = list(map(int, input().split()))

    data = [ [0]*(m) for _ in range(n) ]
    for i in range(n):
        for j in range(m):
            data[i][j] = temp[i*m+j]

    print(solution(n, m, data))
"""

#test1
n, m = 3, 4
temp = [1,3,3,2,2,1,4,1,0,6,4,7]
array = [ [0]*(m+2) for _ in range(n+2) ]
for i in range(n):
    for j in range(m):
        array[i+1][j+1] = temp[i*m+j]
print(solution(n, m, array))

#test2
n, m = 4, 4
temp = [1,3,1,5,2,2,4,1,5,0,2,3,0,6,1,2]
array = [ [0]*(m+2) for _ in range(n+2) ]
for i in range(n):
    for j in range(m):
        array[i+1][j+1] = temp[i*m+j]
print(solution(n, m, array))
