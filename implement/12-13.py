"""
[ch12.구현] 12-13: 치킨 배달 | 난이도2 | 삼성전자sw역량테스트
INPUT: 도시크기n, 남길 치킨집m
    * 첫째 줄에 공백으로 구분되는 n, m (2<=n<=50, 1<=m<=13)
    * 둘째 줄부터 n개의 줄에 도시의 정보 (0:빈칸, 1:집, 2:치킨집)
    * 1<=집 개수<=2n, m<=치킨집 개수<=13
OUTPUT: 도시치킨거리의 최솟값
"""
from itertools import combinations


#input
n, m = map(int, input().split())

chicken, home = [], []
for i in range(n):
    data = list(map(int, input().split()))
    for d in range(n):
        if data[d] == 1:
            home.append((i, d))        #집home
        elif data[d] == 2:
            chicken.append((i, d))    #치킨집chicken

"""
[풀이 구상]
모든 치킨집(최대 13개 가능) 중 순서에 상관없이 M개의 치킨집을 고르는 경우의 수: 조합, 최대 13 C m
    -> m값이 얼마가 되든, 그 값이 100,000을 넘지 않는다고한다(책 설명 참고)
조합을 계산하기 위해 라이브러리 itertools combinations를 사용하자
"""

combis = list(combinations(chicken, m))    #모든 치킨집에서 m개를 뽑는 조합

# 치킨 거리 계산
def calc(combi):
    result = 0
    for hx, hy in home:
        temp = 1e9
        for cx, cy in combi:
            temp = min(temp, abs(hx-cx) + abs(hy-cy))
        result += temp    # 집과 가장 가까운 치킨집과의 거리 더하기
    # 치킨거리 합 반환
    return result

# 치킨 거리의 합 min을 출력
result = 1e9
for combi in combis:
    result = min(result, calc(combi))

#output
print(result)

"""
[느낀점]
+ 큰 수로 초기화 할 때, 1e9를 사용했음...
-> 1e9 = 1*10^9 = 1000000000, 2e9 = 2*10^9 = 2000000000
-> 2e9는 int범위에서 무한대INF를 나타낼 때 사용한다 !

+ itertools의 라이브러리를 사용하는 연습이 필요할 것 같다
"""