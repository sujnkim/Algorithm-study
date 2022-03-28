"""
[ch07.binsearch] 부품찾기 | 난이도1.5 | 실전문제
INPUT: 가게부품n, 가게부품 번호, 요청부품m, 요청부품 번호
    * 첫째 줄 n ( 1<=n<=1,000000)
    * 둘째 줄 공백으로 구분된 n개의 정수 (1이상 1,00,000이하)
    * 셋째 줄 m (1<=m<=100,000)
    * 넷째 줄 공백으로 구분된 m개의 정수 (1이상 1,000,000이하)
OUTPUT: 공백으로 구분하여 각 부품 존재여부 출력
    * 있으면 yes, 없으면 no
"""

# 이진탐색 소스코드(반복문)
def bin_search(array, target, start, end):
    while start <= end:
        mid = (start+end)//2

        if array[mid]==target:
            return mid
        elif target < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return None

    
#input
n = int(input())
data = list(map(int, input().split()))

m = int(input())
want = list(map(int, input().split()))


#solve
data.sort()    # 이진탐색을 하려면 데이터가 정렬되어 있어야 함

for w in want:
    if bin_search(data,w,0,n-1) != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')
