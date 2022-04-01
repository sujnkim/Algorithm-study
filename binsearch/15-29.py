"""
[ch15.이진탐색] 15-29: 공유기 설치 | 난이도2 | 핵심유형
문제링크 : https://www.acmicpc.net/problem/2110
INPUT: 집의 개수n, 공유기 개수c, 집의 좌표
    * 첫째 줄에 공백으로 구분된 n(2<=n<=200,000), c(2<=c<=n)
    * 둘째 줄부터 n개의 줄에 집의 좌표 xi(1<=xi<=1,000,000,000)
    * 집은 서로 다른 좌표를 가짐
OUTPUT: 첫째 줄에 가장 인접한 두 공유기 사이의 최대 거리
"""
import sys

#input
"""
n, c = map(int, input().split())
data = []
for _ in range(n):
    data.append(int(input()))
"""
# input()함수로 좌표 데이터를 입력받을 경우, 시간초과 오류 발생
n, c = map(int, input().split())
array = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

"""
[풀이 구상]
집의 개수 n은 최대 200,000
집의 좌표는 최대 1,000,000,000
-> 값이 최대 10억이므로 이진탐색을 고려
-> 시간복잡도가 logN인 방법을 생각

x = 가장 인접한 공유기 사이의 거리
이 x를 최대로 만들어야 하는 문제
따라서 공유기 사이의 거리가 최대가 될 때를 이진 탐색으로 찾아야 함
-> 거리mid를 설정하여 c개 이상의 공유기를 설치할 수 있는지 확인
-> 할 수 없다면, mid값을 감소
-> 할 수 있다면, 저장 후 mid값을 증가

최적화 문제를 결정 문제로 바꾸어 해결하는 파라메트릭 문제
-> ch07. 떡볶이 떡 문제 참고
"""

#solve
array.sort()        #탐색을 위해 정렬 수행
    
start = 1                    #가능한 최소 거리min gap
end = array[n-1] - array[0]     #가능한 최대 거리max gap
result = 0

while(start <= end):
    mid = (start+end)//2    #가능한 지 확인할 gap크기
    value = array[0]        # 공유기 개수를 계산할 때 쓰기 위한 변수
    count = 1               # 설치한 공유기 개수

    # gap을 mid로 설정했을 때 설치할 수 있는 공유기 개수
    for i in range(1, n):
        if array[i] >= value + mid:
            value = array[i]
            count += 1

    # gap 크기가 mid일 때 공유기 개수 조건을 만족시키는 지 확인
    if count >= c:
        start = mid + 1    #gap크기 증가
        result = mid
    else:
        end = mid - 1     #gap 크기 감소
    

#output
print(result)

