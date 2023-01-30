# 통계학

import sys
input = sys.stdin.readline

n = int(input())
n_list = []
for i in range(n):
    n_list.append(int(input()))

n_list.sort()
print(round(sum(n_list)/n)) # 산술평균
print(n_list[(n-1)//2])

a = {}
for i in range(n):
    if n_list[i] not in a.keys():
        a[n_list[i]] = 1
    else:
        a[n_list[i]] += 1
a = sorted(a.item(), key = lambda x : (-x[1], x[0]))
for i in range(len(a)):
    a[i] = list(a[i])
if len(a) == 1 or a[0][1] != a[1][1]:
    print(a[0][0])
else:
    print(a[1][0])

print(max(n_list)-min(n_list))