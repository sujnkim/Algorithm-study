 #6-4: 퀵 정렬 소스코드

array = [7,5,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
    if start >= end:  # 원소가 1개인 경우 종료
        return

    pivot = start   # 피벗 = 첫 번째 원소
    left = start + 1
    right = end

    while left <= right:
        #피벗보다 큰 데이터를 찾을 때까지
        while left<=end and array[left]<=array[pivot]:
            left += 1
        #피벗보다 작은 데이터를 찾을 때까지
        while right>start and array[right]>=array[pivot]:
            right -= 1

        if left > right:    #엇갈렸다면 작은 데이터-피벗 교체
            array[right], array[pivot] = array[pivot], array[right]
        else:   #엇갈리지 않앟다면 작은데이터-큰 데이터 교체
            array[left], array[right] = array[right], array[left]

        #분할 이후 왼쪽/오른쪽 부분에서 각각 퀵정렬 수행
        quick_sort(array,start,right-1)
        quick_sort(array,right+1,end)


quick_sort(array, 0, len(array)-1)
print(array)