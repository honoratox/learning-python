def main():
    a = input("Digite o valor do primeiro lado do triângulo: ")
    b = input("Digite o valor do segundo lado do triângulo: ")
    c = input("Digite o valor do terceiro lado do triângulo: ")

    return trianguloRetangulo (int(a), int(b), int(c)) #O método trianguloRetangulo() é chamado e passa os valores digitados pelo usuário convertidos em inteiros

def trianguloRetangulo(a, b, c):
    if(a>b>c or a>c>b):
        if(a**2 == b**2 + c**2):
            return "Triângulo Retângulo"
    elif(b>c>a or b>a>c):
        if(b**2 == a**2 + c**2):
            return "Triângulo Retângulo"
    elif(c>a>b or c>b>a): 
        if(c**2 == a**2 + b**2):
            return "Triângulo Retângulo"
    else:
        return "Não é um triângulo retângulo"
    
print(main()) #O método main() é chamado e printa o resultado

print("----------------------------------------------------------------")

import string
def main():
    cadeiaCarac = input("Digite uma cadeia de caracteres: ")

    return palindromo(cadeiaCarac) #O método palindromo() é chamado e passa a cadeia de caracteres digitada pelo usuário


def palindromo(str):

    exclude = set(string.punctuation) #O método set() cria um objeto set, que é uma coleção desordenada de itens, neste caso, de pontuações
    str = ''.join(ch for ch in str if ch not in exclude) #O método join() junta todos os itens de em uma string. 'ch' for 'ch' in str: Esta é a parte que define a iteração. Significa para cada caractere 'ch' em str, e if 'ch' not in 'exclude' é uma condição que verifica se o caractere 'ch' não está na string exclude
    str = str.replace(" ", "") #O método replace() substitui uma string por outra, neste caso, substitui o espaço em branco por nada

    if(str[::] == str[::-1]): #Se a string for igual a ela mesma invertida, ele retorna que é um palíndromo/ o str[::-1] inverte a string já que '::' é um operador de fatiamento faz percorrer do incio ao final da string e o '-1' faz percorrer de trás pra frente
        return "É um palíndromo"
    else:
        return "Não é um palíndromo"
    
print(main()) #O método main() é chamado e printa o resultado