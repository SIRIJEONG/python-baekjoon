# 평균

n= int(input())
n_list = list(map(int, input().split()))
m = max(n_list)
sum = 0

for i in range(n):
    n_list[i]=n_list[i]/m*100
    sum += n_list[i]
print(sum/n)