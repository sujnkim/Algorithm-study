"""
[ch13.DFSBFS] 13-20: 감시 피하기 | 난이도2.5 | 핵심 유형
문제링크 : https://www.acmicpc.net/problem/18428
INPUT: 복도 크기 n, 복도의 정보
    * 첫째 줄에 복도의 크기 자연수 n (3<=n<=6)
    * 둘째 줄 이후 n개의 줄에 걸쳐 복도의 정보
    * 학생s, 선생t, 빈칸x(3개 이상)
OUTPUT: 모든 학생이 감시를 피할 수 있는지 여부 (YES 혹은 NO)
"""

#input
n = int(input())
data=[]
teacher = []
for i in range(n):
    data.append(list(input().split()))
    for j in range(n):
        if data[i][j] == 'T':
            teacher.append((i,j))



"""
[풀이 구상]
빈 칸에 장애물 3개를 설치하는 경우마다 발견여부 체크 필요
복도 크기는 최대 6이므로, 장애물을 설치하는 모든 경우의 수는 36c3
+) 책 답안 설명 추가
10,000이하의 수이므로 완전 탐색으로 모든 조합을 고려하여도 시간 초과없이 문제 해결 가능

장애물을 설치하는 방법 구현... 3-16 연구소 문제처럼 재귀dfs 사용? 조합라이브러리?
-> 13-16.연구소 문제를 복습할 겸 dfs(재귀)로 한 번 풀어보자
-> 이중for를 이용해 data를 돌면서 빈 칸에 벽을 설치->확인->제거 과정을 거침
-> count==3일 때 확인과정을 거친다

발견 여부체크는 함수로 따로 구현: dircheck
    * 학생을 만날 경우 true 반환
    * 장애물을 만나거나 빈칸만 있는 경우 false 반환

선생님 리스트를 돌면서 각 선생님마다 4방향 확인
    * 현재 방향에서 학생을 만날 경우 -> return
    * 현재 방향에서 문제 없을 경우 -> continue(다음 방향 확인)
모든 선생님이 학생을 만나지 못할 경우 result = True
"""

result = False

def dircheck(x, y, dir):
    # 왼쪽
    if dir == 0:
        while y >= 0:
            if data[x][y] == 'S':
                return True
            if data[x][y] == 'O':
                return False
            y -= 1

    # 오른쪽
    if dir == 1:
        while y < n:
            if data[x][y] == 'S':
                return True
            if data[x][y] == 'O':
                return False
            y += 1

    # 위쪽
    if dir == 2:
        while x >= 0:
            if data[x][y] == 'S':
                return True
            if data[x][y] == 'O':
                return False
            x -= 1

    # 아래쪽
    if dir == 3:
        while x < n:
            if data[x][y] == 'S':
                return True
            if data[x][y] == 'O':
                return False
            x += 1

    return False
        
    
def dfs(count):
    global result

    # 장애물이 3개 일 때
    if count == 3:
        for x, y in teacher:
            for dir in range(4):
                # 학생을 발견하면 바로 return
                if dircheck(x, y, dir) == True:
                    return
                else:
                    continue

        #모든 선생님이 학생을 못 찾을 때
        result = True
        return
        
    # 장애물 설치
    for i in range(n):
        for j in range(n):
            if data[i][j] == 'X':
                
                data[i][j] = 'O'
                count += 1

                dfs(count)
                if result == True:
                   return

                data[i][j] = 'X'
                count -= 1


#output
dfs(0)
if result == True:
    print('YES')
else:
    print('NO')


"""
[느낀점]
+ 조합 문제를 dfs 방식으로도 풀 수 있다는 것을 잊지 말기
-> 13-16번 참고

+ dircheck함수에서 dir이라는 인자를 사용해 방향을 구분할 수 있었음
-> 처음에 x,y만으로 짜려니까 복잡해졌는데... 이런 방법이 있었다
"""