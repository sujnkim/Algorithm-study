"""
[ch06.sorting] 6-10: 위에서 아래로 | 난이도1 | T기업코딩테스트
INPUT: 수의 개수n (1<=n<=500), n개의 수(1이상 100,000이하의 자연수)
OUTPUT: 입력으로 주어진 수열이 내림차순으로 정렬된 결과를 공백으로 구분하여 출력
"""

#input
n = int(input())
numbers = []
for _ in range(n):
    numbers.append(int(input()))


#solve
numbers = sorted(numbers, reverse = True)

#output
for i in range(n):
    print(numbers[i], end=' ')

"""
[문제 설명 추가]
+ 기본적인 정렬을 할 수 있는 지 묻는 문제
-> 수의 개수가 500이하, 모든 수는 1이상 100000이하이므로 어떤 정렬 알고리즘이든 상관 없음
"""