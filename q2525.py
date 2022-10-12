# 요리를 넣으면 인공지능이 판단하여 필요한시간을 분단위로 알려준다 현재시간에 필요한 시간을 더하는 프로그램만들기

a,b = map(int , input().split())
c = int(input())

a += c // 60
b += c % 60


if b >= 60:
    a += 1
    b -= 60

if a >= 24:
    a -=24

print(a,b)