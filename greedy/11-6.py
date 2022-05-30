"""
[ch11.greedy] 11-6: 무지의 먹방 라이브 | 난이도1 | 2019카카오
문제 링크: https://programmers.co.kr/learn/courses/30/lessons/42891

제한 사항>
food_times: 각 음식을 모두 먹는 데 필요한 시간이 음식 번호 순으로 들어있는 배열
k: 방송이 중단된 시간
solution: 네트워크가 발생한 k초 이후 몇 번 음식부터 다시 섭취하면 되는 지 return하는 solution 함수
          만약 더 섭취해야 할 음식이 없다면 -1 반환
"""
import heapq

def solution(food_times, k):

    # 더 섭취할 음식이 없는 경우
    if sum(food_times) <= k:
        return -1

    # 우선순위 큐에 삽입 => 최소힙 형성
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))

    
    prev = 0        #이전의 min value(계산을 위한 변수)
    food_cnt = len(food_times)    #남은 음식 종류 개수
    
    while (q[0][0]-prev) * food_cnt <= k:
        now = heapq.heappop(q)[0]    #현재 min value
        k -= (now-prev) * food_cnt    #남은 시간 갱신

        food_cnt -= 1    #남은 음식 종류 개수 갱신
        prev = now        

    # result 리스트: 힙을 2번째 요소(idx)를 기준으로 정렬
    result = sorted(q, key=lambda x: x[1])
    return result[k%food_cnt][1]

    
#----------
food_times = [8, 6, 4]
k = 15

print(solution(food_times, k))