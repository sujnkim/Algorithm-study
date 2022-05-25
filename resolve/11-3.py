"""
문자열 뒤집기
"""

#input
data = input()

#solve
# num[0]: 연속된 0 문자열 개수
# num[1]: 연속된 1 문자열 개수
num = [0, 0]

# 첫 번째 숫자
num[int(data[0])] = 1

# 두 번째 숫자부터 확인
for i in range(len(data)-1):
    if data[i] != data[i+1]:
        num[int(data[i+1])] += 1

#output
print(min(num[0], num[1]))