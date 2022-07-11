data_list = [12, 1, 1, 3, 3, 7, 7, 9, 12, 56]
my_list = [el for el in data_list if data_list.count(el) == 1]
print(my_list)
