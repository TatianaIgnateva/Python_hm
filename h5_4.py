from functools import reduce
#1
print(reduce(lambda a, b: a * b, [i for i in range(100, 1001, 2)]))

#2
my_list = [el for el in range(100, 1001, 2)]
print(my_list)

def func(prev_el, el):
    return prev_el * el
print(reduce(func, my_list))
