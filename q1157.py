# 단어공부

n = input().upper()
n.list = list(set(n))

a = []

for i in n.list:
    b = n.count()
    a.append(b(i))

if a.count(max(a)) > 1:
    print("?")
else:
    print(n.list[(a.index(max(a)))])