count = 0
while(count < 10):
    print(count)
    count += 1 #O '+=' é um operador de atribuição que adiciona o valor do operando direito ao operando esquerdo e atribui o resultado ao operando esquerdo
print("----------------------------------------------------------------")


"""while True:
    user = input("Digite algpo pra continuar e 'q' para sair: ")
    if user == 'q':
        if(input("Deseja mesmo sair? S ou N").lower() == 's'): #O método lower() converte a string em minúsculo, ou seja, se o usuário digitar 'S' ou 's', o resultado será 's'
            print("Saindo...")
            break #O 'break' é um comando que encerra o loop
        else:
            print("Continuando...")
    print(user)"""

count = 1
while (count + 1 <=20):
    if(count%5==0): #Se o resto da divisão de count por 5 for 0, ele pula a
        print("SKIP")
        count +=1
        continue #O 'continue' é um comando que pula a iteração atual do loop
    print(count)
    count +=1
print("----------------------------------------------------------------")


for i in range (1,20):
    if i%5==0:
        print("SKIP")
        continue
    print(i)