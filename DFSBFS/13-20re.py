"""
[책 예시 답안]
+ combinations 라이브러리를 이용한 방식
"""

from itertools import combinations

#input
n = int(input())
board = []
teacher = []
empty = []            #조합을 사용하기 위해 필요
for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        if board[i][j] == 'T':
            teacher.append((i,j))
        if board[i][j] == 'X':
            empty.append((i,j))


# solve
def watch(x, y, dir):
    # (x,y)를 기준으로 특정한 방향dir을 탐색
    # 학생을 찾음: True
    # 학생을 못 찾음(장애물): False
    
    # 왼쪽
    if dir == 0:
        while y >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y -= 1

    # 오른쪽
    if dir == 1:
        while y < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y += 1

    # 위쪽
    if dir == 2:
        while x >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x -= 1

    # 아래쪽
    if dir == 3:
        while x < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x += 1

    return False

    
def process():
    # 모든 선생님이 학생을 감시하는 작업 실행
    # 학생을 찾음: True
    # 학생을 못 찾음: False
    
    # 각 선생님마다 4방향을 확인
    for x, y in teacher:
        for i in range(4):
            if watch(x, y, i):
                return True
    return False


#-----------------------------------

# find 여부 초기화
find = False    

# 3개 뽑는 조합마다 확인
for combi in combinations(empty, 3):

    # 장애물 설치
    for x, y in combi:
        board[x][y] = 'O'

    # 확인
    if not process():
        # process(학생을 찾음)가 False일 경우
        # 모든 학생이 감시를 피하는 경우
        find = True
        break

    # 장애물 제거
    for x, y in combi:
        board[x][y] = 'X'


#output
if find == True:
    print('YES')
else:
    print('NO')


"""
[느낀점]
+ 조합라이브러리에 더 익숙해지도록 하자
-> 조합으로 뽑을 것들을 리스트에 저장
-> for combi in combinations(list, n):
-> list 내에서 n개를 뽑는 조합들을 전부 확인 가능

+ 설치(조작) -> 확인 -> 제거(조작)

+ (x,y)를 기준으로 네 방향을 확인하는 방법
-> 함수에 dir이라는 인자를 설정하여 함수 내에서 if문으로 구분
-> 나는 process랑 watch를 한꺼번에 합쳐서 함수를 짜려고 했는데, 
길이가 길어지니 헷갈려서 시간이 오래 걸렸음
-> 더 좋은 방법이 있을까 고민해봤는데... 이 방식이 직관적이라 쉬운 것 같다
"""