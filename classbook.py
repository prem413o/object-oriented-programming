# Create a class to represent a book with attributes like  
 #title, author, and publication year

class book:

    def __init__(self,title,author,pyear):
        self.title=title
        self.author=author
        self.pyear=pyear


b1=book("ek tha tiger","prem",2014)
print(b1.author)
print(b1.pyear)
print(b1.title)

        