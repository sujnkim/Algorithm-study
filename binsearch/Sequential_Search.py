"""
순차 탐색Sequential Search:
리스트 안에 있는 특정 데이터를 찾기 위해 데이터를 하나씩 차례대로 확인하는 방법. 보통 정렬되어 있지 않은 리스트에서 데이터를 찾아야 할 때 사용
count()메서드를 이용할 때도 내부에서는 순차 탐색이 수행됨
"""

#순차 탐색 소스코드 구현
def sequential_search(n, target, array):
    #각 원소를 하나 씩 확인하며
    for i in range(n):
        #현재 찾고자 하는 원소와 동일한 경우
        if array[i] == target:
            # 현재 위치 반환
            # 인덱스는 0부터 시작하므로 1 더하기
            return i+1


n=5
data = ['Hanul', 'Jonggu', 'Dongbin', 'Taeil', 'Sangwook']
target = 'Dongbin'

print(sequential_search(n,target,data))