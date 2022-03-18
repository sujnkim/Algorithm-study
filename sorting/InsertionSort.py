#삽입정렬Insertion sort 소스코드

array = [7,5,9,0,3,1,6,2,4,8]

#첫 번째 원소(인덱스0)는 이미 그 자체로 정렬되어 있다고 가정
for i in range(1, len(array)): 
    for j in range(i, 0, -1):   #인덱스 i부터 1까지 감소하며 반복
        #한 칸씩 왼쪽으로 이동하면서 비교
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:   #자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break
    
print(array)