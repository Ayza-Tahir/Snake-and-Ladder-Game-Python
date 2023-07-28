#Snake And Ladder
import random
size_game=input("How many players wants to play the game :")
size_game=int(size_game)
list_players=[]
list_scored=[]
list_winner=[]
print("                        Players name ") 
for i in range(size_game):
    #taking names of players                                           #and store in a list
    player=(input("Name :"))
    list_players.append(player) #name in list
    list_scored.append(0)  #score 0 at the start of the game
   
    
win_condition=False

while win_condition!=True:      #turns of players
    for i in range(size_game):
        
        i=int(i)
        turn=(list_players[0])
      
        list_players.remove(turn)  #first player in list 
        
        print("Player ",i + 1," : ", turn)
        
        print("                     Enter d or D to roll the dice")
        dice_p=input("Enter:")
        
        
        if dice_p== 'd' or dice_p== 'D':
            
          score=random.randint(0,7)  #rand dice roll
          print("Dice no :",score)
          score_pp=list_scored[0]
          list_scored.remove(score_pp) #score remove from list
          score=int(score)
          prev=score_pp
          score_pp=score_pp+score # add total
          score_pp=int(score_pp)
          
          print("Total Score of Player {} is {}".format(turn,score_pp))
          
           #conditions check
          
          if score_pp < 100 :
                #ladder condition
                if score_pp==20:
                   score_pp=score_pp+5
                   print("congratulations! you got ladder :)")
                   print("Now your total score is {} of Player {}" .format(score_pp,turn))
                   
                elif score_pp==40:
                    score_pp=score_pp+10
                    print("congratulations! you got ladder :)")
                    print("Now your total score is {} of Player {}" .format(score_pp,turn))
               
                elif score_pp==60:
                    score_pp=score_pp+15
                    print("congratulations! you got ladder :)")
                    print("Now your total score is {} of Player {}" .format(score_pp,turn))
               
                elif score_pp==80:
                   score_pp=score_pp+20
                   print("congratulations! you got ladder :)")
                   print("Now your total score is {} of Player {}" .format(score_pp,turn))
            
          # snake bite
                elif score_pp==25:
                   score_pp=score_pp-10
                   print("Ooh, Snake bites you :(")
                   print("Now your total score is {} of Player {}" .format(score_pp,turn))
                
                elif score_pp ==45:
                    score_pp=score_pp-10
                    print("Ooh, Snake bites you :(")
                    print("Now your total score is {} of Player {}" .format(score_pp,turn))
                 
                elif score_pp== 65:
                    score_pp=score_pp-10
                    print("Ooh, Snake bites you :(")
                    print("Now your total score is {} of Player {}" .format(score_pp,turn))
                    
                elif score_pp==85:
                    score_pp=score_pp-10
                    print("Ooh, Snake bites you :(")
                    print("Now your total score is {} of Player {}" .format(score_pp,turn))
                    
                
        if score_pp==100 and size_game!=1:
            list_winner.append(turn)
            size_game=size_game-1
            
        elif score_pp > 100:
            print ("Ooh Your Score Exceed than 100 so your last score cannot be count ")
            score_pp=prev
            print("Now your total score is {} of Player {}" .format(score_pp,turn))
            # append again in list
        if score_pp < 100 :
          
            list_players.append(turn)
            list_scored.append(score_pp)
            
        if size_game==1:
            
            count_noo=0
            for i in list_winner:
                count_noo=count_noo+1
                print("Player {} got {}".format(i,count_noo))
            print("Player {}  lost the game".format(turn))    
            win_condition=True     
            
