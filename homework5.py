immutable_var = "дом", 15, 5.84, True, [13, 28, 56]
print(immutable_var)
#immutable_var[0] = "крыша"
#print(immutable_var)
# TypeError: 'tuple' object does not support item assignment
mutable_list = [4, 15, 'собака', 'кошка', False]
print(mutable_list)
mutable_list[1] = 48
mutable_list[3] = True
mutable_list[4] = "пицца"
print(mutable_list)