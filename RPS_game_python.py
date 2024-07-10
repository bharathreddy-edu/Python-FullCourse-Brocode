# %%
import random

#variable declaration
choice_list = ["rock", "paper", "scissor"]
playmore_list = ["yes", "no", "n", "y"]
gamenumber = 0;



# %%

#methods

#Game introdution and rules
def intro():
    print("Welcome to Rock Paper Scrissors Game")
    print("Instructions: \n\t\tEnter a choice from below: \n\t\t\t1. Rock\n\t\t\t2. Paper\n\t\t\t3. Scrissor ")
    print("\n\t\tRock wins against scissors;\n\t\tpaper wins against rock;\n\t\tand scissors wins against paper.")

#computer choice using random
def computer_input(choice_list):
    comp_choice = random.choice(choice_list).lower()
    print(f"Computer Choice\tis:\t{comp_choice}")
    return comp_choice

#user input
def call_userinput():
    user_choice = input("Enter your choice \(Rock/Paper/Scrissor\)?: ").lower()
    if (user_choice not in choice_list):
        while(True):
            print("Please Enter Correct Choice")
            print(f"your choices are \n{choice_list}")
            user_choice = input("Enter your choice \(Rock/Paper/Scrissor\)?: ").lower()
            if(user_choice in choice_list):
                break
    print(f"User    Choice\tis:\t{user_choice}")
    return user_choice

def play_the_game():
    userchoice = call_userinput()
    computerchoice = computer_input(choice_list)
    print("--------------------Result--------------------")
    if (userchoice == "rock"):
        if(computerchoice == "rock"):
            print("Game is tie")
        elif(computerchoice == "paper"):
            print("User lost the game")
        else:
            print("User won the game")
    
    elif(userchoice == "paper"):
        if(computerchoice == "rock"):
            print("User won the game")
        elif(computerchoice == "paper"):
            print("Game is tie")
        else:
            print("Computer won the game")
    elif(userchoice == "scissor"):
        if(computerchoice == "rock"):
            print("Computer won the game")
        elif(computerchoice == "paper"):
            print("User won the game")
        else:
            print("Game is tie")
    print("--------------------End Result--------------------")
#Method to check if user is interesed in playinh more games
def play_more_games():
    playnewgame = input("Do you want to play the game - [Yes/Y or No/N]?: ").lower()
    if(playnewgame not in playmore_list):
        while(True):
            print(f"Plese Enter Correct Choice from below \n{playmore_list}")
            playnewgame = input("Do you want to play the game - [Yes/Y or No/N]?: ").lower()
            if(playnewgame in playmore_list):
                play_the_game()
                break
    else:
        if(playnewgame == "no" or playnewgame == "n"):
            exit(0)
        play_the_game()   
    

        
                
            
    

# %%
while (True):
    if(gamenumber == 0):
        intro()
        play_the_game()
        gamenumber += 1
    else:
        gamenumber += 1
        play_more_games()
        print(f"This is {gamenumber} Game")   
        
        


