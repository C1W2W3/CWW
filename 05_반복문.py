# AI반 집중교육 자료1
# 주제: 반복문

# [반복문]
## 반복문이란?: 반복적인 작업을 컴퓨터에 시키기 위한 명령.
## 종류: for문(횟수, 시퀀스 자료형), while문(조건)
## 시퀀스 자료형이란?: "순서"가 있는 자료형 (리스트, 문자열, range객체, 튜블, 딕셔너리)

## range() 함수 연습문제: range()를 활용하여
## 여러 활용 해보기 & list로 만들어 결과 확인하: print(list(range(<숫자대입>))) 활용하기
'''
print(list(range(10)))
print(list(range(3,10)))
print(list(range(3,10,3)))
print(list(range(10,3,-2)))
'''
#for 반복문
## : "횟수 or 시퀀스 자료"에 대한 반복문
## [문법] for 변수 in 시퀀스자료:
##           반복할 문장
## for문 연습문제1: range()를 활용한 "횟수" 반복. 원하는 문자열을 10번 반복해서 출력해보자.
'''
for i in range(2, 11, 2):
    print(i)
'''
## for문 연습문제2: list를 활용하여 for 반복문 실행시켜 보기
'''
for i in [1, 2, 3, 4, 5]:
    print(f"{i}꼬마", end='@@')
    print("안녕!")
    print('안녕', '반가워', '반모', sep='**')
print("인디언")
'''
# for문 연습문제3: 문자열을 활용하여 for 반복문 실행시켜보기
'''
for _ in '안녕하세요':
    print(_)
'''
## while 반복문
## : "조건"에 대한 반복문
## [문법] while 조건:
##          반복할 문장
## while문 연습문제1: 기본적인 활용
'''
i=0
while i<5:
    print("안녕하세요")
    i += 1
print("반갑습니다")
'''


## while문 연습문제2: 무한루프와 break를 활용하여 게임 시작메뉴를 만들어보자
'''
select = 0
while True:
    select = int(input("1. 게임 시작// 2. 나가기"))
    if select == 2:
        break
'''
## while문 연습문제3: continue
## : continue 문을 활용하여 1~10까지 숫자 중 홀수만 출력하는 프로그램 작성
'''
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)
'''

## 반복문 mission1-1: 원하는 단의 구구단만 출력하기
## for 반복문을 활용하여 출력을 원하는 구구단의 단 수를 입력받고, 1~9까지 곱한 구구단 출력하기
'''
n = int(input("구구단의 단 수를 입력해주세요>>"))
for i in range(1, 10):
    print(f"{n} * {i} = {n*i}")
'''

## 반복문 mission1-2: 2~9단 모두 출력하기
## for 반복문을 활용하여, 2단~9단까지 모두 출력하기
'''
print("[구구단 전체 출력]")
for i in range(2, 10):
    print(f"[{i}단]")
    for j in range(1, 10):
        print(f"{i} * {j} = {i*j}")
    print("-----------")
'''
## 반복문 mission2-1: while문을 활용하여 반복문 mission1-1과 같은 결과를 출력해보자


## 반복문 mission2-2: while문을 활용하여 반복문 mission1-2와 같은 결과를 출력해보자.


## 반복문 mission3: 영단어 타자연습 프로그램
# -영타연습 Program-
# 1. 연습할 영단어가 담긴 리스트를 만든다.
# 2. 리스트에서 순서대로 단어를 가져와 화면에 출력한다
# 3. 프로그램 사용자는 단어를 그대로 입력한다.
# 4. 입력이 끝나면 전체 문제, 맞은 문제, 틀린 문제의 수가 출력된다.


## 반복문 mission4-1: turtle을 활용한 미디어아트1
'''
import turtle as t

color = ['red', 'green', 'blue']
t.bgcolor('black')
t.pencolor('green')
t.speed(0)
for i in range(301):
    t.forward(i*2)
    t.right(89)

t.mainloop()


'''
## 반복문 mission4-2: turtle을 활용한 미디어아트1
'''
import turtle as t

n = 120
t.bgcolor('black')
t.pencolor('cyan')
t.speed(0)
for i in range(n):
    t.circle(100)
    t.left(360/n)

t.mainloop()
'''
## 반복문 mission5-1: turtle을 활용한 미디어아트2


## 반복문 mission5-2: turtle을 활용한 미디어아트2


# [반복문 추가 문제]
## 이중 for문 연습문제(warming-up)
## : 이중 for문을 활용하여 높이5의 직각삼각형 만들기


## 반복문 추가문제 Mission1: Up-Down 게임 만들기(feat. random 함수)
## >> random 함수를 활용하여 1~100까지의 숫자를 생성하고 up-down 게임 만들어보기


## 반복문 추가문제 Mission2:  ASCII 코드를 활용한 슬록머신


'''
for i in range(1,6):
    for j in range(i):
        print("*", end='')
    print("")
'''
## 반복문 추가문제 Mission3: turtle 모듈을 활용하여 무지개 만들기
### for 반복문 Mission2: turtle 모듈을 활용하여 무지개 만들기



