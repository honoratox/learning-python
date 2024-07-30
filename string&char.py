class palavraCarac:
    print("Hello" * 5) # O '*' é o simbolo de repetição, ou seja, Hello 5 vezes
    print('x' *3) 

    """class teste:
    print(x * 3) Dá erro, pois x é lido como variável e não como string"""

    #print("hello " + 5) Dá erro, pois não é possível concatenar string com int, o certo seria abaixo
    print("hello " + str(5)) # O str() converte o número em string