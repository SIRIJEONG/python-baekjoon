# 평균은 넘겠지

c = int(input())


for _ in range(c):
    n = list(map(int, input().split()))
    a = sum(n[1:])/n[0]

    b = 0
    for i in n[1:]:
        if i > a:
            b += 1

    d = (b/n[0])*100
    print('%.3f'%d + '%')