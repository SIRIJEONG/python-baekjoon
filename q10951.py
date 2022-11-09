# a+b-4

while True:
    try:
        a,b = map(int, input().split())
    except:
        break
    print(a + b)

# 변수 a,b에 입력이 없으면 에러가 나게 된다 그렇기 때문에 try=except구문을 써야한다
# try=except는 에러가 발생할 가능성이 있는 코드를 처리할수있는 코드이다.
# try: 변수 a,b에 int형이 들어가면 a+b를 출력하고  except: try에 대한 에러가 발생한 경우 while문을 멈춘다.
