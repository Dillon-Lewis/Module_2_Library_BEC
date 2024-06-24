# Welcome to our Signature author list! What can I do for you:

# 1. Add a new author
# 2. Search for an author
# 3. Display full author list
# 4. Back to main menu    

author_list = {
'Lisa Simpson': {'Birthdate' : '4/19/1987', "Short Bio" : 'Avid author and saxaphone player, she has devoted her later years into writing fictional love stories'},
'JJR Tolkien': { "Birthdate ": '1/3/1892', "Short Bio" : 'English writer famously known for his fantasy works like the Hobbit and LOTR',}, 
'Frank Herbert': {"Birthdate": '11/8/1920', "Short Bio" : " American sci-fi writer with a rich history in short stories and newspaper articles"}
}
  

class Author():
    def __init__(self, name, birth_date, short_bio):
        self.name = name
        self.birth_date = birth_date
        self.short_bio = short_bio

    def set_name(self, new_name):
        self.name =  new_name
    
    def set_birth_date(self, birth):
        self.birth_date = birth
    
    def set_short_bio(self,new_bio):
        self.short_bio = new_bio

    def display_author_list():
        print(author_list)

    def add_author():
        add_name = input('Please enter the full name of the Author you would like to add:\n').title()
        add_birthday = input("Please enter the birth date of said author: __/__/__ \n")
        bio = input("A few short words about the person: \n")
        author_list[add_name] = {'Birthdate' : add_birthday, "Short Bio" : bio}
        print(f"{add_name} has successfully been added to the author lsit")
        return
    
    def author_search():
        while True:
            author_search = input("Please enter the full name of the author you are searching for: \n").title()
            if author_search in author_list:
                print(author_list[author_search])
            else:
                print(f"{author_search} was not found in the system, please try again!")
                continue
            

