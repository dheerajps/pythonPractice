import Zoo
import animal

another = 'y'
z = Zoo.Zoo()
while another == 'y':
    print('Zoo Options')
    print('-----------')
    print('1. Add Animal')
    print('2. Show Animals')
    print('3. Exit')
    while(True):
        try:
            choice = int(input('What would you like to do? '))
    #"""
            if choice == 1:
                species = input('What type of animal would you like to create? ')
                name = input('What is the animal\'s name? ')
                obj = animal.Animal(species, name)
                z.add_animal(obj)
                another = 'y'
                exit
    #"""
            elif choice == 2:
                z.show_animals()
                another = 'y'
                exit

    
            elif choice == 3:
                print('Thank you for visiting the zoo!')
                another = 'n'
                exit

            elif (choice <1 or choice >3):
                print('Please select a valid option ')
                continue
        except ValueError:
            print(' Please enter a numeric value ')
            continue
        else:
            break
