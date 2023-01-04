# 소인수분해

n = int(input())
a = 2 # 나누는 수

while n != 1:
    if n % a != 0:
        a+= 1
    else:
        n //=a
        print(a)

