"""
[ch12.구현] 12-9: 문자열 압축 | 난이도1.5 | 2020카카오신입공채
문제링크: https://programmers.co.kr/learn/courses/30/lessons/60057
INPUT: 문자열 s
    * 알파벳 소문자로만 이루어진 s (1<=len(s)<=1,000)
OUTPUT: 1개 이상의 단위로 문자열을 압축한 결과 중 가장 짧은 것의 길이
"""

"""
[풀이 구상]
입력으로 주어지는 문자열의 최대 길이가 1,000이므로 모든 가능한 경우를 확인해도 괜찮을 것 같다
전체 문자열의 길이가 n일 경우, 1 ~ n/2 단위를 사용하여 압축하는 경우를 전부 확인하여 최소값을 반환하자
    * n/2보다 큰 단위의 경우, 1회 이상 연속될 수 없기 때문에 확인하는 의미가 없다

문자열 처음부터 끝까지 돌면서
1부터 s/2만큼씩 묶은 경우를 전부 확인, min인 경우만 저장
"""

# solution function
def solution(s):
    
    min = len(s)     # 입력 문자열 크기로 초기화(적어도 이것보다는 작거나 같게 압축되므로)
    step = 1         # 1개 단위로 자른 경우부터 확인
    for _ in range(len(s)//2 + 1):
        temp = s[0:step]
        cnt = 1
        zip = 0
        for j in range(1, len(s)//step + 1):
            if temp == s[j*step:(j+1)*step]:    # 연속하는 경우
                cnt += 1
            else:                               # 연속이 끝난 경우
                if cnt == 1:    # 1회 연속
                    zip = zip + step
                else:            # 2회 이상 연속
                    zip = zip + len(str(cnt)) + step
                
                temp = s[j*step:(j+1)*step]
                cnt = 1    # cnt 초기화
                
        zip = zip + (len(s)-step*(j))    #남는 문자열 계산

        # 압축했을 때 더 짧은 것의 길이 저장
        if zip<min: 
            min = zip
        step += 1
    
    return min


#input
s = input()

# output
print(solution(s))

"""
[느낀점]
+ for문을 사용할 때 세 번째 인자를 사용하면 step만큼 증가시키면서 반복할 수 있었음...
-> 이 방법이 생각이 나지 않아서 j*step을 계산하는 방식으로 구현함

+ 비교했을 때 다른 문자열이라서 zip을 계산하는 부분에서 실수가 있었음
-> 어떤 예시에서 계속 1~2정도 차이가 나서... 고민했는데
-> cnt가 1인 경우에는 문자열에 1을 적지 않기 때문에 cnt>=2인 경우와 나눠서 계산해야 했음!!
-> 책의 예시 답안에서는 한 문장으로 구현하였음
    zip += len(str(cnt)) + temp + zip if cnt>=2 else temp+zip

+ 책의 예시 답안의 경우 실제로 문자열을 생성한 후, 마지막에 한 번만 len을 계산하였음
-> 나는 처음부터 len으로 계산하여 계산했는데, 구현 도중 오류가 있는지 확인하려면
    책의 방식처럼 하는 편이 나을 것 같다는 생각이 든다...
"""