integers = input()
integer_list = integers.split()

for i in range(len(integer_list)):
    integer_list[i] = int(integer_list[i])

integer_list = list(filter(lambda x: x >= 0, integer_list))
integer_list.sort()
num = 0
for num in range(len(integer_list)):
    if (integer_list[num] >= -1):
        print(integer_list[num], end=' ')