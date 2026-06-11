my_tuple = (1, 2, 3)
print(type(my_tuple))

my_tuple = list(my_tuple)
print(type(my_tuple))
my_tuple.insert(1, "HOLA")

my_tuple = tuple(my_tuple)
print(type(my_tuple))
print(my_tuple)