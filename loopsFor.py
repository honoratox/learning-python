for i in range(10):
    print(i) #O método range() gera uma sequência de números, neste caso, de 0 a 9

print("-------------------")

#tudo além de 'i' gera o mesmo resultado em todas as repetições
for i in range(2, 10):
    print(i) #O método range() gera uma sequência de números, neste caso, de 1 a 10

for x in range(2, 10):
    print(i) #Nesse x é impresso o último valor de i, que é 9

print("----------------------------------------------------------------")

print("FOR-EACH")
for i in "hello":
    print(i) #O método for-each percorre cada caractere da string e printa

print("-------------------")

string = "hakuna matata"
for i in range (len(string)):
    print(string[i]) #O método len() retorna o tamanho da string printando os caracteres, neste caso, 13

print("-------------------")

string = "hakuna matata"
for i in range (len(string)):
    print("Caractere na", i,"º posição: ", string[i])