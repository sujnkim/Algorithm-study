"""
기본적인 서로소 집합 알고리즘 소스코드

1. union(합집합) 연산을 확인하여, 서로 연결된 두 노드 a, b를 확인
    1) a, b의 루트 노드 a', b'를 찾는다 (재귀적으로)
    2) a'<b'인 경우, a'를 b'의 부모 노드로 설정(b'가 a'를 가리킴)
2. 모든 union(합집합) 연산을 처리할 때까지 과정 1을 반복

"""

#특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    #루트 노드를 찾을 때까지 재귀적 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x


# 두 원소가 속한 집합 합치기: union
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 노드 개수, 간선 개수(union 연산횟수) 입력받기
v, e = map(int, input().split())
parent = [0] * (v+1)    #부모테이블 초기화

#부모 테이블에서, 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i


#union 연산 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

    
#각 원소가 속한 집합 출력
print('각 원소가 속한 집합: ', end='')
for i in range(1, v+1):
    print(find_parent(parent, i), end=' ')

print()

# 부모 테이블 내용 출력
print('부모 테이블: ', end='')
for i in range(1, v+1):
    print(parent[i], end=' ')


"""
루트 노드를 찾기 위해서 부모 테이블을 계속해서 확인하며 거슬러 올라가야 함

find함수가 비효율적으로 동작 => 최악의 경우 모든 노드를 확인해야 하므로 복잡도기 O(V)
=> 경로 압축Path Compression으로 최적화, 시간 복잡도 개선 가능
=> find함수를 재귀적으로 호출하여 부모 테이블 값을 갱신하는 기법
"""

# 개선된 서로소집합 알고리즘의 find 함수
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
