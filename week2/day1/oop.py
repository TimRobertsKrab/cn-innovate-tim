class Person():
    def __init__(self,person_name,person_age,person_height):
        self.name = person_name
        self.age = person_age
        self.height = person_height

    def set_age(self,age):
        self.age = age

    def increment_age(self):
        self.age += 1
    
    def set_hair(self,hair):
        self.hair = hair
    
    def get_hair(self):
        print(self.hair)

    def __str__(self):
        return f"{self.name} {self.age} {self.height} {self.hair}"
    
