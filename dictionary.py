dict = {} # cria um dicionário vazio

dict2 = {'a': 5, 'b': 10, 'c': 100, 'd' : 9.5} # cria um dicionário com 4 elementos
print(dict2['b']) # imprime o valor associado à chave 'b'

dict2['b'] = 50 # altera o valor associado à chave 'b'
print(dict2) 

dict2['z'] = 999
print(dict2) # adiciona um novo elemento ao dicionário

# adicionar elementos ao dicionário
dict["greeting"] = "Hello"
dict["alphabet"] = ['a', 'b', 'c', 'd', 'e']
dict["check-in"] = False
dict["phoneNumber"] = 80028922
print(dict) # adiciona 4 novos elementos ao dicionário

dict[('a', 'b', 'c')] = [False, True, False]
print(dict)