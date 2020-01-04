T = int(input())
list = []

for i in range(T):
    list.append(int(input()))

n = max(list)+1

count_list0 = [0]*n
count_list1 = [0]*n

count_list0[0] = 1
count_list1[0] = 0
count_list0[1] = 0
count_list1[1] = 1


for i in range(2, n):
    count_list0[i] = count_list0[i-1] + count_list0[i-2]
    count_list1[i] = count_list1[i-1] + count_list1[i-2]

for i in range(T):
    print(count_list0[list[i]], count_list1[list[i]])


