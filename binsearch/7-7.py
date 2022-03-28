"""
7-5.py 부품 찾기 문제를 집합 자료형을 이용해 풀기
    -> 특정한 수가 한 번이라도 등장했는지 검사하면 됨
    -> set()함수는 집합 자료형을 초기화할 때 사용
"""

#input
n = int(input())

# 가게에 있는 전체 부품 번호를 입력받아 집합 자료형에 기록
data = set(map(int, input().split()))

m = int(input())
want = list(map(int, input().split()))

for w in want:
    if w in data:
        print('yes', end=' ')
    else:
        print('no', end=' ')