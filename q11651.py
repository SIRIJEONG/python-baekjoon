# 수 정렬하기 2

import sys
input = sys.stdin.readline

n = int(input())

n_list = []
for i in range(n):
    a,b = map(int, input().split())
    n_list.append([b,a])

n_n_list = sorted(n_list)

for b,a in n_n_list:
    print(a,b)