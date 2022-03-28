"""
[ch7.binsearch] 떡볶이 떡 만들기 | 난이도2 | 실전문제
INPUT: 떡 개수n, 요청 떡 길이m, 떡의 개별높이
    * 첫째 줄에 공백으로 구분된 n,m
    * (1<=n<=1,000,000, 1<=m<=2,000,000,000)
    * 둘째 줄에 공백으로 구분된 떡의 개별 높이
    * 떡 높이의 총합은 항상 m이상
    * 각 높이는 10억보다 작거나 같은 양의 정수 또는 0
OUTPUT: 적어도 m만큼 떡을 가져가기 위해 설정할 수 있는 높이의 최대값
"""

#input
n, m = map(int, input().split())
data = list(map(int, input().split()))

"""
파라메트릭 서치Parametric Search:
최적화 문제를 결정 문제(yes/no)로 바꾸어 해결하는 기법
-> 원하는 조건을 만족하는 가장 알맞은 값을 찾는 문제에서 주로 사용

적절한 높이를 찾을 때까지 절단기 높이h를 반복해서 조정하는 방식
조건 만족 여부에 따라 탐색 범위를 좁혀서 해결
-> 절단기 높이h 범위는 1부터 10억까지의 정수(매우 큰 수)
    -> 순차 탐색은 시간 초과가 날 것
    -> 이진 탐색으로 찾는 다면 대략 31번만에 모두 고려 가능
-> 떡의 개수n이 최대 1000만 개이므로 1000만*31 = 최대 3,000만 정도
-> 시간 제한이 2초이므로 3000만 번 연산은 아슬하게 시간초과 나지 않을 것

"""
#solve
start = 0
end = max(data)

result = 0
while start < end:
    slice = 0
    mid = (start+end)//2

    for d in data:
        if d > mid:
            slice += (d-mid)

    if slice < m:
        end = mid - 1
    else:
        # 중간값mid는 시간이 지날수록 최적화된 값을 찾음
        # 떡 길이 합이 필요한 떡 길이보다 크거나 같을 때 갱신
        result = mid
        start = mid + 1

#output
print(result)