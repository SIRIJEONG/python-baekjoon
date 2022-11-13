# 과제안내신분!

n_list = [i for i in range(1,31)]

for _ in range(28):
    a = int(input())
    n_list.remove(a)

print(min(n_list))
print(max(n_list))