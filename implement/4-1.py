"""
[ch4.구현] 4-1: 상하좌우 | 난이도1 | 예제
INPUT: 공간크기n, 이동할 계획서 내용
    * 공간 크기 n (1<=n<=100)
    * 공백으로 구분된 이동 계획서 내용 (1<=이동횟수>=100)
OUTPUT: 여행가가 최종적으로 도착할 지점의 좌표를 공백으로 구분
"""
import time

#input
n = int(input())
move = input()

"""
[풀이 구상]
입력받은 계획서 내용을 저장한 move 문자열을 1회 돌면서 이동 작업을 수행
-> 문자열 크기 len(move)만큼 for문을 반복하게 되므로 시간복잡도는 O(n)이 될 것
반복 1회마다 이동, 범위를 벗어나는 경우 처리 작업이 필요
"""
#solve
start = time.time()

x, y = 1, 1    # 출발 위치: (1,1)

# 이동방향 설정
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']


for m in move:
    for i in range(len(move_types)):
        if m == move_types[i]:
            tx = x + dx[i]
            ty = y + dy[i]

    # 벗어나는 경우 처리
    if tx<1 or ty<1 or tx>n or ty>n:
        continue
    # 벗어나지 않는 경우
    x, y = tx, ty

# ---------------------------------------------------
# 4-3을 참고하여 dx,dy를 dloc이라는 한 개의 리스트로 합쳐봄
dloc = [(0,-1),(0,1),(-1,0),(1,0)]
for m in move:
    for i in range(len(move_types)):
        if m==move_types[i]:
            d = dloc[i]
            tx = x + d[0]
            ty = y + d[1]

    # 벗어나는 경우 처리
    if tx<1 or ty<1 or tx>n or ty>n:
        continue
    # 벗어나지 않는 경우
    x, y = tx, ty

#output
print(x,y)

#time check
end = time.time()
print(f"{end-start:.5f} sec")

"""
[느낀점]
반복문 내에 if문을 써서 따로 따로 LRUD를 구분하는 것이 아니라
위의 방식처럼 dx,dy,type을 리스트로 만들어 구성하면
더 깔끔하게 코드를 짤 수 있었음!!!
+ 문제에서 주어진 X,Y 좌표값이 방향에 따라 어떻게 변하는지
헷갈리지 말 것!!

+ 책 설명 추가
일련의 명령에 따라 개체를 차례대로 이동시킨다는 점에서
시뮬레이션Simulation유형이라고 불리기도
"""