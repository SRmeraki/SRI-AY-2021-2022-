 #########################  LIBRARY  #############################################

class Library:
    def __init__(self,list_of_books,lib_name):
        self.list_of_books = list_of_books
        self.lib_name = lib_name

    def display(self):
        print('The Library contains Following Books: \n {0} \n'  
              '{1}'.format(self.lib_name,self.list_of_books))


    # def add_book(self):






book_stock = {'the fault in our starts':'Shailene Woodly','Alice in the Wonderland':'Alice',
                              'The Shiva Triology':'Amish Tripathy','The Shiv Katha':'Swescha Rambal'}          # this is a dictionary that shows library
Harry_lib = Library(book_stock,'Swescha\'s Library')

Harry_lib.display()