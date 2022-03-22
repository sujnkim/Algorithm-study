"""
[ch06.sorting] 6-12: 두 배열의 원소 교체 | 난이도1 | 국제알고리즘대회
INPUT: n, k, 배열 a, b의 정보
    * 첫째 줄에 공백으로 구분된 n, k (1<=n<=100000,0<=k<=n)
    * 둘째 줄에 공백으로 구분된 배열 a의 정보
    * 셋째 줄에 공백으로 구분된 배열 b의 정보
    * 모든 원소는 10,000,000보다 작은 자연수
OUTPUT: 최대 k번 바뀌치기 연산을 수행하여 만들 수 있는 배열 a의 모든 원소의 합의 최대값
    * 바뀌치기 연산: 배열 a와 b의 원소를 하나씩 골라 교환
"""

#input
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

"""
[풀이 구상]
a의 작은 값을 b의 큰 값과 바꾸기 위해 a는 오름차순 정렬, b는 내림차순 정렬
비교해가며 a값이 b값보다 작을 경우 교환(총 k개까지 바꿀 수 있음)

두 배열의 원소가 100,000개까지 이므로 O(NlogN)을 보장하는 정렬 알고리즘을 써야 함
"""

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i]<b[i]:
        a[i],b[i] = b[i],a[i]
    else:
        break

print(sum(a))