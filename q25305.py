#커트라인

n , k = map(int, input().split())
a_list = list(map(int, input().split()))

a_list.sort()
a_list.reverse()
print(a_list[k-1])

