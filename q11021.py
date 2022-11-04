# a+b-7

t = int(input())


for i in range(1, t+1):
    a,b = map(int , input().split())
    print(f'Case #{i}: , {a+b}')
# f-string을 이용하여 문자열안에 {}를 입력하고 괄호안에 변수나 변수를 연산값으로 입력할수 있다.

t = int(input())

for i in range(1, t+1):
    a,b = map(int , input().split())
    print("Case #" + str(i)+':',a+b)
