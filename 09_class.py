# AI반 집중교육 자료1
# 주제: class

# [클래스(class)]

# <class(1): 클래스 기본>
## 클래스와 객체
## 클래스: 객체를 만들기 위한 "설계도"
## 객체: 설계도로부터 만들어낸 "제품"

## 클래스를 사용하는 이유
## LOL 인벤 챔피언들 정보: https://lol.inven.co.kr/dataninfo/champion/compare.php
## LOL 혹은 자신이 좋아하는 게임의 캐릭터 3가지를 선택하여 해당 캐릭터의 정보(채력, 공격력, 이동속도)를 입력하고,
## "게임 시작 인사, 캐릭터 능력을 각각 출력(함수)"등을 수행하는 프로그램을 만들어 보자

## case1: class를 활용하지 않은 경우
# 정보 출력 함수 정의
'''
# character_info() 함수 정의하기
def character_info(name, attack, health, speed):
    print(f"{name}")# name 출력
    print(f"기본 공격력: {attack}")# 기본 공격력(attack) 출력
    print(f"기본 체력: {health}")# 기본 체력(health) 출력
    print(f"기본 속도: {speed}")# 기본 속도(speed) 출력

# character1 만들어주기(정보 할당)
character1_name = "[리신]"  ## character1의 name 정의
character1_attack = 100  ## character1의 attack 정의
character1_health = 500  ## character1의 health 정의
character1_speed = 10    ## character1의 speed 정의
print(f"{character1_name}님 소환사의 협곡에 오신 것을 환영합니다.")

character_info(character1_name, character1_attack, character1_health, character1_speed)

# character2 만들어주기(정보 할당)
character2_name = "[탐켄츠]"  ## character1의 name 정의
character2_attack = 200  ## character1의 attack 정의
character2_health = 700  ## character1의 health 정의
character2_speed = 5    ## character1의 speed 정의
print(f"{character2_name}님 소환사의 협곡에 오신 것을 환영합니다.")

character_info(character2_name, character2_attack, character2_health, character2_speed)

character3_name = "[갈리오]"  ## character1의 name 정의
character3_attack = 200  ## character1의 attack 정의
character3_health = 52  ## character1의 health 정의
character3_speed = 1    ## character1의 speed 정의
print(f"{character3_name}님 소환사의 협곡에 오신 것을 환영합니다.")

character_info(character3_name, character3_attack, character3_health, character3_speed)

## >> 캐릭터를 하나 만들 때마다 작성해야 하는 코드가 많고 복붙해서 수정하기도 귀찮다...
'''
## case2: 클래스를 사용한 경우
'''
class Character:# Character class 정의해주기
    def __init__(self, name, attack, health, speed):# 생성자 정의 - name, attack, health, speed 입력
        self.name = name  # self.name
        self.attack = attack
        self.health = health
        self.speed = speed
        print(f"{self.name}님 소환사의 협곡에 오신 것을 환영합니다.")# 소환사 협곡! 환영!

    def character_info(self): # character_info() 메서드 정의
        print(f"{self.name}")  # name 출력
        print(f"기본 공격력: {self.attack}")  # 기본 공격력(attack) 출력
        print(f"기본 체력: {self.health}")  # 기본 체력(health) 출력
        print(f"기본 속도: {self.speed}")  # 기본 속도(speed) 출력


character1 = Character('리신', 100, 200, 10)
character1.character_info()

character2 = Character('탐켄츠', 300, 100, 5)
character2.character_info()

character3 = Character('할카림', 500, 100, 20)
character3.character_info()
'''

## <class 생성 및 호출>
## <class 생성 문법>
## class 클래스 이름:
##     def 메서드 이름1(self, 입력변수1, 입력변수2, ...):
##         실행명령
##     def 메서드 이름2(self, 입력변수1, 입력변수2. ...):
##         실행명령

## <class 호출 문법>
## 클래스 선언하기: 인스턴스 = 클래스이름()
## 매서드 호출하기: 인스턴스.메서드()

## 연습문제: 모든 자료형은 class이다.
## 정수형, 실수형, 문자열, 불린형 등의 다양한 자료형을 가진 변수를 선언 후
## type() 명령을 통해 자료형을 출력하여 보자(class 확인 할 것)
## + 추가적으로 .__dir__() 역시 출력해보자
'''
a = 12              # int
b = 0.125           # float
c = '안녕하세요'      # str
d = True            # bool

print(type(a))
print(type(b))
print(type(c))
print(type(d))

print(a.__dir__())
print(b.__dir__())
print(c.__dir__())
print(d.__dir__())
'''

## class Mission1
## : Mission에 언급된 내용대로 Cat class를 만들어 보자
'''
class Cat:
    def cry(self):
        print("야옹!")
    def tail_wag(self):
        print("야옹! 야옹!")
    def translate_cry(self):
        print("하찮은 닝겐! 밥을 대령하라!")
    def translate_tw(self):
        print("핸드폰을 떨구자!")

Takealook = Cat()
Takealook.cry()
Takealook.tail_wag()
Takealook.translate_cry()
Takealook.translate_tw()
'''

# <class(2): 생성자와 상속>
## <생성자>
## : 객체가 생성될 때 자동으로 호출되는 메서드.
## [문법] class 클래스이름:
##           def __init__(self, 입력변수들):
##               초기화 실행 문장

## 생성자 연습문제
## : Monster 클래스를 만들고 step에 따라 생성자와 메서드가 추가된 Monster 클래스를 만들어보자.
## step1) 가장 기본적인 Monster 클래스를 만들어 보자
##        : say 메서드만을 가지는 Monster 클래스
'''
# <Moster class 만들기>
class Monster:
    def __init__(self, name , attack, health, speed):
        self.name = name
        self.attack = attack
        self.health = health
        self.speed = speed
        print(f"나는 아주아주 무서운 {self.name}이다")
    def say(self):
        print("나는 아주아주 무서운 몬스터다!!!")
    def decrease_health(self,num):
        self.health -= num
    def get_health(self):
        return self.health
    def info(self):
        print(f"[{self.name} 스테이터스]")
        print(f"공격력: {self.attack}")
        print(f"체력: {self.health}")
        print(f"이속: {self.speed}")

#<Monster 객체 생성 및 say 메서드 호출하기>
goblin = Monster('고블린', 10, 100, 5)
wolf = Monster('늑대', 20, 150, 10)


goblin.info()
goblin.decrease_health(20)
print(f'고블린 체력: {goblin.get_health()}')
print()
goblin.info()
'''
## step2) Monster 클래스에 속성(name, health, attack, speed)을 추가하여 초기화해보자.
##        또한, 인스턴스 생성 시에 say의 내용이 출력되도록 만들어보자.




## step3) Monster 클래스에 메서드(decrease_health, get_health, info)를 추가한 후,
##        goblin과 wolf 객체를 생성하여 각 메서드들을 호출해보자.
'''
<Monster 객체에 여러가지 메서드 추가하기 >

<golblin과 wolf를 Monster 객체로 선언하고 메서드 호출하기>
'''

## <상속>
## : 부모 클래스의 속성과 메서드를 자식클래스가 물려받을 수 있도록 만든 기능
## 상속을 사용하는 이유: 클래스들에 중복된 코드를 제거하고 유지보수를 하기 위해 사용하기 위해서 사용.

## <메서드 오버라이딩(덮어쓰기)>
## : 부모 클래스에 있는 메서드를 자식클래스에서 동일한 이름으로 다시 만드는 것

## 상속 연습문제
## :Monster 클래스를 만들고, 상속을 활용하여 Wolf, Shark, Dragon 클래스를 만들어,각각의 객체를 생성해보자.
##
## step1) 부모 클래스: Monster 클래스 정의하기
## - 속성: name, health, attack
## - 메서드: move("self.name 지상에서 이동하기"를 출력하는 메서드, 이후 해당 몬스터의 이동방법이 출력되도록 할 것임.)
'''
class Monster:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
    def move(self):
        print(f'{self.name}뛰어다니기')

'''
## step2) 자식 클래스: Wolf, Shark, Dragon
## - Monster 클래스를 상속 받을 것.
## - 몬스터의 속성에 맞게 move를 메서드 오버라이딩할 것.
'''
class Wolf(Monster):
    pass

class Shark(Monster):
    def move(self):
        print(f"{self.name} 헤엄치기")

class Dragon(Monster):
    def move(self):
        print(f"{self.name} 날기")

wolf = Wolf('늑대', 100, 50)
shark = Shark('아기상어', 300, 300)
dragon = Dragon('투슬리스', 1000, 500)

wolf.move()
shark.move()
dragon.move()
'''
# <class(3): super()와 클래스 변수>
## super(): 부모클래스의 메서드들의 내용들을 그대로 가져와  자식 클래스 추가하고 싶은 경우에 사용하는 명령
## 클래스변수: 해당 클래스로 만든 모든 객체들이 공유하는 변수

## super()와 클래스 변수 연습문제: RPG게임 업데이트
## : ‘상속 및 메서드 오버라이딩 연습문제’에서 만들었던 내용들을 업데이트해보자
## - 드래곤 클래스에 ‘인스턴스 속성’으로 ‘3개의 스킬(불뿜기, 꼬리치기, 날개치기)’을 추가
## - 드래곤이 스킬을 쓰면 속성 중 하나가 무작위로 사용되도록 설정(random 모듈 이용)

import random

class Monster:
    Monster_num = 1000
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        Monster.Monster_num -= 1
        print("생성가능 몬스터 수: " ,Monster.Monster_num)

    def move(self):
        print(f'{self.name}뛰어다니기')

class Wolf(Monster):
    pass

class Shark(Monster):
    def move(self):
        print(f"{self.name} 헤엄치기")

class Dragon(Monster):
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)
        self.skills = '불뿜기', '헬파이어', '꼬리치기'

    def move(self):
        print(f"{self.name} 날기")
    def skill(self):
        print(f'{self.name}가 {self.skills[random.randint(0,2)]}을(를)사용했다!')

wolf = Wolf('늑대', 100, 50)
shark = Shark('아기상어', 300, 300)
dragon = Dragon('투슬리스', 1000, 500)

wolf.move()
shark.move()
dragon.move()

dragon.skill()

## class Mission: 아이템 구성안과 설계도를 활용하여, class와 객체를 생성해 보자
## 이때, 부모 클래스: Item // 자식 클래스: WearableItem, UsableItem 이다.


