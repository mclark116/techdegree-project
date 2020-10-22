"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random

history = []

def start_game():
    print(
    """
    ____________________________________
    Welcome to the Number Guessing Game!
    ____________________________________
    """)
    solution = random.randint(1,10)
    
    print(solution)
    
    value = "Oh no! That's not a valid value. Please try again."
    
    attempt = 0
    
    while True:
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
                    value
                else:     
                    print("It's higher!")
                    attempt +=1
            
            elif prompt == solution:
                attempt +=1
                print("Got it!")
                if attempt == 1:
                    print("It took you {} try!".format(attempt))
                else:
                    print("It took you {} tries!".format(attempt))
                print("Game Over!")
                history.append(attempt)
                another = (input("Would you like to play again? y/n "))
                if another.lower()=="y":
                    print("High Score: {}".format(min(history)))
                    start_game()
                elif another.lower()!="y":
                    break
                    
               
       

start_game()