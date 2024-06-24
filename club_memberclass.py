# Welcome to the Springfield Library Book Club! How can I help you friend:

# 1. Become a member
# 2. Search for a member
# 3. Display full member list
# 4. Back to main menu             

members ={
        'Marge Simpson': {'User_id' : 4567891230, 'Rentals out': 0},
    'Crusty the Clown': {'User_id': 12345678990, 'Rentals out' : 0},
    'John Snow': {'User_id': 1548756512, 'Rentals out' : 0},
    'Ned Flanders': {'User_id': 156165000, 'Rentals out' : 0}
    }
class Member():


    def __init__(self, name, user_id, current_rentals):
        self.name = name
        self.__user_id = user_id
        self.current_rentals = current_rentals

    def get_info(self):
        print(f"{self.name} currently has the following books on rental:\n{self.current_rentals}")
        
    def get_name(self):
        return self.name
    def set_name(self, new_name):
        self.name = new_name

    def get_id(self):
        return self.__user_id
    def set_id(self, new_id):
        self.__user_id = new_id
    
    def get_rentals(self):
        return self.current_rentals
    def set_rentals(self, new_rental):
        self.current_rentals = new_rental

    # def search(self):
    #     members = input("Please enter the full name of the author you are searching for: \n").title()
    #     for 

    def print_members():
        print(members)

    def add_member():
        while True:
            add_name = input("Please enter the name of the person you would like to add:\n").title()
            add_id = input("Please enter your phone number with no spaces, dashes or parenthesis:\n")
            rentals = 0
            members[add_name] = {"User id": add_id, "Rentals out": 0}
            print(f"{add_name} has been added to the Springfield Library Club")
            return
                  

    def search_member():
        while True:
            member_name = input("Please enter the full name of the member you are searching for: \n").title()
            if member_name in members:
                print(members[member_name])
            else:
                print(f"{member_name} was not found in the system, please try again!")
                continue

            
        
    


