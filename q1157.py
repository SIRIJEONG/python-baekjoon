# 단어공부

n = input().upper()
n_list = list(set(n))

a = []

for i in n_list:
    b = n.count
    a.append(b(i))

if a.count(max(a)) > 1:
    print("?")
else:
    print(n_list[(a.index(max(a)))])