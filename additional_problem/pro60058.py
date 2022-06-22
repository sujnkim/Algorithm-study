"""
[프로그래머스] 60058: 괄호 변환
문제링크: https://programmers.co.kr/learn/courses/30/lessons/60058
INPUT: 균형잡힌 문자열 p
    * '('와 ')'로만 이루어진 문자열
    * 길이는 2이상 1000이하 짝수 (괄호의 개수가 항상 같음)
OUTPUT:
    * 올바른 괄호 문자열로 변환한 결과를 return
"""
def check(p):
    cnt = 0
    for i in range(len(p)):
        if p[i] == '(':
            cnt += 1
        else:
            cnt -= 1

        if cnt < 0:
            return False
            
    return True
    

def solution(p):

    #p가 빈 문자열 -> 빈 문자열 반환
    if p == '':
        return p

    #p가 올바른 문자열 -> 그대로 반환
    if check(p) == True:
        return p

    #p를 u, v로 분리
    cnt, idx = 0, 0
    for i in range(len(p)):
        if p[i]=='(':
            cnt += 1
        elif p[i]==')':
            cnt -= 1

        if cnt == 0:
            idx = i
            break

    u = p[:idx+1]
    v = p[idx+1:]

    
    #u가 올바른 문자열인 경우
    if check(u)==True:
        return u + solution(v)
    
    #u가 올바른 문자열이 아닌 경우
    else:
        answer = '(' + solution(v) + ')'
        
        for i in range(1, len(u)-1):
            if u[i] == '(':
                answer += ')'
            else:
                answer += '('

    return answer


#input
p = input()

#output
print(solution(p))