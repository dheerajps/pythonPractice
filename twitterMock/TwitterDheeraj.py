import TweetDheeraj
import pickle

twitter_file_name= "tweets.dat"
try:
    tweet_read=open(twitter_file_name, "rb")
    tweet_list=pickle.load(tweet_read)
    tweet_read.close()
except:
    tweet_list=[]
    
another = 'y'
while another == 'y':
    print('Tweet Menu')
    print('----------')
    print('1. Make a Tweet')
    print('2. View Recent Tweets')
    print('3. Search Tweets')
    print('4. Quit')

    while(True):

        try:
            print()
            choice = int(input('What would you like to do? '))

            if choice == 1:
                               
                name = input('What is your name? ')
                tweet = input('What would you like to tweet? ')
                length = len(tweet)
                while length > 140:
                    print('Tweets can only be 140 characters!')
                    print()
                    tweet = input('What would you like to tweet? ')
                    length = len(tweet)
                obj = TweetDheeraj.Tweet(name, tweet)
                tweet_list.append(obj)
                tweet_write=open(twitter_file_name,"wb")
                pickle.dump(tweet_list,tweet_write)
                tweet_write.close()
                print( name ,", your tweet has been saved.")
                another = 'y'
                exit

            elif choice == 2:
                print('Recent Tweets')
                print('-------------')

                if (len(tweet_list)<1):
                    print(" There are no recent tweets.")
                else:
                    reversed_tweet_list=reversed(tweet_list[-5:])

                    for count in reversed_tweet_list:
                        print(count.get_author(), "-", count.get_age())
                        print(" ", count.get_text())
                        print()
                        
                another = 'y'
                exit

            elif choice == 3:
                if(len(tweet_list)<1):
                    print(" There are no tweets to search. ")
                else:
                    search_key=input(" What would you like to search for? ")

                    print("\nSearch Results")
                    print("--------------")

        
                    reversed_list = reversed(tweet_list)
                    success = False


                    for tweet in reversed_list:
                        if (search_key in tweet.get_text()):
                            print(tweet.get_author(), "-", tweet.get_age())
                            print(" ", tweet.get_text())
                            success= True

                    if (not success):
                        print("No tweets contained", search_key) 

                another = 'y'
                exit

            elif choice == 4:
                print('Thank you for using the Tweet Manager!')
                another = 'n'
                exit

            elif (choice<1) or (choice>4):
                print('Please select a valid option.')
                continue

        except ValueError:
            print('Please enter a numeric value.')
        else:
            break
                
                

                    
                         
