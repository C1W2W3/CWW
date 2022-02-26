################# 1924번 2007년 ###############
##############################################

'''
day_of_week = ['일','월','화','수','목','금','토']
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

m, d = map(int, input().split())
Day = 0

for i in range(m-1):
    Day += month[i]
Day += d

Day = Day % 7
## m월 d일 - 1월 1일
## hint - for문, month 리스트 사용

print(day_of_week[Day])
'''
'''
##################################################
#############16433번 주디와 당근농장#################
#################################################

N,R,C = map(int,input().split())

## N x N행 리스트 껍데기 만들기
field = [[0 for j in range(N)] for i in range(N)]

if (R + C) % 2 == 0:
    ## 2중 for문을 사용해서 리스트에 'v', '.'을 집어넣기
    ## 리스트 인덱스는 0부터 시작하는 것을 명심!
    for i in range(1, N+1):
        for j in range(1, N+1):
            if (i+j) % 2 == 0:
                field[i-1][j-1] = 'v'
            else:
                field[i - 1][j - 1] = '.'
else:
    for i in range(1,N+1):
        for j in range(1,N+1):
            if (i + j) % 2 == 0:
                field[i - 1][j - 1] = 'v'
            else:
                field[i - 1][j - 1] = '.'
    ## 2중 for문을 사용해서 리스트에 'v', '.'을 집어넣기

for i in range(0, N):
    for j in range(0, N):
        print(field[i][j], end=" ")
    print("\n")

'''
################################################
################# 369게임 ########################
##################################################

start, end = map(int, input().split())
clap = 0

for i in range(start, end+1):
    ## 1000의 자리 숫자, 100의 자리 숫자,,,구하기
    i_1000 = i // 1000
    i_100 = (i % 1000) //100
    i_10 = (i % 100) //10
    i_1 = i % 10
    ## 조건문을 이용
    if i > 1000:
        if i % 3 == 0 and i_1000 % 3 == 0 or i_100 % 3 == 0 or i_10 % 3 == 0 or i_1 % 3 == 0:
            clap += 1
    elif i <= 1000 and i > 100:
        if i % 3 == 0 and i_100 % 3 == 0 or i_10 % 3 == 0 or i_1 % 3 == 0:
            clap += 1
    elif i <= 100 and i > 10:
        if i % 3 == 0 and i_10 % 3 == 0 or i_1 % 3 == 0:
            clap += 1
    elif i <= 10 and i > 0:
        if i % 3 == 0 and i_1 % 3 == 0:
            clap += 1

print(clap)


