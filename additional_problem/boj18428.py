"""
[BOJ] 18428: 감시 피하기
INPUT:
* 첫째 줄에 자연수 n (3<=n<=6)
* n개의 줄에 복도의 정보
    * 학생이 있으면s, 선생이 있으면t, 아무것도 없으면x

OUTPUT: 정확히 3개의 장애물을 설치하여
모든 학생이 감시를 피할 수 있으면 "YES", 아니면 "NO" 출력
"""
import sys

#input
inputdata = sys.stdin.readline

n = int(inputdata())

data = []
teachers = []

for i in range(n):
    data.append(list(inputdata().split()))
    for j in range(n):
        if data[i][j] == 'T':
            teachers.append((i, j))

#solve
result = False  # 감시 피하기 실패로 초기화


#각 선생님이 감시를 수행하는 함수
#학생 발견 시 True를 반환
def dircheck(x, y, dir):

    if dir==0:  #왼쪽
        while y>=0:
            if data[x][y] == 'S':
                return True
            if data[x][y] == 'O':
                return False
            y -= 1

    if dir==1:  #오른쪽
        while y < n:
            if data[x][y] == 'S':
                return True
            if data[x][y] == 'O':
                return False
            y += 1

    if dir==2:  #위쪽
        while x >= 0:
            if data[x][y] == 'S':
                return True
            if data[x][y] == 'O':
                return False
            x -= 1

    if dir==3:  #아래쪽
        while x < n:
            if data[x][y] == 'S':
                return True
            if data[x][y] == 'O':
                return False
            x += 1

    return False


def put_wall(cnt):
    global result

    # 장애물을 3개를 설치완료
    if cnt==3:
        for x, y in teachers:       #각 선생님에 대해 확인
            for dir in range(4):    #각 방향(상,하, 좌, 우)에 대해 확인
                if dircheck(x, y, dir)==True:   #학생 발견
                    return                    
                else:                           #학생 미발견
                    continue
       
        result = True   #감시 피하기 성공으로 갱신
        return


    #장애물 개수가 3개보다 적을 경우
    for i in range(n):
        for j in range(n):

            #빈칸인 경우
            if data[i][j]=='X':   

                #장애물 설치
                data[i][j] = 'O'
                cnt += 1

                put_wall(cnt)
                    
                #장애물 삭제
                data[i][j] = 'X'
                cnt -= 1


#output
put_wall(0)

if result == True:
    print("YES")
else:
    print("NO")
