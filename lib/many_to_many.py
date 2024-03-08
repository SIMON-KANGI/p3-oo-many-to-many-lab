from datetime import datetime

class Author:
    all = []

    def __init__(self, name):
        self.name = name
        self.contracts = []
        Author.all.append(self)

    def sign_contract(self, book, date, royalties=0):
        if not isinstance(book, Book):
            raise TypeError("Invalid type for book")
        if not isinstance(date,str):
            raise TypeError("Invalid type for date")
        if not isinstance(royalties, int):
            raise TypeError("Invalid type for royalties")
        
        contract = Contract(book, self, date, royalties)
        self.contracts.append(contract)
        book.sign_contract(contract)

       

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts)

    def contracts(self):
        return self.contracts
    def books(self):
        return [contract.book for contract in self.contracts]
class Book:
    all = []

    def __init__(self, title):
        self.title = title
        self.contracts = []
        Book.all.append(self)
        self.books=[]
    
    def books(self,books):
        return [book for book in books]
        
    
    def contracts(self):
        return self.contracts

    def authors(self):
        return [contract.author for contract in self.contracts] 
    
        
class Contract:
    all = []

    def __init__(self, book, author, date, royalties=0):
       
        self.book = book
        self.author = author
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)
        self.contracts_by_date()
        
    @classmethod
    def contracts_by_date(cls):
        return sorted(cls.all)
    
    def typeAuthor(self,author):
        if not isinstance(author,Author):
           raise TypeError("Invalid type")
    
    def typeBook(self,book):
        if not isinstance(book,Book):
           raise TypeError("Invalid type")
            
    def typeDate(self,date):
        if not isinstance(date,str):
           raise TypeError("Invalid type")
    def typeRoyalties(self,royalties):
        if not isinstance(royalties,int):
           raise TypeError("Invalid type")
    
    
    