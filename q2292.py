# 벌집

n = int(input())

a = 1 #벌집갯수 1개부터 시작
b = 1

while n > a:
    a += 6*b  # 벌집의 갯수가 6의 배수로 증가
    b += 1 # 반복문을 반복하는 횟수

print(b)