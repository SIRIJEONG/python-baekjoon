# 나머지

n_list = []

for i in range(10):
    a = int(input())
    n_list.append(a%42)
    
n_list = set(n_list)
print(len(n_list))

#set함수는 중복을 제거하는 필터역할을 하는 함수