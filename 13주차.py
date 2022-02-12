'''
for i in range(1, 10):
    for j in range(1, 10):
        print(f" {i} * {j}= ", i * j)
'''


m = int(input())
dr = int(input())

change_money = m - dr
print(f"거스름돈은 {change_money}원 입니다.")

change_1000 = change_money // 1000
change_500 = (change_money % 1000) // 500
change_100 = (change_money % 500) // 100

print(f"1000원 지폐의 수 => {change_1000}")
print(f"500원 지폐의 수 => {change_500}")
print(f"100원 지폐의 수 => {change_100}")

'''
X = int(input())
num = list(map(int, input().split()))
prime_num = 0

for N in num:
    is_prime = True
    if 1 < N:
        for i in range(2, N):
            if N%i==0 :
                is_prime = False
        if is_prime ==True:
            prime_num += 1

print(prime_num)
'''

'''
n = int(input())

def f(n):
    for i in range(1, n):
        n *= i
    return n


print(f(n))
'''

'''
test = int(input())

for _ in range(test):
    floor = int(input())
    ho = int(input())
    f_n = list(range(1,ho+1))

    for i in range(floor):
        for j in range(1, ho):
            f_n[j] += f_n[j-1]
        print(f_n)
    print(f_n[-1])
'''