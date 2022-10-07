# 주어진 좌표가 사분면중 어디에 들어가는지 출력하는 함수

a = int(input())
b = int(input())
# a != 0   b !=0
if a > 0 and b > 0:
    print('1')
elif a < 0 and b > 0:
    print('2')
elif a < 0 and b < 0:
    print('3')
else:
    print('4')