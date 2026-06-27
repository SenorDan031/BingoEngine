import time
from Engine import GameEngine as util


def score_calci(nm1,nm2,scr1,scr2):
    
    if scr1 > scr2:
        print(f"\n\t\t{nm1} is the Winner\n\n\tFinal Scores:\t {nm1} scored {scr1} (winner) VS {nm2} scored {scr2}")
        
        if nm2=="BingoBot31":
            
            if scr1-scr2>=10 :
                
                time.sleep(1.1)
                print("\n\t\t\tBingoBot31: Luck was on your side Today!")
                
            elif scr1-scr2 >=5 and scr1-scr2<10 :
                
                time.sleep(1.1)
                print(f"\n\t\t\tBingoBot31: Almost got you {nm1}, feel lucky!")
                
            elif scr1-scr2>=1 and scr1-scr2<=3 :
                
                time.sleep(1.1)
                print(f"\n\t\t\tBingoBot31: close one {nm1}, But will you be favoured in our Re-Match? ")

    elif scr2 > scr1:
        print(f"\n\t\t{nm2} is the Winner\n\n\tFinal Scores:\t {nm2} scored {scr2} (winner) VS {nm1} scored {scr1}")
        
        if nm2=="BingoBot31":
            
            if scr2-scr1>=10 :
                
                time.sleep(1.1)
                print("\n\t\t\tBingoBot31: Dont know what to feel Pity or Embarrased, lost to a bot XD!")
                
            elif scr2-scr1 >=5 and scr2-scr1<10 :
                
                time.sleep(1.1)
                print(f"\n\t\t\tBingoBot31: Almost had me {nm1},anyways feelin sad T_T (wished could have felt it actually)!")
                
            elif scr2-scr1>=1 and scr2-scr1<=3 :
                
                time.sleep(1.1)
                print(f"\n\tBingoBot31: close one {nm1}, Wanna test it in a Re-Match?  or 'Better luck Next time' ahh screen ")

    else :
        print("Its a tie !!")



    

    