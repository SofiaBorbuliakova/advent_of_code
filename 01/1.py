x = open('1.txt', 'r').readlines()
print(x)
cisla = []
new_list = [[hodnota] for hodnota in x]
print(new_list)
for i in new_list:
    print(i)
    neviem = []
    for j in i[0]:
        if j.isdigit():
            neviem.append(j)
    print(neviem)
    if neviem:
        combined_number = neviem[0] + neviem[-1]
        cisla.append(int(combined_number))

print(cisla)
sucet = sum(cisla)
print(sucet)







