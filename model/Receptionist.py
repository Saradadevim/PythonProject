class Receptionist:
    def __init__(self, name):
        self.name = name  # Example attribute

    def print_message(self):
        print(f"Hello, welcome to the clinic! My name is {self.name}. How can I assist you?")
RecepPage=Receptionist()
RecepPage.print_message()