"""
모험가 길드
"""

#input
n = int(input())    #모험가 수
data = list(map(int, input().split()))    #공포도


#solve
data.sort()

result = 0
cnt = 0

# 현재 확인하는 공포도를 x라고 할 때
# 현재 그룹에 포함된 수 >= x일 경우 그룹 결성 가능
for d in data:
    # 현재 그룹에 1명 추가
    cnt += 1

    if cnt >= d:
        result += 1
        cnt = 0
    

#output
print(result)