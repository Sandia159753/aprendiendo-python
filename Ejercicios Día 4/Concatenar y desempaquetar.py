lista_1 = [1, 2, 3]
lista_2 = [4, 5, 6]

lista_3 = lista_1 + lista_2
print(lista_3)

primero, segundo, tercero = lista_1
print(primero)
print(segundo)
print(tercero)

#Tambien podemos usar asteriscos

lista_1 = [10, 11, 12, 13, 14]
diez, *medio, final = lista_1
print(diez)
print(medio)
print(final)