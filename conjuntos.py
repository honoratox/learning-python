newSet = set() # Cria um conjunto vazio
print(newSet)

ex1 = {1, 2, 2, 1, 1} # Cria um conjunto com elementos, ignorando duplicatas
print("Ex1 inicial: ", ex1)

ex2 = {j for j in range (10)} # Cria um conjunto com elementos de 10 termos - 0 a 9
print("Ex2 inicial: ", ex2)

ex2.add(2) # Adiciona um elemento ao conjunto
ex2.add(100) # Adiciona um elemento ao conjunto
ex2.add(50) # Adiciona um elemento ao conjunto
print("Ex2 pós adição de termos: ", ex2)

"""d_set = {[1,2,3]}
print(d_set) # Erro, pois não é possível criar um conjunto com listas"""
ages = [10, 5, 4, 5, 2, 1, 5]
set_of_ages = set(ages) # a função set() cria um conjunto a partir de uma lista, ignorando duplicatas
print("Conjunto a partir da lista: ", set_of_ages)

list_of_ages = list(set_of_ages) # a função list() cria uma lista a partir de um conjunto
print("Lista a partir do conjunto: ", list_of_ages)