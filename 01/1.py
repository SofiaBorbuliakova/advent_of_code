x = open('1.txt', 'r').readlines()
print(x)
numbers = []
new_list = [[value] for value in x]
print(new_list)
for i in new_list:
    print(i)
    only_number = []
    for j in i[0]:
        if j.isdigit():
            only_number.append(j)
    print(only_number)
    if only_number:
        combined_number = only_number[0] + only_number[-1]
        numbers.append(int(combined_number))

print(numbers)
sucet = sum(numbers)
print(sucet)
