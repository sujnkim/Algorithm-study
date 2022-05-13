"""
[BOJ] 4796: 캠핑
문제 링크: https://www.acmicpc.net/problem/4796
INPUT: 여러 개의 테스트 케이스마다 L, P, V가 주어짐 (1<L<P<V)
    * 연속하는 P일 중, L일동안만 캠핑장 사용 가능
    * V일짜리 휴가를 시작
    * 마지막 케이스에는 0, 0, 0이 주어짐
OUTPUT: 각 테스트 케이스에 대해서, 캠핑장을 최대 며칠동안 사용할 수 있는지 출력
"""

tc = 0
while(1):
    #input
    l, p, v = map(int, input().split())

    # 테스트 케이스 종료 조건
    if l==0 and p==0 and v==0:
        break
    
    #solve
    cycle = v // p
    rest = v % p

    # 나머지와 l의 대소에 따라 계산식이 다름(주의)
    if rest >= l:
        result = cycle * l + l
    else:
        result = cycle * l + rest
    tc += 1
    
    
    #output
    print(f"Case {tc}: {result}")