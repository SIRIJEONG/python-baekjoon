#베르트랑 공준

import math

m = 123456

arr1 = [True for _ in range(2 * m + 1)]
arr1[0], arr1[1] = False, False

for i in range(2, int(math.sqrt(2*m) + 1)):
    if arr1[i]:
        j = 2
        while i * j <= 2*m:
            arr1[i * j] = False
            j += 1

while True:
    n = int(input())
    if n == 0:
        break

    cnt = 0

    for i in range(n+1, 2*n+1):
        if arr1[i]:
            cnt += 1
    print(cnt)