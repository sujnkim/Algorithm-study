"""
[BOJ] 8958: OX퀴즈
문제 링크: https://www.acmicpc.net/problem/8958
INPUT: 여러 개의 테스트 케이스마다 OX로 이루어진 문자열이 주어짐
    * 첫째 줄에 테스트 케이스 개수 tc
    * OX로 이루어진 문자열 한 줄 (1<=문자열길이<=80)
OUTPUT: 각 테스트 케이스에 대해서, 점수를 출력
    * 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 됨
"""
import sys

for tc in range(int(input())):
    
    #input
    data = sys.stdin.readline()
        
    #solve
    result = 0        #결과
    zero_cnt = 0      # 현재 O이 몇 번 반복되었는지
    
    for d in data:
        if d == 'O':
            zero_cnt += 1
            result += zero_cnt
        else:
            zero_cnt = 0
    
    #output
    print(result)