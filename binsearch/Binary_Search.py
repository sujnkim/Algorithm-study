"""
이진탐색Binary Search:
배열 내부의 데이터가 정렬되어 있어야만 사용할 수 있는 탐색 알고리즘
    -> 이미 정렬되어 있다면 매우 빠르게 데이터를 찾을 수 있음
탐색 범위를 절반씩 좁혀나가며 데이터를 탐색
    -> 찾으려는 데이터와 중간점Middle 데이터를 반복적으로 비교
    -> 중간점이 실수일 때는 소수점 이하를 버림
    -> 시간복잡도: O(NlogN)
    -> 한 단계마다 원소가 평균적으로 절반으로 감소
구현 방법: 재귀함수 or 반복문
탐색 범위가 큰 상황에서 이진탐색으로 접근해보기
    -> 100,000만 단위 이상으로 넘어가면
        O(NlogN)의 속도를 내는 알고리즘을 떠올려야 함
"""

#이진 탐색 소스코드 구현(재귀함수)
def binary_search(array, target, start, end):
    if start > end:
        return None

    mid = (start+end)//2

    # 찾은 경우: 중간점 인덱스 반환
    if array[mid] == target:
        return mid

    # 타겟 < 중간점 : 왼쪽 확인
    if target < array[mid]:
        return binary_search(array, target, start, mid-1)
    # 중간점 < 타겟 : 오른쪽 확인
    else:
        return binary_search(array, target, mid+1, end)

#이진 탐색 소스코드 구현(반복문)
def binary_search2(array, target, start, end):
    while start <= end:
        mid = (start+end)//2

        if array[mid] == target:
            return mid
        elif target < array[mid]:
            end = mid-1
        else:
            start = mid+1
    return None


n, target = 10, 7
data = [1,3,5,7,9,11,13,15,17,19]

#test 1
result = binary_search(data, target, 0, n-1)
if result == None:
    print('원소가 존재하지 않음')
else:
    print(result+1)

#test 2
result = binary_search2(data, target, 0, n-1)
if result == None:
    print('원소가 존재하지 않음')
else:
    print(result+1)