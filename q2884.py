# 시간을 설정할때 45분빨리 알람을 맞추는 프로그램

a,b = input().split()

h = int(a)
m = int(b)

if 1 <= h <=23 and 0 <= m < 45:
    print((h-1) , 60-(45-m))
elif h == 0 and 0 <= m < 45:
    print(23 , 60-(45-m))
elif h == 0 and 45 <= m <60:
    print(0, m-45)
else:
    print(h,m-45)

