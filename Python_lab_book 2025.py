

OLD_PLAYERS={}

while True:    
     print("WELCOME TO MANCHESTER OLD PLAYERS ASSOCIATION" , sep=':')
     print("MAIN MENU")
     print("OPTION 1 ADD PLAYERS NAME:")
     print("OPTION 2 VIEW ALL PLAYERS:")
     print ("OPTION 3 ADD PLAYERS SHIRT NUMBER:")
     print("OPTION 4 ADD PLAYERS SCORE:")
     print("OPTION 5 DISPLAY PLAYER NAME,SHIRT NUMBER AND SCORE:")
     print ("OPTION 5 EXIT")
     choice=int(input("ENTER OPTION:"))
     if choice==1:
        Team_player=input("ENTER PLAYER NAME:") .upper()
        if Team_player in OLD_PLAYERS:
         print ("PLAYER EXISTS")
        else:OLD_PLAYERS[len(OLD_PLAYERS) + 1] = Team_player
        print(f"PLAYER SUCCESSFULLY ADDED ",OLD_PLAYERS)
        
     elif choice==5:
         print ("PROGRAM EXIT") 
     break




     
