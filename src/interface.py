class Interface:
    def __init__(self):
        self.select = None

    def greet(self):
        print("------------------------------")
        print("Welcome To Book List!")
        print("------------------------------")
        print('\n')

    def set_selection(self, select):
        self.select = select

    def menu(self):
        self.greet()

        print("1) New Book")
        print("2) Find Book")
        print("3) Update Book")
        print("4) Delete Book")
        print("5) Quit")