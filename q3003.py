#  임의의 말의 수에서 얼만큼의 수를 더해야 정해진 수가 되는가에서 얼만큼의 수를 출력하는 문제

chess = [1,1,2,2,2,8]

a = list(map(int,input().split()))

for b in range(6):
    print(chess[b] - a[b], end=' ')