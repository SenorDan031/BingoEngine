import time
import os
import random
import msvcrt
# PowerUps= ["Plus One", "Minus Two", "Re-Roll", "Take 4", "Pop Last",  "Gift"]
player1=[]
player2=[]
bot=[]
rpsAction= ["Rock","Scissors", "Paper"]

def res_scrn() :
    time.sleep(1.3)
    os.system('cls')

def game_rounds() :
    while True:
        
       rounds=input("\n\nEnter the number of rounds to be played [10]max [5]min : ")
       
       check=rounds.isdigit()
       
       if check and int(rounds)<=10 and int(rounds)>=5:
           return rounds
       
       elif rounds=="" :
           rounds=5
           return rounds
           
       elif check and int(rounds)<5 :
           print("\n\n\t\t\tGame rounds cant be less than 5!!")
           res_scrn()
           
       elif check and int(rounds)>10 :
           print("\n\n\t\t\tGame rounds cant be more than 10!!")
           res_scrn()
           
       else :
           print("\n\n\t\t\tEnter value in number, not in alphabetic pr other  invalid characters!!!!")
           res_scrn()

def rules_setRoll()  :
    
    print("\n=================RULES====================================================\t\t\n")
    print("\n1. Each player will get their chance turn by turn to roll the dice")
    print("\n2. Player that gets 6 3x in a row, will get to choose 2 power-ups")
    print("\n3. Player need to play a min of 5 rounds ")
    print("\n4. Player with the most scores in the end of the game will become the winner!")
    print("\n===============================================================================")
    
def rules_setRPS()  :
    
    print("\n=================RULES====================================================\t\t\n")
    print("\n1. Each player will get their chance turn by turn ")
    print("\n2. Rock beats Scissor , Scissor beats Paper and Paper beats Rock")
    print("\n3. Player need to play a min of 5 rounds ")
    print("\n4. Player with the most points in the end of the game will become the winner!")
    print("\n===============================================================================")
    
def main_menu():
    
    print("=================================================================================")
    print("\n1. Human vs Human")
    print("\n2. Human vs Bot")
    print("\n3. Exit Game")
    ch1= input("\nEnter valid choice from above:> " )
    print("\n=================================================================================")
    return ch1
    
def any_key_inp():
    
    print("Press any key to start the game, when ready....")       
    msvcrt.getch()
    
    
def roll_dice():
    while True:
        print("\n\nPress 'R' to roll the dice !:")
        key = msvcrt.getch().decode().lower()
        if key.lower() == "r":
            return True
        else :
            inv_input()

def roll_action() :
    while True :
        key = msvcrt.getch().decode().lower()
        if key.lower() == 'r' :
            return True
        else :
            inv_input()

def player1_name():
    nm1= input("\nEnter Player 1 Name:> ")
    return nm1
    
def player2_name():
    nm2= input("\nEnter Player 2 Name:> ")
    return nm2
    
def  player1_turn(nm1):
    
    while True:
                    
        if roll_dice() or roll_action():
            value=random.randint(1,6)
            print(f"\n\n\t\t\t{nm1} got {value}\n\n")
            player1.append(value)
            break
            
def  player2_turn(nm2):
    
    while True:

        if roll_dice() or roll_action() :
            value=random.randint(1,6)
            print(f"\n\n\t\t\t{nm2} bagged a {value}\n\n")
            player2.append(value)
            break
            
      
def bot_turn() :
    
    print("\n\nBingoBot31 will roll the  dice now!\n")               
    value=random.randint(1,6)
    bot.append(value)
    print(f"\n\n\n\t\tBingoBot31 bagged a {value}")
    res_scrn()

def res_scores() :
    
    player1.clear()
    player2.clear()
    bot.clear()


def replay_opt():
    
    while True :
    
        print("\n\nDo you want to replay this match?\n\n")   
        print("\n\npress y to replay or n to go to main menu!\n\n")   
        
        key=msvcrt.getch().decode().lower()
        
        if key.lower() == "y":
            
            print("\n\n\t\t\tRestarting Match ....")
            res_scrn()
            break
            
        elif  key.lower()== "n" :
            
            print("\n\n\t\tGoing back to main menu....")
            return key
            
        else :
            print("Enter valid input y  or n !")
            res_scrn()
    
        

def inv_input() :
    
    print("Invalid option entry detected! make your choice  again!")
    res_scrn()  

def  game_exit() :
    
    print("Closing Game! Please wait for few seconds")
    res_scrn()
    print("game closed!") 