# 숫자 뒤집기

a,b = input().split()

c = int(str(a)[::-1])
d = int(str(b)[::-1])

if c > d:
    print(c)
elif c < d:
    print(d)
else:
    print()