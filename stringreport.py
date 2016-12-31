my=input('Enter the string : ')
leng=len(my)
print(' The length is : ',leng)
print(' The first character is :  ',my[0])
print(' The last character is :  ',my[leng-1])
if 'open' in my or 'OPEN' in my or 'Open' in my:
    print(' Open is present in the string ')
else:
    print(' Open is not present in the string ')

if ' ' in my:
    my1=my.replace(" ","")
    if my1.isalpha():
        print(' contains alphabets and whitespaces only : True')
    else:
        print(' contains alphabets and whitespaces only : False')
else:
    print(' contains alphabets and whitespaces only : False')
    
if my.isdigit():
    print(' The string contains only digits')
else:
    print('The string doesnt contain only digits')
if my.islower():
    print('All characters are in lower case')
else:
    print('All characters are not in lower case ')

if my.isupper():
    print('All characters are in Upper case')
else:
    print('All characters are not in Upper case ')
    
