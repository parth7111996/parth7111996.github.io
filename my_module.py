class Person:
    def __init__(self,initialAge):
        self.initialAge = age
        if self.initialAge < 0:
            print("Age is not valid, setting age to 0.")
            self.initialAge = 0
    def amIOld(self):
        if self.initialAge < 13:
            print("You are young.")
        elif self.initialAge < 18 and self.initialAge >= 13:
            print("You are a teenager.")
        else:
            print("You are old.")
    def yearPasses(self):
        self.initialAge = self.initialAge+1
        # Increment the age of the person in here