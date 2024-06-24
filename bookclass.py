# Welcome to the Book Encyclopedia, what would you like to do:

# 1. Add a new book
# 2. Borrow/Rent a book
# 3. Return a book
# 4. Search the Encyclopedia 
# 5. Display the Encyclopedia
# 6. Back to main menu

Book_list = {
'Dune': {"author" : 'Frank Herbert', "Genre": 'Science Fiction', "Summary" : 'The battle for spice is on and there can only be one victor in charge of the spice fields', "Available" : True},
'The Hobbit': {"author" :  'JRR Tolkien', 'Genre' : 'Fantasy', 'Summary' : 'A group of friend must travel through Middle Earth to defeat a dragon and save the Dwarven Homeland','Available': True},
'Saxaphonie': {"author": 'Lisa Simpson', 'Genre': 'Romance', 'Summary' : 'A women falls in love wiht an Orchestrator that has a hidden past that slow becomes revieled', 'Available' : True}                
    }

class Book():
    

    def __init__(self, title, author, genre, summary, availability):
        self.title = title
        self.author = author
        self.genre = genre
        self.summary = summary 
        self.availability = availability

    def book_search():
        while True:
            book = input("Please enter the full name of the Book you are searching for: \n").title()
            if book in Book_list:
                print(Book_list[book])
            else:
                print(f'{book} was not found in the Encyclopedia, please try again')
           
    def change_rental(self):
        while True:
            book_search = input(" Please enter the full name of the book you are searching for: ").title()
    
    def add_book():
        while True:
            add_title = input("Please enter the title of the book you would like to add: \n").title()
            add_author = input("Please enter the name of the Author:\n").title()
            add_genre = input("What genre would you put this under: \n").title()
            add_summary = input('Give us a short summary of the book: \n')
            Book_list[add_title] = {'author': add_author, "Genre" : add_genre, "Summary" : add_summary}
            print(f"{add_title} by {add_author} has been added to the Encyclopedia")
            return

    def print_books():
        print(Book_list)            
                
    def get_title(self):
        return self.title
    def set_title(self, new_title):
        self.title = new_title

    def get_author(self):
        return self.author
    def set_author(self, new_author):
        self.author = new_author

    def get_genre(self):
        return self.genre
    def set_gerne(self, new_genre):
        self.genre = new_genre

    def get_summary(self):
        return self.summary
    def set_summary(self, new_summary):
        self.summary = new_summary

    def get_availability(self):
        return self.availability
    def set_availability(self, New_avail):
        self.availability = New_avail

    # def borrowed(self):
    #     while True:
    #         rental = input("Please enter the title of the book you are looking to rent: \n")
    #         for rent in rental:
    #             if rental in self.title: