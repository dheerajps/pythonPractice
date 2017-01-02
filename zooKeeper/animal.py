import random
class Animal:
    def __init__(self, animal_type, name):
        self.__animal_type = animal_type
        self.__name = name
        self.__mood = 'Happy'

        
    def get_animal_type(self):
        return self.__animal_type
    def get_name(self):
        return self.__name
    def check_mood(self):
        if random.randint(1,3) == 1:
            self.__mood = 'Happy'
        elif random.randint(1,3) == 2:
            self.__mood = 'Hungry'
        else:
            self.__mood = 'Sleepy'
        return self.__mood

    
