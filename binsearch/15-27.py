"""
[ch15.이진탐색] 정렬된 배열에서 특정 수의 개수 구하기 | 난이도2 | Zoho인터뷰
INPUT: n개의 원소를 포함하고 있는 오름차순으로 정렬된 수열, 찾을 수x
    * 첫째 줄에 공백으로 구분된 n, x (1<=n<=1000000)
    * 공백으로 구분된 n개의 원소
OUTPUT: 수열의 원소 중에서 값이 x인 원소의 개수 출력
    * x인 원소가 하나도 없다면 -1 출력
"""
from bisect import bisect_left, bisect_right

#input 
n, x = map(int, input().split())
data = list(map(int, input().split()))

"""
[풀이 구상]
시간 복잡도 O(logN)으로 알고리즘을 설계해야 함
주어지는 데이터 개수가 최대 1,000,000개
    -> 처음부터 하나씩 확인하는 순차탐색 방법은 불가능
오름차순으로 정렬되어 있으므로 이진탐색 방법을 이용하자

원소들이 오름차순으로 정렬되어 있으므로 여러개 있을 경우 모여있을 것
target이 처음 등장하는 인덱스와 마지막으로 등장하는 인덱스의 차이를 계산
"""

def count_target(array, target):
    left_idx =  bisect_left(array, target)
    right_idx = bisect_right(array, target)
    return right_idx - left_idx


#output
result = count_target(data, x)
if result == 0:
    print(-1)
else:
    print(result)