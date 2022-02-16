"""
[ch3.greedy] 3-1: 거스름돈
INPUT: N(거슬러줘야 할 금액, 10의 배수)
OUTPUT: 거슬러 줄 동전의 최소 개수
* 사용할 동전 금액 종류 : 500, 100, 50, 10(무한개)
"""

#input
n=1260
coin_types=[500,100,50,10]  #사용할 동전 종류(type)

# solve
cnt=0
for coin in coin_types:
    cnt+=n//coin
    n=n%coin

#output
print(cnt)