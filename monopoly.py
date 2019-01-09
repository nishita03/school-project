#%%
import random
dice =[1,2,3,4,5,6]
n=22# no of places on board
place_names=['old kent road','whitechapel road','euston road','the angel,islington','pentonville road','pall mall','whitehall','northumburdavenue','bow street','marlborough street','vine street','strand','the fleet street','trafalgfar square','leicester square','coventry street','piccadilly','regent street','oxford street','bond street','park lane','mayfair']
place_prices=[60,60,100,100,120,140,140,160,180,180,200,220,220,240,260,260,280,300,300,320,350,400]
place_rents=[place_prices[i]//10 for i in range(n)]
positions=[[place_names[i],place_prices[i],place_rents[i]]for i in range(n)]


def showgrid():
    #function to show board
    print('-'*25)
    for i in positions:
        print(i[0],end=(' '*(30-len(i[0]))))
    print()    
    print('-'*25)    
showgrid()
incorrect=True
print('welcome to monopoly\n the rules are simple the last person left with money wins\n type b to buy property')
    
    

while incorrect:# ignore this loop as it only takes int input
    try:
        player_num=int(input('Enter number of players(minimum 2):'))
        if player_num<=1:
            print('Enter number of players again..You cant possibly be so lonely:')
            pc=int('a')
        incorrect=False
    except:
        print('not  a number')
        incorrect=True
player_names=[]
player_positions=[]
player_money=[]
player_prop=[]
for i in range(player_num):
    player_names.append(input('Enter name of player:'))
    player_positions.append(0)
    player_money.append(1500)
    player_prop.append([])
print(player_names)
gamewin=False
print('b to buy')

rentpaid=False


def lost(loser):
    
    x=player_names.index(loser)
    player_names.pop(x)
    player_money.pop(x)
    player_positions.pop(x)
    player_prop.pop(x)
    
    
while not gamewin:
    for i in range(player_num):
        print('press enter to continue or q to quit')
        x=input()
        if x=='q':
            gamewin=True
            break
        roll=random.choice(dice)
        pos=player_positions[i]
        name=player_names[i]
        if pos+roll>=n:
            print('you passed Go collect 200 rupees')
            player_money[i]+=00
            pos=pos+roll-n
            #if player gets more than n positon
        else:
            pos=pos+roll
        cost=positions[pos][1]
        player_positions[i]=pos#to update the position and save it in the list
        place_name=positions[pos][0]
        print(name,'rolled a ',roll,'and got to ',positions[pos][0],'its cost is',positions[pos][1])
        showgrid()
        if place_name in player_prop[i]:
            print('you already own this property')
            continue
        else:
            for o in range(player_num):
                if rentpaid:
                    break
                j=player_prop[o]
                for k in range(len(j)):
                    if place_name==j[k]:
                        print('you owe rent to',player_names[o],'you need to pay',positions[pos][2])
                        rentpaid=True
                        if player_money[i]<=positions[pos][2]:
                            print(name,"can't pay rent")
                            player_num-=1
                            lost(name)
                            break
                            
                            
                        else:
                            player_money[i]-=positions[pos][2]
                            player_money[o]+=positions[pos][2]
                            print(name,'has',player_money[i],'left',player_names[o],'has',player_money[o])
                            break
        if player_num==1:
            print(player_names[0],'has won')
            gamewin=True
            break                    
        if rentpaid:
            rentpaid=False
            continue            
        print('what will you do?')
        action=input()    
        if action=='b':
            if cost<player_money[i]:
                print('you bought',place_name,'for the cost of',cost)
                player_money[i]-=cost
                print('you have',player_money[i],'money left')
                player_prop[i].append(place_name)
                print('you own',player_prop[i])
                
            else:
                print('insufficent balance')
        
        
                    
    



    