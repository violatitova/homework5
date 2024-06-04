immutable_var = 1, 'course', 8, 5.5
print(immutable_var)
immutable_var[0] = 2
print(immutable_var[0]) # кортеж не поддерживает обращение по элементам

mutable_list = [2, 5, 'list', 6.3]
print(mutable_list)
mutable_list[1] = 8
print(mutable_list[1])




