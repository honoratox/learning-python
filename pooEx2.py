class LibraryBook:
    # O parâmetro self é OBRIGATÓRIO dentro da classe, 
    # porque ele diz ao programa para buscar/atuar sobre o objeto de instância
    # que a executou.
    
    def __init__(self, title, author, pub_year, call_no):
        self.title = title
        self.author = author
        self.pub_year = pub_year
        self.call_number = call_no

    def title_and_author(self):
        return "{} {} {}".format(self.author[1], self.author[0], self.title) # Retorna o nome do autor, depois o título
    def __str__(self):
        return "{} {} ({}): {}".format(self.author[1], self.author[0], self.pub_year, self.title) # Retorna o nome do autor, depois o título e o ano de publicação
        return "<Book: {} ({})>".format(self.title, self.call_number) # Retorna o título e o número de chamada
    
new_book = LibraryBook("Harry Potter and the Sorcerer's Stone", ("Rowling","J.K."), 1998, "PZ7.R79835") # Cria um novo objeto de instância da classe LibraryBook
print(new_book)