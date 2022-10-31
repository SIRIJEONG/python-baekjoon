# n 이 주어졌을때 1부터 n의 합을 구하는 프로그램

n = int(input())
a = 0

for i in range(1,n+1):
    a = a + i
print(a)