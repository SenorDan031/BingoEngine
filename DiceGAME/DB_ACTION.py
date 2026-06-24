from Engine import GameEngine as util
import msvcrt
import random
# PowerUps= ["Plus One", "Minus Two", "Re-Roll", "Take 4", "Pop Last",  "Gift"]
player1=[]
player2=[]
bot=[]


def rules_setRoll()  :
    
    print("\n=================RULES====================================================\t\t\n")
    print("\n1. Each player will get their chance turn by turn to roll the dice")
    print("\n2. Player that gets 6 3x in a row, will get to choose 2 power-ups")
    print("\n3. Player need to play a min of 5 rounds ")
    print("\n4. Player with the most scores in the end of the game will become the winner!")
    print("\n===============================================================================")

    
def roll_dice():
    while True:
        print("\n\nPress 'R' to roll the dice !:")
        key = msvcrt.getch().decode().lower()
        if key.lower() == "r":
            return True
        else :
            util.inv_input()

    
def  player1_turn(nm1):
    
    while True:
                    
        if roll_dice() :
            value=random.randint(1,6)
            print(f"\n\n\t\t\t{nm1} got {value}\n\n")
            player1.append(value)
            break
            
def  player2_turn(nm2):
    
    while True:

        if roll_dice() :
            value=random.randint(1,6)
            print(f"\n\n\t\t\t{nm2} bagged a {value}\n\n")
            player2.append(value)
            break
            
      
def bot_turn() :
    dice_for_bot= [1,5,2,3,1,3,4,2,4,1,5,5,3,6,4,6]
    print("\n\nBingoBot31 will roll the  dice now!\n")               
    value=random.randint(0,len(dice_for_bot)-1)
    bot.append(dice_for_bot[value])
    print(f"\n\n\n\t\tBingoBot31 bagged a {dice_for_bot[value]}")
    util.res_scrn()

def res_scores() :
    
    player1.clear()
    player2.clear()
    bot.clear()
