# AI반 집중교육 자료1
# 주제: 함수

# [함수]
##: 여러개의 명령어들을 묶어서 한꺼번에 처리할 수 있도록 만든 하나의 명령어 묶음에 이름을 붙인 것.
## 문법: def 함수이름(매개변수1, 매개변수2, ...):
##         명령어 블럭
##         return 반환값

## docstring: 함수에 대한 설명을 나타내는 문장


## 연습문제1: 입력X, 출력X인 함수
## >> 함수를 호출하면 별모양을 그리는 DrawStar_100()
'''
import turtle as t
def DrawStar_100():
    """
    한 변의 길이가 100인 별을 그리는 함수
    """
    for i in range(5):
        t.forward(100)
        t.right(144)
        t.forward(100)
        t.left(72)

win = t.Screen()
DrawStar_100()
win.mainloop()
'''
## 연습문제2: 입력O, 출력X인 함수
## >> 한 변의 길이를 입력하면, 그 한변의 길이를 가지는 별을 그리는 DrawStar()
'''
import turtle as t
def DrawStar(length):
    """
    한 변의 길이가 length인 별을 그리는 함수
    """
    for i in range(5):
        t.forward(length)
        t.right(144)
        t.forward(length)
        t.left(72)

win = t.Screen()
DrawStar(1)
win.mainloop()
'''

## 연습문제3: 입력X, 출력O인 함수
## >> 1~100까지 랜덤한 정수 1개를 반환하는 getRandomNum()
'''
import random
def getRandomNum():
    return random.randint(1, 100)

num = getRandomNum()
print(num)
print(getRandomNum())
'''
## 연습문제4: 입력O, 출력O인 함수
## >> a,b를 입력하면 두 수의 합을 반환하는 add()
'''
def add(a, b):
    return a+b

X = add(int(input()), int(input()))
print(X)
'''
## 함수 Mission: 앞서 반복문 Mission4에서 그린 무지개를 "함수"로 만들어보자
## 조건은 ppt 30p - 함수 Mission 참고
'''
# Mission: draw_rainbow() 함수 정의하기
def draw_rainbow(t, rainbow_size, pen_size, x, y):
    """
    입력한 t가 rainbow_size크기의 지름과 pen_size 두께의 색상띠를 가지는 무지개를 (x,y)에 그리는 함수
    :param t: 그림을 그릴 turtle 객체
    :param rainbow_size: 무지개의 지름
    :param pen_size: 무지개를 그릴 펜의 두께
    :param x: 무지개가 그려질 x좌표
    :param y: 무지개가 그려질 y좌표
    """
    # 설정(작성할 부분1)


    # 그리기(작성할 부분2)


import turtle

win = turtle.Screen()
win.screensize(1000,1000)
t = turtle.Turtle('turtle')
t.speed(0)

# 이제 draw_rainbow를 활용하여 무지개를 마음껏 그려보자(작성할 부분3)


turtle.mainloop()
'''

