class Person:
    
    def __init__(self, name):
        self.name = name
        
        
    def talk(self):
        print("Talking..")
    
    def meeting(self):
        print(f"My name's {self.name}" )
        
    def greetings(self):
        print("Hi !!")

Anna = Person("Ania")
Anna.greetings()
Anna.meeting()
Anna.talk()
