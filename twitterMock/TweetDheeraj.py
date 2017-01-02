import time
class Tweet:
    def __init__(self, author, text):
        self.__author = author
        self.__text = text
        self.__age = time.time()

    def get_author(self):
        return self.__author
    def get_text(self):
        return self.__text
    def get_age(self):
        present= time.time()
        s=present-self.__age
        h=s//3600
        m=s//60

        if (h>0):
            return str(int(h)) + "h"
        elif (m>0):
            return str(int(m)) + "m"
        else:
            return str(int(s)) + "s"
        
