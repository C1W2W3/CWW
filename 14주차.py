#가위바위보

'''
import random

play_win = 0
com_win = 0

while True:

    player = input()
    RSP = ['가위', '바위', '보']
    computer = random.choice(RSP)

    if (player == '가위' and computer == '보') or (player == '바위' and computer == '가위') or (player == '보' and computer == '바위'):
        print(f"computer = {computer}, player = {player}이기 때문에 player 승리!")
        play_win += 1


    elif (computer=='가위'and player=='보')or(computer=='바위' and player=='가위')or(computer=='보' and player=='바위'):
        print(f"computer = {computer}, player = {player}이기 때문에 computer 승리!")
        com_win += 1

    else:
        print(f"computer = {computer}, player = {player}이기 때문에 computer 무승부!")

    if play_win == 2 or com_win == 2:
        결과 = False
        print(f"player가 {play_win}회, computer가 {com_win}회 승리했습니다.")
        break
'''

'''
A = int(input())
B = int(input())
V = int(input())

days = 0
now = 0

while True:

    days += 1
    now = now + A
    if now >= V:
        print(days)
        break

    else :
        now = now - B
'''

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
c = 0

A = sorted(A)
B = sorted(B, reverse=True)

for i in range(N):
    c +=(A[i] * B[i])

print(c)