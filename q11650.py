# 좌표 정렬하기
import sys
input = sys.stdin.readline

n = int(input())

n_list = []
for i in range(n):
    [a,b] = map(int, input().split())
    n_list.append([a,b])

n_n_list = sorted(n_list)

for i in range(n):
    print(n_n_list[i][0], n_n_list[i][1])