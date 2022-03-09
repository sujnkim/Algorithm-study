"""
[ch5.DFSBFS] 5-10: 음료수 얼려먹기 | 난이도1.5 | 실전문제
INPUT: 얼음틀 세로길이n, 가로길이m, 얼음틀의 형태
    * 첫째 줄 공백으로 구분된 n, m ( 1<=n,m<=1000)
    * 둘째 줄부터 공백없이 주어지는 N+1 얼음틀의 형태 (구멍:0, 막힘:1)
OUTPUT: 한 번에 만들 수 있는 아이스크림의 개수 출력
"""

#input
n, m = map(int, input().split())

#얼음 틀 정보 채우기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

"""
[풀이구상]
얼음을 얼릴 수 있는 공간이 상, 하, 좌, 우 로 연결 -> 그래프 형태로 모델링 가능, DFS알고리즘 사용

1) 특정 지점 주변의 (상,하,좌,우)를 살펴보며 값이 0인(아직 방문하지 않았고 구멍이 뚫린) 지점에 방문
2) 방문한 지점의 (상,하,좌,우)를 살펴보며 방문을 다시 진행 -> 연결된 모든 지점 방문 가능
3) 1)~2)의 과정을 모든 노드에 반복하며 방문하지 않은 지점의 수를 센다
"""
def dfs(x, y):
    # 범위 체크 -> 벗어나면 즉시 종료
    if x<0 or x>n-1 or y<0 or y>m-1:
        return False

    # 값이 0일 때만 주변을 방문할 수 있음
    if graph[x][y] == 0:
        graph[x][y]=1    # 방문 노드 처리

        # 재귀함수를 이용하여 주변 칸(상,우,하,좌)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True

    # 값이 1인 경우 false 반환
    return False

  
#solve
result = 0

for i in range(n):
    for j in range(m):
        if dfs(i, j)==True:
            result += 1

#output
print(result)


"""
[느낀점]
+ 얼음틀 입력을 받을 때 공백없는 입력인데 split()을 사용해버려서, 오류발생
-> 어디서 오류가 발생한 것인지 알아채지 못해서 허둥지둥했다. 입력이 잘 받아졌는지 확인 할 것
"""