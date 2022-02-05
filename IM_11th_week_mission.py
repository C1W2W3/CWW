# Ai반 2기 python 중급반 - 11주차 정규수업(16:30~18:30) mission
'''
[수업을 시작하기 전에!]
1. 웨일ON으로 원격 회의실 접속하기
2. NAS 서버 접속(접속이 안될 경우 말해주기~)
3. 탐색기를 활용하여 내가 현재 작업하고 있는 파일 경로 열어두기
4. Pycharm 수업 코드 다운로드 받아 열어두기~
5. 수업시간 집중~~~!! 딴 짓! 멈춰~~~~~!
'''

# Problem 1: 더하기 사이클
'''
import copy

N = int(input())
if N < 10:
    N *= 10
n = copy.copy(N)
count = 0

while True:
    n = (n%10)*10 + (n//10 + n%10)%10
    count += 1

    if N == n:
        break

print(count)
'''

# Problem 2: 평균은 넘겠지
'''
C = int(input())
N = []
scores = []
result = []

for i in range(C):
    temp = list(map(int, input().split()))
    N.append(temp[0])
    scores.append(temp[1:])

for i in range(C):

    avg = sum(scores[i]) / N[i]
    count = 0
    for score in scores[i]:
        if score > avg:
            count += 1
    percent = count / N[i] * 100
    result.append(percent) ##= (count / N[i]) * 100

for i in result:
    print(f"{i:.3f}%")
'''

# Problem 3: 셀프 넘버

import copy

N = 10000
numbers = [True] * (N+1)

def d(n):
    temp = n + sum(list(map(int, list(str(n)))))
    if temp <= N:
        numbers[temp] = False

for i in range(1, N+1):
    d(i)

for i in range(1, N+1):
    if numbers[i] == True:
        print(i)

# 추가 문제: ACM 호텔

