"""
[ch11.greedy] 11-3: 문자열 뒤집기 | 난이도 1 | 핵심유형
INPUT:
    * 첫째 줄 문자열 s (0과 1로 구성/100만 이하)
OUTPUT: 문자열을 전부 같게 만들때 해야하는 행동의 최소 횟수
"""
import time

#input
s = input()

"""
문자열s = 0 또는 1이 연속된 문자열들의 연결
작업: 0 또는 1이 연속된 문자열 하나를 고른 후 변환
* 0이 연속된 경우: 0->1
* 1이 연속된 경우: 1->0

feasible solution: 문자열s가 한 가지 숫자로만 구성되어야 함
optimal solution: 변환 횟수가 최소

1회 작업마다, 0이 연속된 문자열 / 1이 연속된 문자열 중 적은 경우를 변환
* 0이 연속된 문자열 개수: num[0]
* 1이 연속된 문자열 개수: num[1]

"""
start = time.time()
#solve
result = 0
num = [0,0]

# 연속된 문자열 개수를 num에 저장
num[int(s[0])]=1    #첫번째숫자
for i in range(len(s)-1):   #두번째부터 끝까지
    if s[i]!=s[i+1]:
        num[int(s[i+1])]+=1

#print(num[0], num[1])
result = min(num[0],num[1])

#output
print(result)

#time check
end = time.time()
print(f"{end-start:.5f} sec")

"""
느낀점?

변환 횟수만 구하면 되니까
진짜로 문자열을 수정 할 필요는 없었음(...)
"""