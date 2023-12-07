#number2
#(i)
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")

# Creating an instance of the Book class
my_book = Book(title="How to become rich without working", author="Mahoro Kathy", pages=100)

# Displaying information about the book
my_book.display_info()




#(ii)
class Book:
    def __init__(self, title, pages, author):
        self.title = title
        self.pages = pages
        self.author = author

class EBook(Book):
    def __init__(self, title, pages, author, format_type):
        # Call the constructor of the base class (Book) using super()
        super().__init__(title, pages, author)
        self.format_type = format_type


# Creating an instance of the Book class
books = Book("Allah yeka", 200, "alfonso bukenya")

# Creating an instance of the EBook class
my_ebook = EBook("how to get rich without working", 100, "mahoro cathy","online")

# attributes of the Book class
print(f"Book Title: {books.title}")
print(f"Book Pages: {books.pages}")
print(f"Book Author: {books.author}")

# adding attribute formating
print(f"EBook Title: {my_ebook.title}")
print(f"EBook Pages: {my_ebook.pages}")
print(f"EBook Author: {my_ebook.author}")
print(f"EBook Format Type: {my_ebook.format_type}")




          #(iii)
class Book:
    def __init__(self, title, pages, author):
        self.title = title
        self.pages = pages
        self.author = author          
          
    def only_title_and_outhor(self):
        return(f"{self.title} book by {self.author}")
    

books = Book("how to get rich without working", 100, " mahoro kathy")

 # Calling the function to get title and author
title_and_author = books.only_title_and_outhor()
print(title_and_author)






#(iv)
#a class is a container that stores two or more variables.

#an object are variables that store information