lista1 = [1,2,3,4,5,6,7]
lista2 = [1,2,3,8,9,10]
listafinal = []
func = [lista1.append(i) for i in lista2 if i not in lista1]
print(lista1)