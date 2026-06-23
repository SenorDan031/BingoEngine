# This program allows a 2-users to roll dice, user with the highest no. of points wins the game.
import GameEngine as util
import DB_ACTION as action

while True :
    print("\t\tWelcome to Luck n Roll\t\t" )
    ch1= util.main_menu()
    match ch1 :
        
        case '1' :
            util.res_scrn()
            print("\t\t Human vs Human Selected\t\t")
            nm1=util.player1_name()
            nm2=util.player2_name()
            print(f" {nm1.capitalize()} vs {nm2.capitalize()}\n")
            
            while util.replay_opt() :
                
                util.any_key_inp()
                
                util.res_scrn()
                
                action.rules_setRoll() 
                
                limits=int(util.game_rounds())
                    
                print(f"\n\n\t\tGAME set for {limits} rounds!!  ")
                util.res_scrn()
                
                print("\nLet's Begin Rolling!!! \n\n")
                
                for round in  range(limits) :
                    
                    print(f"\t\t\t\tRound {round+1}")
                    print(f"\n\n\t\t{nm1} {sum(action.player1)} :  {nm2} {sum(action.player2)}\n\n")
                    
                    print(f"\n\n{nm1} will roll the  dice now!\n")
                    action.player1_turn(nm1)
                            
                    print(f"\n\n{nm2} will roll the  dice now!\n")
                    action.player2_turn(nm2)
                    
                    util.res_scrn()
                            
                util.res_scrn()
                
                sum1= sum(action.player1)
                sum2= sum(action.player2)
                        
                if sum2>sum1 :
                    print(f"{nm2} is  the winner!\n\n")
                    
                    print(f"{nm1} scored {sum1} : {nm2} scored {sum2} (Winner) ")
                        
                elif sum1>sum2 :
                    print(f"{nm1} is the winner!\n\n")
                    print(f"{nm1} scored {sum1} (Winner)  : {nm2} scored {sum2}")
                        
                else :
                    print("It's a tie ")
                    print(f"{nm1} {sum1} : {nm2} {sum2}")
                    
                action.res_scores()
          
        case '2' :      
            util.res_scrn()
            print("\t\t Human vs BOT Selected\t\t")
            
            nm1= util.player1_name()
            print(f" {nm1.capitalize()} vs BingoBot31\n")
            
            while True :

                util.any_key_inp()
                
                util.res_scrn()
                
                action.rules_setRoll() 
                
                limits=int(util.game_rounds())
                    
                print(f"\n\n\t\tGAME set for {limits} rounds!!  ")
                util.res_scrn()
                
                print("current match score  0 for all\nLet's Begin Rolling!!! \n\n")
                
                for round in  range(limits) :
                    
                    print(f"\t\t\t\tRound {round+1}")       
                    print(f"\n\n\t\t{nm1} {sum(action.player1)} :  BingoBot31 {sum(action.bot)}\n\n")
                    
                    action.player1_turn(nm1)
                            
                    action.bot_turn()
                
                util.res_scrn()
                
                sum1= sum(action.player1)
                sum2= sum(action.bot)
                        
                if sum2>sum1 :
                    print("BingoBot31 is  the winner!")
                    print(f"{nm1} scored {sum1}  : BingoBot31 scored {sum2} (Winner) ")
                        
                elif sum1>sum2 :
                    print(f"{nm1} is the winner! ")
                    print(f"{nm1} scored {sum1} (Winner) : BingoBot31 scored {sum2} ")
                        
                else :
                    print("It's a tie ")
                  
                action.res_scores()
                opt= util.replay_opt()
                if opt=='n':
                    util.res_scrn()
                    break
                
        case '3' :
            util.game_exit() 
            break
              
        case _ :
            util.inv_input()         