# numstat2.py

# Read integer numbers from a file and determine the
# sum, count, average, maximum, minimum,range,median and mode.
# Each number is an a separate line in the file.

# This solution uses lists. 


# Loop the program
while (True):
    
    # Initialize variables
    number_sum = 0
    number_count = 0
    number_average = 0
    number_maximum = 0
    number_minimum = 0
    number_range = 0

    try:
        # Ask the user for a file of random numbers
        number_file_name = input("Enter the name of the file you would like to process: ")

        # Open the file
        number_file = open(number_file_name, "r")

        # Use a variable to indicate when the first line of the file is being read
        is_first_number = True

        # For each line in the file
        for number in number_file:
            # Convert the line to an integer
            number = int(number)

            # If this is the first number in the file...
            if (is_first_number):
                # We'll say it is both the max and the min
                number_maximum = number
                number_minimum = number
                # Turn is_first_number flag to False so this doesn't happen again
                is_first_number = False


            # Add the number to the running sum
            number_sum += number

            # Count the number
            number_count += 1

            # Determine if it is greater than the max
            if (number > number_maximum):
                number_maximum = number
            # Determine if it is lesser than the min
            if (number < number_minimum):
                number_minimum = number


        # Calculate the average
        number_average = number_sum / number_count
        # Calculate the range
        number_range = number_maximum - number_minimum

        # Close the file
        number_file.close()

    # If there's a problem reading the file, print an error
    except Exception as err:
        print ('An error occurred reading', number_file_name)
        print ('The error is', err)

    # If the file was read successfully...
    else:
        # Print the calculated statistics
        print("File name:", number_file_name)
        print("Sum:", number_sum)
        print("Count:", number_count)
        print("Average:", number_average)
        print("Maximum:", number_maximum)
        print("Minimum:", number_minimum)
        print("Range:", number_range)

        number_file = open(number_file_name, "r")
        list1=number_file.readlines()
        number_file.close

        index=0
        while index<len(list1):
            list1[index]=int(list1[index].strip('\n'))
            index+=1
        list1.sort()
        length=len(list1)
        if length%2==1:
            median=list1[int(length/2)]
            print('Median: ',median)
        if length%2==0:
            mid1=list1[int(length/2)]
            mid2=list1[int(length/2-1)]
            median=float((mid1+mid2)/2)
            print('Median: ',median)

        dictionary={} #dictionary created to store key value pair 
        for values in list1: #going through list of numbers in list1
            if values in dictionary:
                dictionary[values]+=1 #if number is present in dictionary, bump the counter+1(repeated occurance)
            else:
                dictionary[values]=1 #else let the counter be equal to 1 (first occurance)

        #end of for loop which goes through each number in the list1 and also checks how many times it is present in dictionary

        maxList=[0] #another list to hold the list of all numbers which repeat the maximum number of times.In other words, it contains the MODES. 
        max_val=0 #The value(or number of times )a number in list1 repeats
        for values in dictionary:       #check for each number is dictionary
            if dictionary[values]>max_val:
                max_val=dictionary[values]  #will check and assign the number of times a number occurs, to max_val
                while len(maxList)!=0: #if the list maxList is empty, then pop/remove the zero and add the value of current max_val to the maxList
                    maxList.pop()       #remove the old value from maxList
                maxList.append(values) #add the new value into the maxList

            elif dictionary[values]==max_val: #if there is another number which is present same number of times as the current one(as of now 476 is present,then,later,as 660 is also repeated twice) even it gets added to the maxList.
                max_val=dictionary[values]
                maxList.append(values)  #append is to add a new element to the list maxList
                
        print('Mode: ',maxList)     #maxList conatins the list of numbers which repeat the most, in other words MODE.
        # Ask to try again
        calculate_again = input("Would you like to evaluate another file? (y/n) ")
        if (calculate_again != "y"):
            break


