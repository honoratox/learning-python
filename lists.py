list2=['hello', 'hola', 'olá']

print("Primeiro elemento da lista: ", list2[0])
print("Segundo elemento da lista: ", list2[1])

list2.insert(2, 'hallo') # usa o '.insert' pra adicionar um elemento na posição x
print(list2[2])

list2.append('bye') # usa o '.append' pra adicionar um elemento no final da lista
print(list2)

list2.remove('hello') # usa o '.remove' pra remover um elemento da lista
print(list2)

list2.sort() # usa o '.sort' pra ordenar a lista em ordem alfabética
print(list2)

print("-----------------------------------------------------------------")

lists = [] # cria uma lista vazia, nesse caso uma lista de listas
lists.append([1, 2, 3])
lists.append(['a', 'b', 'c'])
print(lists)
print(lists[1])