# 분해합

n = int(input())

a = 0

for i in range(1,n+1):
    b = list(map(int,str(i)))
    a = i + sum(b)
    if a == n:
        print(i)
        break

    if i == n:
        print(0)


