def switcher(number):

    return{
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }.get(number, "Invalid month") #O .get() é um método que retorna o valor da chave especificada, caso não exista, retorna o valor padrão

number = int(input("Entre com um número de 1 a 12: ")) # o 'int'' converte a string em número inteiro para poder ser comparado
if(number >= 1 or number <= 12): #Se o número digitado for maior ou igual a 1 e menor ou igual a 12 ele entra no bloco
    print(switcher(number)) #O método switcher() é chamado e passa o número digitado pelo usuário
else:
    print("Número inválido")