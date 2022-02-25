"""
[ch11.greedy] 11-4: 만들 수 없는 금액 | 난이도 1 | K기출대회
INPUT: 동전의 개수n, 화폐 단위를 나타내는 n개의 자연수
    * 첫째 줄 양의 정수 n (1<=n<=1000)
    * 둘째 줄 공백으로 구분된 n개의 자연수 (화폐단위는 1,000,000이하의 자연수)
OUTPUT: 주어진 동전으로 만들 수 없는 금액의 최소값
"""
import time

#input
n = int(input())
coins = list(map(int, input().split()))

"""
[풀이 구상]
만들 수 없는 최소값을 구하는 문제이므로 우선 데이터 오름차순 정렬을 수행했음
또한 1부터 점차 값을 올리며 제일 먼저 만들 수 없는 값을 찾는 게 빠를 거라고 생각
"""
#solve
start = time.time()

coins.sort()

check = 1
for c in coins:
    if check < c:
        break
    check += c

#output
print(check)

#time check
end = time.time()
print(f"{end-start:.5f} sec")

"""
[느낀점]----------------------------------
뭔가... data로 받은 리스트를 하나씩 확인하면서
더 최대/최소값인지 확인,수정해서 해결하는 문제가 많은듯?
이게 <그리디>문제 인건가...?!
"""