"""
[ch14.sorting] 14-23: 국영수 | 난이도1 | 핵심 유형
문제 링크 : https://www.acmicpc.net/problem/10825
INPUT: 학생 n명의 이름, 국어/영어/수학 점수
OUTPUT: 주어진 정렬 기준으로 정렬 후 각 학생의 이름을 한 줄 씩 출력
"""

#input
"""
n = int(input())
data = []
for _ in range(n):
    name, a, b, c = input().split()
    data.append((name, int(a), int(b), int(c)))
"""
n = 12
data = [
    ('Junkyu', 50, 60, 100),
    ('Sangkeun', 80, 60, 50),
    ('Sunyoung', 80, 70, 100),
    ('Soong', 50, 60, 90),
    ('Haebin', 50, 60, 100),
    ('Kangsoo', 60, 80, 100),
    ('Donghyuk', 80, 60, 100),
    ('Sei', 70, 70, 70),
    ('Wonseob', 70, 70, 90),
    ('Sanghyun', 70, 70, 80),
    ('nsj', 80, 80, 80),
    ('Taewhan', 50, 60, 90)
]

"""
[풀이 구상]
1. 국어 내림차순
2. 국어가 같으면, 영어 오름차순
3. 국어 같음 & 영어 같으면, 수학 내림차순
4. 모두 같으면, 이름이 사전 순으로 증가하는 순서(아스키코드에서 대문자는 소문자보다 앞임)

+ 책 설명)
파이썬에서 '튜플'을 원소로 하는 리스트를 정렬하면 기본적으로 각 튜플을 구성하는 원소의 순서에 맞게 정렬됨
리스트의 원소를 정렬할 때 sort()함수의 key속성에 값을 대입하여 내가 원하는 조건에 맞게 튜플을 정렬시킬 수 있음
"""
#solve
data.sort(key= lambda x: (-x[1], x[2], -x[3], x[0]) )

#output
for i in range(n):
    print(data[i][0])