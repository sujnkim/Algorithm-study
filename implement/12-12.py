"""
[ch12.구현] 12-12: 기둥과 보 설치 | 난이도1.5 | 2020카카오신입공채
문제링크 : https://programmers.co.kr/learn/courses/30/lessons/60061
INPUT:
    * 벽면의 크기n (5<=n<=100)
    * 작업명령(설치,삭제)이 담긴 2차원 배열 build_frame (1<=행길이<=1,000)(열길이=4) : [x,y,a,b]형태
    * x,y : 교차점의 좌표, a: 작업 구조물 종류(0:기둥, 1:보), b: 작업내용(0:삭제, 1:설치)
OUTPUT: 모든 명령을 수행한 후의 구조물 상태를 return
    * [x,y,a] 형식, x-y-a기준으로 오름차순 정렬
"""

"""
[풀이 구상]
처음에 생각했을 때에는 조건을 전부 따져서 가능할 때에만 작업을 수행하는 방식으로 구현하려고 했음
그러나 삭제작업 구현이 너무 복잡해져서... 이게 맞나 고민하던 도중 12-10.자물쇠와 열쇠문제에서 깨달음을 얻음
넣거나 빼기 전에 확인을 거치고 작업을 수행하는 방식은 if문이 너무 복잡해지니까
그렇다면 이 문제... 일단 삽입/삭제를 한 뒤에 되는지 확인을 하면 어떨까.?
일단 작업 수행(삽입/삭제) -> 가능여부확인 -> 되면 넘어가고 안되면 원상복귀(삭제,삽입)
이런 방식으로 풀어보기로 함
"""
def isokay(answer):
    
    for x, y, struct in answer:
        
        if struct == 0:    #기둥
            # 바닥 or 다른 기둥 위 or 한쪽 보 위(2방향)
            if y==0 or [x,y-1,0] in answer or [x,y,1] in answer or [x-1,y,1] in answer:
                continue
            else:
                return False

        if struct == 1:    #보
            #한쪽 끝이 기둥 위(2가지) or 양쪽이 다른 보와 연결(양쪽비교)
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer):
                continue
            else:
                return False

    # 전부 확인되는 경우
    return True
    

def solution(n, build_frame):
    answer = []

    # 작업(work)의 최대 개수는 1000개
    for work in build_frame:
        x, y, struct, do = work

        if do == 1:
            # 일단 설치
            answer.append([x,y,struct])
            if isokay(answer) == False:
                answer.remove([x,y,struct])    #불가능->다시 삭제
            
        if do == 0:
            # 일단 삭제
            answer.remove([x,y,struct])
            if isokay(answer) == False:
                answer.append([x,y,struct])    #불가능->다시 추가

    # 오름차순 정렬
    #return sorted(answer)
    answer.sort()
    
    return answer


ex1 = [
    [1,0,0,1],
    [1,1,1,1],
    [2,1,0,1],
    [2,2,1,1],
    [5,0,0,1],
    [5,1,0,1],
    [4,2,1,1],
    [3,2,1,1]
]

ex2 = [
    [0,0,0,1],
    [2,0,0,1],
    [4,0,0,1],
    [0,1,1,1],
    [1,1,1,1],
    [2,1,1,1],
    [3,1,1,1],
    [2,0,0,0],
    [1,1,1,0],
    [2,2,0,1],
]

print(solution(5,ex1))
print(solution(5,ex2))


"""
[느낀점]
+전체 명령 개수(M)은 1000개 이하이고 시간 제한은 5초이므로 O(M^3)의 알고리즘을 이용해도 정답판정이 된다고...
-> 아... 이거 전혀 신경쓰지 않고 풀었는데, 문제 풀기 전에 입력데이터 크기와 시간을 항상 확인하도록 하자.

+ O(M^3)의 시간복잡도로 문제를 해결하는 가장 간단한 방법 : 설치/삭제 연산을 수행할 때마다 '전체 구조물'을 확인하는 방식.
예시 답안에서는 일단 설치/삭제를 한 뒤 -> possible()함수로 전체구조물 가능 여부 체크 -> 안되면 다시 삭제/설치
-> 이 풀이 방식... 12-10. 자물쇠와 열쇠 문제에서도 본 것이 맞음!! 혹시 시뮬레이션 문제에서 자주 쓰는 방식인 걸까?

+ x,y,a,b에 값을 넣을 때 하나씩 인덱스로 접근했었는데, 그냥 x,y,a,b = work라고 하면 한 번에 넣어진다 !!
-> 뒤의 방식이 더 쉽고 간결해서 가독성 높아 좋은 것 같다

+ for 문을 쓸때 for x,y,struct in answer 이라고 작성하면, answer에서 가져오는 한 요소의 값들이 x,y,struct에 알아서 들어감
-> 나는 이걸 일단 가져와서 인덱스 접근으로 변수마다 따로 값을 넣었는데 그럴 필요가 없었다...()

+ if문을 쓸때에도 answer의 각 요소를 비교하는 것이 아니라 [x,y,a] in answer 이런 방식으로 한 번에 비교 가능...
-> 이런 방식이 ... ? 있었군요 .. ?

+ list.append([x,y,a]) / list.remove([x,y,a]) : 해당 자료를 리스트에서 바로 추가/삭제 가능
-> append는 자주 사용해서 금방 생각나지만, remove는 생각나지 않아서 찾아봄 ㅎㅎ... 기본 문법 공부를 착실히 합시다;;

+ sort/sorted 함수의 차이는 ?
-> sort : 기존의 리스트를 정렬
-> sorted : 리스트를 정렬 후 새로운 리스트를 반환
"""