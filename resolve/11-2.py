"""
곱하기 혹은 더하기
"""

#input
data = input()

"""
1. 0이 섞인 경우 => 곱하면 안됨
2. 1이 섞인 경우 => 곱하는 것보다 덧셈이 이득 (주의)
>> 1 이하의 값인 경우 덧셈 / 이외에는 곱셈

3. 첫 번째 숫자가 0이나 1이하인 경우가 있을 수 있음
>> 만약, 12894인 경우 1*2가 아니라 1+2로 계산해야 함
"""

# 제일 첫 번째 숫자
result = int(data[0])

for i in range(1, len(data)):

    # 현재 확인할 숫자
    now = int(data[i])
    
    # 현재 숫자가 1 이하 or 결과가 1이하인 경우 => 덧셈 수행
    if now <= 1 or result <=1 :
        result += now

    # 이외의 경우 => 곱셈 수행
    else:
        result *= now

#output
print(result)