# 소수 구하기

# m,n = map(int, input().split())
#
# for i in range(m,n+1):
#     error = 0
#     if i > 1:
#         for j in range(2,i):
#             if i % j == 0:
#                 error += 1
#                 break
#         if error == 0:
#             print(i)


m,n = map(int, input().split())

for i in range(m,n+1):
    if i == 1: # 1은 소수가 아니므로 제외
        continue
    for j in range(2,int(i**0.5)+1):
        if i%j == 0: # 약수가 존재하므로 소수가 아님
            break # 더이상 검사할 필요가 없으므로 멈춤
    else:
        print(i)

# 처음 처럼 풀면 시간초과가 뜬다
# 이문제는 에라토스테네스의 체(소수구하기) 문제이다.
# 범위는 2부터 int(i**0.5)+1까지이다. 특정 수의 저곱근을 구해 그 제곱근 까지의 약수를 구하면 해당 약수를 포함하는 수를 모두 제거할 수 있다. 이렇기 떄문에
# 범위를 위와같이 설정해주었다.
