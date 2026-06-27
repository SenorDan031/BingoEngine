# This program allows a 2-users to roll dice, user with the highest no. of points wins the game.
from Engine import GameEngine as util
from DiceGAME import DB_ACTION as action
from DiceGAME import DB_SCOREBRD as calc

def main():
    
    while True :
        print("\t\tWelcome to Luck n Roll\t\t" )
        ch1= util.main_menu()
        match ch1 :
            
            case '1' :
                util.res_scrn()
                print("\t\t Human vs Human Selected\t\t")
                nm1=util.player_names(1)
                nm2=util.player_names(2)
                print(f" {nm1} vs {nm2}\n")
                util.any_key_inp()
                
                while True:
                    player1_score=[]
                    player2_score=[]
                    util.res_scrn()
                    
                    action.rules_setRoll()
                    
                    limits=int(util.game_rounds())
                        
                    print(f"\n\n\t\tGAME set for {limits} Rounds!!  ")
                    util.res_scrn()
                    
                    print("\nLet's Begin Rolling!!! \n\n")
                    
                    for Round in  range(limits) :
                        
                        print(f"\t\t\t\tRound {Round+1}")
                        print(f"\n\n\t\t{nm1} {sum(player1_score)} :  {nm2} {sum(player2_score)}\n\n")
                        
                        print(f"\n\n{nm1} will roll the  dice now!\n")
                        score1=action.player_turn(nm1,player1_score)
                        player1_score.append(score1)
                                
                        print(f"\n\n{nm2} will roll the  dice now!\n")
                        score2=action.player_turn(nm2,player2_score)
                        player2_score.append(score2)
                        
                        util.res_scrn()
                                
                    util.res_scrn()
                    
                    scr1= sum(player1_score)
                    scr2= sum(player2_score)
                            
                    calc.score_calci(nm1,nm2,scr1,scr2)
                    if not util.replay_opt():
                        break
            
            case '2':
                
                util.res_scrn()
                print("\t\t Human vs BOT Selected\t\t")
                bot="BingoBot31"
                nm1=util.player_names(1)
                print(f" {nm1} vs BingoBot31\n")
                
                while True:
                    player1_score=[]
                    bot_score=[]

                    util.any_key_inp()
                    
                    util.res_scrn()
                    
                    action.rules_setRoll()
                    
                    limits=int(util.game_rounds())
                        
                    print(f"\n\n\t\tGAME set for {limits} Rounds!!  ")
                    util.res_scrn()
                    
                    print("current match score  0 for all\nLet's Begin Rolling!!! \n\n")
                    
                    for Round in  range(limits) :
                        
                        print(f"\t\t\t\tRound {Round+1}")
                        print(f"\n\n\t\t{nm1} {sum(player1_score)} :  BingoBot31 {sum(bot_score)}\n\n")
                        
                        print(f"\n\n{nm1} will roll the  dice now!\n")
                        score1=action.player_turn(nm1,player1_score)
                        player1_score.append(score1)
                                
                        action.bot_turn(bot_score)
                    
                    util.res_scrn()
                    
                    scr1= sum(player1_score)
                    scr2= sum(bot_score)
                    calc.score_calci(nm1,bot,scr1,scr2)
                    
                    if not  util.replay_opt():
                        break
                    
            case '3' :
                util.game_exit()
                break
                
            case _ :
                util.inv_input()         