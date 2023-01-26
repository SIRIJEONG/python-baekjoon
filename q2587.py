# 대표값


n_list = []
for i in range(5):
    n_list.append(int(input()))

n_list.sort()
print(int((n_list[0]+n_list[1]+n_list[2]+n_list[3]+n_list[4])/5))
print(n_list[2])