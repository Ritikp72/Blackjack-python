# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 18:07:20 2021

@author: ritik
"""


import random
import sys
playerid=[]
playername=[]
player_cards=[]
dealer_cards=[]
new_deck1=[]
new_deck2=[]
new_deck3=[]
new_deck4=[]
player_card2=[]
playerscore=0
dealerscore=0
player_balance=500
b=50
a=()
c=()
Total_Game=1
win=0
loose=0
card_colour= ['Diamond','Hearts','Spades','Clubs']

card_name= {'Ace':11,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,
             '10':10,'Jack':10,'Queen':10,'King':10}

#***************************************************Creating deck**************************************************
    

The_Deck = []
for number in card_name:
   for kind in card_colour:
    The_Deck.append(list([number,kind]))
    
#**************************************************Search user name*******************************************
    
def search_user(playername):
    name=str(input("Enter your name to search=")) 
    f=open('data.txt','r')
    for line in f:
        if name in line:
         print("Your name has found:",line)
         playername=line
         break;
        else:
         file=open('data.txt','a')
         print("*******************Data not found*************************")
         playername=str("Enter your name:")
         file.write(playername + '\n')
         break;
        return playername        
        f.close()
    
    
#**********************************Adds user********************************************************************
def add_user(playername):
    f=()
    f=str(input("Do you already have a account(Type y for yes n/no for no"))
    if f=="y" or f=="yes":
       playername=search_user(playername)
    if f=="n" or f=="no":
     print("****************Create an account****************************")
     file=open('data.txt','a')
     playername=str(input("Enter your name="))
     print("The data has been added successfully")
     file.write(playername+ '\n')
     file.close()
     return playername
 
    

    
    


#*********************************Checks Ace*********************************************************************




def checkace():
    ekka=int(input("Enter the value of ace(1/11)"))
    if ekka==1:
        return 1
    if ekka==11:
       return 11
   
    
    
    
    
#***********************************Replay the game**************************************************************

def playagain(player_cards,dealer_cards,The_Deck,playerscore,new_deck1,dealerscore,player_balance,Total_Game):
    x=str(input("Do you want to start new game ?Type Y for yes N for no"))
    if x=="Y":
        Total_Game=Total_Game+1
        print("Your total game is ",Total_Game)
        dealer_cards.clear()
        player_cards.clear()
        new_deck1.clear()
        while player_cards != 2:
         player_cards.append(random.choice(The_Deck))
         if len(player_cards) == 2:
          print ("The two cards you got are:",player_cards)
          if card_name[player_cards[0][0]]==11 and card_name[player_cards[1][0]]==11:
            playerscore=checkace()
            playerscore1=checkace() 
            playerscore=playerscore+playerscore1
            print("Your Score Is :: ",playerscore)
            break;
            #return playerscore
          elif card_name[player_cards[0][0]]==11 or card_name[player_cards[1][0]]==11:
            playerscore=checkace()
            playerscore=playerscore+card_name[player_cards[0][0]]+card_name[player_cards[1][0]]-11
            print("Your Score Is :: ",playerscore)
            break;
            #return playerscore
          else :
           playerscore=card_name[player_cards[0][0]]+card_name[player_cards[1][0]]
           print("Your Score Is :: ",playerscore)
           break;
          # return playerscore
        new_deck1= [x for x in The_Deck if (x not in player_cards)] 
        while dealer_cards != 2:
         dealer_cards.append(random.choice(new_deck1)) 
         if len(dealer_cards) == 2:
          print("*******************************************************************")
          print("*******************************************************************")  
          print("Dealer's First Card is :: ",dealer_cards[1])
          print("And the second card is still hidden !!")
          print("*******************************************************************")
          print("*******************************************************************")
          dealerscore=card_name[dealer_cards[0][0]]+card_name[dealer_cards[1][0]]
          break;
        if playerscore==21:
          print("*******************************************************************")
          print(playername,"You won with a Black Jack Congrats !!")
          player_balance=player_balance+b
          print("Your balance is=",player_balance)
          print("*******************************************************************")
          Total_Game=playagain(player_cards,dealer_cards,The_Deck,playerscore,new_deck1,dealerscore,player_balance,Total_Game)
          sys.exit() 
        if playerscore>21:
          print("*******************************************************************")
          print(playername,"You are busted !! Sorry")
          player_balance=player_balance-b
          print("Your balance is=",player_balance)
          print("*******************************************************************")
          Total_Game=playagain(player_cards,dealer_cards,The_Deck,playerscore,new_deck1,dealerscore,player_balance,Total_Game)
          sys.exit()
        choice=str(input("Do you want to Stand or Hit ? Type H for Hit S for Stand :: "))
        if choice == 'S' :
           if playerscore>dealerscore:
                print("You win the game")
                sys.exit
           if playerscore > dealerscore and dealerscore>19 :
            print("*******************************************************************")
            print(" Computer's Score was ",dealerscore,playername,"You Won !! Congratulation")
            player_balance=player_balance+b
            print("Your balance is=",player_balance)
            print("*******************************************************************")
            Total_Game=playagain(player_cards,dealer_cards,The_Deck,playerscore,new_deck1,dealerscore,player_balance,Total_Game)
            sys.exit()
           if playerscore < dealerscore and dealerscore>19 :
            print("*******************************************************************")
            print(playername,"You Lost !! Computer's total was ",dealerscore)
            player_balance=player_balance-b
            print("Your balance is=",player_balance)
            print("*******************************************************************")
            Total_Game=playagain(player_cards,dealer_cards,The_Deck,playerscore,new_deck1,dealerscore,player_balance,Total_Game)
            sys.exit()
           if playerscore < dealerscore  and dealerscore<19:
            dealercounter=2
            #print(dealerscore)
            dealerscore=dealercard(dealerscore,dealercounter,player_balance,playerscore)
            check(playerscore,dealerscore,a,c,player_balance)
            Total_Game=playagain(player_cards,dealer_cards,The_Deck,playerscore,new_deck1,dealerscore,player_balance,Total_Game)
            sys.exit()
           if playerscore > dealerscore and dealerscore<19 :
            dealercounter=2
            #print(dealerscore)
            dealerscore=dealercard(dealerscore,dealercounter,player_balance,playerscore)
            check(playerscore,dealerscore,a,c,player_balance)
            Total_Game=playagain(player_cards,dealer_cards,The_Deck,playerscore,new_deck1,dealerscore,player_balance,Total_Game)
            sys.exit()
           if playerscore==dealerscore:
            print("*******************************************************************")
            print("It's a TIE !!")
            print("Your balance is=",player_balance)
            print("*******************************************************************")
            Total_Game=playagain(player_cards,dealer_cards,The_Deck,playerscore,new_deck1,dealerscore,player_balance,Total_Game)
            sys.exit()
        if choice == 'H' :
           roundcounter=2  
           dealercounter=2 
           #print(roundcounter)
           playerscore=playercard_new(The_Deck,player_cards,roundcounter,playerscore,player_balance,Total_Game)
           print("Dealer Final Score is :: ",dealerscore)
           delaerscore=dealercard(dealerscore,dealercounter,player_balance,playerscore)
           check(playerscore,dealerscore,a,c,player_balance)
    if x=="N":
        print("You have played",Total_Game,"game")
        print("Thankyou for playing this game")
        sys.exit()

        

#*********************************PLayer picks 2 cards*****************************************

def  playercard_pick(The_Deck,player_cards):
    while player_cards != 2:
        player_cards.append(random.choice(The_Deck))
        if len(player_cards) == 2:
         print ("The two cards you got are:",player_cards)
         print("*******************************************************************")
         if card_name[player_cards[0][0]]==11 and card_name[player_cards[1][0]]==11:
            playerscore=checkace()
            playerscore1=checkace() 
            playerscore=playerscore+playerscore1
            print("Your Score Is :: ",playerscore)
            return playerscore
         elif card_name[player_cards[0][0]]==11 or card_name[player_cards[1][0]]==11:
            playerscore=checkace()
            playerscore=playerscore+card_name[player_cards[0][0]]+card_name[player_cards[1][0]]-11
            print("Your Score Is :: ",playerscore)
            return playerscore
         else :
          playerscore=card_name[player_cards[0][0]]+card_name[player_cards[1][0]]
          print("Your Score Is :: ",playerscore)
          return playerscore
          break;
    if playerscore==21:
        print("YOu got Blackjack!!!You win")    
        playagain(player_cards,dealer_cards,The_Deck,playerscore,new_deck1,dealerscore,player_balance,Total_Game)
        sys.exit() 
       
   

#***************************************Dealer picks the card**************************************


def dealercard_pick(new_deck1,dealer_cards):
    while dealer_cards != 2:
        dealer_cards.append(random.choice(new_deck1))
        if len(dealer_cards) == 2:
         print("*******************************************************************")
         print("*******************************************************************")  
         print("Dealer's First Card is :: ",dealer_cards[1])
         print("And the second card is still hidden !!")
         print("*******************************************************************")
         print("*******************************************************************")
         dealerscore=card_name[dealer_cards[0][0]]+card_name[dealer_cards[1][0]]
         break;
    if dealerscore>21:
        print("Dealer is Busted!!!!You won")
        print("Dealer's score is",dealerscore)
        playagain(player_cards,dealer_cards,The_Deck,playerscore,new_deck1,dealerscore,player_balance,Total_Game)
        sys.exit()
         
    return dealerscore
         
 #************************Player picks extra cards*********************************************        
def  playercard_new(The_Deck,player_cards,roundcounter,playerscore,player_balance,Total_Game):
    a=roundcounter+1
    print("round=",a)
    while player_cards != a :
        player_cards.append(random.choice(new_deck2))
        if len(player_cards) == a:
         newcard=player_cards[roundcounter]
         print("*******************************************************************")
         print ("Your New Card is:",newcard)
         if card_name[player_cards[2][0]]==11:
            playerscore1=checkace()
            playerscore=playerscore1+player_cards[2][0]-11
         else:
            playerscore=playerscore+card_name[player_cards[2][0]]
         print("Player score Now",playerscore)
         print("*******************************************************************")
         if playerscore>21:
             print("Sorry You're Busted !! ")
             player_balance=player_balance-b
             print("Your balance is=",player_balance)  
             playagain(player_cards,dealer_cards,The_Deck,playerscore,new_deck1,dealerscore,player_balance,Total_Game)
             exit()
         if playerscore==21:
             print("You win!!!!You have got Blackjack")
             player_balance=player_balance+b
             print("Your balance is=",player_balance)  
             playagain(player_cards,dealer_cards,The_Deck,playerscore,new_deck1,dealerscore,player_balance,Total_Game)
             exit()
         choice=str(input("Do you want to Stand or Hit ? Type H for Hit S for Stand :: "))    
         print("*******************************************************************")
         if choice=='S':
             if playerscore>dealerscore:
               print("You win the game")
               return playerscore
               break;
         if choice=='H':
             roundcounter=roundcounter+1
             playerscore=playercard_new(The_Deck,player_cards,roundcounter,playerscore,player_balance,Total_Game)
             break;
         return a
             
#*******************************Check who won the game******************************************
def check(playerscore,dealerscore,a,c,player_balance):
    if playerscore>21:
     print("*******************************************************************")  
     print(playername,"You are busted !! Sorry")
     player_balance=player_balance-b
     print("Your remaining balance is",player_balance)
     print("*******************************************************************")
     playagain(player_cards,dealer_cards,The_Deck,playerscore,new_deck1,dealerscore,player_balance,Total_Game)
     sys.exit()
    if playerscore<dealerscore :
        print("*******************************************************************")
        print(playername,"Sorry You Lost !! Computer Total is ",dealerscore)
        player_balance=player_balance-b
        print("Your balance is=",player_balance)
        print("*******************************************************************")
        playagain(player_cards,dealer_cards,The_Deck,playerscore,new_deck1,dealerscore,player_balance,Total_Game)
        sys.exit()
    if playerscore==dealerscore:
        print("*******************************************************************")
        print("It's a Tie ")
        print("Your balance is",player_balance)
        print("*******************************************************************")
        playagain(player_cards,dealer_cards,The_Deck,playerscore,new_deck1,dealerscore,player_balance,Total_Game)
        sys.exit()
    if playerscore>dealerscore :
        print("*******************************************************************")
        print("Congratulation",playername," You Won !! ")
        player_balance=player_balance+b
        print("Your balance is=",player_balance)
        print("*******************************************************************")
        playagain(player_cards,dealer_cards,The_Deck,playerscore,new_deck1,dealerscore,player_balance,Total_Game)
        sys.exit()
    if dealerscore>21 :
        print("*******************************************************************")
        print("Congratulation",playername," You Won !! Computer Busted ",dealerscore)
        player_balance=player_balance+b
        print("Your balance is=",player_balance)
        print("*******************************************************************")
        playagain(player_cards,dealer_cards,The_Deck,playerscore,new_deck1,dealerscore,player_balance,Total_Game)
        sys.exit() 
    if a==5:
        print("********************************************************************")
        print("Congratulation",playername,"You Won !!")
        player_balance=player_balance+b
        print("Your balance is=",player_balance)
        print("*********************************************************************")
        playagain(player_cards,dealer_cards,The_Deck,playerscore,new_deck1,dealerscore,player_balance,Total_Game)
        sys.exit()
    if c==5:
        print("********************************************************************")
        print(playername," Sorry You Lost!!")
        player_balance=player_balance+b
        print("Your balance is=",player_balance)
        print("*********************************************************************")
        playagain(player_cards,dealer_cards,The_Deck,playerscore,new_deck1,dealerscore,player_balance,Total_Game)
        sys.exit()
     
#**************************Dealer picks extra cards***********************************  
def dealercard(dealerscore,dealercounter,player_balance,playerscore):
    c=dealercounter+1
    print("round=",c)
    #print(dealerscore)
    while dealerscore<=18:
       while dealer_cards != c :
         dealer_cards.append(random.choice(new_deck2))
         if len(dealer_cards) == c:
           newcard=dealer_cards[dealercounter]
           print("*******************************************************************")
           print ("Dealers New Card is:",newcard)
           print("*******************************************************************")
           dealerscore=dealerscore+card_name[dealer_cards[dealercounter][0]]
           print("*******************************************************************")
           print("Dealer score Now",dealerscore)
           print("*******************************************************************")
           c=c+1
           new_deck4=[x for x in The_Deck if (x not in dealer_cards)]
           new_deck3=new_deck4
           dealercounter=dealercounter+1
           break;
    
           
    if dealerscore>21:
               print("Dealer is Busted!!! Congratulation ",playername,"You win")
               player_balance=player_balance+b
               print("Your balance is=",player_balance)
               playagain(player_cards,dealer_cards,The_Deck,playerscore,new_deck1,dealerscore,player_balance,Total_Game)
               sys.exit()
    if dealerscore==21:
            print("Dealer has Blackjack.You lost!!!!")
            player_balance=player_balance-b
            print("Your balance is=",player_balance)
            playagain(player_cards,dealer_cards,The_Deck,playerscore,new_deck1,dealerscore,player_balance,Total_Game)
    return dealerscore    
                 
    
#***********************Intro***************************************************
print("*******************************************************************")
print("*******************************************************************")
print("*****************WELCOME TO BLACK JACK GAME IN PYTHON *************")
print("*******************************************************************")
print("*******************************************************************")
playername=add_user(playername)
print("Congratulation ",playername,"You got 500 Starting Balance !!")
print("*******************************************************************")
print("Welcome  to my BlackJack Simulator! Below are the basic rules:\n**\t- Beat the dealer's hand without going over 21.\n**\t- Face cards are worth 10, Aces are worth 1 or 11, whichever makes a better \n**\thand.\n**\t- Each player starts with two cards, and one of the dealer's cards is hidden \n**\tuntil the end.\n**\t- Type 'H' to ask for another card. Type 'S' to hold your total and end your \n**\tturn.\n**\t- If you go over 21 you bust, and the dealer wins regardless of his hand.\n**\t- If you are dealt 21 from the start (Ace & 10), you got a blackjack. If you \n**\tget a blackjack, you win 2 times   \n**\t-The amount of your bet automatically, unless the dealer also gets a blackjack, \n**\tin which case it is Dealer wins\n**\t- Remember: Type 'H' to get another card, and 'S' to hold. At the beginning of the round, type the quantit**\t  y you want to bet .\n**\t  Type 'play' to begin,type 'help' to get a list of valid commands.\n")

#*****************calling the funtions and creatin new deck*********************

playerscore=playercard_pick(The_Deck,player_cards)
new_deck1= [x for x in The_Deck if (x not in player_cards)]
dealerscore=dealercard_pick(new_deck1,dealer_cards)
new_deck2=[x for x in new_deck1 if (x not in dealer_cards)]
new_deck3=[x for x in new_deck2 if (x not in player_cards)]
roundcounter=()
dealercounter=()
if playerscore==21:
   print("*******************************************************************")
   print(playername,"You won with a Black Jack Congrats !!")
   player_balance=player_balance+b
   print("Your balance is=",player_balance)
   print("*******************************************************************")
   playagain(player_cards,dealer_cards,The_Deck,playerscore,new_deck1,dealerscore,player_balance,Total_Game)
   sys.exit()
if playerscore>21:
   print("*******************************************************************")
   print(playername,"You are busted !! Sorry")
   player_balance=player_balance-b
   print("Your balance is=",player_balance)
   print("*******************************************************************")
   playagain(player_cards,dealer_cards,The_Deck,playerscore,new_deck1,dealerscore,player_balance,Total_Game)
   sys.exit()
choice=str(input("Do you want to Stand or Hit ? Type H for Hit S for Stand :: "))


#*********************Checking after user enter stand******************************
if choice == 'S' :
    if playerscore>dealerscore:
        print("You won the game")
        sys.exit()
    if playerscore > dealerscore and dealerscore>18  :
        print("*******************************************************************")
        print(" Dealer's Score was ",dealerscore,playername,"You Won !! Congratulation")
        player_balance=player_balance+b
        print("Your balance is=",player_balance)
        print("*******************************************************************")
        playagain(player_cards,dealer_cards,The_Deck,playerscore,new_deck1,dealerscore,player_balance,Total_Game)
        sys.exit()
    if playerscore < dealerscore and dealerscore>18 :
        print("*******************************************************************")
        print(playername,"You Lost !! Dealer's total was ",dealerscore)
        player_balance=player_balance-b
        print("Your balance is=",player_balance)
        print("*******************************************************************")
        playagain(player_cards,dealer_cards,The_Deck,playerscore,new_deck1,dealerscore,player_balance,Total_Game)
        sys.exit()
    if playerscore < dealerscore and dealerscore<18 :
        dealercounter=2
        dealerscore=dealercard(dealerscore,dealercounter,player_balance,playerscore)
        check(playerscore,dealerscore,a,c,player_balance)
        playagain(player_cards,dealer_cards,The_Deck,playerscore,new_deck1,dealerscore,player_balance,Total_Game)
        sys.exit()
    if playerscore > dealerscore and dealerscore>18 :
        dealercounter=2
        print(dealerscore)
        dealerscore=dealercard(dealerscore,dealercounter,player_balance,playerscore)
        check(playerscore,dealerscore,a,c,player_balance)
        playagain(player_cards,dealer_cards,The_Deck,playerscore,new_deck1,dealerscore,player_balance,Total_Game)
        sys.exit()
    if playerscore==dealerscore and dealerscore<18:
        dealercounter=2
        dealerscore=dealercard(dealerscore,dealercounter,player_balance,playerscore)
        check(playerscore,dealerscore,a,c,player_balance)
        playagain(player_cards,dealer_cards,The_Deck,playerscore,new_deck1,dealerscore,player_balance,Total_Game)
        sys.exit()
        
    if playerscore==dealerscore:
        print("*******************************************************************")
        print("It's a TIE !!")
        print("Your balance is=",player_balance)
        print("*******************************************************************")
        playagain(player_cards,dealer_cards,The_Deck,playerscore,new_deck1,dealerscore,player_balance,Total_Game)
        sys.exit()
        

#*****************************For hitting the player cards*********************************     
     
if choice == 'H' :
    roundcounter=2  
    dealercounter=2 
    #print(roundcounter)
    playerscore=playercard_new(The_Deck,player_cards,roundcounter,playerscore,player_balance,Total_Game)
    #new_deck3=[x for x in new_deck1 if (x not in dealer_cards)]
    print("Dealer Final Score is :: ",dealerscore)
    delaerscore=dealercard(dealerscore,dealercounter,player_balance,playerscore)
    check(playerscore,dealerscore,a,c,player_balance)

