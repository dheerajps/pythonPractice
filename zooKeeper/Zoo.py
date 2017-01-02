import animal
class Zoo:
    def __init__(self):
        self.__animals =[]
    def add_animal(self,ani):
        self.__animals.append(ani)
    def show_animals(self):
        size = len(self.__animals)
        if size == 0:
            print('There are no animals in your zoo!')
        else:    
            print('Animal List')
            print('-----------')
            for count in self.__animals:
                print(count.get_name(), 'the', count.get_animal_type(), 'is', count.check_mood())
                print()
