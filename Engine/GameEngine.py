import time
import os
import random
import msvcrt


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
    
def roll_action() :
    while True :
        key = msvcrt.getch().decode().lower()
        if key.lower() == 'r' :
            return True
        else :
            inv_input()
            
def player_names(P_no):
    while True :
        name= input(f"\nEnter player {P_no} name here>> ").title().strip()
        
        if len(name)== 0:
            print("Player Name cannot be empty !!")
            res_scrn()
            
        elif len(name) > 10 :
            print("Player name cannot be more than 10 characters!!")
            res_scrn()
        
        else:
            return name

def replay_opt():
    
    while True :
    
        print("\n\nDo you want to replay this match?\n\n")   
        print("\n\npress y to replay or n to go to main menu!\n\n")   
        
        key=msvcrt.getch().decode().lower()
        
        if key.lower() == "y":
            
            print("\n\n\t\t\tRestarting Match ....")
            res_scrn()
            return True
            
        elif  key.lower()== "n" :
            
            print("\n\n\t\tGoing back to main menu....")
            res_scrn()
            return False
            
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