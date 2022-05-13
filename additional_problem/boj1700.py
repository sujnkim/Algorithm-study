"""
[BOJ] 1700: 멀티탭 스케줄링
문제 링크: https://www.acmicpc.net/problem/1700
INPUT: 콘센트 개수N, 꽂는 순서 개수K
    * 첫째 줄에 n, k (1<=n,k<=100)
    * 둘째 줄에 k개의 순서가 주어짐 (k개의 자연수)
OUTPUT: 플러그를 뽑는 최소 횟수
"""

"""
생각해볼 수 있는 경우
1. 이미 탭에 꽂혀 있는 경우 -> 그냥 넘어가기 continue
2. 탭에 빈 자리가 있어 그냥 꽂아도 되는 경우 -> append
3. 탭에 빈 자리가 없어 하나를 제거하고 꽂아야 하는 경우
    -> 어느 것을 제거할 것인지 고려 필요. 최소 횟수를 구해야 하므로...
        ith 데이터 이후 사용되지 않을 것이나, 가장 나중에 다시 사용될 것을 뽑자
    -> 현재 상황에서 가장 좋아보이는 것을 선택, 그리디
    1) 앞으로 사용되지 않을 콘센트를 제거
    2) 1)이 없을 경우, 더 나중에 다시 사용될 콘센트를 제거

"""
#input
n, k = map(int, input().split())
process = list(map(int, input().split()))


#solve
plugs = []
result = 0

#사용 순서를 하나씩 확인하며
for i in range(k):
    
    # 1. 이미 탭에 꽂혀있는 경우
    if process[i] in plugs:
        continue
    
    # 2. 제거하지 않고 꽂아도 되는 경우
    if len(plugs) < n:
        plugs.append(process[i])
        continue

    # 3. 하나를 제거하고 꽂아야하는 경우
    idxs=[]
    for t in plugs:
        # 앞으로 사용되지 않는 경우
        if t not in process[i:]:
            idx = 101

        # 사용 되는 경우
        else:
            idx = process[i:].index(t)
            
        idxs.append(idx)

    del_idx = idxs.index(max(idxs))
    plugs[del_idx] = process[i]
    result += 1


#output
print(result)

"""
풀이1. 
가장 나중에 사용되는 경우를 찾을 때
아직 확인하지 않은 사용 순서를 뒤에서부터 탐색하려고 했음(for문 사용)

=> index 메소드를 사용하면 for문을 쓰지 않고 구현이 가능했음
    cf. 리스트의 index 메소드: list.index(value)
        list 내의 가장 처음 나오는 value의 인덱스를 반환
=> plugs에 꽂혀있는 각 플러그에 대해 다음에 사용되는 인덱스를 계산
=> 다시 사용되지 않을 경우, 플러그 최대 개수보다 큰 101로 설정
=> 인덱스 값이 큰 것이 더 나중에 사용되거나 사용되지 않을 것이므로 제거대상

"""