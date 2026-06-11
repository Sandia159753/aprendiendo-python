### Tuples ###

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (22, 1.70, "Sai", "Vargas","Sai")
my_other_tuple = (35, 60, 30) 

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[4]) IndexError
#print(my_tuple[-6]) IndexError

print(my_tuple.count("Sai"))
print(my_tuple.index("Vargas"))
print(my_tuple.index("Sai"))


my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "Sai"
my_tuple.insert(1, "Azul")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

del my_tuple
print(my_tuple)