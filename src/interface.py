class Interface:
    def __init__(self, db_table):
        self.db_table = db_table
        self.selections = {'1': self.create_book, '2': self.find_book,
                           '3': self.update_book, '4': self.delete_book,
                           '5': self.quit
                          }

    def greet(self):
        """ Greets the user with a welcoming message """
        print("------------------------------")
        print("Welcome To Book List!")
        print("------------------------------")
        print('\n')

    def menu(self):
        """ Display a menu for the user to choose from """
        self.greet()

        print("1) New Book")
        print("2) Find Book")
        print("3) Update Book")
        print("4) Delete Book")
        print("5) Quit")

    def get_selection(self):
        """ Gets the selection from the user """
        select = input("Make Selection: ")
        self.selections[select]()

    def main(self):
        """ Main function that runs the interface logic """
        self.menu()
        self.get_selection()