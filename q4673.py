#셀프넘버

number_list = list(range(1,10001))
remove_list = []
for i in number_list :
    for n in str(i):
        i += int(n)
    if i <= 10000:
        remove_list.append(i)

for a in set(remove_list):
    number_list.remove(a)
for b in number_list :
    print(b)