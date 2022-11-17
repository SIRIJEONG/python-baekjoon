# ox퀴즈

a = int(input())


for _ in range(a):
    n_list = list(input())
    score = 0
    sum = 0

    for i in n_list:
        if i == 'O':
            score += 1
            sum = sum + score
        else:
            score = 0
    print(sum)

