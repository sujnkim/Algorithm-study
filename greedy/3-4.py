"""
[ch3.greedy] 3-4: 1이 될 때까지
INPUT: 어떠한 수n, 나누는 수k
    * 첫째 줄에 공백으로 구분되는 자연수 n,k(2이상 100,000이하)
    * n은 항상 k보다 크거나 같음
OUTPUT: n이 1이 될 때까지 수행해야하는 최소 과정 횟수
"""
import time

#input
n,k = map(int, input().split())

"""
# 알고리즘 구상
1. n에서 1을 뺀다
2. (n이 k로 나누어 떨어질때) n을 k로 나눈다
n이 1이 될 때까지 1 or 2 과정을 반복: 반복while문 종료 조건

적은 횟수의 과정으로 n을 1로 만들려면 과정2가 효율적
최대한 과정2를 많이 사용하면 됨: greedy
"""
start = time.time()

#solve
result = 0
"""
# 처음 짠 코드
# 이 방식은 100억 이상의 수로 실행할 경우 시간이 오래 걸린다!!
# 1을 뺄 때 불필요하게 반복문을 쓰기 때문
while n!=1: #n이 1이 되면 종료
    if(n%k==0): #과정2 이행가능 여부 확인
        n=n//k
    else:       #과정1 이행
        n-=1
    result+=1   #반복마다 한 개의 과정을 수행
"""

# 1st 수정 코드(책 설명 참고)
while True:
    # 과정1
    # 반복문으로 1씩 빼는 게 아니라 한 번에 계산
    target = (n//k)*k
    n = target
    result += (n-target)

    if n<k: # 종료조건
        break
    # 과정2
    n//=k
    result+=1

# 남은 수 반영
result += (n-1)

#output
print(result)

end = time.time()
print(f"{end-start:.5f} sec")