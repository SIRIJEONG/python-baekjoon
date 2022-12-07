# 전화 다이얼

a = input().upper()
d = ["ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]
time = 0
for i in range(len(a)):
    for j in d:
        if a[i] in j:
            time += d.index(j) + 3
print(time)