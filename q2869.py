#달팽이는 올라가고싶다
#
# a,b,v = map(int, input().split())
#
# k = 0 # 올라가는데 걸리는 일수
# d = 0 # 올라간 높이
#
# while 1:
#     k+= 1
#     if a*k-b*(k-1)>=v:
#         break
# print(k)

a,b,v = map(int, input().split())

x = (v-b)/(a-b)
if x == int(x):
    print(int(x))
else:
    print(int(x) + 1)
