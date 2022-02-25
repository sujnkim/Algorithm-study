"""
[ch11.greedy] 11-5: 볼링공 고르기 | 난이도 1 | 2019sw마에스트로
INPUT: 볼링공의 개수n, 공의 최대 무게m, 각 볼링공의 무게
    * 첫째 줄 공백으로 구분된 n, m (1<=n<=1000, 1<=m<=10)
    * 둘째 줄 공백으로 구분된 각 볼링공의 무게 k개 (1<=k<=m)
OUTPUT: 두 사람이 서로 무게가 다른 볼링공을 고르는 경우의 수
"""
import time

#input
n, m = map(int, input().split())
ball = list(map(int, input().split()))

"""
[풀이 구상]
목적: 서로 다른 무게의 공을 고르는 경우의 수
조건: 같은 무게의 공은 다른 공으로 취급
result = 두 사람이 공을 고르는 경우의 수 - 같은 무게의 공을 고르는 경우의 수
"""
#solve
start = time.time()

# ary = 무게 별 공의 개수
ary = [0]*11    # 최대무게 m<=10이므로 11칸
for d in ball:
    ary[d]+=1

result = int(n*(n-1)/2)    # 두 사람이 공을 고르는 경우의 수
for i in ary:
    if i>=2:
        no = int(i*(i-1)/2)    # 같은 무게를 고르는 경우
        result = result - no    # 전체에서 제외

#output
print(result)

#time check
end = time.time()
print(f"{end-start:.5f} sec")

# [solution]---------------------------------------------------
"""
*무게 별 공의 개수를 ary에 저장까지는 동일

* a가 특정 무게의 공을 선택했을 때, b가 선택하는 경우를 더해나감
result = 0
for i in range(1,m+1):
    n -= ary[i]            # b가 선택할 수 있는 개수(a의 선택 제외)
    result = n * ary[i]    # a가 선택 * b가 선택
"""
#---------------------------------------------------------------

"""
[느낀점]---------------------------------------------
이게 왜 greedy 문제인지 고민
"""