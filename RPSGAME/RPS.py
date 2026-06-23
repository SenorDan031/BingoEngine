import GameEngine as util


while True :
    
    print("\n\t\t Welcome to RPS \n\n")
    ch1=util.main_menu()
    
    match ch1 :
        
        case '1' :
            util.res_scrn()
            print("\n\t\t Human vs Human selected !\n\n")
            nm1=util.player1_name()
            nm2=util.player2_name()
            print(f"\n\n\t\t{nm1.capitalize()} vs {nm2.capitalize()}\n")
            
            while True :
                util.any_key_inp()
                util.res_scrn()
                # util.rules_setRPS()
                limits= int(util.game_rounds())
                
                print(f"\n\n\t\tGame set for {limits} rounds!!\n")
                util.res_scrn()
                
                for round in range(limits) :
                    
                    print