class Author:
    all = []

    def __init__(self, name):
        self.name = name
        self._contract = []
        self. _books = []
        Author.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
     
    def books(self):
        return [book for book in self._books]

    def sign_contract(self, book, date, royalties):
         if isinstance(book, Book) and isinstance(date, str) and isinstance(royalties, int):
            contract = Contract(self, book, date, royalties)   
            self._contract.append(contract)
            self._books.append(book) 
            return contract
         else:
            raise Exception("invalid input")
         
    def contracts(self):
        pass
    def total_royalties(self):
         return sum(contract.royalties for contract in self._contract)
     
         
class Book:
    all = []
    def __init__(self,title):
        self.title = title
        self._contract = []
        Book.all.append(self)

    @property
    def book(self):
        return self._book
        
    def books(self):
        return [book for book in Book.all if book.contract == self]

    def contracts(self):
       return [book.contract for book in self.books()]  
     
   

class Contract:
     all = []
     def __init__(self, author, book, date, royalties):
        self.author = author
        self.book =  book
        self.date = date
        self.royalties = royalties
        book._contract.append(self)
        author._contract.append(self)
        author._books.append(book)
        Contract.all.append(self)

    
     @classmethod
     def contracts_by_date(cls, date):
         return [contract for contract in cls.all if contract.date == date]

author = Author("Rick Warren")       


book = Book("Purpose Driven Life")

sign_contract1 = Contract( author, book, '2/4/2024', 20)