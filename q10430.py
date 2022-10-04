#  세 수 A, B, C가 주어졌을 때 첫째 줄에 (A+B)%C, 둘째 줄에 ((A%C) + (B%C))%C, 셋째 줄에 (A×B)%C, 넷째 줄에 ((A%C) × (B%C))%C를 출력한다.

a,b,c = input().split()

d = int(a)
e = int(b)
f = int(c)

print((d+e)%f)
print(((d%f)+(e%f))%f)
print((d*e)%f)
print(((d%f)*(e%f))%f)



