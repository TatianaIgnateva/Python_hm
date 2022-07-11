old_list = [300, 2, 12, 44, 1, 1, 4, 10, 123, 55, 200]

new_list = [old_list[el] for el in range(1, len(old_list)) if old_list[el] > old_list[el - 1]]
print(new_list)
