class LibraryBook:
    # O parâmetro self é OBRIGATÓRIO dentro da classe, 
    # porque ele diz ao programa para buscar/atuar sobre o objeto de instância
    # que a executou.
    
    def __init__(self, title, author, pub_year, call_no):
        self.title = title
        self.author = author
        self.pub_year = pub_year
        self.call_number = call_no
        self.checked_out = False

# Criando uma instância da classe LibraryBook
my_book = LibraryBook("Harry Potter and the Philosopher's Stone", ('Rowling', 'J.K.'), 1998, "PZ7.R79835")

# Verificando o tipo da instância
print(type(my_book))

# Acessando os atributos da instância
print(my_book.title)
print(my_book.author)
print(my_book.pub_year)
print(my_book.call_number)
print(my_book.checked_out)



