
#Write a Python program using dictionary to manage the scores of n players in a game. Each player has a name and a score (runs scored). The program should provide tasks:
1#.	Add a player's name and score.
2.#	Update the score of an existing player.
3.#	Find and display the score of a particular player.
4.#	Display a scoreboard showing all players and their scores, along with the total score.
5.#	Exit the program.

   
TEAM_PLAYERS = {} 
while True:
  
   print("WELCOME TO MANCHESTER UNITED ACADEMY")
   print ("CHOOSE OPTION 1 ADD A PLAYER:")
   print("CHOOSE OPTION 2 to UPDATE THE SCORE OF EXISTING PLAYER")
   input_option=int(input("ENTER OPTION"))
   if input_option==1:
    name=input("INPUT PLAYER NAME:")
   score=int(input("ENTER SCORE"))
      if name in TEAM_PLAYERS:
       print("NAME ALREADY EXISTS")
      else:
       TEAM_PLAYERS[name]=score
       
               elif input_option == 2:
    name = input("ENTER PLAYER NAME: ")
    if name in TEAM_PLAYERS:
        score = int(input("ENTER NEW SCORE: "))
        TEAM_PLAYERS[name] = score