"""
[ch15.이진탐색] 15-28: 고정점 찾기 | 난이도1.5 | Amazon인터뷰
INPUT: 원소개수n, n개의 원소 데이터
    * 첫째 줄에 n (1<=n<=1,000,000)
    * 둘째 줄에 공백으로 구분된 n개의 정수
OUTPUT: 고정점을 출력, 없다면 -1 출력
"""

"""
[풀이 구상]
고정점: 수열의 원소 중에서 그 값이 인덱스와 동일한 원소
주어진 수열은 n개의 서로 다른 원소가 오름차순으로 정렬됨
시간 복잡도 O(logN) 으로 알고리즘을 설계해야 함
-> 이진탐색

1) mid == array[mid] : return mid
2) mid > array[mid] : mid 오른쪽 탐색
3) mid < array[mid] : mid 왼쪽 탐색
"""

#solve
def bin_search(array, start, end):
    while start <= end:
        mid = (start+end)//2

        if array[mid] == mid:
            return mid
        elif array[mid] < mid:
            start = mid + 1
        else:
            end = mid - 1
    
    return -1 


#input
n = int(input())
data = list(map(int, input().split()))

#output
result = bin_search(data, 0, n-1)
print(result)
