"""
[ch3.greedy] 3-2: 큰 수의 법칙
INPUT: 배열크기N, 총 더해지는 횟수M, 반복가능횟수K
    * 첫째 줄에 공백으로 구분된 N, M, K
    * 둘째 줄에 N개의 자연수(1이상 10000이하)
    * K는 M보다 작거나 같음
OUTPUT: 큰 수의 법칙에 따라 더해진 결과
"""
import time

# input
n,m,k=map(int,input().split())
data = list(map(int,input().split()))

start=time.time()

# solve
result=0
data.sort() #input data 정렬
first=data[n-1]    # 첫 번째로 큰 수
second=data[n-2]   # 두 번째로 큰 수

"""
#처음 짠 코드
# (첫 번째 큰 수 k번, 두 번째 큰 수 1번)이 반복
for i in range(m//(k+1)):
    result+=first*k
    result+=second
result+=first*(m%(k+1))
"""

# 1st 수정
# 반복문을 쓸 필요가 없었음
result+=(first*k+second)*int(m/(k+1))
result+=first*(m%(k+1))

"""
#책 예시
#cnt: 첫 번째 큰 수가 더해지는 횟수
cnt=int(m/(k+1))*k + m%(k+1)
result += first*cnt
result += second*(m-cnt)
"""

# output
print(result)

# time check
end=time.time()
print(f"{end-start:.5f} sec")