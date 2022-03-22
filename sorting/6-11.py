"""
[ch06.sorting] 6-11: 성적이 낮은 순서로 학생 출력하기 | 난이도1 | D기업프로그래밍콘테스트예선
INPUT: 학생 수n, n명의 학생(이름,성적) 데이터
    * 첫째 줄 n ( 1<=n<=100,000)
    * 둘째 줄 이후 n개의 줄에 공백으로 구분된 학생이름 문자열과 학생의 성적
OUTPUT: 모든 학생의 이름을 성적이 낮은 순서대로 출력. 성적이 동일할 경우 순서 자유
"""

#input
"""
n = int(input())
data = []
for _ in range(n):
    name, score = input().split()
    data.append((name, int(score)))
"""
n = 3
data = [ ('홍길동',95), ('이순신',77), ('아무개',50) ]

# solve
# lambda 매개변수:결과
data = sorted(data, key = lambda student:student[1])
#output
for d in data:
    print(d[0], d[1], end=' ')
print('')

# key에 -부호를 붙이면 역순으로 정렬
data = sorted(data, key = lambda student:-student[1])
#output
for d in data:
    print(d[0], d[1], end=' ')

"""
+ 학생의 정보가 100,000개까지 입력될 수 있음
-> 최악의 경우 O(NlogN)을 보장하는 알고리즘이나 O(N)을 보장하는 계수 정렬 사용
-> 파이썬 기본정렬 라이브러리

+ sort, sorted 함수의 key로 람다함수를 잘 사용한다
-> 람다함수 쓰는 방법을 알아두자
"""