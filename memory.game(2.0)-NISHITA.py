#%%
#guessing game

import random

n=random.randint(1,99) 
a=0 #the no. of tries
x=False

name=input("Enter player name: ")
print("Hell!", name, ". Welcome to the GUESSING GAME!")

y=input("Enter 'Y' to play or 'Q' to quit: ")

if y.lower()=='q':
      print("Well, bye!")
      
elif y.lower()=='y':
      print("I'm thinking of a number between 1 to 100.")
      while not x:
            g=int(input("Enter you guessed number: "))
            a=a+1
            if g==n:
                x=True
            elif g>n:
                print("Guess a lower number.")
            elif g<n:
                print("Guess a higher number.")
      print("Congratulations! You win! You guess the number correctly.")
      print("The number was: ", n)
      print("It took you",a,"tries to get it right.")

#%%

#nim's game

import time
print("Welcome to the Game of Nim.")
print(" R  U  L  E  S ")
print("There is a stack of stones with specific number of stones on it.") 
print("It's a multipLayer game, so make sure there's someone you can play with.")
print("The players have to one by one enter the number(between 1 to 3) of stone they want to remove from the stack.")
print("The player who gets the last stone wins!")

y= input("Press 'y' to play or 'q' to quit: ")
if y.lower()=='q':
    print("Goodbye, then!")
elif y.lower()=='y':
    print("Great! Let's play!")
    time.sleep(1)
    player=1
    object=21
    while True:
        print("Player", player)
        while True:
            move=int(input("Enter your move: "))
            if (move in [1,2,3] and (move<object)):
                 break
            print("Illegal move. Please enter a number between 1 to 3.")
        object=object-move
        print("The number of stones now becomes", object)
        time.sleep(1)
        if object==1:
            print("Player", player, "wins!")
            break
        #switching b/w players
        if player==1:
             player=2
        else:
             player=1
    print("Game is over!")
    print("Thank you for playing!")


#%%

#the excuse maker

import random
import time

print("Did you forgot to do your homework?")
print("NO worries! We've got you covered.")
print("Welcome to excuse maker, shall we find your perfect excuse")

l1=['My mother','My Dog','My pinky toe','A random guy','The toilet','A cockroach']
l2=['tore up','ate','stepped on','injured','smacked','smooshed']
l3=['my homework','my bus','my bedroom','my clothes','my lunch','my money']

a=random.choice(l1)
b=random.choice(l2)
c=random.choice(l3)

y=input("Enter 'y' to play or 'n' to quit: ")

if y.lower()=='n':
    print('Goobye, then!')


elif y.lower()=='y':
    print("Great! Your excuse is being ready!")
    time.sleep(2)
    print('Your excuse is ready!')
    print(a,b,c)
    print("Hope this gets you out of trouble! Thank you for playing.")
    
#%%


    
    
    
    
    



















