"""
[ch13.DFSBFS] 괄호 변환 | 난이도1 | 2020카카오신입공채1차
문제링크 : https://programmers.co.kr/learn/courses/30/lessons/60058
INPUT: '(', ')'로만 이루어진 문자열 p (2<=len(p)<=1,000인 짝수)
OUTPUT: 균형잡힌 문자열 p를 올바른 괄호 문자열로 변환하여 출력
"""

"""
#input
p = input()
"""
#p = '()))((()'

def check(p):
    # 올바른 괄후 문자열 확인 함수
    cnt1, cnt2 = 0, 0
    for i in range(len(p)):
        if p[i] == '(':
            cnt1 += 1
        else:
            cnt2 += 1

        if cnt1 < cnt2:
            return False

    return True
    

def solution(p):

    # 1. 빈 문자열 -> 빈 문자열 return
    if len(p) == 0:
        return ''

    # p가 올바른 괄호 문자열 -> 그대로 return
    if check(p) == True:
        return p

    # 2. 균형잡힌 괄호 문자열 계산
    cnt1, cnt2 = 0, 0
    for i in range(len(p)):
        if p[i] == '(':
            cnt1 += 1
        else:
            cnt2 += 1

        # ()의 개수가 같을 때
        if cnt1 == cnt2:
            break

    # u, v 분리
    u = p[:cnt1+cnt2]
    v = p[cnt1+cnt2:]

    
    # 3. if, u가 올바른 괄호 문자열인 경우
    if check(u) == True:
        # 문자열 v에 대해 과정 수행 -> u+v return
        return u+solution(v)

    # 4. u가 올바른 괄호 문자열이 아닌 경우
    else:
        #4-1~3
        temp = '(' + solution(v) + ')'    
        
        #4-4: u의 첫,마지막 글자 제거 후 괄호 뒤집기
        u = u[1:len(u)-1]
        for i in range(len(u)):
            if u[i] == '(':
                temp = temp +')'
            else:
                temp = temp + '('

        return temp


#output
#print(solution(p))

"""
[느낀점]
괄호방향 때문에 헷갈릴 수도 있지만, 문제 조건과 규칙만 잘 파악한다면 쉽게 풀 수 있는 문제
재귀함수를 사용하라고 문제에 적혀있어서... 쉬웠을지도 ?
"""