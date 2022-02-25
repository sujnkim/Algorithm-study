"""
[ch11.greedy] 11-2: 곱하기 혹은 더하기 | 난이도 1 | Facebook 인터뷰
INPUT: 여러 개의 숫자로 구성된 문자열 s
    * 첫째 줄 문자열 s (1<=s의 길이<=20)
OUTPUT: 만들 수 있는 가장 큰 수
"""
import time

#input
s = input()

"""
[풀이 구상]
solution: 숫자 사이에 + or x를 넣어 만들 수 있는 가장 큰 수

-> 덧셈보다 곱셈을 많이 쓸 수록 큰 수를 만들 수 있음. 최대한 곱셈을 많이 쓰기
단, 계산하는 수에 0이 포함될 때 곱셈을 하면 0이 되므로 이를 잘 처리할 필요가 있음
계산하는 수에 1이 포함될 때 곱셈을 하는 것보다 덧셈을 해야 값이 더 커짐

* 계산하는 두 수 중 0이나 1이 포함되면 +
* 포함되지 않으면 x
"""
#solve
start = time.time()

result = 0
idx = 0

# 첫 번째 숫자
result = int(s[0])
for i in range(1,len(s)):
    if result<=1:
        result = result + int(s[i])
    else:
        idx = i
        break
        
# 두 번째 숫자부터 계산
for i in range(idx, len(s)):
    if s[i]=='0' or s[i]=='1':  #0 또는 1인 경우, 곱셈
        result += int(s[i])
    else:                        #0 이나 1이 아닌 경우, 덧셈
        result *= int(s[i])

#output
print(result)

#time check
end = time.time()
print(f"{end-start:.5f} sec")

"""
[느낀점]-------------------------------
계산하는 수에 0이 들어가는 경우는 덧셈을 해야한다고 쉽게 떠올릴 수 있으나,
1이 포함될 때 곱셈이 아니라 덧셈을 해야한다고 연상하는 것은 조금 어려울 수도 있겠다 싶었음
"""