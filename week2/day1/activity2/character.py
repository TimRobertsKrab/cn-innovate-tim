
class Character():
    # initialise the constructor method
    def __init__(self, real_name,suphero_name):
        self.real_name = real_name.title()
        self.superhero_name = suphero_name

    # have a setter method for the power
    def set_power(self,power):
        self.power = power

    # have a getter method for the power
    def get_power(self):
        return self.power

    def set_weakness(self,weakness:str):
        self.weakness = weakness

    def get_weakness(self):
        return self.weakness

    def __str__(self):
        return f"{self.superhero_name}'s real name is {self.real_name}. Their power is {self.power}. Their weakness is {self.weakness}."

    