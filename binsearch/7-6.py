"""
7-5.py 부품 찾기 문제를 계수 정렬 알고리즘으로 풀기
    -> 모든 원소의 번호를 포함할 수 있는 크기의 리스트count를 만든다
    -> 리스트의 인덱스에 직접 접근하여 요청 부품의 존재를 확인
"""

#input
n = int(input())

# solve: 계수 정렬
count = [0] * 1000001    # 1<=n<=1,000000

for i in input().split():
    count[int(i)] += 1
    

m = int(input())
want = list(map(int, input().split()))

    
#output
for w in want:
    if count[w] != 0:
        print('yes', end=' ')
    else:
        print('no', end=' ')