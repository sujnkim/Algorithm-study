"""
[ch08.dp] 8-5: 1로 만들기 | 난이도1.5 | 실전문제
INPUT: 정수 x (1<=x<=30,000)
OUTPUT: 연산을 하는 횟수의 최솟값
"""
#input
x = int(input())

"""
[풀이]
연산 4가지를 적절히 사용해서 1로 만들기
1) x가 5의 배수 -> 5로 나눔
2) x가 3의 배수 -> 3으로 나눔
3) x가 2의 배수 -> 2로 나눔
4) x에서 1을 뺌
"""
#solve
dp = [0] * 30001    # 연산 횟수를 저장하는 dp테이블 초기화

# 보텀업 다이나믹 프로그래밍
for i in range(2, x+1):
    
    dp[i] = dp[i-1] + 1

    if i%2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
    if i%3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)
    if i%5 == 0:
        dp[i] = min(dp[i], dp[i//5]+1)    

#output
print(dp[x])
