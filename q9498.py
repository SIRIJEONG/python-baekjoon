#점수별 성적 구분하여 출력하기

b = int(input())

if 100 >= b >= 90:
    print('A')
elif 89 >= b >= 80:
    print('B')
elif 79 >= b >= 70:
    print('C')
elif 69 >= b >= 60:
    print('D')
else:
    print('F')