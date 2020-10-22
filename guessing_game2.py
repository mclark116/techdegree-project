import random

history = []

def welcome():
    print(
    """
    ____________________________________
    Welcome to the Number Guessing Game!
    ____________________________________
    """)
    
#have game stop adding up tries with each new game
#have game pick new number for each new game instead of keeping the old one


def start_game():
    another = "y"
    solution = random.randint(1,10)
    value = "Oh no! That's not a valid value. Please chose a number between 1 and 10."
    attempt = 0
    while another == "y":
        try:
            prompt = int(input("Pick a number between 1 and 10: "))
        except ValueError:
            print(value)
        else: 
            if prompt > solution:
                if prompt > 10:
                    print(value)
                else:
                    print("It's lower!")
                    attempt +=1
        
            elif prompt < solution:
                if prompt < 1:
                    print(value)
                else:     
                    print("It's higher!")
                    attempt +=1
        
            elif prompt == solution:
                attempt +=1
                if attempt == 1:
                    print("\nGot it! It took you {} try!".format(attempt))
                else:
                    print("\nGot it! It took you {} tries!".format(attempt))
                    print("Game Over!")
                    history.append(attempt)
                    solution = random.randint(1,10)
                    attempt = 0
                    another = input("Would you like to play again? y/n ")
                    if another.lower()=="y":
                        print("\nHigh Score: {}".format(min(history)))
                    elif another.lower()!="y":
                        if another.lower()=="n":
                            print("\nGame Over! Thanks for playing.")
                            break
                        else:
                            while another.lower !="y" or "n":
                                print("Please choose y or n")
                                another = input("Would you like to play again? y/n ")  
                                if another.lower()=="y":
                                    print("\nHigh Score: {}".format(min(history)))
                                    break
                                elif another.lower()!="y":
                                    if another.lower()=="n":
                                        break
welcome()
start_game()