"""
[ch3.greedy] 3-3: 숫자 카드 게임
INPUT: 행의 개수N, 열의 개수M
    * 첫째 줄에 공백으로 구분된 N, M
    * 둘째 줄 부터 M개의 자연수(1이상 10,000이하)를 N번
OUTPUT: 게임 룰에 맞게 선택된 숫자
"""
#import time

#input
n,m = map(int, input().split())

#start=time.time()

"""
각 행에서 최소인 숫자 중 최대인 것이 result(최종결과)
* 각 행에서 최소인 것을 선택: min함수
* 현재 result와 비교, 큰 숫자가 result: max함수
"""
#solve
result= 0   #input은 1이상 10000이하의 숫자이므로 0으로 초기화
for i in range(n): 
    data = list(map(int,input().split())) #한 행씩 input
    minum=min(data) #행의 최소숫자 선택
    result = max(result,minum)  #현재 result와 최소숫자 중 큰 것

#output
print(result)

#time check
#end=time.time()
#print(f"{end-start:.5f} sec")
