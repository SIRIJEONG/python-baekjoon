# 블랙잭

n , m = map(int, input().split())
a_list = list(map(int, input().split()))
b_list = []

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            c = a_list[i]+a_list[j]+a_list[k]
            if c > m:
                continue
            else:
                b_list.append(c)
print(max(b_list))

