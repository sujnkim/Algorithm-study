"""
[ch14.sorting] 14-25: 실패율 | 난이도1 | 2019카카오신입공채
문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/42889
INPUT: 스테이지 개수n, 게임 이용자가 멈춘 스테이지 번호 배열 stages
OUTPUT: 실패율이 높은 스테이지부터 내림차순으로 스테이지 번호가 담긴 배열
"""

#input
n1 = 5
st1 = [2,1,2,6,2,4,3,3]

n2 = 4
st2 = [4,4,4,4,4]


#solve
"""
#런타임에러가 발생
def solution(N, stages):

    cnt = [0] * (N+2)
    for i in stages:
        cnt[i] += 1
    #print(cnt)

    temp = []
    sum = cnt[N+1]
    for i in range(N,0,-1):
        sum += cnt[i]
        cnt[i] = cnt[i] / sum
        temp.append((cnt[i], i))
    temp.sort( key=lambda x: (-x[0], x[1]) )
    
    #print(cnt)
    #print(temp)
    
    result = [i[1] for i in temp]
    
    return result
"""

def solution(N, stages):

    """
    스테이지 번호i를 증가시키며 해당 단계에 있는 플레이어 수count를 계산
    최종적으로 실패율이 높은 스테이지부터 내림차순으로 정렬 수행
    전체 스테이지 수가 200,000 이하이므로 기본정렬 라이브러리 사용
    """
    
    result = []
    length = len(stages)
    
    for i in range(1, N+1):
        # 현재 스테이지에 머무른 사람 수 계산
        count = stages.count(i)

        if length == 0:
            fail = 0
        else:
            fail = count / length

        result.append((i,fail))

        # 다음 스테이지에 도달한 사람 수
        length -= count

    result = sorted(result, key=lambda x: x[1], reverse=True)
    result = [i[0] for i in result]
    return result
    
#output
print(solution(n1,st1))    #3,4,2,1,5
print(solution(n2,st2))    #4,1,2,3

"""
[느낀점]
+ count 함수를 사용하면 해당 스테이지에 머무른 사람 수를 쉽게 계산할 수 있음
-> stages.count(i) : stages에서 i의 개수를 반환
"""