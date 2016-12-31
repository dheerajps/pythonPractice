import animal #import the module where class Animal is stored
print(' Welcome to the animal generator! ')
print()
print(' This program creates Animal objects ')
print(' \n ')
again='y' #for looping and asking user multiple inputs
animal_list=[] #create an empty list to store each object
while again=='y': #go as long as user hits 'y'
    atype=input('What type of animal would you like to create? ')
    aname=input('What is the animal\'s name? ')
    an=animal.Animal(atype,aname) #create a new animal object in memory and assign it to the variable 'an'

    animal_list.append(an) #add the object to the list
    print('\n \n')
    again=input('Would you like to add more animals (y/n)? ') #ask user if he wants to repeat

print('\n ANIMAL LIST \n')
print(' ---------------- ')
for item in animal_list: #print each element(animal object in the list
    print(item.get_name(),' the ',item.get_animal_type(),' is ', item.check_mood())
    print()
#using the accessor methods to retrieve the attributes    
