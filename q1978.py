#소수 찾기

n = int(input())
n_list = list(map(int, input().split(' ')))
a = 0 # 소수의 갯수

for i in n_list:
    b = 0
    if(i == 1):  # 1은 소수가 아님
        continue
    for j in range(2, i+1):
        if(i % j == 0):
            b += 1
    if(b == 1):
        a += 1
print(a)
