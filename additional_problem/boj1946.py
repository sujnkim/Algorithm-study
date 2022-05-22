"""
[BOJ] 1946: 신입 사원
문제 링크: https://www.acmicpc.net/problem/1946
INPUT: 테스트케이스 tc, 지원자 수n, 지원자 별 서류/면접 성적
    * 첫째 줄에 tc (1<=tc<=20)
    * 각 tc별 첫째 줄에 n (1<=n<=100,000)
    * 각 tc별 n개의 줄에 공백으로 구분된 서류 성적, 면접 성적 등수
OUTPUT: 각 테스트 케이스에 대해서 선발할 수 있는 신입사원의 최대 인원수를 한 줄에 하나씩 출력
"""

"""
선발 원칙
다른 모든 지원자와 비교했을 때 적어도 하나가 다른 지원자보다 떨어지지 않는 사람
A의 성적이 어떤 다른 지원자 B의 성적보다 모두(둘 다) 떨어지는 경우 => 선택 x

n이 최대 100,000이므로
=> 이중for문을 사용하여 전부 비교할 경우 시간초과가 날 것
=> readline으로 입력을 받아주기

서류 성적 등수가 높은 순으로 정렬(오름차순) -> 서류 성적은 신경쓸 필요가 없어짐
면접 성적과 현재 높은 등수 값(high)을 비교
    -> 면접 성적 등수가 더 낮을 경우 선택x
    -> 면접 성적 등수가 high보다 높을 경우 high를 변경해주기
                        
"""
import sys
input = sys.stdin.readline

for tc in range(int(input())):

    #input
    n = int(input())

    score = []
    for _ in range(n):
        a, b = map(int, input().split())
        score.append((a, b))


    #solve

    #서류 점수 기준으로 정렬 => 면접 점수만 비교
    score.sort()    

    result = 0
    high = score[0][1]
    
    for i in range(n):
        a, b = score[i]

        # 면접 등수가 낮을 경우
        if high < b:
            continue

        # 면접 등수가 높거나 같을 경우
        result += 1
        high = min(high, b)
        
    #output
    print(result)