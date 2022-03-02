"""
[ch12.구현] 12-8: 문자열 재정렬 | 난이도1 | Facebook인터뷰
INPUT: 하나의 문자열 s
    * 첫째 줄에 알파벳 대문자와 숫자(0~9)로 이루어진 문자열 s (1<=len(s)<=10,000)
OUTPUT: 문제에서 요구하는 정답 출력
"""
import time

#input
data = input()

"""
[풀이 구상]
모든 알파벳 오름차순 정렬 -> 이어서 출력
+ 모든 숫자를 더한 값 -> 이어서 출력

입력받은 문자열 s를 한바퀴 돌면서 한 문자씩 확인
for d in data:
    if 문자 -> 결과에 추가: append
    else -> sum에 더하기

반복문이 끝나면 문자열을 오름차순으로 정렬: sort?
정렬한 결과에 sum을 추가한 후 출력: append

append, sort를 쓰려면 result를 리스트로 선언해야 할 것 같다
"""

#solve
start = time.time()

result = []    # 결과를 저장할 리스트
sum = 0        # 숫자 더하기 저장 변수

for d in data:
    # 문자라면 리스트에 append, 문자가 아니라면 int로 변환 후 sum에 덧셈
    if d.isalpha()==True:
        result.append(d)
    else:
        sum += int(d)

result.sort()            # 결과 리스트의 문자를 오름차순 정렬

if sum != 0:
    result.append(str(sum))    # 계산한 숫자를 리스트에 추가

result = ''.join(result)    # 리스트를 문자열로 변환


#output
print(result)

#timecheck
end = time.time()
print(f"{end-start:.5f} sec")

"""
[느낀점]
+ 문자열 확인 함수 isalpha() 및 관련 함수들을 한 번 정리해야 할 것 같다.
-> 문자열 전체가 문자로만 구성되어 있어야 True를 반환함
-> 숫자나 공백이 있을 경우 False !!
-> 이 문제의 경우에는 문자 하나씩 가져왔기 때문에 상관없었으나...

+ 리스트를 문자열로 변환하려고 했는데 어떻게 하는 지 몰라서 검색해보았다
-> 함수 .join(list)를 사용하면 된다고 함

+ 예시 답안의 경우, 숫자의 합이 0이 아닌 경우에만 이어서 출력을 하였다...
-> 문제에서 0인 경우에는 따로 처리하라는 말이 없어서 생각하지도 못한 부분이었다.
-> 언급이 없으니까 0일 때 출력해도 상관없지 않을까 ?
"""