# 소수

m = int(input())
n = int(input())
n_list = []
for i in range(m,n+1):
    if i == 1:
        pass
    elif i == 2:
        n_list.append(i)
    else:
        for j in range(2,j):
            if i%j == 0:
                break
            elif j == i-1:
                n_list.append(i)
if len(n_list)==0:
    print(-1)
else:
    print(sum(n_list))
    print(min(n_list))

