from Engine import GameEngine as util
import msvcrt
import random
# PowerUps= ["Plus One", "Minus Two", "Re-Roll", "Take 4", "Pop Last",  "Gift"]



def rules_setRoll()  :
    
    print("\n=================RULES====================================================\t\t\n")
    print("\n1. Each player will get their chance turn by turn to roll the dice")
    print("\n2. Player that gets 6 3x in a row, will get to choose 2 power-ups")
    print("\n3. Player need to play a min of 5 rounds ")
    print("\n4. Player with the most scores in the end of the game will become the winner!")
    print("\n===============================================================================")
            
def player_turn(name,player_score):
    
    while True :
        if util.roll_action():
            value=random.randint(1,6)
            print(f"\n\n\t\t\t{name} bagged a {value}")
            break
    return value
        
def bot_turn(bot_scores) :
    dice_for_bot= [1,5,2,3,1,3,4,2,4,1,5,5,3,6,4,6]
    print("\n\nBingoBot31 will roll the  dice now!\n")               
    value=random.randint(0,len(dice_for_bot)-1)
    bot_scores.append(dice_for_bot[value])
    print(f"\n\n\n\t\tBingoBot31 bagged a {dice_for_bot[value]}")
    util.res_scrn()

def res_scores() :
    
    pass
