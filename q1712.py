# 손익 분기점

a,b,c = map(int,input().split())
#a는 매년 고정비용 b는 노트북 한대의 재료비 인건비 c는 노트북 가격
# 총수입이 총비용보다 많아지게 되는 손익분기점을 구하는 프로그램


if b >= c:
    print(-1)
else:
    print(int(a/(c-b)+1))
