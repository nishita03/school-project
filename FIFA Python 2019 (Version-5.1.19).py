#%%
import numpy as np
import pylab as pl
from matplotlib import collections  as mc
import random
import matplotlib.pyplot as plt 

print()
print('                       ELECTRONIC ARTS SPORTS           ')
for i in range(20):
    n=1
    for i in range(1,25000):
        n=n*i
    n=1
print('                In association with HANAN CORPORATIONS  ')
for i in range(20):
    n=1
    for i in range(1,25000):
        n=n*i
    n=1
print()
print('                             presents                   ')
for i in range(20):
    n=1
    for i in range(1,25000):
        n=n*i
    n=1
print()
print('              _________ _______  _________                             ')
print('              |            |     |             /\                      ') 
print('              |            |     |            /  \                     ') 
print('              |______      |     |______     /____\                    ') 
print('              |            |     |          /      \                   ') 
print('              |            |     |         /        \                  ')
print('              |         ___|___  |        /          \                 ')
print()
for i in range(20):
    n=1
    for i in range(1,25000):
        n=n*i
    n=1
print('                              PYTHON 2019                             ')
for i in range(20):
    n=1
    for i in range(1,25000):
        n=n*i
    n=1
print()
print('                       NEYMAR JR  :  THE HISTOIRE                     ')
for i in range(20):
    n=1
    for i in range(1,25000):
        n=n*i
    n=1
print()
print()
start=input('                       Press ENTER to start the game             ')
for i in range(20):
    n=1
    for i in range(1,25000):
        n=n*i
    n=1
print()
print('                               LOADING                                 ')
print()
print('              ',end='')
print('',end=' ')
for i in range(20):
    n=1
    for i in range(1,25000):
        n=n*i
    n=1
    print('>',end=' ')
print('')
print()
print()
for i in range(20):
    n=1
    for i in range(1,25000):
        n=n*i
    n=1
print('                               RULES OF GAME                     ')
print('_______________________________________________________________________________')
print()
print('      1>The player with ball plays his turn until possession is lost')
print('      2>The moves of play are:')
print('            a>to PASS , press p and then press enter')
print('            b>to CROSS , press c and then press enter')
print('            c>to GIVE THROUGH BALL, press tb and then press enter')
print('            d>to SHOOT , press s and then press enter')
print('            e>to do SKILLS , press skill and then press enter')
print('            f>to SUBSTITUTE , press sub and then press enter')
print('                     NOTE : A player can be substituted once in the game')
print('            g>Anything except the above commands your player will commit FOUL ')
print('            h>to read the RULES again , press rules and then press enter')
print('            i>to QUIT , press quit and then press enter')
print()
print('                          Barcelona VS PSG                             ')
print('_______________________________________________________________________________')
print()


x=random.randint(0,1)
time=0

playerpin1='Buffon'
playerpin2=0
playerpin3=0
playerpin4=0
playerpin5=0
playerpin6=0
playerpin7=0
playerpin8=0
playerpin9=0
playerpin10=0
playerpin11=0

playerbin1='Ter Stegnen'
playerbin2=0
playerbin3=0
playerbin4=0
playerbin5=0
playerbin6=0
playerbin7=0
playerbin8=0
playerbin9=0
playerbin10=0
playerbin11=0

subb1=0
subb2=0
subb3=0
subb4=0
subb5=0
subb6=0
subb7=0
subb8=0
subb9=0
subb10=0
subb11=0

subp1=0
subp2=0
subp3=0
subp4=0
subp5=0
subp6=0
subp7=0
subp8=0
subp9=0
subp10=0
subp11=0

HP=10

hp1=HP
hp2=HP
hp3=HP
hp4=HP
hp5=HP
hp6=HP
hp7=HP
hp8=HP
hp9=HP
hp10=HP
hp11=HP

hb1=HP
hb2=HP
hb3=HP
hb4=HP
hb5=HP
hb6=HP
hb7=HP
hb8=HP
hb9=HP
hb10=HP
hb11=HP

s1='Akka'
s2='Around The World'
s3='Elastico'
s4='Neymar Rocket'
s5='Rainbow'
s6='Hocus Pocus'
s7='Matrix'
s8='Juggling'
s9='D-Trec'
s10='No Look Pass'
s11='Roulette Panna'
s12='Tornado Twist'
s13='Nutmeg'
s14='Stepovers'
s15='Whiplash'
s16='Scissor Move'
s17='Lizard'
s18='Heel Flick'
s19='Pro-Mora'
s20='Fake Shot'


q=0
quitme=0

n=0
playerb=10
playerbn='Messi'
playerp=10
playerpn='Neymar'
bar=0
psg=0
bargoal=0
psggoal=0
h=2

for i in range(20):
    n=1
    for i in range(1,25000):
        n=n*i
    n=1
print()

if x==0:
    bar=1
    print('               Good Morning, Welcome to Barcelona stadium...       ')
    print('_______________________________________________________________________________')  
    print()
    print('Messi (10) starts...')
    
else:
    psg=1
    print('                Good Morning, Welcome to Paris stadium..           ')
    print('_______________________________________________________________________________')  
    print()
    print('Neymar (10) starts...')    
    
while time!=60:

    if quitme==1:
	    break
        
    if quit==2:
        for i in range(20):
    n=1
    for i in range(1,25000):
        n=n*i
    n=1
        quit=0
        print('      a>to PASS , press p and then press enter')
        print('      b>to CROSS , press c and then press enter')
        print('      c>to GIVE THROUGH BALL, press tb and then press enter')
        print('      d>to SHOOT , press s and then press enter')
        print('      e>to do SKILLS , press skill and then press enter')
        print('      f>to SUBSTITUTE , press sub and then press enter')
        print('                     NOTE : A player in a particualar position can only be substituted once in the game')
        print('      g>if you enter anything except the above commands your player will commit FOUL ')
        print('      h>to read the RULES again , press rules and then press enter')
        print('      i>to QUIT , press quit and then press enter')
        

    if bar==1:

        playerp=12-playerb  
        
        if hb1<(0.3*HP):
            print('Commentatory:',playerbn,'is really tired. Please Substitute...')
        if hb2<(0.3*HP):
            print('Commentatory:',playerbn,'is really tired. Please Substitute...')
        if hb3<(0.3*HP):
            print('Commentatory:',playerbn,'is really tired. Please Substitute...')
        if hb4<(0.3*HP):
            print('Commentatory:',playerbn,'is really tired. Please Substitute...')
        if hb5<(0.3*HP):
            print('Commentatory:',playerbn,'is really tired. Please Substitute...')
        if hb6<(0.3*HP):
            print('Commentatory:',playerbn,'is really tired. Please Substitute...')
        if hb7<(0.3*HP):
            print('Commentatory:',playerbn,'is really tired. Please Substitute...')
        if hb8<(0.3*HP):
            print('Commentatory:',playerbn,'is really tired. Please Substitute...')
        if hb9<(0.3*HP):
            print('Commentatory:',playerbn,'is really tired. Please Substitute...')
        if hb11<(0.3*HP):
            print('Commentatory:',playerbn,'is really tired. Please Substitute...')
                 
        if playerb==1:
            playerbn='Ter Stegnen'
            if subb1!=0:
                playerbn=playerbin1        
        if playerb==2:
            playerbn='Umtiti'
            if subb2!=0:
                playerbn=playerbin2    
        if playerb==3:
            playerbn='Pique'
            if subb3!=0:
                playerbn=playerbin3    
        if playerb==4:
            playerbn='Rakitic'
            if subb4!=0:
                playerbn=playerbin4
        if playerb==5:
            playerbn='Sergio Busquets'
            if subb5!=0:
                playerbn=playerbin5    
        if playerb==6:
            playerbn='Denis Suarez'
            if subb6!=0:
                playerbn=playerbin6    
        if playerb==7:
            playerbn='Coutinho'
            if subb7!=0:
                playerbn=playerbin7    
        if playerb==8:
            playerbn='Arthur'
            if subb8!=0:
                playerbn=playerbin8    
        if playerb==9:
            playerbn='Suarez'
            if subb9!=0:
                playerbn=playerbin9    
        if playerb==10:
            playerbn='Messi'
            if subb10!=0:
                playerbn=playerbin10    
        if playerb==11:
            playerbn='Dembele'
            if subb11!=0:
                playerbn=playerbin11    
        if playerp==1:
            playerpn='Buffon'
            if subp1!=0:
                playerpn=playerpin1
        if playerp==2:
            playerpn='Thiago Silva'
            if subp2!=0:
                playerpn=playerpin2    
        if playerp==3:
            playerpn='Kimbempe'
            if subp3!=0:
                playerpn=playerpin3     
        if playerp==4:
            playerpn='Meunier'
            if subp4!=0:
                playerpn=playerpin4    
        if playerp==5:
            playerpn='Marquinhos'
            if subp5!=0:
                playerpn=playerpin5    
        if playerp==6:
            playerpn='Verrati'
            if subp6!=0:
                playerpn=playerpin6    
        if playerp==7:
            playerpn='Dani Alves'
            if subp7!=0:
                playerpn=playerpin7    
        if playerp==8:
            playerpn='Rabiot'
            if subp8!=0:
                playerpn=playerpin8    
        if playerp==9:
            playerpn='Cavani'
            if subp9!=0:
                playerpn=playerpin9    
        if playerp==10:
            playerpn='Neymar JR'
            if subp10!=0:
                playerpn=playerpin10    
        if playerp==11:
            playerpn='Mbappe'
            if subp11!=0:
                playerpn=playerpin11 
                
        n=0          
        print('What should',playerbn,'(',playerb,') do ?')
        m=input('>>>')
        time.sleep(1)

        if hb1<(0.2*HP): 
            m='sub'
            print('Commentatory:',playerbn,'is injured due to exhaustion !! Please Substitute NOW..')
        if hb2<(0.2*HP):
            m='sub'
            print('Commentatory:',playerbn,'is injured due to exhaustion !! Please Substitute NOW..')
        if hb3<(0.2*HP):
            m='sub'
            print('Commentatory:',playerbn,'is injured due to exhaustion !! Please Substitute NOW..')
        if hb4<(0.2*HP):
            m='sub'
            print('Commentatory:',playerbn,'is injured due to exhaustion !! Please Substitute NOW..')
        if hb5<(0.2*HP):
            m='sub'
            print('Commentatory:',playerbn,'is injured due to exhaustion !! Please Substitute NOW..')
        if hb6<(0.2*HP):
            m='sub'
            print('Commentatory:',playerbn,'is injured due to exhaustion !! Please Substitute NOW..')
        if hb7<(0.2*HP):
            m='sub'
            print('Commentatory:',playerbn,'is injured due to exhaustion !! Please Substitute NOW..')
        if hb8<(0.2*HP):
            m='sub'
            print('Commentatory:',playerbn,'is injured due to exhaustion !! Please Substitute NOW..')
        if hb9<(0.2*HP):
            m='sub'
            print('Commentatory:',playerbn,'is injured due to exhaustion !! Please Substitute NOW..')
        if hb11<(0.2*HP):
            m='sub'
            print('Commentatory:',playerbn,'is injured due to exhaustion !! Please Substitute NOW..')

        if m=='skill' or m=='skills' or m=='skl' or m=='9':
            q=random.randint(1,25)
            if q==1:
                print('Commentatory: What a beautiful',s1,'done by',playerbn,'(',playerb,') !!!')
            if q==2:
                print('Commentatory: Look at that',s2,'done by',playerbn,'(',playerb,') !!!')
            if q==3:
                print('Commentatory:OMG!!',s3,'done by',playerbn,'(',playerb,') !!!')
            if q==4:
                print('Commentatory: What a beautiful',s4,'done by',playerbn,'(',playerb,') !!!')
            if q==5:
                print('Commentatory:',s5,'done by',playerbn,'(',playerb,') !!!') 
            if q==6:
                print('Commentatory:The astounding',s6,'by ',playerbn,'(',playerb,') !!!')
            if q==7:
                print('Commentatory: What a beautiful',s7,'done by',playerbn,'(',playerb,') !!!')
            if q==8:
                print('Commentatory: Look at that',s8,'done by',playerbn,'(',playerb,') !!!')
            if q==9:
                print('Commentatory:OMG!!',s9,'done by',playerbn,'(',playerb,') !!!')
            if q==10:
                print('Commentatory: Unbelievable',s10,'done by',playerbn,'(',playerb,') !!!')
            if q==11:
                print('Commentatory: Remarkable',s11,'done by',playerbn,'(',playerb,') !!!') 
            if q==12:
                print('Commentatory:The astounding',s12,'by ',playerbn,'(',playerb,') !!!')
            if q==13:
                print('Commentatory: Ha Ha Ha !!! What a beautiful',s13,'done by',playerbn,'(',playerb,') under',playerpn,'(',playerp,') !!!')
            if q==14:
                print('Commentatory: Look at that',s14,'done by',playerbn,'(',playerb,') !!!')
            if q==15:
                print('Commentatory:OMG!!',s15,'done by',playerbn,'(',playerb,') !!!')
            if q==16:
                print('Commentatory: What a beautiful',s16,'done by',playerbn,'(',playerb,') !!!')
            if q==17:
                print('Commentatory:',s17,'done by',playerbn,'(',playerb,') !!!') 
            if q==18:
                print('Commentatory:The astounding',s18,'by ',playerbn,'(',playerb,') !!!')
            if q==19:
                print('Commentatory: What a beautiful',s19,'done by',playerbn,'(',playerb,') !!!')
            if q==20:
                print('Commentatory: Look at that',s20,'done by',playerbn,'(',playerb,') !!!')   
                if playerb!=11:
                    playerb=playerb+1
                else:
                    playerb=playerb-1
            if q==21:
                psg=1
                bar=0
                print('Commentatory: Ha Ha Ha !!! Skill Failed !! Ball intercepted by',playerpn,'(',playerp,') of PSG !!')     
            if q==22:
                psg=1
                bar=0
                print('Commentatory: OH  MY GOD!!! Skill Failed !! Ball intercepted by',playerpn,'(',playerp,') of PSG !!')
            if q==23:
                psg=1
                bar=0
                print('Commentatory: Ha Ha Ha !!! Skill Failed !! Nice Interception by',playerpn,'(',playerp,') of PSG !!')
            if q==24:
                psg=1
                bar=0
                print('Commentatory:What a Joke !!! Skill Failed !! Ball intercepted by',playerpn,'(',playerp,') of PSG !!') 
            if q==25:
                psg=1
                bar=0
                print('Commentatory: LOOK !!! Skill Failed !! Ball intercepted by',playerpn,'(',playerp,') of PSG !!')
                
        if m=='q' or m=='quit' or m=='esc' or m=='exit' or m=='0':
            quitme=1
            continue                             
              
               
        if m=='rules' or m=='rule' or m=='r':
            quit=2

        if m=='p' or m=='2':
            n=1
        if m=='c' or m=='4':
            n=2
        if m=='tb' or m=='8':
            n=3
        if m=='s' or m=='6':
            n=4
        if m=='sub' or m=='7':
            bar=1
            psg=0
            playerbout=input('Enter name of player to be substituted..')
            if playerbout=='ter stegnen' or playerbout=='ter' or playerbout=='stegnen':                
                subb1=1
                playerbin1=input('Enter name of player who goes in...')
                print('Commentatory:',playerbout,'goes out and here comes in',playerbin1)
                hb1=HP
            if playerbout=='umtiti':                
                subb2=1
                playerbin2=input('Enter name of player who goes in...')
                print('Commentatory:',playerbout,'goes out and here comes in',playerbin2)
                hb2=HP
            if playerbout=='pique':                
                subb3=1
                playerbin3=input('Enter name of player who goes in...')
                print('Commentatory:',playerbout,'goes out and here comes in',playerbin3)
                hb3=HP
            if playerbout=='rakitic':                
                subb4=1
                playerbin4=input('Enter name of player who goes in...')
                print('Commentatory:',playerbout,'goes out and here comes in',playerbin4)
                hb4=HP
            if playerbout=='sergio busquets' or playerbout=='sergio' or playerbout=='busquets':  
                subb5=1   
                playerbin5=input('Enter name of player who goes in...')
                print('Commentatory:',playerbout,'goes out and here comes in',playerbin5)
                hb5=HP
            if playerbout=='denis suarez' or playerbout=='denis':                
                subb6=1
                playerbin6=input('Enter name of player who goes in...')
                print('Commentatory:',playerbout,'goes out and here comes in',playerbin6)
                hb6=HP
            if playerbout=='coutinho':                
                subb7=1
                playerbin7=input('Enter name of player who goes in...')
                print('Commentatory:',playerbout,'goes out and here comes in',playerbin7)
                hb7=HP
            if playerbout=='arthur':                
                subb8=1
                playerbin8=input('Enter name of player who goes in...')
                print('Commentatory:',playerbout,'goes out and here comes in',playerbin8)
                hb8=HP
            if playerbout=='suarez':                
                subb9=1
                playerbin9=input('Enter name of player who goes in...')
                print('Commentatory:',playerbout,'goes out and here comes in',playerbin9)
                hb9=HP
            if playerbout=='messi' or playerbout=='lionel messi': 
                print("Hey ! You can't substitute ME ! I am the Captain !!")
                hb10=HP
            if playerbout=='dembele':                
                subb11=1
                playerbin11=input('Enter name of player who goes in...')
                print('Commentatory:',playerbout,'goes out and here comes in',playerbin11)
                hb11=HP
        
        y=random.randint(1,4)
        if n==1 and y!=1:
            if playerb<11:
                playerb=playerb+1
                if playerb==1:
                    playerbn='Ter Stegnen'
                    if subb1!=0:
                        playerbn=playerbin1        
                if playerb==2:
                    playerbn='Umtiti'
                    if subb2!=0:
                        playerbn=playerbin2    
                if playerb==3:
                    playerbn='Pique'
                    if subb3!=0:
                        playerbn=playerbin3    
                if playerb==4:
                    playerbn='Rakitic'
                    if subb4!=0:
                        playerbn=playerbin4
                if playerb==5:
                    playerbn='Sergio Busquets'
                    if subb5!=0:
                        playerbn=playerbin5    
                if playerb==6:
                    playerbn='Denis Suarez'
                    if subb6!=0:
                        playerbn=playerbin6    
                if playerb==7:
                    playerbn='Coutinho'
                    if subb7!=0:
                        playerbn=playerbin7    
                if playerb==8:
                    playerbn='Arthur'
                    if subb8!=0:
                        playerbn=playerbin8    
                if playerb==9:
                    playerbn='Suarez'
                    if subb9!=0:
                        playerbn=playerbin9    
                if playerb==10:
                    playerbn='Messi'
                    if subb10!=0:
                        playerbn=playerbin10    
                if playerb==11:
                    playerbn='Dembele'
                    if subb11!=0:
                        playerbn=playerbin11    
                if playerp==1:
                    playerpn='Buffon'
                    if subp1!=0:
                        playerpn=playerpin1
                if playerp==2:
                    playerpn='Thiago Silva'
                    if subp2!=0:
                        playerpn=playerpin2    
                if playerp==3:
                    playerpn='Kimbempe'
                    if subp3!=0:
                        playerpn=playerpin3     
                if playerp==4:
                    playerpn='Meunier'
                    if subp4!=0:
                        playerpn=playerpin4    
                if playerp==5:
                    playerpn='Marquinhos'
                    if subp5!=0:
                        playerpn=playerpin5    
                if playerp==6:
                    playerpn='Verrati'
                    if subp6!=0:
                        playerpn=playerpin6    
                if playerp==7:
                    playerpn='Dani Alves'
                    if subp7!=0:
                        playerpn=playerpin7    
                if playerp==8:
                    playerpn='Rabiot'
                    if subp8!=0:
                        playerpn=playerpin8    
                if playerp==9:
                    playerpn='Cavani'
                    if subp9!=0:
                        playerpn=playerpin9    
                if playerp==10:
                    playerpn='Neymar JR'
                    if subp10!=0:
                        playerpn=playerpin10    
                if playerp==11:
                    playerpn='Mbappe'
                    if subp11!=0:
                        playerpn=playerpin11
                print('Commentatory: Pass to player',playerbn,'succesful !! Nice Pass man!!')
                                
                time=time+1
                print()
                
                print('           [ Time :',time,'min || PSG:',psggoal,'| BAR:',bargoal,']')    
            
                h=2
                ppx1=h*5
                ppx2=random.randint(h*10,h*30)
                ppx3=random.randint(h*10,h*30)
                ppx4=random.randint(h*10,h*30)
                ppx5=random.randint(h*10,h*30)
                ppx6=random.randint(h*35,h*55)
                ppx7=random.randint(h*35,h*55)
                ppx8=random.randint(h*35,h*55)
                ppx9=random.randint(h*60,h*85)
                ppx10=random.randint(h*65,h*90)
                ppx11=random.randint(h*60,h*85)
                
                ppy1=random.randint(h*40,h*60)
                ppy2=random.randint(h*0,h*15)
                ppy3=random.randint(h*30,h*45)
                ppy4=random.randint(h*55,h*70)
                ppy5=random.randint(h*85,h*100)
                ppy6=random.randint(h*0,h*20)
                ppy7=random.randint(h*40,h*60)
                ppy8=random.randint(h*80,h*100)
                ppy9=random.randint(h*15,h*30)
                ppy10=random.randint(h*45,h*55)
                ppy11=random.randint(h*70,h*85)
                
                pbx1=h*95
                pbx2=random.randint(h*70,h*90)
                pbx3=random.randint(h*70,h*90)
                pbx4=random.randint(h*70,h*90)
                pbx5=random.randint(h*70,h*90)
                pbx6=random.randint(h*45,h*65)
                pbx7=random.randint(h*45,h*65)
                pbx8=random.randint(h*45,h*65)
                pbx9=random.randint(h*15,h*40)
                pbx10=random.randint(h*10,h*35)
                pbx11=random.randint(h*15,h*40)
                
                pby1=random.randint(h*40,h*60)
                pby2=random.randint(h*0,h*15)
                pby3=random.randint(h*30,h*45)
                pby4=random.randint(h*55,h*70)
                pby5=random.randint(h*85,h*100)
                pby6=random.randint(h*0,h*20)
                pby7=random.randint(h*40,h*60)
                pby8=random.randint(h*80,h*100)
                pby9=random.randint(h*15,h*30)
                pby10=random.randint(h*45,h*55)
                pby11=random.randint(h*70,h*85)
                
                print('          ',end='')
                lines = [[(h*0, h*35), (h*0, h*65)], [(h*100, h*35), (h*100, h*65)], [(h*50, h*105), (h*50, h*-5)], [(h*-10, h*105), (h*110, h*105)], [(h*-10, h*-5), (h*110, h*-5)], [(h*-10, h*105), (h*-10, h*-5)], [(h*110, h*105), (h*110, h*-5)], [(h*0, h*35), (h*-10, h*35)], [(h*0, h*65), (h*-10, h*65)], [(h*100, h*35), (h*110, h*35)], [(h*100, h*65), (h*110, h*65)]]
                c = np.array([(1, 0, 0, 1), (1, 0, 0, 1), (1, 0, 0, 1)])
                
                lc = mc.LineCollection(lines, colors=c, linewidths=1)
                fig, ax = pl.subplots()
                ax.set_facecolor('xkcd:sky blue')
                ax.set_facecolor((0.8, 1, 0.5))
                ax.add_collection(lc)
                ax.autoscale()
                ax.margins(0.1)
            
                psgx = [ppx2,ppx3,ppx4,ppx5,ppx6,ppx7,ppx8,ppx9,ppx10,ppx11] 
                psgy = [ppy2,ppy3,ppy4,ppy5,ppy6,ppy7,ppy8,ppy9,ppy10,ppy11] 
            
                plt.scatter(ppx1,ppy1,color= "purple",marker= "*", s=100)      # GK edit colour
                plt.scatter(psgx, psgy,color= "blue",marker= "*", s=80)  
             
                barx = [pbx2,pbx3,pbx4,pbx5,pbx6,pbx7,pbx8,pbx9,pbx10,pbx11] 
                bary = [pby2,pby3,pby4,pby5,pby6,pby7,pby8,pby9,pby10,pby11]
            
                plt.scatter(pbx1,pby1,color= "violet",marker= "o", s=100)      # GK edit colour
                plt.scatter(barx, bary, color= "red",marker= "o", s=80)       
                
                if playerb==1:
                    hb1-=1
                    plt.scatter(pbx1,pby1, label= "Ter Stegnen", color= "black",marker= "o", s=110)
                if playerb==2:
                    hb2-=1
                    plt.scatter(pbx2,pby2, label= "Umtiti", color= "black",marker= "o", s=110)
                if playerb==3:
                    hb3-=1
                    plt.scatter(pbx3,pby3, label= "Pique", color= "black",marker= "o", s=110)
                if playerb==4:
                    hb4-=1
                    plt.scatter(pbx4,pby4, label= "Rakitic", color= "black",marker= "o", s=110)
                if playerb==5:
                    hb5-=1
                    plt.scatter(pbx5,pby5, label= "Sergio Busquets", color= "black",marker= "o", s=110)
                if playerb==6:
                    hb6-=1
                    plt.scatter(pbx6,pby6, label= "Denis Suarez", color= "black",marker= "o", s=110)
                if playerb==7:
                    hb7-=1
                    plt.scatter(pbx7,pby7, label= "Coutinho", color= "black",marker= "o", s=110)
                if playerb==8:
                    hb8-=1
                    plt.scatter(pbx8,pby8, label= "Arthur", color= "black",marker= "o", s=110)
                if playerb==9:
                    hb9-=1
                    plt.scatter(pbx9,pby9, label= "Suarez", color= "black",marker= "o", s=110)
                if playerb==10:
                    hb10-=1
                    plt.scatter(pbx10,pby10, label= "Messi", color= "black",marker= "o", s=110)
                if playerb==11:
                    hb11-=1
                    plt.scatter(pbx11,pby11, label= "Dembele", color= "black",marker= "o", s=110)
                    
                plt.xlabel('Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! ') 
            
                plt.ylabel('Messi! Messi! Messi! Messi! Messi! Messi!') 
             
                plt.title('FIFA PYTHON 18\nPSG(BLUE) VS BARCELONA(RED)')  
            
                plt.show()     
                
                print() 

                continue 

            else:
                playerb=playerb-1
                if playerb==1:
                    playerbn='Ter Stegnen'
                    if subb1!=0:
                        playerbn=playerbin1        
                if playerb==2:
                    playerbn='Umtiti'
                    if subb2!=0:
                        playerbn=playerbin2    
                if playerb==3:
                    playerbn='Pique'
                    if subb3!=0:
                        playerbn=playerbin3    
                if playerb==4:
                    playerbn='Rakitic'
                    if subb4!=0:
                        playerbn=playerbin4
                if playerb==5:
                    playerbn='Sergio Busquets'
                    if subb5!=0:
                        playerbn=playerbin5    
                if playerb==6:
                    playerbn='Denis Suarez'
                    if subb6!=0:
                        playerbn=playerbin6    
                if playerb==7:
                    playerbn='Coutinho'
                    if subb7!=0:
                        playerbn=playerbin7    
                if playerb==8:
                    playerbn='Arthur'
                    if subb8!=0:
                        playerbn=playerbin8    
                if playerb==9:
                    playerbn='Suarez'
                    if subb9!=0:
                        playerbn=playerbin9    
                if playerb==10:
                    playerbn='Messi'
                    if subb10!=0:
                        playerbn=playerbin10    
                if playerb==11:
                    playerbn='Dembele'
                    if subb11!=0:
                        playerbn=playerbin11    
                if playerp==1:
                    playerpn='Buffon'
                    if subp1!=0:
                        playerpn=playerpin1
                if playerp==2:
                    playerpn='Thiago Silva'
                    if subp2!=0:
                        playerpn=playerpin2    
                if playerp==3:
                    playerpn='Kimbempe'
                    if subp3!=0:
                        playerpn=playerpin3     
                if playerp==4:
                    playerpn='Meunier'
                    if subp4!=0:
                        playerpn=playerpin4    
                if playerp==5:
                    playerpn='Marquinhos'
                    if subp5!=0:
                        playerpn=playerpin5    
                if playerp==6:
                    playerpn='Verrati'
                    if subp6!=0:
                        playerpn=playerpin6    
                if playerp==7:
                    playerpn='Dani Alves'
                    if subp7!=0:
                        playerpn=playerpin7    
                if playerp==8:
                    playerpn='Rabiot'
                    if subp8!=0:
                        playerpn=playerpin8    
                if playerp==9:
                    playerpn='Cavani'
                    if subp9!=0:
                        playerpn=playerpin9    
                if playerp==10:
                    playerpn='Neymar JR'
                    if subp10!=0:
                        playerpn=playerpin10    
                if playerp==11:
                    playerpn='Mbappe'
                    if subp11!=0:
                        playerpn=playerpin11
                print('Commentatory: Pass to player',playerbn,'succesful !!')

                time=time+1
                print()
                
                print('           [ Time :',time,'min || PSG:',psggoal,'| BAR:',bargoal,']')    
            
                h=2
                ppx1=h*5
                ppx2=random.randint(h*10,h*30)
                ppx3=random.randint(h*10,h*30)
                ppx4=random.randint(h*10,h*30)
                ppx5=random.randint(h*10,h*30)
                ppx6=random.randint(h*35,h*55)
                ppx7=random.randint(h*35,h*55)
                ppx8=random.randint(h*35,h*55)
                ppx9=random.randint(h*60,h*85)
                ppx10=random.randint(h*65,h*90)
                ppx11=random.randint(h*60,h*85)
                
                ppy1=random.randint(h*40,h*60)
                ppy2=random.randint(h*0,h*15)
                ppy3=random.randint(h*30,h*45)
                ppy4=random.randint(h*55,h*70)
                ppy5=random.randint(h*85,h*100)
                ppy6=random.randint(h*0,h*20)
                ppy7=random.randint(h*40,h*60)
                ppy8=random.randint(h*80,h*100)
                ppy9=random.randint(h*15,h*30)
                ppy10=random.randint(h*45,h*55)
                ppy11=random.randint(h*70,h*85)
                
                pbx1=h*95
                pbx2=random.randint(h*70,h*90)
                pbx3=random.randint(h*70,h*90)
                pbx4=random.randint(h*70,h*90)
                pbx5=random.randint(h*70,h*90)
                pbx6=random.randint(h*45,h*65)
                pbx7=random.randint(h*45,h*65)
                pbx8=random.randint(h*45,h*65)
                pbx9=random.randint(h*15,h*40)
                pbx10=random.randint(h*10,h*35)
                pbx11=random.randint(h*15,h*40)
                
                pby1=random.randint(h*40,h*60)
                pby2=random.randint(h*0,h*15)
                pby3=random.randint(h*30,h*45)
                pby4=random.randint(h*55,h*70)
                pby5=random.randint(h*85,h*100)
                pby6=random.randint(h*0,h*20)
                pby7=random.randint(h*40,h*60)
                pby8=random.randint(h*80,h*100)
                pby9=random.randint(h*15,h*30)
                pby10=random.randint(h*45,h*55)
                pby11=random.randint(h*70,h*85)
                
                print('          ',end='')
                lines = [[(h*0, h*35), (h*0, h*65)], [(h*100, h*35), (h*100, h*65)], [(h*50, h*105), (h*50, h*-5)], [(h*-10, h*105), (h*110, h*105)], [(h*-10, h*-5), (h*110, h*-5)], [(h*-10, h*105), (h*-10, h*-5)], [(h*110, h*105), (h*110, h*-5)], [(h*0, h*35), (h*-10, h*35)], [(h*0, h*65), (h*-10, h*65)], [(h*100, h*35), (h*110, h*35)], [(h*100, h*65), (h*110, h*65)]]
                c = np.array([(1, 0, 0, 1), (1, 0, 0, 1), (1, 0, 0, 1)])
                
                lc = mc.LineCollection(lines, colors=c, linewidths=1)
                fig, ax = pl.subplots()
                ax.set_facecolor('xkcd:sky blue')
                ax.set_facecolor((0.8, 1, 0.5))
                ax.add_collection(lc)
                ax.autoscale()
                ax.margins(0.1)
            
                psgx = [ppx2,ppx3,ppx4,ppx5,ppx6,ppx7,ppx8,ppx9,ppx10,ppx11] 
                psgy = [ppy2,ppy3,ppy4,ppy5,ppy6,ppy7,ppy8,ppy9,ppy10,ppy11] 
            
                plt.scatter(ppx1,ppy1,color= "purple",marker= "*", s=100)      # GK edit colour
                plt.scatter(psgx, psgy,color= "blue",marker= "*", s=80)  
             
                barx = [pbx2,pbx3,pbx4,pbx5,pbx6,pbx7,pbx8,pbx9,pbx10,pbx11] 
                bary = [pby2,pby3,pby4,pby5,pby6,pby7,pby8,pby9,pby10,pby11]
            
                plt.scatter(pbx1,pby1,color= "violet",marker= "o", s=100)      # GK edit colour
                plt.scatter(barx, bary, color= "red",marker= "o", s=80)       
                
                if playerb==1:
                    hb1-=1
                    plt.scatter(pbx1,pby1, label= "Ter Stegnen", color= "black",marker= "o", s=110)
                if playerb==2:
                    hb2-=1
                    plt.scatter(pbx2,pby2, label= "Umtiti", color= "black",marker= "o", s=110)
                if playerb==3:
                    hb3-=1
                    plt.scatter(pbx3,pby3, label= "Pique", color= "black",marker= "o", s=110)
                if playerb==4:
                    hb4-=1
                    plt.scatter(pbx4,pby4, label= "Rakitic", color= "black",marker= "o", s=110)
                if playerb==5:
                    hb5-=1
                    plt.scatter(pbx5,pby5, label= "Sergio Busquets", color= "black",marker= "o", s=110)
                if playerb==6:
                    hb6-=1
                    plt.scatter(pbx6,pby6, label= "Denis Suarez", color= "black",marker= "o", s=110)
                if playerb==7:
                    hb7-=1
                    plt.scatter(pbx7,pby7, label= "Coutinho", color= "black",marker= "o", s=110)
                if playerb==8:
                    hb8-=1
                    plt.scatter(pbx8,pby8, label= "Arthur", color= "black",marker= "o", s=110)
                if playerb==9:
                    hb9-=1
                    plt.scatter(pbx9,pby9, label= "Suarez", color= "black",marker= "o", s=110)
                if playerb==10:
                    hb10-=1
                    plt.scatter(pbx10,pby10, label= "Messi", color= "black",marker= "o", s=110)
                if playerb==11:
                    hb11-=1
                    plt.scatter(pbx11,pby11, label= "Dembele", color= "black",marker= "o", s=110)
                    
                plt.xlabel('Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! ') 
            
                plt.ylabel('Messi! Messi! Messi! Messi! Messi! Messi!') 
             
                plt.title('FIFA PYTHON 18\nPSG(BLUE) VS BARCELONA(RED)')  
            
                plt.show()     
                
                print() 

                continue 
        
        if n==2 and y!=2:
            if playerb<10:
                playerb=playerb+2
                if playerb==1:
                    playerbn='Ter Stegnen'
                    if subb1!=0:
                        playerbn=playerbin1        
                if playerb==2:
                    playerbn='Umtiti'
                    if subb2!=0:
                        playerbn=playerbin2    
                if playerb==3:
                    playerbn='Pique'
                    if subb3!=0:
                        playerbn=playerbin3    
                if playerb==4:
                    playerbn='Rakitic'
                    if subb4!=0:
                        playerbn=playerbin4
                if playerb==5:
                    playerbn='Sergio Busquets'
                    if subb5!=0:
                        playerbn=playerbin5    
                if playerb==6:
                    playerbn='Denis Suarez'
                    if subb6!=0:
                        playerbn=playerbin6    
                if playerb==7:
                    playerbn='Coutinho'
                    if subb7!=0:
                        playerbn=playerbin7    
                if playerb==8:
                    playerbn='Arthur'
                    if subb8!=0:
                        playerbn=playerbin8    
                if playerb==9:
                    playerbn='Suarez'
                    if subb9!=0:
                        playerbn=playerbin9    
                if playerb==10:
                    playerbn='Messi'
                    if subb10!=0:
                        playerbn=playerbin10    
                if playerb==11:
                    playerbn='Dembele'
                    if subb11!=0:
                        playerbn=playerbin11    
                if playerp==1:
                    playerpn='Buffon'
                    if subp1!=0:
                        playerpn=playerpin1
                if playerp==2:
                    playerpn='Thiago Silva'
                    if subp2!=0:
                        playerpn=playerpin2    
                if playerp==3:
                    playerpn='Kimbempe'
                    if subp3!=0:
                        playerpn=playerpin3     
                if playerp==4:
                    playerpn='Meunier'
                    if subp4!=0:
                        playerpn=playerpin4    
                if playerp==5:
                    playerpn='Marquinhos'
                    if subp5!=0:
                        playerpn=playerpin5    
                if playerp==6:
                    playerpn='Verrati'
                    if subp6!=0:
                        playerpn=playerpin6    
                if playerp==7:
                    playerpn='Dani Alves'
                    if subp7!=0:
                        playerpn=playerpin7    
                if playerp==8:
                    playerpn='Rabiot'
                    if subp8!=0:
                        playerpn=playerpin8    
                if playerp==9:
                    playerpn='Cavani'
                    if subp9!=0:
                        playerpn=playerpin9    
                if playerp==10:
                    playerpn='Neymar JR'
                    if subp10!=0:
                        playerpn=playerpin10    
                if playerp==11:
                    playerpn='Mbappe'
                    if subp11!=0:
                        playerpn=playerpin11
                print('Commentatory: Cross to player',playerbn,'succesful !! WOW! What a trap!! ')
                time=time+1
                print()
                
                print('           [ Time :',time,'min || PSG:',psggoal,'| BAR:',bargoal,']')    
            
                h=2
                ppx1=h*5
                ppx2=random.randint(h*10,h*30)
                ppx3=random.randint(h*10,h*30)
                ppx4=random.randint(h*10,h*30)
                ppx5=random.randint(h*10,h*30)
                ppx6=random.randint(h*35,h*55)
                ppx7=random.randint(h*35,h*55)
                ppx8=random.randint(h*35,h*55)
                ppx9=random.randint(h*60,h*85)
                ppx10=random.randint(h*65,h*90)
                ppx11=random.randint(h*60,h*85)
                
                ppy1=random.randint(h*40,h*60)
                ppy2=random.randint(h*0,h*15)
                ppy3=random.randint(h*30,h*45)
                ppy4=random.randint(h*55,h*70)
                ppy5=random.randint(h*85,h*100)
                ppy6=random.randint(h*0,h*20)
                ppy7=random.randint(h*40,h*60)
                ppy8=random.randint(h*80,h*100)
                ppy9=random.randint(h*15,h*30)
                ppy10=random.randint(h*45,h*55)
                ppy11=random.randint(h*70,h*85)
                
                pbx1=h*95
                pbx2=random.randint(h*70,h*90)
                pbx3=random.randint(h*70,h*90)
                pbx4=random.randint(h*70,h*90)
                pbx5=random.randint(h*70,h*90)
                pbx6=random.randint(h*45,h*65)
                pbx7=random.randint(h*45,h*65)
                pbx8=random.randint(h*45,h*65)
                pbx9=random.randint(h*15,h*40)
                pbx10=random.randint(h*10,h*35)
                pbx11=random.randint(h*15,h*40)
                
                pby1=random.randint(h*40,h*60)
                pby2=random.randint(h*0,h*15)
                pby3=random.randint(h*30,h*45)
                pby4=random.randint(h*55,h*70)
                pby5=random.randint(h*85,h*100)
                pby6=random.randint(h*0,h*20)
                pby7=random.randint(h*40,h*60)
                pby8=random.randint(h*80,h*100)
                pby9=random.randint(h*15,h*30)
                pby10=random.randint(h*45,h*55)
                pby11=random.randint(h*70,h*85)
                
                print('          ',end='')
                lines = [[(h*0, h*35), (h*0, h*65)], [(h*100, h*35), (h*100, h*65)], [(h*50, h*105), (h*50, h*-5)], [(h*-10, h*105), (h*110, h*105)], [(h*-10, h*-5), (h*110, h*-5)], [(h*-10, h*105), (h*-10, h*-5)], [(h*110, h*105), (h*110, h*-5)], [(h*0, h*35), (h*-10, h*35)], [(h*0, h*65), (h*-10, h*65)], [(h*100, h*35), (h*110, h*35)], [(h*100, h*65), (h*110, h*65)]]
                c = np.array([(1, 0, 0, 1), (1, 0, 0, 1), (1, 0, 0, 1)])
                
                lc = mc.LineCollection(lines, colors=c, linewidths=1)
                fig, ax = pl.subplots()
                ax.set_facecolor('xkcd:sky blue')
                ax.set_facecolor((0.8, 1, 0.5))
                ax.add_collection(lc)
                ax.autoscale()
                ax.margins(0.1)
            
                psgx = [ppx2,ppx3,ppx4,ppx5,ppx6,ppx7,ppx8,ppx9,ppx10,ppx11] 
                psgy = [ppy2,ppy3,ppy4,ppy5,ppy6,ppy7,ppy8,ppy9,ppy10,ppy11] 
            
                plt.scatter(ppx1,ppy1,color= "purple",marker= "*", s=100)      # GK edit colour
                plt.scatter(psgx, psgy,color= "blue",marker= "*", s=80)  
             
                barx = [pbx2,pbx3,pbx4,pbx5,pbx6,pbx7,pbx8,pbx9,pbx10,pbx11] 
                bary = [pby2,pby3,pby4,pby5,pby6,pby7,pby8,pby9,pby10,pby11]
            
                plt.scatter(pbx1,pby1,color= "violet",marker= "o", s=100)      # GK edit colour
                plt.scatter(barx, bary, color= "red",marker= "o", s=80)       
                
                if playerb==1:
                    hb1-=1
                    plt.scatter(pbx1,pby1, label= "Ter Stegnen", color= "black",marker= "o", s=110)
                if playerb==2:
                    hb2-=1
                    plt.scatter(pbx2,pby2, label= "Umtiti", color= "black",marker= "o", s=110)
                if playerb==3:
                    hb3-=1
                    plt.scatter(pbx3,pby3, label= "Pique", color= "black",marker= "o", s=110)
                if playerb==4:
                    hb4-=1
                    plt.scatter(pbx4,pby4, label= "Rakitic", color= "black",marker= "o", s=110)
                if playerb==5:
                    hb5-=1
                    plt.scatter(pbx5,pby5, label= "Sergio Busquets", color= "black",marker= "o", s=110)
                if playerb==6:
                    hb6-=1
                    plt.scatter(pbx6,pby6, label= "Denis Suarez", color= "black",marker= "o", s=110)
                if playerb==7:
                    hb7-=1
                    plt.scatter(pbx7,pby7, label= "Coutinho", color= "black",marker= "o", s=110)
                if playerb==8:
                    hb8-=1
                    plt.scatter(pbx8,pby8, label= "Arthur", color= "black",marker= "o", s=110)
                if playerb==9:
                    hb9-=1
                    plt.scatter(pbx9,pby9, label= "Suarez", color= "black",marker= "o", s=110)
                if playerb==10:
                    hb10-=1
                    plt.scatter(pbx10,pby10, label= "Messi", color= "black",marker= "o", s=110)
                if playerb==11:
                    hb11-=1
                    plt.scatter(pbx11,pby11, label= "Dembele", color= "black",marker= "o", s=110)
                    
                plt.xlabel('Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! ') 
            
                plt.ylabel('Messi! Messi! Messi! Messi! Messi! Messi!') 
             
                plt.title('FIFA PYTHON 18\nPSG(BLUE) VS BARCELONA(RED)')  
            
                plt.show()     
                
                print() 

                continue 
            
            else:
                playerb=playerb-2
                if playerb==1:
                    playerbn='Ter Stegnen'
                    if subb1!=0:
                        playerbn=playerbin1        
                if playerb==2:
                    playerbn='Umtiti'
                    if subb2!=0:
                        playerbn=playerbin2    
                if playerb==3:
                    playerbn='Pique'
                    if subb3!=0:
                        playerbn=playerbin3    
                if playerb==4:
                    playerbn='Rakitic'
                    if subb4!=0:
                        playerbn=playerbin4
                if playerb==5:
                    playerbn='Sergio Busquets'
                    if subb5!=0:
                        playerbn=playerbin5    
                if playerb==6:
                    playerbn='Denis Suarez'
                    if subb6!=0:
                        playerbn=playerbin6    
                if playerb==7:
                    playerbn='Coutinho'
                    if subb7!=0:
                        playerbn=playerbin7    
                if playerb==8:
                    playerbn='Arthur'
                    if subb8!=0:
                        playerbn=playerbin8    
                if playerb==9:
                    playerbn='Suarez'
                    if subb9!=0:
                        playerbn=playerbin9    
                if playerb==10:
                    playerbn='Messi'
                    if subb10!=0:
                        playerbn=playerbin10    
                if playerb==11:
                    playerbn='Dembele'
                    if subb11!=0:
                        playerbn=playerbin11    
                if playerp==1:
                    playerpn='Buffon'
                    if subp1!=0:
                        playerpn=playerpin1
                if playerp==2:
                    playerpn='Thiago Silva'
                    if subp2!=0:
                        playerpn=playerpin2    
                if playerp==3:
                    playerpn='Kimbempe'
                    if subp3!=0:
                        playerpn=playerpin3     
                if playerp==4:
                    playerpn='Meunier'
                    if subp4!=0:
                        playerpn=playerpin4    
                if playerp==5:
                    playerpn='Marquinhos'
                    if subp5!=0:
                        playerpn=playerpin5    
                if playerp==6:
                    playerpn='Verrati'
                    if subp6!=0:
                        playerpn=playerpin6    
                if playerp==7:
                    playerpn='Dani Alves'
                    if subp7!=0:
                        playerpn=playerpin7    
                if playerp==8:
                    playerpn='Rabiot'
                    if subp8!=0:
                        playerpn=playerpin8    
                if playerp==9:
                    playerpn='Cavani'
                    if subp9!=0:
                        playerpn=playerpin9    
                if playerp==10:
                    playerpn='Neymar JR'
                    if subp10!=0:
                        playerpn=playerpin10    
                if playerp==11:
                    playerpn='Mbappe'
                    if subp11!=0:
                        playerpn=playerpin11
                print('Commentatory: Cross to player',playerbn,'succesful !!')

                time=time+1
                print()
                
                print('           [ Time :',time,'min || PSG:',psggoal,'| BAR:',bargoal,']')    
            
                h=2
                ppx1=h*5
                ppx2=random.randint(h*10,h*30)
                ppx3=random.randint(h*10,h*30)
                ppx4=random.randint(h*10,h*30)
                ppx5=random.randint(h*10,h*30)
                ppx6=random.randint(h*35,h*55)
                ppx7=random.randint(h*35,h*55)
                ppx8=random.randint(h*35,h*55)
                ppx9=random.randint(h*60,h*85)
                ppx10=random.randint(h*65,h*90)
                ppx11=random.randint(h*60,h*85)
                
                ppy1=random.randint(h*40,h*60)
                ppy2=random.randint(h*0,h*15)
                ppy3=random.randint(h*30,h*45)
                ppy4=random.randint(h*55,h*70)
                ppy5=random.randint(h*85,h*100)
                ppy6=random.randint(h*0,h*20)
                ppy7=random.randint(h*40,h*60)
                ppy8=random.randint(h*80,h*100)
                ppy9=random.randint(h*15,h*30)
                ppy10=random.randint(h*45,h*55)
                ppy11=random.randint(h*70,h*85)
                
                pbx1=h*95
                pbx2=random.randint(h*70,h*90)
                pbx3=random.randint(h*70,h*90)
                pbx4=random.randint(h*70,h*90)
                pbx5=random.randint(h*70,h*90)
                pbx6=random.randint(h*45,h*65)
                pbx7=random.randint(h*45,h*65)
                pbx8=random.randint(h*45,h*65)
                pbx9=random.randint(h*15,h*40)
                pbx10=random.randint(h*10,h*35)
                pbx11=random.randint(h*15,h*40)
                
                pby1=random.randint(h*40,h*60)
                pby2=random.randint(h*0,h*15)
                pby3=random.randint(h*30,h*45)
                pby4=random.randint(h*55,h*70)
                pby5=random.randint(h*85,h*100)
                pby6=random.randint(h*0,h*20)
                pby7=random.randint(h*40,h*60)
                pby8=random.randint(h*80,h*100)
                pby9=random.randint(h*15,h*30)
                pby10=random.randint(h*45,h*55)
                pby11=random.randint(h*70,h*85)
                
                print('          ',end='')
                lines = [[(h*0, h*35), (h*0, h*65)], [(h*100, h*35), (h*100, h*65)], [(h*50, h*105), (h*50, h*-5)], [(h*-10, h*105), (h*110, h*105)], [(h*-10, h*-5), (h*110, h*-5)], [(h*-10, h*105), (h*-10, h*-5)], [(h*110, h*105), (h*110, h*-5)], [(h*0, h*35), (h*-10, h*35)], [(h*0, h*65), (h*-10, h*65)], [(h*100, h*35), (h*110, h*35)], [(h*100, h*65), (h*110, h*65)]]
                c = np.array([(1, 0, 0, 1), (1, 0, 0, 1), (1, 0, 0, 1)])
                
                lc = mc.LineCollection(lines, colors=c, linewidths=1)
                fig, ax = pl.subplots()
                ax.set_facecolor('xkcd:sky blue')
                ax.set_facecolor((0.8, 1, 0.5))
                ax.add_collection(lc)
                ax.autoscale()
                ax.margins(0.1)
            
                psgx = [ppx2,ppx3,ppx4,ppx5,ppx6,ppx7,ppx8,ppx9,ppx10,ppx11] 
                psgy = [ppy2,ppy3,ppy4,ppy5,ppy6,ppy7,ppy8,ppy9,ppy10,ppy11] 
            
                plt.scatter(ppx1,ppy1,color= "purple",marker= "*", s=100)      # GK edit colour
                plt.scatter(psgx, psgy,color= "blue",marker= "*", s=80)  
             
                barx = [pbx2,pbx3,pbx4,pbx5,pbx6,pbx7,pbx8,pbx9,pbx10,pbx11] 
                bary = [pby2,pby3,pby4,pby5,pby6,pby7,pby8,pby9,pby10,pby11]
            
                plt.scatter(pbx1,pby1,color= "violet",marker= "o", s=100)      # GK edit colour
                plt.scatter(barx, bary, color= "red",marker= "o", s=80)       
                
                if playerb==1:
                    hb1-=1
                    plt.scatter(pbx1,pby1, label= "Ter Stegnen", color= "black",marker= "o", s=110)
                if playerb==2:
                    hb2-=1
                    plt.scatter(pbx2,pby2, label= "Umtiti", color= "black",marker= "o", s=110)
                if playerb==3:
                    hb3-=1
                    plt.scatter(pbx3,pby3, label= "Pique", color= "black",marker= "o", s=110)
                if playerb==4:
                    hb4-=1
                    plt.scatter(pbx4,pby4, label= "Rakitic", color= "black",marker= "o", s=110)
                if playerb==5:
                    hb5-=1
                    plt.scatter(pbx5,pby5, label= "Sergio Busquets", color= "black",marker= "o", s=110)
                if playerb==6:
                    hb6-=1
                    plt.scatter(pbx6,pby6, label= "Denis Suarez", color= "black",marker= "o", s=110)
                if playerb==7:
                    hb7-=1
                    plt.scatter(pbx7,pby7, label= "Coutinho", color= "black",marker= "o", s=110)
                if playerb==8:
                    hb8-=1
                    plt.scatter(pbx8,pby8, label= "Arthur", color= "black",marker= "o", s=110)
                if playerb==9:
                    hb9-=1
                    plt.scatter(pbx9,pby9, label= "Suarez", color= "black",marker= "o", s=110)
                if playerb==10:
                    hb10-=1
                    plt.scatter(pbx10,pby10, label= "Messi", color= "black",marker= "o", s=110)
                if playerb==11:
                    hb11-=1
                    plt.scatter(pbx11,pby11, label= "Dembele", color= "black",marker= "o", s=110)
                    
                plt.xlabel('Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! ') 
            
                plt.ylabel('Messi! Messi! Messi! Messi! Messi! Messi!') 
             
                plt.title('FIFA PYTHON 18\nPSG(BLUE) VS BARCELONA(RED)')  
            
                plt.show()     
                
                print() 

                continue 
                
        if n==3 and y!=3:
            if playerb<9:
                playerb=playerb+3
                if playerb==1:
                    playerbn='Ter Stegnen'
                    if subb1!=0:
                        playerbn=playerbin1        
                if playerb==2:
                    playerbn='Umtiti'
                    if subb2!=0:
                        playerbn=playerbin2    
                if playerb==3:
                    playerbn='Pique'
                    if subb3!=0:
                        playerbn=playerbin3    
                if playerb==4:
                    playerbn='Rakitic'
                    if subb4!=0:
                        playerbn=playerbin4
                if playerb==5:
                    playerbn='Sergio Busquets'
                    if subb5!=0:
                        playerbn=playerbin5    
                if playerb==6:
                    playerbn='Denis Suarez'
                    if subb6!=0:
                        playerbn=playerbin6    
                if playerb==7:
                    playerbn='Coutinho'
                    if subb7!=0:
                        playerbn=playerbin7    
                if playerb==8:
                    playerbn='Arthur'
                    if subb8!=0:
                        playerbn=playerbin8    
                if playerb==9:
                    playerbn='Suarez'
                    if subb9!=0:
                        playerbn=playerbin9    
                if playerb==10:
                    playerbn='Messi'
                    if subb10!=0:
                        playerbn=playerbin10    
                if playerb==11:
                    playerbn='Dembele'
                    if subb11!=0:
                        playerbn=playerbin11    
                if playerp==1:
                    playerpn='Buffon'
                    if subp1!=0:
                        playerpn=playerpin1
                if playerp==2:
                    playerpn='Thiago Silva'
                    if subp2!=0:
                        playerpn=playerpin2    
                if playerp==3:
                    playerpn='Kimbempe'
                    if subp3!=0:
                        playerpn=playerpin3     
                if playerp==4:
                    playerpn='Meunier'
                    if subp4!=0:
                        playerpn=playerpin4    
                if playerp==5:
                    playerpn='Marquinhos'
                    if subp5!=0:
                        playerpn=playerpin5    
                if playerp==6:
                    playerpn='Verrati'
                    if subp6!=0:
                        playerpn=playerpin6    
                if playerp==7:
                    playerpn='Dani Alves'
                    if subp7!=0:
                        playerpn=playerpin7    
                if playerp==8:
                    playerpn='Rabiot'
                    if subp8!=0:
                        playerpn=playerpin8    
                if playerp==9:
                    playerpn='Cavani'
                    if subp9!=0:
                        playerpn=playerpin9    
                if playerp==10:
                    playerpn='Neymar JR'
                    if subp10!=0:
                        playerpn=playerpin10    
                if playerp==11:
                    playerpn='Mbappe'
                    if subp11!=0:
                        playerpn=playerpin11
                print('Commentatory: Through ball to player',playerbn,'succesful !! what ball man !! WOW!!')
                               
                time=time+1
                print()
                
                print('           [ Time :',time,'min || PSG:',psggoal,'| BAR:',bargoal,']')    
            
                h=2
                ppx1=h*5
                ppx2=random.randint(h*10,h*30)
                ppx3=random.randint(h*10,h*30)
                ppx4=random.randint(h*10,h*30)
                ppx5=random.randint(h*10,h*30)
                ppx6=random.randint(h*35,h*55)
                ppx7=random.randint(h*35,h*55)
                ppx8=random.randint(h*35,h*55)
                ppx9=random.randint(h*60,h*85)
                ppx10=random.randint(h*65,h*90)
                ppx11=random.randint(h*60,h*85)
                
                ppy1=random.randint(h*40,h*60)
                ppy2=random.randint(h*0,h*15)
                ppy3=random.randint(h*30,h*45)
                ppy4=random.randint(h*55,h*70)
                ppy5=random.randint(h*85,h*100)
                ppy6=random.randint(h*0,h*20)
                ppy7=random.randint(h*40,h*60)
                ppy8=random.randint(h*80,h*100)
                ppy9=random.randint(h*15,h*30)
                ppy10=random.randint(h*45,h*55)
                ppy11=random.randint(h*70,h*85)
                
                pbx1=h*95
                pbx2=random.randint(h*70,h*90)
                pbx3=random.randint(h*70,h*90)
                pbx4=random.randint(h*70,h*90)
                pbx5=random.randint(h*70,h*90)
                pbx6=random.randint(h*45,h*65)
                pbx7=random.randint(h*45,h*65)
                pbx8=random.randint(h*45,h*65)
                pbx9=random.randint(h*15,h*40)
                pbx10=random.randint(h*10,h*35)
                pbx11=random.randint(h*15,h*40)
                
                pby1=random.randint(h*40,h*60)
                pby2=random.randint(h*0,h*15)
                pby3=random.randint(h*30,h*45)
                pby4=random.randint(h*55,h*70)
                pby5=random.randint(h*85,h*100)
                pby6=random.randint(h*0,h*20)
                pby7=random.randint(h*40,h*60)
                pby8=random.randint(h*80,h*100)
                pby9=random.randint(h*15,h*30)
                pby10=random.randint(h*45,h*55)
                pby11=random.randint(h*70,h*85)
                
                print('          ',end='')
                lines = [[(h*0, h*35), (h*0, h*65)], [(h*100, h*35), (h*100, h*65)], [(h*50, h*105), (h*50, h*-5)], [(h*-10, h*105), (h*110, h*105)], [(h*-10, h*-5), (h*110, h*-5)], [(h*-10, h*105), (h*-10, h*-5)], [(h*110, h*105), (h*110, h*-5)], [(h*0, h*35), (h*-10, h*35)], [(h*0, h*65), (h*-10, h*65)], [(h*100, h*35), (h*110, h*35)], [(h*100, h*65), (h*110, h*65)]]
                c = np.array([(1, 0, 0, 1), (1, 0, 0, 1), (1, 0, 0, 1)])
                
                lc = mc.LineCollection(lines, colors=c, linewidths=1)
                fig, ax = pl.subplots()
                ax.set_facecolor('xkcd:sky blue')
                ax.set_facecolor((0.8, 1, 0.5))
                ax.add_collection(lc)
                ax.autoscale()
                ax.margins(0.1)
            
                psgx = [ppx2,ppx3,ppx4,ppx5,ppx6,ppx7,ppx8,ppx9,ppx10,ppx11] 
                psgy = [ppy2,ppy3,ppy4,ppy5,ppy6,ppy7,ppy8,ppy9,ppy10,ppy11] 
            
                plt.scatter(ppx1,ppy1,color= "purple",marker= "*", s=100)      # GK edit colour
                plt.scatter(psgx, psgy,color= "blue",marker= "*", s=80)  
             
                barx = [pbx2,pbx3,pbx4,pbx5,pbx6,pbx7,pbx8,pbx9,pbx10,pbx11] 
                bary = [pby2,pby3,pby4,pby5,pby6,pby7,pby8,pby9,pby10,pby11]
            
                plt.scatter(pbx1,pby1,color= "violet",marker= "o", s=100)      # GK edit colour
                plt.scatter(barx, bary, color= "red",marker= "o", s=80)       
                
                if playerb==1:
                    hb1-=1
                    plt.scatter(pbx1,pby1, label= "Ter Stegnen", color= "black",marker= "o", s=110)
                if playerb==2:
                    hb2-=1
                    plt.scatter(pbx2,pby2, label= "Umtiti", color= "black",marker= "o", s=110)
                if playerb==3:
                    hb3-=1
                    plt.scatter(pbx3,pby3, label= "Pique", color= "black",marker= "o", s=110)
                if playerb==4:
                    hb4-=1
                    plt.scatter(pbx4,pby4, label= "Rakitic", color= "black",marker= "o", s=110)
                if playerb==5:
                    hb5-=1
                    plt.scatter(pbx5,pby5, label= "Sergio Busquets", color= "black",marker= "o", s=110)
                if playerb==6:
                    hb6-=1
                    plt.scatter(pbx6,pby6, label= "Denis Suarez", color= "black",marker= "o", s=110)
                if playerb==7:
                    hb7-=1
                    plt.scatter(pbx7,pby7, label= "Coutinho", color= "black",marker= "o", s=110)
                if playerb==8:
                    hb8-=1
                    plt.scatter(pbx8,pby8, label= "Arthur", color= "black",marker= "o", s=110)
                if playerb==9:
                    hb9-=1
                    plt.scatter(pbx9,pby9, label= "Suarez", color= "black",marker= "o", s=110)
                if playerb==10:
                    hb10-=1
                    plt.scatter(pbx10,pby10, label= "Messi", color= "black",marker= "o", s=110)
                if playerb==11:
                    hb11-=1
                    plt.scatter(pbx11,pby11, label= "Dembele", color= "black",marker= "o", s=110)
                    
                plt.xlabel('Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! ') 
            
                plt.ylabel('Messi! Messi! Messi! Messi! Messi! Messi!') 
             
                plt.title('FIFA PYTHON 18\nPSG(BLUE) VS BARCELONA(RED)')  
            
                plt.show()     
                
                print() 

                continue 

            else:
                playerb=playerb-3
                if playerb==1:
                    playerbn='Ter Stegnen'
                    if subb1!=0:
                        playerbn=playerbin1        
                if playerb==2:
                    playerbn='Umtiti'
                    if subb2!=0:
                        playerbn=playerbin2    
                if playerb==3:
                    playerbn='Pique'
                    if subb3!=0:
                        playerbn=playerbin3    
                if playerb==4:
                    playerbn='Rakitic'
                    if subb4!=0:
                        playerbn=playerbin4
                if playerb==5:
                    playerbn='Sergio Busquets'
                    if subb5!=0:
                        playerbn=playerbin5    
                if playerb==6:
                    playerbn='Denis Suarez'
                    if subb6!=0:
                        playerbn=playerbin6    
                if playerb==7:
                    playerbn='Coutinho'
                    if subb7!=0:
                        playerbn=playerbin7    
                if playerb==8:
                    playerbn='Arthur'
                    if subb8!=0:
                        playerbn=playerbin8    
                if playerb==9:
                    playerbn='Suarez'
                    if subb9!=0:
                        playerbn=playerbin9    
                if playerb==10:
                    playerbn='Messi'
                    if subb10!=0:
                        playerbn=playerbin10    
                if playerb==11:
                    playerbn='Dembele'
                    if subb11!=0:
                        playerbn=playerbin11    
                if playerp==1:
                    playerpn='Buffon'
                    if subp1!=0:
                        playerpn=playerpin1
                if playerp==2:
                    playerpn='Thiago Silva'
                    if subp2!=0:
                        playerpn=playerpin2    
                if playerp==3:
                    playerpn='Kimbempe'
                    if subp3!=0:
                        playerpn=playerpin3     
                if playerp==4:
                    playerpn='Meunier'
                    if subp4!=0:
                        playerpn=playerpin4    
                if playerp==5:
                    playerpn='Marquinhos'
                    if subp5!=0:
                        playerpn=playerpin5    
                if playerp==6:
                    playerpn='Verrati'
                    if subp6!=0:
                        playerpn=playerpin6    
                if playerp==7:
                    playerpn='Dani Alves'
                    if subp7!=0:
                        playerpn=playerpin7    
                if playerp==8:
                    playerpn='Rabiot'
                    if subp8!=0:
                        playerpn=playerpin8    
                if playerp==9:
                    playerpn='Cavani'
                    if subp9!=0:
                        playerpn=playerpin9    
                if playerp==10:
                    playerpn='Neymar JR'
                    if subp10!=0:
                        playerpn=playerpin10    
                if playerp==11:
                    playerpn='Mbappe'
                    if subp11!=0:
                        playerpn=playerpin11
                print('Commentatory: Through ball to player',playerbn,'succesful !!')

                time=time+1
                print()
                
                print('           [ Time :',time,'min || PSG:',psggoal,'| BAR:',bargoal,']')    
            
                h=2
                ppx1=h*5
                ppx2=random.randint(h*10,h*30)
                ppx3=random.randint(h*10,h*30)
                ppx4=random.randint(h*10,h*30)
                ppx5=random.randint(h*10,h*30)
                ppx6=random.randint(h*35,h*55)
                ppx7=random.randint(h*35,h*55)
                ppx8=random.randint(h*35,h*55)
                ppx9=random.randint(h*60,h*85)
                ppx10=random.randint(h*65,h*90)
                ppx11=random.randint(h*60,h*85)
                
                ppy1=random.randint(h*40,h*60)
                ppy2=random.randint(h*0,h*15)
                ppy3=random.randint(h*30,h*45)
                ppy4=random.randint(h*55,h*70)
                ppy5=random.randint(h*85,h*100)
                ppy6=random.randint(h*0,h*20)
                ppy7=random.randint(h*40,h*60)
                ppy8=random.randint(h*80,h*100)
                ppy9=random.randint(h*15,h*30)
                ppy10=random.randint(h*45,h*55)
                ppy11=random.randint(h*70,h*85)
                
                pbx1=h*95
                pbx2=random.randint(h*70,h*90)
                pbx3=random.randint(h*70,h*90)
                pbx4=random.randint(h*70,h*90)
                pbx5=random.randint(h*70,h*90)
                pbx6=random.randint(h*45,h*65)
                pbx7=random.randint(h*45,h*65)
                pbx8=random.randint(h*45,h*65)
                pbx9=random.randint(h*15,h*40)
                pbx10=random.randint(h*10,h*35)
                pbx11=random.randint(h*15,h*40)
                
                pby1=random.randint(h*40,h*60)
                pby2=random.randint(h*0,h*15)
                pby3=random.randint(h*30,h*45)
                pby4=random.randint(h*55,h*70)
                pby5=random.randint(h*85,h*100)
                pby6=random.randint(h*0,h*20)
                pby7=random.randint(h*40,h*60)
                pby8=random.randint(h*80,h*100)
                pby9=random.randint(h*15,h*30)
                pby10=random.randint(h*45,h*55)
                pby11=random.randint(h*70,h*85)
                
                print('          ',end='')
                lines = [[(h*0, h*35), (h*0, h*65)], [(h*100, h*35), (h*100, h*65)], [(h*50, h*105), (h*50, h*-5)], [(h*-10, h*105), (h*110, h*105)], [(h*-10, h*-5), (h*110, h*-5)], [(h*-10, h*105), (h*-10, h*-5)], [(h*110, h*105), (h*110, h*-5)], [(h*0, h*35), (h*-10, h*35)], [(h*0, h*65), (h*-10, h*65)], [(h*100, h*35), (h*110, h*35)], [(h*100, h*65), (h*110, h*65)]]
                c = np.array([(1, 0, 0, 1), (1, 0, 0, 1), (1, 0, 0, 1)])
                
                lc = mc.LineCollection(lines, colors=c, linewidths=1)
                fig, ax = pl.subplots()
                ax.set_facecolor('xkcd:sky blue')
                ax.set_facecolor((0.8, 1, 0.5))
                ax.add_collection(lc)
                ax.autoscale()
                ax.margins(0.1)
            
                psgx = [ppx2,ppx3,ppx4,ppx5,ppx6,ppx7,ppx8,ppx9,ppx10,ppx11] 
                psgy = [ppy2,ppy3,ppy4,ppy5,ppy6,ppy7,ppy8,ppy9,ppy10,ppy11] 
            
                plt.scatter(ppx1,ppy1,color= "purple",marker= "*", s=100)      # GK edit colour
                plt.scatter(psgx, psgy,color= "blue",marker= "*", s=80)  
             
                barx = [pbx2,pbx3,pbx4,pbx5,pbx6,pbx7,pbx8,pbx9,pbx10,pbx11] 
                bary = [pby2,pby3,pby4,pby5,pby6,pby7,pby8,pby9,pby10,pby11]
            
                plt.scatter(pbx1,pby1,color= "violet",marker= "o", s=100)      # GK edit colour
                plt.scatter(barx, bary, color= "red",marker= "o", s=80)       
                
                if playerb==1:
                    hb1-=1
                    plt.scatter(pbx1,pby1, label= "Ter Stegnen", color= "black",marker= "o", s=110)
                if playerb==2:
                    hb2-=1
                    plt.scatter(pbx2,pby2, label= "Umtiti", color= "black",marker= "o", s=110)
                if playerb==3:
                    hb3-=1
                    plt.scatter(pbx3,pby3, label= "Pique", color= "black",marker= "o", s=110)
                if playerb==4:
                    hb4-=1
                    plt.scatter(pbx4,pby4, label= "Rakitic", color= "black",marker= "o", s=110)
                if playerb==5:
                    hb5-=1
                    plt.scatter(pbx5,pby5, label= "Sergio Busquets", color= "black",marker= "o", s=110)
                if playerb==6:
                    hb6-=1
                    plt.scatter(pbx6,pby6, label= "Denis Suarez", color= "black",marker= "o", s=110)
                if playerb==7:
                    hb7-=1
                    plt.scatter(pbx7,pby7, label= "Coutinho", color= "black",marker= "o", s=110)
                if playerb==8:
                    hb8-=1
                    plt.scatter(pbx8,pby8, label= "Arthur", color= "black",marker= "o", s=110)
                if playerb==9:
                    hb9-=1
                    plt.scatter(pbx9,pby9, label= "Suarez", color= "black",marker= "o", s=110)
                if playerb==10:
                    hb10-=1
                    plt.scatter(pbx10,pby10, label= "Messi", color= "black",marker= "o", s=110)
                if playerb==11:
                    hb11-=1
                    plt.scatter(pbx11,pby11, label= "Dembele", color= "black",marker= "o", s=110)
                    
                plt.xlabel('Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! ') 
            
                plt.ylabel('Messi! Messi! Messi! Messi! Messi! Messi!') 
             
                plt.title('FIFA PYTHON 18\nPSG(BLUE) VS BARCELONA(RED)')  
            
                plt.show()     
                
                print() 

                continue            
                
        if n==4 and y==4:
            if playerb>8:
                bargoal=bargoal+1
                bar=0
                psg=1
                playerp=10
                print('Commentatory:',playerbn,'scores!!! Goooooal!! Awesome!!! BARCELONA',bargoal,'and PSG',psggoal)
                print('Commentatory: Now Neymar starts...' )
                print()        
                time=time+1
                print()
                
                print('           [ Time :',time,'min || PSG:',psggoal,'| BAR:',bargoal,']')    
            
                h=2
                ppx1=h*5
                ppx2=random.randint(h*10,h*30)
                ppx3=random.randint(h*10,h*30)
                ppx4=random.randint(h*10,h*30)
                ppx5=random.randint(h*10,h*30)
                ppx6=random.randint(h*35,h*55)
                ppx7=random.randint(h*35,h*55)
                ppx8=random.randint(h*35,h*55)
                ppx9=random.randint(h*60,h*85)
                ppx10=random.randint(h*65,h*90)
                ppx11=random.randint(h*60,h*85)
                
                ppy1=random.randint(h*40,h*60)
                ppy2=random.randint(h*0,h*15)
                ppy3=random.randint(h*30,h*45)
                ppy4=random.randint(h*55,h*70)
                ppy5=random.randint(h*85,h*100)
                ppy6=random.randint(h*0,h*20)
                ppy7=random.randint(h*40,h*60)
                ppy8=random.randint(h*80,h*100)
                ppy9=random.randint(h*15,h*30)
                ppy10=random.randint(h*45,h*55)
                ppy11=random.randint(h*70,h*85)
                
                pbx1=h*95
                pbx2=random.randint(h*70,h*90)
                pbx3=random.randint(h*70,h*90)
                pbx4=random.randint(h*70,h*90)
                pbx5=random.randint(h*70,h*90)
                pbx6=random.randint(h*45,h*65)
                pbx7=random.randint(h*45,h*65)
                pbx8=random.randint(h*45,h*65)
                pbx9=random.randint(h*15,h*40)
                pbx10=random.randint(h*10,h*35)
                pbx11=random.randint(h*15,h*40)
                
                pby1=random.randint(h*40,h*60)
                pby2=random.randint(h*0,h*15)
                pby3=random.randint(h*30,h*45)
                pby4=random.randint(h*55,h*70)
                pby5=random.randint(h*85,h*100)
                pby6=random.randint(h*0,h*20)
                pby7=random.randint(h*40,h*60)
                pby8=random.randint(h*80,h*100)
                pby9=random.randint(h*15,h*30)
                pby10=random.randint(h*45,h*55)
                pby11=random.randint(h*70,h*85)
                
                print('          ',end='')
                lines = [[(h*0, h*35), (h*0, h*65)], [(h*100, h*35), (h*100, h*65)], [(h*50, h*105), (h*50, h*-5)], [(h*-10, h*105), (h*110, h*105)], [(h*-10, h*-5), (h*110, h*-5)], [(h*-10, h*105), (h*-10, h*-5)], [(h*110, h*105), (h*110, h*-5)], [(h*0, h*35), (h*-10, h*35)], [(h*0, h*65), (h*-10, h*65)], [(h*100, h*35), (h*110, h*35)], [(h*100, h*65), (h*110, h*65)]]
                c = np.array([(1, 0, 0, 1), (1, 0, 0, 1), (1, 0, 0, 1)])
                
                lc = mc.LineCollection(lines, colors=c, linewidths=1)
                fig, ax = pl.subplots()
                ax.set_facecolor('xkcd:sky blue')
                ax.set_facecolor((0.8, 1, 0.5))
                ax.add_collection(lc)
                ax.autoscale()
                ax.margins(0.1)
            
                psgx = [ppx2,ppx3,ppx4,ppx5,ppx6,ppx7,ppx8,ppx9,ppx10,ppx11] 
                psgy = [ppy2,ppy3,ppy4,ppy5,ppy6,ppy7,ppy8,ppy9,ppy10,ppy11] 
            
                plt.scatter(ppx1,ppy1,color= "purple",marker= "*", s=100)      # GK edit colour
                plt.scatter(psgx, psgy,color= "blue",marker= "*", s=80)  
             
                barx = [pbx2,pbx3,pbx4,pbx5,pbx6,pbx7,pbx8,pbx9,pbx10,pbx11] 
                bary = [pby2,pby3,pby4,pby5,pby6,pby7,pby8,pby9,pby10,pby11]
            
                plt.scatter(pbx1,pby1,color= "violet",marker= "o", s=100)      # GK edit colour
                plt.scatter(barx, bary, color= "red",marker= "o", s=80)       
                
                if playerp==1:
                    hp1=-1
                    plt.scatter(ppx1,ppy1, label= "Buffon", color= "black",marker= "*", s=110)
                if playerp==2:
                    hp2=-1
                    plt.scatter(ppx2,ppy2, label= "Thiago Silva", color= "black",marker= "*", s=110)
                if playerp==3:
                    hp3=-1
                    plt.scatter(ppx3,ppy3, label= "Kimbempe", color= "black",marker= "*", s=110)
                if playerp==4:
                    hp4=-1
                    plt.scatter(ppx4,ppy4, label= "Meunier", color= "black",marker= "*", s=110)
                if playerp==5:
                    hp5=-1
                    plt.scatter(ppx5,ppy5, label= "Marquinhos", color= "black",marker= "*", s=110)
                if playerp==6:
                    hp6=-1
                    plt.scatter(ppx6,ppy6, label= "Verrati", color= "black",marker= "*", s=110)
                if playerp==7:
                    hp7=-1
                    plt.scatter(ppx7,ppy7, label= "Dani Alves", color= "black",marker= "*", s=110)
                if playerp==8:
                    hp8=-1
                    plt.scatter(ppx8,ppy8, label= "Rabiot", color= "black",marker= "*", s=110)
                if playerp==9:
                    hp9=-1
                    plt.scatter(ppx9,ppy9, label= "Cavani", color= "black",marker= "*", s=110)
                if playerp==10:
                    hp10=-1
                    plt.scatter(ppx10,ppy10, label= "Neymar", color= "black",marker= "*", s=110)
                if playerp==11:
                    hp11=-1
                    plt.scatter(ppx11,ppy11, label= "Mbappe", color= "black",marker= "*", s=110)
                    
                plt.xlabel('Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! ') 
            
                plt.ylabel('Messi! Messi! Messi! Messi! Messi! Messi!') 
            
                plt.title('FIFA PYTHON 18\nPSG(BLUE) VS BARCELONA(RED)')  
            
                plt.show()     
                
                print()

                continue

            if playerb<=8:
                psg=1
                bar=0
                playerp=1                
                if playerp==1:
                    playerpn='Buffon'
                    if subp1!=0:
                        playerpn=playerpin1
                print('Commentatory:',playerpin1,'saves it')
                time=time+1
                print()
                
                print('           [ Time :',time,'min || PSG:',psggoal,'| BAR:',bargoal,']')    
            
                h=2
                ppx1=h*5
                ppx2=random.randint(h*10,h*30)
                ppx3=random.randint(h*10,h*30)
                ppx4=random.randint(h*10,h*30)
                ppx5=random.randint(h*10,h*30)
                ppx6=random.randint(h*35,h*55)
                ppx7=random.randint(h*35,h*55)
                ppx8=random.randint(h*35,h*55)
                ppx9=random.randint(h*60,h*85)
                ppx10=random.randint(h*65,h*90)
                ppx11=random.randint(h*60,h*85)
                
                ppy1=random.randint(h*40,h*60)
                ppy2=random.randint(h*0,h*15)
                ppy3=random.randint(h*30,h*45)
                ppy4=random.randint(h*55,h*70)
                ppy5=random.randint(h*85,h*100)
                ppy6=random.randint(h*0,h*20)
                ppy7=random.randint(h*40,h*60)
                ppy8=random.randint(h*80,h*100)
                ppy9=random.randint(h*15,h*30)
                ppy10=random.randint(h*45,h*55)
                ppy11=random.randint(h*70,h*85)
                
                pbx1=h*95
                pbx2=random.randint(h*70,h*90)
                pbx3=random.randint(h*70,h*90)
                pbx4=random.randint(h*70,h*90)
                pbx5=random.randint(h*70,h*90)
                pbx6=random.randint(h*45,h*65)
                pbx7=random.randint(h*45,h*65)
                pbx8=random.randint(h*45,h*65)
                pbx9=random.randint(h*15,h*40)
                pbx10=random.randint(h*10,h*35)
                pbx11=random.randint(h*15,h*40)
                
                pby1=random.randint(h*40,h*60)
                pby2=random.randint(h*0,h*15)
                pby3=random.randint(h*30,h*45)
                pby4=random.randint(h*55,h*70)
                pby5=random.randint(h*85,h*100)
                pby6=random.randint(h*0,h*20)
                pby7=random.randint(h*40,h*60)
                pby8=random.randint(h*80,h*100)
                pby9=random.randint(h*15,h*30)
                pby10=random.randint(h*45,h*55)
                pby11=random.randint(h*70,h*85)
                
                print('          ',end='')
                lines = [[(h*0, h*35), (h*0, h*65)], [(h*100, h*35), (h*100, h*65)], [(h*50, h*105), (h*50, h*-5)], [(h*-10, h*105), (h*110, h*105)], [(h*-10, h*-5), (h*110, h*-5)], [(h*-10, h*105), (h*-10, h*-5)], [(h*110, h*105), (h*110, h*-5)], [(h*0, h*35), (h*-10, h*35)], [(h*0, h*65), (h*-10, h*65)], [(h*100, h*35), (h*110, h*35)], [(h*100, h*65), (h*110, h*65)]]
                c = np.array([(1, 0, 0, 1), (1, 0, 0, 1), (1, 0, 0, 1)])
                
                lc = mc.LineCollection(lines, colors=c, linewidths=1)
                fig, ax = pl.subplots()
                ax.set_facecolor('xkcd:sky blue')
                ax.set_facecolor((0.8, 1, 0.5))
                ax.add_collection(lc)
                ax.autoscale()
                ax.margins(0.1)
            
                psgx = [ppx2,ppx3,ppx4,ppx5,ppx6,ppx7,ppx8,ppx9,ppx10,ppx11] 
                psgy = [ppy2,ppy3,ppy4,ppy5,ppy6,ppy7,ppy8,ppy9,ppy10,ppy11] 
            
                plt.scatter(ppx1,ppy1,color= "purple",marker= "*", s=100)      # GK edit colour
                plt.scatter(psgx, psgy,color= "blue",marker= "*", s=80)  
             
                barx = [pbx2,pbx3,pbx4,pbx5,pbx6,pbx7,pbx8,pbx9,pbx10,pbx11] 
                bary = [pby2,pby3,pby4,pby5,pby6,pby7,pby8,pby9,pby10,pby11]
            
                plt.scatter(pbx1,pby1,color= "violet",marker= "o", s=100)      # GK edit colour
                plt.scatter(barx, bary, color= "red",marker= "o", s=80)       
                
                if playerp==1:
                    hp1=-1
                    plt.scatter(ppx1,ppy1, label= "Buffon", color= "black",marker= "*", s=110)
                if playerp==2:
                    hp2=-1
                    plt.scatter(ppx2,ppy2, label= "Thiago Silva", color= "black",marker= "*", s=110)
                if playerp==3:
                    hp3=-1
                    plt.scatter(ppx3,ppy3, label= "Kimbempe", color= "black",marker= "*", s=110)
                if playerp==4:
                    hp4=-1
                    plt.scatter(ppx4,ppy4, label= "Meunier", color= "black",marker= "*", s=110)
                if playerp==5:
                    hp5=-1
                    plt.scatter(ppx5,ppy5, label= "Marquinhos", color= "black",marker= "*", s=110)
                if playerp==6:
                    hp6=-1
                    plt.scatter(ppx6,ppy6, label= "Verrati", color= "black",marker= "*", s=110)
                if playerp==7:
                    hp7=-1
                    plt.scatter(ppx7,ppy7, label= "Dani Alves", color= "black",marker= "*", s=110)
                if playerp==8:
                    hp8=-1
                    plt.scatter(ppx8,ppy8, label= "Rabiot", color= "black",marker= "*", s=110)
                if playerp==9:
                    hp9=-1
                    plt.scatter(ppx9,ppy9, label= "Cavani", color= "black",marker= "*", s=110)
                if playerp==10:
                    hp10=-1
                    plt.scatter(ppx10,ppy10, label= "Neymar", color= "black",marker= "*", s=110)
                if playerp==11:
                    hp11=-1
                    plt.scatter(ppx11,ppy11, label= "Mbappe", color= "black",marker= "*", s=110)
                    
                plt.xlabel('Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! ') 
            
                plt.ylabel('Messi! Messi! Messi! Messi! Messi! Messi!') 
            
                plt.title('FIFA PYTHON 18\nPSG(BLUE) VS BARCELONA(RED)')  
            
                plt.show()     
                
                print()

                continue
                    
            if n==4 and y!=4:
                bar=0
                psg=1
                playerp=1
                if playerp==1:
                    playerpn='Buffon'
                    if subp1!=0:
                        playerpn=playerpin1
                print('Commentatory:',playerpin1,'saves it')
                time=time+1
                print()
                
                print('           [ Time :',time,'min || PSG:',psggoal,'| BAR:',bargoal,']')    
            
                h=2
                ppx1=h*5
                ppx2=random.randint(h*10,h*30)
                ppx3=random.randint(h*10,h*30)
                ppx4=random.randint(h*10,h*30)
                ppx5=random.randint(h*10,h*30)
                ppx6=random.randint(h*35,h*55)
                ppx7=random.randint(h*35,h*55)
                ppx8=random.randint(h*35,h*55)
                ppx9=random.randint(h*60,h*85)
                ppx10=random.randint(h*65,h*90)
                ppx11=random.randint(h*60,h*85)
                
                ppy1=random.randint(h*40,h*60)
                ppy2=random.randint(h*0,h*15)
                ppy3=random.randint(h*30,h*45)
                ppy4=random.randint(h*55,h*70)
                ppy5=random.randint(h*85,h*100)
                ppy6=random.randint(h*0,h*20)
                ppy7=random.randint(h*40,h*60)
                ppy8=random.randint(h*80,h*100)
                ppy9=random.randint(h*15,h*30)
                ppy10=random.randint(h*45,h*55)
                ppy11=random.randint(h*70,h*85)
                
                pbx1=h*95
                pbx2=random.randint(h*70,h*90)
                pbx3=random.randint(h*70,h*90)
                pbx4=random.randint(h*70,h*90)
                pbx5=random.randint(h*70,h*90)
                pbx6=random.randint(h*45,h*65)
                pbx7=random.randint(h*45,h*65)
                pbx8=random.randint(h*45,h*65)
                pbx9=random.randint(h*15,h*40)
                pbx10=random.randint(h*10,h*35)
                pbx11=random.randint(h*15,h*40)
                
                pby1=random.randint(h*40,h*60)
                pby2=random.randint(h*0,h*15)
                pby3=random.randint(h*30,h*45)
                pby4=random.randint(h*55,h*70)
                pby5=random.randint(h*85,h*100)
                pby6=random.randint(h*0,h*20)
                pby7=random.randint(h*40,h*60)
                pby8=random.randint(h*80,h*100)
                pby9=random.randint(h*15,h*30)
                pby10=random.randint(h*45,h*55)
                pby11=random.randint(h*70,h*85)
                
                print('          ',end='')
                lines = [[(h*0, h*35), (h*0, h*65)], [(h*100, h*35), (h*100, h*65)], [(h*50, h*105), (h*50, h*-5)], [(h*-10, h*105), (h*110, h*105)], [(h*-10, h*-5), (h*110, h*-5)], [(h*-10, h*105), (h*-10, h*-5)], [(h*110, h*105), (h*110, h*-5)], [(h*0, h*35), (h*-10, h*35)], [(h*0, h*65), (h*-10, h*65)], [(h*100, h*35), (h*110, h*35)], [(h*100, h*65), (h*110, h*65)]]
                c = np.array([(1, 0, 0, 1), (1, 0, 0, 1), (1, 0, 0, 1)])
                
                lc = mc.LineCollection(lines, colors=c, linewidths=1)
                fig, ax = pl.subplots()
                ax.set_facecolor('xkcd:sky blue')
                ax.set_facecolor((0.8, 1, 0.5))
                ax.add_collection(lc)
                ax.autoscale()
                ax.margins(0.1)
            
                psgx = [ppx2,ppx3,ppx4,ppx5,ppx6,ppx7,ppx8,ppx9,ppx10,ppx11] 
                psgy = [ppy2,ppy3,ppy4,ppy5,ppy6,ppy7,ppy8,ppy9,ppy10,ppy11] 
            
                plt.scatter(ppx1,ppy1,color= "purple",marker= "*", s=100)      # GK edit colour
                plt.scatter(psgx, psgy,color= "blue",marker= "*", s=80)  
             
                barx = [pbx2,pbx3,pbx4,pbx5,pbx6,pbx7,pbx8,pbx9,pbx10,pbx11] 
                bary = [pby2,pby3,pby4,pby5,pby6,pby7,pby8,pby9,pby10,pby11]
            
                plt.scatter(pbx1,pby1,color= "violet",marker= "o", s=100)      # GK edit colour
                plt.scatter(barx, bary, color= "red",marker= "o", s=80)       
                
                if playerp==1:
                    hp1=-1
                    plt.scatter(ppx1,ppy1, label= "Buffon", color= "black",marker= "*", s=110)
                if playerp==2:
                    hp2=-1
                    plt.scatter(ppx2,ppy2, label= "Thiago Silva", color= "black",marker= "*", s=110)
                if playerp==3:
                    hp3=-1
                    plt.scatter(ppx3,ppy3, label= "Kimbempe", color= "black",marker= "*", s=110)
                if playerp==4:
                    hp4=-1
                    plt.scatter(ppx4,ppy4, label= "Meunier", color= "black",marker= "*", s=110)
                if playerp==5:
                    hp5=-1
                    plt.scatter(ppx5,ppy5, label= "Marquinhos", color= "black",marker= "*", s=110)
                if playerp==6:
                    hp6=-1
                    plt.scatter(ppx6,ppy6, label= "Verrati", color= "black",marker= "*", s=110)
                if playerp==7:
                    hp7=-1
                    plt.scatter(ppx7,ppy7, label= "Dani Alves", color= "black",marker= "*", s=110)
                if playerp==8:
                    hp8=-1
                    plt.scatter(ppx8,ppy8, label= "Rabiot", color= "black",marker= "*", s=110)
                if playerp==9:
                    hp9=-1
                    plt.scatter(ppx9,ppy9, label= "Cavani", color= "black",marker= "*", s=110)
                if playerp==10:
                    hp10=-1
                    plt.scatter(ppx10,ppy10, label= "Neymar", color= "black",marker= "*", s=110)
                if playerp==11:
                    hp11=-1
                    plt.scatter(ppx11,ppy11, label= "Mbappe", color= "black",marker= "*", s=110)
                    
                plt.xlabel('Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! ') 
            
                plt.ylabel('Messi! Messi! Messi! Messi! Messi! Messi!') 
            
                plt.title('FIFA PYTHON 18\nPSG(BLUE) VS BARCELONA(RED)')  
            
                plt.show()     
                
                print()

                continue
            
        if n!=4 and n==y :
                bar=0
                psg=1
                playerp=12-playerb
                if playerb==1:
                    playerbn='Ter Stegnen'
                    if subb1!=0:
                        playerbn=playerbin1        
                if playerb==2:
                    playerbn='Umtiti'
                    if subb2!=0:
                        playerbn=playerbin2    
                if playerb==3:
                    playerbn='Pique'
                    if subb3!=0:
                        playerbn=playerbin3    
                if playerb==4:
                    playerbn='Rakitic'
                    if subb4!=0:
                        playerbn=playerbin4
                if playerb==5:
                    playerbn='Sergio Busquets'
                    if subb5!=0:
                        playerbn=playerbin5    
                if playerb==6:
                    playerbn='Denis Suarez'
                    if subb6!=0:
                        playerbn=playerbin6    
                if playerb==7:
                    playerbn='Coutinho'
                    if subb7!=0:
                        playerbn=playerbin7    
                if playerb==8:
                    playerbn='Arthur'
                    if subb8!=0:
                        playerbn=playerbin8    
                if playerb==9:
                    playerbn='Suarez'
                    if subb9!=0:
                        playerbn=playerbin9    
                if playerb==10:
                    playerbn='Messi'
                    if subb10!=0:
                        playerbn=playerbin10    
                if playerb==11:
                    playerbn='Dembele'
                    if subb11!=0:
                        playerbn=playerbin11    
                if playerp==1:
                    playerpn='Buffon'
                    if subp1!=0:
                        playerpn=playerpin1
                if playerp==2:
                    playerpn='Thiago Silva'
                    if subp2!=0:
                        playerpn=playerpin2    
                if playerp==3:
                    playerpn='Kimbempe'
                    if subp3!=0:
                        playerpn=playerpin3     
                if playerp==4:
                    playerpn='Meunier'
                    if subp4!=0:
                        playerpn=playerpin4    
                if playerp==5:
                    playerpn='Marquinhos'
                    if subp5!=0:
                        playerpn=playerpin5    
                if playerp==6:
                    playerpn='Verrati'
                    if subp6!=0:
                        playerpn=playerpin6    
                if playerp==7:
                    playerpn='Dani Alves'
                    if subp7!=0:
                        playerpn=playerpin7    
                if playerp==8:
                    playerpn='Rabiot'
                    if subp8!=0:
                        playerpn=playerpin8    
                if playerp==9:
                    playerpn='Cavani'
                    if subp9!=0:
                        playerpn=playerpin9    
                if playerp==10:
                    playerpn='Neymar JR'
                    if subp10!=0:
                        playerpn=playerpin10    
                if playerp==11:
                    playerpn='Mbappe'
                    if subp11!=0:
                        playerpn=playerpin11        
                print('Commentatory: Ball intercepted by player',playerpn,'of PSG')              
                
                time=time+1
                print()
                
                print('           [ Time :',time,'min || PSG:',psggoal,'| BAR:',bargoal,']')    
            
                h=2
                ppx1=h*5
                ppx2=random.randint(h*10,h*30)
                ppx3=random.randint(h*10,h*30)
                ppx4=random.randint(h*10,h*30)
                ppx5=random.randint(h*10,h*30)
                ppx6=random.randint(h*35,h*55)
                ppx7=random.randint(h*35,h*55)
                ppx8=random.randint(h*35,h*55)
                ppx9=random.randint(h*60,h*85)
                ppx10=random.randint(h*65,h*90)
                ppx11=random.randint(h*60,h*85)
                
                ppy1=random.randint(h*40,h*60)
                ppy2=random.randint(h*0,h*15)
                ppy3=random.randint(h*30,h*45)
                ppy4=random.randint(h*55,h*70)
                ppy5=random.randint(h*85,h*100)
                ppy6=random.randint(h*0,h*20)
                ppy7=random.randint(h*40,h*60)
                ppy8=random.randint(h*80,h*100)
                ppy9=random.randint(h*15,h*30)
                ppy10=random.randint(h*45,h*55)
                ppy11=random.randint(h*70,h*85)
                
                pbx1=h*95
                pbx2=random.randint(h*70,h*90)
                pbx3=random.randint(h*70,h*90)
                pbx4=random.randint(h*70,h*90)
                pbx5=random.randint(h*70,h*90)
                pbx6=random.randint(h*45,h*65)
                pbx7=random.randint(h*45,h*65)
                pbx8=random.randint(h*45,h*65)
                pbx9=random.randint(h*15,h*40)
                pbx10=random.randint(h*10,h*35)
                pbx11=random.randint(h*15,h*40)
                
                pby1=random.randint(h*40,h*60)
                pby2=random.randint(h*0,h*15)
                pby3=random.randint(h*30,h*45)
                pby4=random.randint(h*55,h*70)
                pby5=random.randint(h*85,h*100)
                pby6=random.randint(h*0,h*20)
                pby7=random.randint(h*40,h*60)
                pby8=random.randint(h*80,h*100)
                pby9=random.randint(h*15,h*30)
                pby10=random.randint(h*45,h*55)
                pby11=random.randint(h*70,h*85)
                
                print('          ',end='')
                lines = [[(h*0, h*35), (h*0, h*65)], [(h*100, h*35), (h*100, h*65)], [(h*50, h*105), (h*50, h*-5)], [(h*-10, h*105), (h*110, h*105)], [(h*-10, h*-5), (h*110, h*-5)], [(h*-10, h*105), (h*-10, h*-5)], [(h*110, h*105), (h*110, h*-5)], [(h*0, h*35), (h*-10, h*35)], [(h*0, h*65), (h*-10, h*65)], [(h*100, h*35), (h*110, h*35)], [(h*100, h*65), (h*110, h*65)]]
                c = np.array([(1, 0, 0, 1), (1, 0, 0, 1), (1, 0, 0, 1)])
                
                lc = mc.LineCollection(lines, colors=c, linewidths=1)
                fig, ax = pl.subplots()
                ax.set_facecolor('xkcd:sky blue')
                ax.set_facecolor((0.8, 1, 0.5))
                ax.add_collection(lc)
                ax.autoscale()
                ax.margins(0.1)
            
                psgx = [ppx2,ppx3,ppx4,ppx5,ppx6,ppx7,ppx8,ppx9,ppx10,ppx11] 
                psgy = [ppy2,ppy3,ppy4,ppy5,ppy6,ppy7,ppy8,ppy9,ppy10,ppy11] 
            
                plt.scatter(ppx1,ppy1,color= "purple",marker= "*", s=100)      # GK edit colour
                plt.scatter(psgx, psgy,color= "blue",marker= "*", s=80)  
            
                barx = [pbx2,pbx3,pbx4,pbx5,pbx6,pbx7,pbx8,pbx9,pbx10,pbx11] 
                bary = [pby2,pby3,pby4,pby5,pby6,pby7,pby8,pby9,pby10,pby11]
            
                plt.scatter(pbx1,pby1,color= "violet",marker= "o", s=100)      # GK edit colour
                plt.scatter(barx, bary, color= "red",marker= "o", s=80)       
                
                if playerp==1:
                    hp1=-1
                    plt.scatter(ppx1,ppy1, label= "Buffon", color= "black",marker= "*", s=110)
                if playerp==2:
                    hp2=-1
                    plt.scatter(ppx2,ppy2, label= "Thiago Silva", color= "black",marker= "*", s=110)
                if playerp==3:
                    hp3=-1
                    plt.scatter(ppx3,ppy3, label= "Kimbempe", color= "black",marker= "*", s=110)
                if playerp==4:
                    hp4=-1
                    plt.scatter(ppx4,ppy4, label= "Meunier", color= "black",marker= "*", s=110)
                if playerp==5:
                    hp5=-1
                    plt.scatter(ppx5,ppy5, label= "Marquinhos", color= "black",marker= "*", s=110)
                if playerp==6:
                    hp6=-1
                    plt.scatter(ppx6,ppy6, label= "Verrati", color= "black",marker= "*", s=110)
                if playerp==7:
                    hp7=-1
                    plt.scatter(ppx7,ppy7, label= "Dani Alves", color= "black",marker= "*", s=110)
                if playerp==8:
                    hp8=-1
                    plt.scatter(ppx8,ppy8, label= "Rabiot", color= "black",marker= "*", s=110)
                if playerp==9:
                    hp9=-1
                    plt.scatter(ppx9,ppy9, label= "Cavani", color= "black",marker= "*", s=110)
                if playerp==10:
                    hp10=-1
                    plt.scatter(ppx10,ppy10, label= "Neymar", color= "black",marker= "*", s=110)
                if playerp==11:
                    hp11=-1
                    plt.scatter(ppx11,ppy11, label= "Mbappe", color= "black",marker= "*", s=110)
                    
                plt.xlabel('Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! ') 
            
                plt.ylabel('Messi! Messi! Messi! Messi! Messi! Messi!') 
            
                plt.title('FIFA PYTHON 18\nPSG(BLUE) VS BARCELONA(RED)')  
            
                plt.show()     
                
                print()

                continue
        
        if m!='s' and m!='c' and m!='tb' and m!='p' and m!='sub' and m!='skill' and m!='skills' and m!='0' and m!='2' and m!='4' and m!='6' and m!='7' and m!='8' and m!='9':
            bar=0
            psg=1
            playerp=10
            time=time+1
            print()
            
            print('           [ Time :',time,'min || PSG:',psggoal,'| BAR:',bargoal,']')    
        
            h=2
            ppx1=h*5
            ppx2=random.randint(h*50,h*60)
            ppx3=random.randint(h*50,h*60)
            ppx4=random.randint(h*50,h*60)
            ppx5=random.randint(h*50,h*60)
            ppx6=random.randint(h*50,h*60)
            ppx7=random.randint(h*50,h*60)
            ppx8=random.randint(h*50,h*60)
            ppx9=random.randint(h*50,h*60)
            ppx10=random.randint(h*50,h*60)
            ppx11=random.randint(h*50,h*60)
            
            ppy1=random.randint(h*40,h*60)
            ppy2=random.randint(h*0,h*15)
            ppy3=random.randint(h*30,h*45)
            ppy4=random.randint(h*55,h*70)
            ppy5=random.randint(h*85,h*100)
            ppy6=random.randint(h*0,h*20)
            ppy7=random.randint(h*40,h*60)
            ppy8=random.randint(h*80,h*100)
            ppy9=random.randint(h*15,h*30)
            ppy10=random.randint(h*45,h*55)
            ppy11=random.randint(h*70,h*85)
            
            pbx1=h*95
            pbx2=random.randint(h*50,h*60)
            pbx3=random.randint(h*50,h*60)
            pbx4=random.randint(h*50,h*60)
            pbx5=random.randint(h*50,h*60)
            pbx6=random.randint(h*50,h*60)
            pbx7=random.randint(h*50,h*60)
            pbx8=random.randint(h*50,h*60)
            pbx9=random.randint(h*50,h*60)
            pbx10=h*80
            pbx11=random.randint(h*50,h*60)
            
            pby1=random.randint(h*40,h*60)
            pby2=random.randint(h*0,h*15)
            pby3=random.randint(h*30,h*45)
            pby4=random.randint(h*55,h*70)
            pby5=random.randint(h*85,h*100)
            pby6=random.randint(h*0,h*20)
            pby7=random.randint(h*40,h*60)
            pby8=random.randint(h*80,h*100)
            pby9=random.randint(h*15,h*30)
            pby10=h*50
            pby11=random.randint(h*70,h*85)
            
            print('          ',end='')
            lines = [[(h*0, h*35), (h*0, h*65)], [(h*100, h*35), (h*100, h*65)], [(h*50, h*105), (h*50, h*-5)], [(h*-10, h*105), (h*110, h*105)], [(h*-10, h*-5), (h*110, h*-5)], [(h*-10, h*105), (h*-10, h*-5)], [(h*110, h*105), (h*110, h*-5)], [(h*0, h*35), (h*-10, h*35)], [(h*0, h*65), (h*-10, h*65)], [(h*100, h*35), (h*110, h*35)], [(h*100, h*65), (h*110, h*65)]]
            c = np.array([(1, 0, 0, 1), (1, 0, 0, 1), (1, 0, 0, 1)])
            
            lc = mc.LineCollection(lines, colors=c, linewidths=1)
            fig, ax = pl.subplots()
            ax.set_facecolor('xkcd:sky blue')
            ax.set_facecolor((0.8, 1, 0.5))
            ax.add_collection(lc)
            ax.autoscale()
            ax.margins(0.1)
        
            psgx = [ppx2,ppx3,ppx4,ppx5,ppx6,ppx7,ppx8,ppx9,ppx10,ppx11] 
            psgy = [ppy2,ppy3,ppy4,ppy5,ppy6,ppy7,ppy8,ppy9,ppy10,ppy11] 
        
            plt.scatter(ppx1,ppy1,color= "purple",marker= "*", s=100)      # GK edit colour
            plt.scatter(psgx, psgy,color= "blue",marker= "*", s=80)  
         
            barx = [pbx2,pbx3,pbx4,pbx5,pbx6,pbx7,pbx8,pbx9,pbx10,pbx11] 
            bary = [pby2,pby3,pby4,pby5,pby6,pby7,pby8,pby9,pby10,pby11]
        
            plt.scatter(pbx1,pby1,color= "violet",marker= "o", s=100)      # GK edit colour
            plt.scatter(barx, bary, color= "red",marker= "o", s=80)      
                    
            if playerp==1:
                plt.scatter(ppx1,ppy1, label= "Buffon", color= "black",marker= "*", s=110)
            if playerp==2:
                plt.scatter(ppx2,ppy2, label= "Thiago Silva", color= "black",marker= "*", s=110)
            if playerp==3:
                plt.scatter(ppx3,ppy3, label= "Kimbempe", color= "black",marker= "*", s=110)
            if playerp==4:
                plt.scatter(ppx4,ppy4, label= "Meunier", color= "black",marker= "*", s=110)
            if playerp==5:
                plt.scatter(ppx5,ppy5, label= "Marquinhos", color= "black",marker= "*", s=110)
            if playerp==6:
                plt.scatter(ppx6,ppy6, label= "Verrati", color= "black",marker= "*", s=110)
            if playerp==7:
                plt.scatter(ppx7,ppy7, label= "Dani Alves", color= "black",marker= "*", s=110)
            if playerp==8:
                plt.scatter(ppx8,ppy8, label= "Rabiot", color= "black",marker= "*", s=110)
            if playerp==9:
                plt.scatter(ppx9,ppy9, label= "Cavani", color= "black",marker= "*", s=110)
            if playerp==10:
                plt.scatter(ppx10,ppy10, label= "Neymar JR", color= "black",marker= "*", s=110)
            if playerp==11:
                plt.scatter(ppx11,ppy11, label= "Mbappe", color= "black",marker= "*", s=110)
                
            plt.xlabel('Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! ') 
        
            plt.ylabel('Messi! Messi! Messi! Messi! Messi! Messi!') 
         
            plt.title('FIFA PYTHON 18\nPSG(BLUE) VS BARCELONA(RED)')  
        
            plt.show()     
            
            print()
            
            print('Foul!! Penalty awarded to PSG !')
            print('Neymar is taking the penalty > (l or r)')
            freekick=input('>>>')
            g=random.randint(0,1)
            if freekick=='l' and g==0:
                psggoal=psggoal+1
                bar=1
                psg=0
                playerb=10
                print('Commentatory: Neymar JR scores!!! Goooooal!! Awesome!!! BARCELONA',bargoal,'and PSG',psggoal)
                print('Commentatory: Now Messi starts...' )
                print()
                time=time+1
                print()
                
                print('           [ Time :',time,'min || PSG:',psggoal,'| BAR:',bargoal,']')    
            
                h=2
                ppx1=h*5
                ppx2=random.randint(h*10,h*30)
                ppx3=random.randint(h*10,h*30)
                ppx4=random.randint(h*10,h*30)
                ppx5=random.randint(h*10,h*30)
                ppx6=random.randint(h*35,h*55)
                ppx7=random.randint(h*35,h*55)
                ppx8=random.randint(h*35,h*55)
                ppx9=random.randint(h*60,h*85)
                ppx10=random.randint(h*65,h*90)
                ppx11=random.randint(h*60,h*85)
                
                ppy1=random.randint(h*40,h*60)
                ppy2=random.randint(h*0,h*15)
                ppy3=random.randint(h*30,h*45)
                ppy4=random.randint(h*55,h*70)
                ppy5=random.randint(h*85,h*100)
                ppy6=random.randint(h*0,h*20)
                ppy7=random.randint(h*40,h*60)
                ppy8=random.randint(h*80,h*100)
                ppy9=random.randint(h*15,h*30)
                ppy10=random.randint(h*45,h*55)
                ppy11=random.randint(h*70,h*85)
                
                pbx1=h*95
                pbx2=random.randint(h*70,h*90)
                pbx3=random.randint(h*70,h*90)
                pbx4=random.randint(h*70,h*90)
                pbx5=random.randint(h*70,h*90)
                pbx6=random.randint(h*45,h*65)
                pbx7=random.randint(h*45,h*65)
                pbx8=random.randint(h*45,h*65)
                pbx9=random.randint(h*15,h*40)
                pbx10=random.randint(h*10,h*35)
                pbx11=random.randint(h*15,h*40)
                
                pby1=random.randint(h*40,h*60)
                pby2=random.randint(h*0,h*15)
                pby3=random.randint(h*30,h*45)
                pby4=random.randint(h*55,h*70)
                pby5=random.randint(h*85,h*100)
                pby6=random.randint(h*0,h*20)
                pby7=random.randint(h*40,h*60)
                pby8=random.randint(h*80,h*100)
                pby9=random.randint(h*15,h*30)
                pby10=random.randint(h*45,h*55)
                pby11=random.randint(h*70,h*85)
                
                print('          ',end='')
                lines = [[(h*0, h*35), (h*0, h*65)], [(h*100, h*35), (h*100, h*65)], [(h*50, h*105), (h*50, h*-5)], [(h*-10, h*105), (h*110, h*105)], [(h*-10, h*-5), (h*110, h*-5)], [(h*-10, h*105), (h*-10, h*-5)], [(h*110, h*105), (h*110, h*-5)], [(h*0, h*35), (h*-10, h*35)], [(h*0, h*65), (h*-10, h*65)], [(h*100, h*35), (h*110, h*35)], [(h*100, h*65), (h*110, h*65)]]
                c = np.array([(1, 0, 0, 1), (1, 0, 0, 1), (1, 0, 0, 1)])
                
                lc = mc.LineCollection(lines, colors=c, linewidths=1)
                fig, ax = pl.subplots()
                ax.set_facecolor('xkcd:sky blue')
                ax.set_facecolor((0.8, 1, 0.5))
                ax.add_collection(lc)
                ax.autoscale()
                ax.margins(0.1)
            
                psgx = [ppx2,ppx3,ppx4,ppx5,ppx6,ppx7,ppx8,ppx9,ppx10,ppx11] 
                psgy = [ppy2,ppy3,ppy4,ppy5,ppy6,ppy7,ppy8,ppy9,ppy10,ppy11] 
            
                plt.scatter(ppx1,ppy1,color= "purple",marker= "*", s=100)      # GK edit colour
                plt.scatter(psgx, psgy,color= "blue",marker= "*", s=80)  
             
                barx = [pbx2,pbx3,pbx4,pbx5,pbx6,pbx7,pbx8,pbx9,pbx10,pbx11] 
                bary = [pby2,pby3,pby4,pby5,pby6,pby7,pby8,pby9,pby10,pby11]
            
                plt.scatter(pbx1,pby1,color= "violet",marker= "o", s=100)      # GK edit colour
                plt.scatter(barx, bary, color= "red",marker= "o", s=80)       
                
                if playerb==1:
                    hb1-=1
                    plt.scatter(pbx1,pby1, label= "Ter Stegnen", color= "black",marker= "o", s=110)
                if playerb==2:
                    hb2-=1
                    plt.scatter(pbx2,pby2, label= "Umtiti", color= "black",marker= "o", s=110)
                if playerb==3:
                    hb3-=1
                    plt.scatter(pbx3,pby3, label= "Pique", color= "black",marker= "o", s=110)
                if playerb==4:
                    hb4-=1
                    plt.scatter(pbx4,pby4, label= "Rakitic", color= "black",marker= "o", s=110)
                if playerb==5:
                    hb5-=1
                    plt.scatter(pbx5,pby5, label= "Sergio Busquets", color= "black",marker= "o", s=110)
                if playerb==6:
                    hb6-=1
                    plt.scatter(pbx6,pby6, label= "Denis Suarez", color= "black",marker= "o", s=110)
                if playerb==7:
                    hb7-=1
                    plt.scatter(pbx7,pby7, label= "Coutinho", color= "black",marker= "o", s=110)
                if playerb==8:
                    hb8-=1
                    plt.scatter(pbx8,pby8, label= "Arthur", color= "black",marker= "o", s=110)
                if playerb==9:
                    hb9-=1
                    plt.scatter(pbx9,pby9, label= "Suarez", color= "black",marker= "o", s=110)
                if playerb==10:
                    hb10-=1
                    plt.scatter(pbx10,pby10, label= "Messi", color= "black",marker= "o", s=110)
                if playerb==11:
                    hb11-=1
                    plt.scatter(pbx11,pby11, label= "Dembele", color= "black",marker= "o", s=110)
                    
                plt.xlabel('Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! ') 
            
                plt.ylabel('Messi! Messi! Messi! Messi! Messi! Messi!') 
             
                plt.title('FIFA PYTHON 18\nPSG(BLUE) VS BARCELONA(RED)')  
            
                plt.show()     
                
                print()
            if freekick=='r' and g==1:
                psggoal=psggoal+1
                bar=1
                psg=0
                playerb=10
                print('Commentatory: Neymar JR scores!!! Goooooal!! Awesome!!! BARCELONA',bargoal,'and PSG',psggoal)
                print('Commentatory: Now Messi starts...' )
                print()
                time=time+1
                print()
                
                print('           [ Time :',time,'min || PSG:',psggoal,'| BAR:',bargoal,']')    
            
                h=2
                ppx1=h*5
                ppx2=random.randint(h*10,h*30)
                ppx3=random.randint(h*10,h*30)
                ppx4=random.randint(h*10,h*30)
                ppx5=random.randint(h*10,h*30)
                ppx6=random.randint(h*35,h*55)
                ppx7=random.randint(h*35,h*55)
                ppx8=random.randint(h*35,h*55)
                ppx9=random.randint(h*60,h*85)
                ppx10=random.randint(h*65,h*90)
                ppx11=random.randint(h*60,h*85)
                
                ppy1=random.randint(h*40,h*60)
                ppy2=random.randint(h*0,h*15)
                ppy3=random.randint(h*30,h*45)
                ppy4=random.randint(h*55,h*70)
                ppy5=random.randint(h*85,h*100)
                ppy6=random.randint(h*0,h*20)
                ppy7=random.randint(h*40,h*60)
                ppy8=random.randint(h*80,h*100)
                ppy9=random.randint(h*15,h*30)
                ppy10=random.randint(h*45,h*55)
                ppy11=random.randint(h*70,h*85)
                
                pbx1=h*95
                pbx2=random.randint(h*70,h*90)
                pbx3=random.randint(h*70,h*90)
                pbx4=random.randint(h*70,h*90)
                pbx5=random.randint(h*70,h*90)
                pbx6=random.randint(h*45,h*65)
                pbx7=random.randint(h*45,h*65)
                pbx8=random.randint(h*45,h*65)
                pbx9=random.randint(h*15,h*40)
                pbx10=random.randint(h*10,h*35)
                pbx11=random.randint(h*15,h*40)
                
                pby1=random.randint(h*40,h*60)
                pby2=random.randint(h*0,h*15)
                pby3=random.randint(h*30,h*45)
                pby4=random.randint(h*55,h*70)
                pby5=random.randint(h*85,h*100)
                pby6=random.randint(h*0,h*20)
                pby7=random.randint(h*40,h*60)
                pby8=random.randint(h*80,h*100)
                pby9=random.randint(h*15,h*30)
                pby10=random.randint(h*45,h*55)
                pby11=random.randint(h*70,h*85)
                
                print('          ',end='')
                lines = [[(h*0, h*35), (h*0, h*65)], [(h*100, h*35), (h*100, h*65)], [(h*50, h*105), (h*50, h*-5)], [(h*-10, h*105), (h*110, h*105)], [(h*-10, h*-5), (h*110, h*-5)], [(h*-10, h*105), (h*-10, h*-5)], [(h*110, h*105), (h*110, h*-5)], [(h*0, h*35), (h*-10, h*35)], [(h*0, h*65), (h*-10, h*65)], [(h*100, h*35), (h*110, h*35)], [(h*100, h*65), (h*110, h*65)]]
                c = np.array([(1, 0, 0, 1), (1, 0, 0, 1), (1, 0, 0, 1)])
                
                lc = mc.LineCollection(lines, colors=c, linewidths=1)
                fig, ax = pl.subplots()
                ax.set_facecolor('xkcd:sky blue')
                ax.set_facecolor((0.8, 1, 0.5))
                ax.add_collection(lc)
                ax.autoscale()
                ax.margins(0.1)
            
                psgx = [ppx2,ppx3,ppx4,ppx5,ppx6,ppx7,ppx8,ppx9,ppx10,ppx11] 
                psgy = [ppy2,ppy3,ppy4,ppy5,ppy6,ppy7,ppy8,ppy9,ppy10,ppy11] 
            
                plt.scatter(ppx1,ppy1,color= "purple",marker= "*", s=100)      # GK edit colour
                plt.scatter(psgx, psgy,color= "blue",marker= "*", s=80)  
             
                barx = [pbx2,pbx3,pbx4,pbx5,pbx6,pbx7,pbx8,pbx9,pbx10,pbx11] 
                bary = [pby2,pby3,pby4,pby5,pby6,pby7,pby8,pby9,pby10,pby11]
            
                plt.scatter(pbx1,pby1,color= "violet",marker= "o", s=100)      # GK edit colour
                plt.scatter(barx, bary, color= "red",marker= "o", s=80)       
                
                if playerb==1:
                    hb1-=1
                    plt.scatter(pbx1,pby1, label= "Ter Stegnen", color= "black",marker= "o", s=110)
                if playerb==2:
                    hb2-=1
                    plt.scatter(pbx2,pby2, label= "Umtiti", color= "black",marker= "o", s=110)
                if playerb==3:
                    hb3-=1
                    plt.scatter(pbx3,pby3, label= "Pique", color= "black",marker= "o", s=110)
                if playerb==4:
                    hb4-=1
                    plt.scatter(pbx4,pby4, label= "Rakitic", color= "black",marker= "o", s=110)
                if playerb==5:
                    hb5-=1
                    plt.scatter(pbx5,pby5, label= "Sergio Busquets", color= "black",marker= "o", s=110)
                if playerb==6:
                    hb6-=1
                    plt.scatter(pbx6,pby6, label= "Denis Suarez", color= "black",marker= "o", s=110)
                if playerb==7:
                    hb7-=1
                    plt.scatter(pbx7,pby7, label= "Coutinho", color= "black",marker= "o", s=110)
                if playerb==8:
                    hb8-=1
                    plt.scatter(pbx8,pby8, label= "Arthur", color= "black",marker= "o", s=110)
                if playerb==9:
                    hb9-=1
                    plt.scatter(pbx9,pby9, label= "Suarez", color= "black",marker= "o", s=110)
                if playerb==10:
                    hb10-=1
                    plt.scatter(pbx10,pby10, label= "Messi", color= "black",marker= "o", s=110)
                if playerb==11:
                    hb11-=1
                    plt.scatter(pbx11,pby11, label= "Dembele", color= "black",marker= "o", s=110)
                    
                plt.xlabel('Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! ') 
            
                plt.ylabel('Messi! Messi! Messi! Messi! Messi! Messi!') 
             
                plt.title('FIFA PYTHON 18\nPSG(BLUE) VS BARCELONA(RED)')  
            
                plt.show()     
                
                print()

            if freekick=='l' and g==1:
                bar=1
                psg=0
                playerb=1
                if playerb==1:
                    playerbn='Ter Stegnen'
                    if subb1!=0:
                        playerbn=playerbin1
                print('Commentatory:',playerbin1,'saves it')
                
                time=time+1
                print()
                
                print('           [ Time :',time,'min || PSG:',psggoal,'| BAR:',bargoal,']')    
            
                h=2
                ppx1=h*5
                ppx2=random.randint(h*50,h*60)
                ppx3=random.randint(h*50,h*60)
                ppx4=random.randint(h*50,h*60)
                ppx5=random.randint(h*50,h*60)
                ppx6=random.randint(h*50,h*60)
                ppx7=random.randint(h*50,h*60)
                ppx8=random.randint(h*50,h*60)
                ppx9=random.randint(h*50,h*60)
                ppx10=random.randint(h*50,h*60)
                ppx11=random.randint(h*50,h*60)
                
                ppy1=random.randint(h*40,h*60)
                ppy2=random.randint(h*0,h*15)
                ppy3=random.randint(h*30,h*45)
                ppy4=random.randint(h*55,h*70)
                ppy5=random.randint(h*85,h*100)
                ppy6=random.randint(h*0,h*20)
                ppy7=random.randint(h*40,h*60)
                ppy8=random.randint(h*80,h*100)
                ppy9=random.randint(h*15,h*30)
                ppy10=random.randint(h*45,h*55)
                ppy11=random.randint(h*70,h*85)
                
                pbx1=h*95
                pbx2=random.randint(h*50,h*60)
                pbx3=random.randint(h*50,h*60)
                pbx4=random.randint(h*50,h*60)
                pbx5=random.randint(h*50,h*60)
                pbx6=random.randint(h*50,h*60)
                pbx7=random.randint(h*50,h*60)
                pbx8=random.randint(h*50,h*60)
                pbx9=random.randint(h*50,h*60)
                pbx10=h*80
                pbx11=random.randint(h*50,h*60)
                
                pby1=random.randint(h*40,h*60)
                pby2=random.randint(h*0,h*15)
                pby3=random.randint(h*30,h*45)
                pby4=random.randint(h*55,h*70)
                pby5=random.randint(h*85,h*100)
                pby6=random.randint(h*0,h*20)
                pby7=random.randint(h*40,h*60)
                pby8=random.randint(h*80,h*100)
                pby9=random.randint(h*15,h*30)
                pby10=h*50
                pby11=random.randint(h*70,h*85)
                
                print('          ',end='')
                lines = [[(h*0, h*35), (h*0, h*65)], [(h*100, h*35), (h*100, h*65)], [(h*50, h*105), (h*50, h*-5)], [(h*-10, h*105), (h*110, h*105)], [(h*-10, h*-5), (h*110, h*-5)], [(h*-10, h*105), (h*-10, h*-5)], [(h*110, h*105), (h*110, h*-5)], [(h*0, h*35), (h*-10, h*35)], [(h*0, h*65), (h*-10, h*65)], [(h*100, h*35), (h*110, h*35)], [(h*100, h*65), (h*110, h*65)]]
                c = np.array([(1, 0, 0, 1), (1, 0, 0, 1), (1, 0, 0, 1)])
                
                lc = mc.LineCollection(lines, colors=c, linewidths=1)
                fig, ax = pl.subplots()
                ax.set_facecolor('xkcd:sky blue')
                ax.set_facecolor((0.8, 1, 0.5))
                ax.add_collection(lc)
                ax.autoscale()
                ax.margins(0.1)
            
                psgx = [ppx2,ppx3,ppx4,ppx5,ppx6,ppx7,ppx8,ppx9,ppx10,ppx11] 
                psgy = [ppy2,ppy3,ppy4,ppy5,ppy6,ppy7,ppy8,ppy9,ppy10,ppy11] 
            
                plt.scatter(ppx1,ppy1,color= "purple",marker= "*", s=100)      # GK edit colour
                plt.scatter(psgx, psgy,color= "blue",marker= "*", s=80)  
             
                barx = [pbx2,pbx3,pbx4,pbx5,pbx6,pbx7,pbx8,pbx9,pbx10,pbx11] 
                bary = [pby2,pby3,pby4,pby5,pby6,pby7,pby8,pby9,pby10,pby11]
            
                plt.scatter(pbx1,pby1,color= "violet",marker= "o", s=100)      # GK edit colour
                plt.scatter(barx, bary, color= "red",marker= "o", s=80)      
                        
                if playerp==1:
                    plt.scatter(ppx1,ppy1, label= "Buffon", color= "black",marker= "*", s=110)
                if playerp==2:
                    plt.scatter(ppx2,ppy2, label= "Thiago Silva", color= "black",marker= "*", s=110)
                if playerp==3:
                    plt.scatter(ppx3,ppy3, label= "Kimbempe", color= "black",marker= "*", s=110)
                if playerp==4:
                    plt.scatter(ppx4,ppy4, label= "Meunier", color= "black",marker= "*", s=110)
                if playerp==5:
                    plt.scatter(ppx5,ppy5, label= "Marquinhos", color= "black",marker= "*", s=110)
                if playerp==6:
                    plt.scatter(ppx6,ppy6, label= "Verrati", color= "black",marker= "*", s=110)
                if playerp==7:
                    plt.scatter(ppx7,ppy7, label= "Dani Alves", color= "black",marker= "*", s=110)
                if playerp==8:
                    plt.scatter(ppx8,ppy8, label= "Rabiot", color= "black",marker= "*", s=110)
                if playerp==9:
                    plt.scatter(ppx9,ppy9, label= "Cavani", color= "black",marker= "*", s=110)
                if playerp==10:
                    plt.scatter(ppx10,ppy10, label= "Neymar JR", color= "black",marker= "*", s=110)
                if playerp==11:
                    plt.scatter(ppx11,ppy11, label= "Mbappe", color= "black",marker= "*", s=110)
                    
                plt.xlabel('Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! ') 
            
                plt.ylabel('Messi! Messi! Messi! Messi! Messi! Messi!') 
             
                plt.title('FIFA PYTHON 18\nPSG(BLUE) VS BARCELONA(RED)')  
            
                plt.show()     
                
                print()
            if freekick=='r' and g==0:
                bar=1
                psg=0
                playerb=1
                if playerb==1:
                    playerbn='Ter Stegnen'
                    if subb1!=0:
                        playerbn=playerbin1
                print('Commentatory:',playerbin1,'saves it')
                
                time=time+1
                print()
                
                print('           [ Time :',time,'min || PSG:',psggoal,'| BAR:',bargoal,']')    
            
                h=2
                ppx1=h*5
                ppx2=random.randint(h*50,h*60)
                ppx3=random.randint(h*50,h*60)
                ppx4=random.randint(h*50,h*60)
                ppx5=random.randint(h*50,h*60)
                ppx6=random.randint(h*50,h*60)
                ppx7=random.randint(h*50,h*60)
                ppx8=random.randint(h*50,h*60)
                ppx9=random.randint(h*50,h*60)
                ppx10=random.randint(h*50,h*60)
                ppx11=random.randint(h*50,h*60)
                
                ppy1=random.randint(h*40,h*60)
                ppy2=random.randint(h*0,h*15)
                ppy3=random.randint(h*30,h*45)
                ppy4=random.randint(h*55,h*70)
                ppy5=random.randint(h*85,h*100)
                ppy6=random.randint(h*0,h*20)
                ppy7=random.randint(h*40,h*60)
                ppy8=random.randint(h*80,h*100)
                ppy9=random.randint(h*15,h*30)
                ppy10=random.randint(h*45,h*55)
                ppy11=random.randint(h*70,h*85)
                
                pbx1=h*95
                pbx2=random.randint(h*50,h*60)
                pbx3=random.randint(h*50,h*60)
                pbx4=random.randint(h*50,h*60)
                pbx5=random.randint(h*50,h*60)
                pbx6=random.randint(h*50,h*60)
                pbx7=random.randint(h*50,h*60)
                pbx8=random.randint(h*50,h*60)
                pbx9=random.randint(h*50,h*60)
                pbx10=h*80
                pbx11=random.randint(h*50,h*60)
                
                pby1=random.randint(h*40,h*60)
                pby2=random.randint(h*0,h*15)
                pby3=random.randint(h*30,h*45)
                pby4=random.randint(h*55,h*70)
                pby5=random.randint(h*85,h*100)
                pby6=random.randint(h*0,h*20)
                pby7=random.randint(h*40,h*60)
                pby8=random.randint(h*80,h*100)
                pby9=random.randint(h*15,h*30)
                pby10=h*50
                pby11=random.randint(h*70,h*85)
                
                print('          ',end='')
                lines = [[(h*0, h*35), (h*0, h*65)], [(h*100, h*35), (h*100, h*65)], [(h*50, h*105), (h*50, h*-5)], [(h*-10, h*105), (h*110, h*105)], [(h*-10, h*-5), (h*110, h*-5)], [(h*-10, h*105), (h*-10, h*-5)], [(h*110, h*105), (h*110, h*-5)], [(h*0, h*35), (h*-10, h*35)], [(h*0, h*65), (h*-10, h*65)], [(h*100, h*35), (h*110, h*35)], [(h*100, h*65), (h*110, h*65)]]
                c = np.array([(1, 0, 0, 1), (1, 0, 0, 1), (1, 0, 0, 1)])
                
                lc = mc.LineCollection(lines, colors=c, linewidths=1)
                fig, ax = pl.subplots()
                ax.set_facecolor('xkcd:sky blue')
                ax.set_facecolor((0.8, 1, 0.5))
                ax.add_collection(lc)
                ax.autoscale()
                ax.margins(0.1)
            
                psgx = [ppx2,ppx3,ppx4,ppx5,ppx6,ppx7,ppx8,ppx9,ppx10,ppx11] 
                psgy = [ppy2,ppy3,ppy4,ppy5,ppy6,ppy7,ppy8,ppy9,ppy10,ppy11] 
            
                plt.scatter(ppx1,ppy1,color= "purple",marker= "*", s=100)      # GK edit colour
                plt.scatter(psgx, psgy,color= "blue",marker= "*", s=80)  
             
                barx = [pbx2,pbx3,pbx4,pbx5,pbx6,pbx7,pbx8,pbx9,pbx10,pbx11] 
                bary = [pby2,pby3,pby4,pby5,pby6,pby7,pby8,pby9,pby10,pby11]
            
                plt.scatter(pbx1,pby1,color= "violet",marker= "o", s=100)      # GK edit colour
                plt.scatter(barx, bary, color= "red",marker= "o", s=80)      
                        
                if playerp==1:
                    plt.scatter(ppx1,ppy1, label= "Buffon", color= "black",marker= "*", s=110)
                if playerp==2:
                    plt.scatter(ppx2,ppy2, label= "Thiago Silva", color= "black",marker= "*", s=110)
                if playerp==3:
                    plt.scatter(ppx3,ppy3, label= "Kimbempe", color= "black",marker= "*", s=110)
                if playerp==4:
                    plt.scatter(ppx4,ppy4, label= "Meunier", color= "black",marker= "*", s=110)
                if playerp==5:
                    plt.scatter(ppx5,ppy5, label= "Marquinhos", color= "black",marker= "*", s=110)
                if playerp==6:
                    plt.scatter(ppx6,ppy6, label= "Verrati", color= "black",marker= "*", s=110)
                if playerp==7:
                    plt.scatter(ppx7,ppy7, label= "Dani Alves", color= "black",marker= "*", s=110)
                if playerp==8:
                    plt.scatter(ppx8,ppy8, label= "Rabiot", color= "black",marker= "*", s=110)
                if playerp==9:
                    plt.scatter(ppx9,ppy9, label= "Cavani", color= "black",marker= "*", s=110)
                if playerp==10:
                    plt.scatter(ppx10,ppy10, label= "Neymar JR", color= "black",marker= "*", s=110)
                if playerp==11:
                    plt.scatter(ppx11,ppy11, label= "Mbappe", color= "black",marker= "*", s=110)
                    
                plt.xlabel('Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! ') 
            
                plt.ylabel('Messi! Messi! Messi! Messi! Messi! Messi!') 
             
                plt.title('FIFA PYTHON 18\nPSG(BLUE) VS BARCELONA(RED)')  
            
                plt.show()     
                
                print()
            
            
    if psg==1:

        playerb=12-playerp

        if hp1<(0.3*HP):
            print('Commentatory:',playerpn,'is really tired. Please Substitute...')
        if hp2<(0.3*HP):
            print('Commentatory:',playerpn,'is really tired. Please Substitute...')
        if hp3<(0.3*HP):
            print('Commentatory:',playerpn,'is really tired. Please Substitute...')
        if hp4<(0.3*HP):
            print('Commentatory:',playerpn,'is really tired. Please Substitute...')
        if hp5<(0.3*HP):
            print('Commentatory:',playerpn,'is really tired. Please Substitute...')
        if hp6<(0.3*HP):
            print('Commentatory:',playerpn,'is really tired. Please Substitute...')
        if hp7<(0.3*HP):
            print('Commentatory:',playerpn,'is really tired. Please Substitute...')
        if hp8<(0.3*HP):
            print('Commentatory:',playerpn,'is really tired. Please Substitute...')
        if hp9<(0.3*HP):
            print('Commentatory:',playerpn,'is really tired. Please Substitute...')
        if hp11<(0.3*HP):
            print('Commentatory:',playerpn,'is really tired. Please Substitute...')   
        
        if playerb==1:
            playerbn='Ter Stegnen'
            if subb1!=0:
                playerbn=playerbin1        
        if playerb==2:
            playerbn='Umtiti'
            if subb2!=0:
                playerbn=playerbin2    
        if playerb==3:
            playerbn='Pique'
            if subb3!=0:
                playerbn=playerbin3    
        if playerb==4:
            playerbn='Rakitic'
            if subb4!=0:
                playerbn=playerbin4
        if playerb==5:
            playerbn='Sergio Busquets'
            if subb5!=0:
                playerbn=playerbin5    
        if playerb==6:
            playerbn='Denis Suarez'
            if subb6!=0:
                playerbn=playerbin6    
        if playerb==7:
            playerbn='Coutinho'
            if subb7!=0:
                playerbn=playerbin7    
        if playerb==8:
            playerbn='Arthur'
            if subb8!=0:
                playerbn=playerbin8    
        if playerb==9:
            playerbn='Suarez'
            if subb9!=0:
                playerbn=playerbin9    
        if playerb==10:
            playerbn='Messi'
            if subb10!=0:
                playerbn=playerbin10    
        if playerb==11:
            playerbn='Dembele'
            if subb11!=0:
                playerbn=playerbin11    
        if playerp==1:
            playerpn='Buffon'
            if subp1!=0:
                playerpn=playerpin1
        if playerp==2:
            playerpn='Thiago Silva'
            if subp2!=0:
                playerpn=playerpin2    
        if playerp==3:
            playerpn='Kimbempe'
            if subp3!=0:
                playerpn=playerpin3     
        if playerp==4:
            playerpn='Meunier'
            if subp4!=0:
                playerpn=playerpin4    
        if playerp==5:
            playerpn='Marquinhos'
            if subp5!=0:
                playerpn=playerpin5    
        if playerp==6:
            playerpn='Verrati'
            if subp6!=0:
                playerpn=playerpin6    
        if playerp==7:
            playerpn='Dani Alves'
            if subp7!=0:
                playerpn=playerpin7    
        if playerp==8:
            playerpn='Rabiot'
            if subp8!=0:
                playerpn=playerpin8    
        if playerp==9:
            playerpn='Cavani'
            if subp9!=0:
                playerpn=playerpin9    
        if playerp==10:
            playerpn='Neymar JR'
            if subp10!=0:
                playerpn=playerpin10    
        if playerp==11:
            playerpn='Mbappe'
            if subp11!=0:
                playerpn=playerpin11
        
        n=0        
        print('What should',playerpn,'(',playerp,') do ?')
        m=input('>>>')
        time.sleep(1)

        if hp1<(0.2*HP):
            m='sub'
            print('Commentatory:',playerpn,'is injured due to exhaustion !! Please Substitute NOW..')
        if hp2<(0.2*HP):
            m='sub'
            print('Commentatory:',playerpn,'is injured due to exhaustion !! Please Substitute NOW..')
        if hp3<(0.2*HP):
            m='sub'
            print('Commentatory:',playerpn,'is injured due to exhaustion !! Please Substitute NOW..')
        if hp4<(0.2*HP):
            m='sub'
            print('Commentatory:',playerpn,'is injured due to exhaustion !! Please Substitute NOW..')
        if hp5<(0.2*HP):
            m='sub'
            print('Commentatory:',playerpn,'is injured due to exhaustion !! Please Substitute NOW..')
        if hp6<(0.2*HP):
            m='sub'
            print('Commentatory:',playerpn,'is injured due to exhaustion !! Please Substitute NOW..')
        if hp7<(0.2*HP):
            m='sub'
            print('Commentatory:',playerpn,'is injured due to exhaustion !! Please Substitute NOW..')
        if hp8<(0.2*HP):
            m='sub'
            print('Commentatory:',playerpn,'is injured due to exhaustion !! Please Substitute NOW..')
        if hp9<(0.2*HP):
            m='sub'
            print('Commentatory:',playerpn,'is injured due to exhaustion !! Please Substitute NOW..')
        if hp11<(0.2*HP):
            m='sub'
            print('Commentatory:',playerpn,'is injured due to exhaustion !! Please Substitute NOW..') 

        print()
        
        if m=='skill' or m=='skills' or m=='skl' or m=='skls' or m=='9':
            q=random.randint(1,25)
            if q==1:
                print('Commentatory: What a beautiful',s1,'done by',playerpn,'(',playerp,') !!!')
            if q==2:
                print('Commentatory: Look at that',s2,'done by',playerpn,'(',playerp,') !!!')
            if q==3:
                print('Commentatory:OMG!!',s3,'done by',playerpn,'(',playerp,') !!!')
            if q==4:
                print('Commentatory: What a beautiful',s4,'done by',playerpn,'(',playerp,') !!!')
            if q==5:
                print('Commentatory:',s5,'done by',playerpn,'(',playerp,') !!!') 
            if q==6:
                print('Commentatory:The astounding',s6,'by ',playerpn,'(',playerp,') !!!')
            if q==7:
                print('Commentatory: What a beautiful',s7,'done by',playerpn,'(',playerp,') !!!')
            if q==8:
                print('Commentatory: Look at that',s8,'done by',playerpn,'(',playerp,') !!!')
            if q==9:
                print('Commentatory:OMG!!',s9,'done by',playerpn,'(',playerp,') !!!')
            if q==10:
                print('Commentatory: Unbelievable',s10,'done by',playerpn,'(',playerp,') !!!')
            if q==11:
                print('Commentatory: Remarkable',s11,'done by',playerpn,'(',playerp,') !!!') 
            if q==12:
                print('Commentatory:The astounding',s12,'by ',playerpn,'(',playerp,') !!!')
            if q==13:
                print('Commentatory: Ha Ha Ha !!! What a beautiful',s13,'done by',playerpn,'(',playerp,') under',playerbn,'(',playerb,') !!!')
            if q==14:
                print('Commentatory: Look at that',s14,'done by',playerpn,'(',playerp,') !!!')
            if q==15:
                print('Commentatory:OMG!!',s15,'done by',playerpn,'(',playerp,') !!!')
            if q==16:
                print('Commentatory: What a beautiful',s16,'done by',playerpn,'(',playerp,') !!!')
            if q==17:
                print('Commentatory:',s17,'done by',playerpn,'(',playerp,') !!!') 
            if q==18:
                print('Commentatory:The astounding',s18,'by ',playerpn,'(',playerp,') !!!')
            if q==19:
                print('Commentatory: What a beautiful',s19,'done by',playerpn,'(',playerp,') !!!')
            if q==20:
                print('Commentatory: Look at that',s20,'done by',playerpn,'(',playerp,') !!!')
                if playerp!=11:
                    playerp=playerp+1
                else:
                    playerp=playerp-1
            if q==21:
                psg=0
                bar=1
                print('Commentatory: Ha Ha Ha !!! Skill Failed !! Ball intercepted by',playerbn,'(',playerb,') of Barcelona !!')     
            if q==22:
                psg=0
                bar=1
                print('Commentatory: OH  MY GOD!!! Skill Failed !! Ball intercepted by',playerbn,'(',playerb,') of Barcelona !!')
            if q==23:
                psg=0
                bar=1
                print('Commentatory: Ha Ha Ha !!! Skill Failed !! Nice Interception by',playerbn,'(',playerb,') of Barcelona !!')
            if q==24:
                psg=0
                bar=1
                print('Commentatory:What a Joke !!! Skill Failed !! Ball intercepted by',playerbn,'(',playerb,') of Barcelona !!') 
            if q==25:
                psg=0
                bar=1
                print('Commentatory: LOOK !!! Skill Failed !! Ball intercepted by',playerbn,'(',playerb,') of Barcelona !!')
        
        if m=='q' or m=='quit' or m=='esc' or m=='exit' or m=='0':
            quitme=1
            continue                      
        
        if m=='rules' or m=='rule' or m=='r':
            quit=2

        if m=='p' or m=='2':
            n=1
        if m=='c' or m=='4':
            n=2
        if m=='tb' or m=='8':
            n=3
        if m=='s' or m=='6':
            n=4
        if m=='sub' or m=='7':
            bar=0
            psg=1
            playerpout=input('Enter name of player to be substituted..')
            if playerpout=='buffon':                
                subp1=1
                playerpin1=input('Enter name of player who goes in...')
                print('Commentatory:',playerpout,'goes out and here comes in',playerpin1)
                hp1=HP
            if playerpout=='thiago silva' or playerpout=='silva' or playerpout=='thiago':                
                subp2=1
                playerpin2=input('Enter name of player who goes in...')
                print('Commentatory:',playerpout,'goes out and here comes in',playerpin2)
                hp2=HP
            if playerpout=='kimbempe':                
                subp3=1
                playerpin3=input('Enter name of player who goes in...')
                print('Commentatory:',playerpout,'goes out and here comes in',playerpin3)
                hp3=HP
            if playerpout=='meunier':                
                subp4=1
                playerpin4=input('Enter name of player who goes in...')
                print('Commentatory:',playerpout,'goes out and here comes in',playerpin4)
                hp4=HP
            if playerpout=='marquinhos':                
                subp5=1
                playerpin5=input('Enter name of player who goes in...')
                print('Commentatory:',playerpout,'goes out and here comes in',playerpin5)
                hp5=HP
            if playerpout=='verrati':        
                subp6=1
                playerpin6=input('Enter name of player who goes in...')
                print('Commentatory:',playerpout,'goes out and here comes in',playerpin6)
                hp6=HP
            if playerpout=='dani alves' or playerpout=='alves' or playerpout=='dani':                
                subp7=1
                playerpin7=input('Enter name of player who goes in...')
                print('Commentatory:',playerpout,'goes out and here comes in',playerpin7)
                hp7=HP
            if playerpout=='rabiot':                
                subp8=1
                playerpin8=input('Enter name of player who goes in...')
                print('Commentatory:',playerpout,'goes out and here comes in',playerpin8)
                hp8=HP
            if playerpout=='cavani':                
                subp9=1
                playerpin9=input('Enter name of player who goes in...')
                print('Commentatory:',playerpout,'goes out and here comes in',playerpin9)
                hp9=HP
            if playerpout=='neymar' or playerpout=='neymar jr':                
                print("Hey Man ! You can't substitute ME ! I am the Captain !!")
                hp10=HP
            if playerpout=='mbappe':                
                subp11=1  
                playerpin11=input('Enter name of player who goes in...')
                print('Commentatory:',playerpout,'goes out and here comes in',playerpin11)
                hp11=HP
            
        y=random.randint(1,4)
        if n==1 and y!=1:
            if playerp<11:
                playerp=playerp+1
                if playerb==1:
                    playerbn='Ter Stegnen'
                    if subb1!=0:
                        playerbn=playerbin1        
                if playerb==2:
                    playerbn='Umtiti'
                    if subb2!=0:
                        playerbn=playerbin2    
                if playerb==3:
                    playerbn='Pique'
                    if subb3!=0:
                        playerbn=playerbin3    
                if playerb==4:
                    playerbn='Rakitic'
                    if subb4!=0:
                        playerbn=playerbin4
                if playerb==5:
                    playerbn='Sergio Busquets'
                    if subb5!=0:
                        playerbn=playerbin5    
                if playerb==6:
                    playerbn='Denis Suarez'
                    if subb6!=0:
                        playerbn=playerbin6    
                if playerb==7:
                    playerbn='Coutinho'
                    if subb7!=0:
                        playerbn=playerbin7    
                if playerb==8:
                    playerbn='Arthur'
                    if subb8!=0:
                        playerbn=playerbin8    
                if playerb==9:
                    playerbn='Suarez'
                    if subb9!=0:
                        playerbn=playerbin9    
                if playerb==10:
                    playerbn='Messi'
                    if subb10!=0:
                        playerbn=playerbin10    
                if playerb==11:
                    playerbn='Dembele'
                    if subb11!=0:
                        playerbn=playerbin11    
                if playerp==1:
                    playerpn='Buffon'
                    if subp1!=0:
                        playerpn=playerpin1
                if playerp==2:
                    playerpn='Thiago Silva'
                    if subp2!=0:
                        playerpn=playerpin2    
                if playerp==3:
                    playerpn='Kimbempe'
                    if subp3!=0:
                        playerpn=playerpin3     
                if playerp==4:
                    playerpn='Meunier'
                    if subp4!=0:
                        playerpn=playerpin4    
                if playerp==5:
                    playerpn='Marquinhos'
                    if subp5!=0:
                        playerpn=playerpin5    
                if playerp==6:
                    playerpn='Verrati'
                    if subp6!=0:
                        playerpn=playerpin6    
                if playerp==7:
                    playerpn='Dani Alves'
                    if subp7!=0:
                        playerpn=playerpin7    
                if playerp==8:
                    playerpn='Rabiot'
                    if subp8!=0:
                        playerpn=playerpin8    
                if playerp==9:
                    playerpn='Cavani'
                    if subp9!=0:
                        playerpn=playerpin9    
                if playerp==10:
                    playerpn='Neymar JR'
                    if subp10!=0:
                        playerpn=playerpin10    
                if playerp==11:
                    playerpn='Mbappe'
                    if subp11!=0:
                        playerpn=playerpin11
                print('Commentatory: Pass to player',playerpn,'succesful !! Nice Pass man!!')
                time=time+1
                print()
                
                print('           [ Time :',time,'min || PSG:',psggoal,'| BAR:',bargoal,']')    
            
                h=2
                ppx1=h*5
                ppx2=random.randint(h*10,h*30)
                ppx3=random.randint(h*10,h*30)
                ppx4=random.randint(h*10,h*30)
                ppx5=random.randint(h*10,h*30)
                ppx6=random.randint(h*35,h*55)
                ppx7=random.randint(h*35,h*55)
                ppx8=random.randint(h*35,h*55)
                ppx9=random.randint(h*60,h*85)
                ppx10=random.randint(h*65,h*90)
                ppx11=random.randint(h*60,h*85)
                
                ppy1=random.randint(h*40,h*60)
                ppy2=random.randint(h*0,h*15)
                ppy3=random.randint(h*30,h*45)
                ppy4=random.randint(h*55,h*70)
                ppy5=random.randint(h*85,h*100)
                ppy6=random.randint(h*0,h*20)
                ppy7=random.randint(h*40,h*60)
                ppy8=random.randint(h*80,h*100)
                ppy9=random.randint(h*15,h*30)
                ppy10=random.randint(h*45,h*55)
                ppy11=random.randint(h*70,h*85)
                
                pbx1=h*95
                pbx2=random.randint(h*70,h*90)
                pbx3=random.randint(h*70,h*90)
                pbx4=random.randint(h*70,h*90)
                pbx5=random.randint(h*70,h*90)
                pbx6=random.randint(h*45,h*65)
                pbx7=random.randint(h*45,h*65)
                pbx8=random.randint(h*45,h*65)
                pbx9=random.randint(h*15,h*40)
                pbx10=random.randint(h*10,h*35)
                pbx11=random.randint(h*15,h*40)
                
                pby1=random.randint(h*40,h*60)
                pby2=random.randint(h*0,h*15)
                pby3=random.randint(h*30,h*45)
                pby4=random.randint(h*55,h*70)
                pby5=random.randint(h*85,h*100)
                pby6=random.randint(h*0,h*20)
                pby7=random.randint(h*40,h*60)
                pby8=random.randint(h*80,h*100)
                pby9=random.randint(h*15,h*30)
                pby10=random.randint(h*45,h*55)
                pby11=random.randint(h*70,h*85)
                
                print('          ',end='')
                lines = [[(h*0, h*35), (h*0, h*65)], [(h*100, h*35), (h*100, h*65)], [(h*50, h*105), (h*50, h*-5)], [(h*-10, h*105), (h*110, h*105)], [(h*-10, h*-5), (h*110, h*-5)], [(h*-10, h*105), (h*-10, h*-5)], [(h*110, h*105), (h*110, h*-5)], [(h*0, h*35), (h*-10, h*35)], [(h*0, h*65), (h*-10, h*65)], [(h*100, h*35), (h*110, h*35)], [(h*100, h*65), (h*110, h*65)]]
                c = np.array([(1, 0, 0, 1), (1, 0, 0, 1), (1, 0, 0, 1)])
                
                lc = mc.LineCollection(lines, colors=c, linewidths=1)
                fig, ax = pl.subplots()
                ax.set_facecolor('xkcd:sky blue')
                ax.set_facecolor((0.8, 1, 0.5))
                ax.add_collection(lc)
                ax.autoscale()
                ax.margins(0.1)
            
                psgx = [ppx2,ppx3,ppx4,ppx5,ppx6,ppx7,ppx8,ppx9,ppx10,ppx11] 
                psgy = [ppy2,ppy3,ppy4,ppy5,ppy6,ppy7,ppy8,ppy9,ppy10,ppy11] 
            
                plt.scatter(ppx1,ppy1,color= "purple",marker= "*", s=100)      # GK edit colour
                plt.scatter(psgx, psgy,color= "blue",marker= "*", s=80)  
            
                barx = [pbx2,pbx3,pbx4,pbx5,pbx6,pbx7,pbx8,pbx9,pbx10,pbx11] 
                bary = [pby2,pby3,pby4,pby5,pby6,pby7,pby8,pby9,pby10,pby11]
            
                plt.scatter(pbx1,pby1,color= "violet",marker= "o", s=100)      # GK edit colour
                plt.scatter(barx, bary, color= "red",marker= "o", s=80)      
                        
                if playerp==1:
                    hp1=-1
                    plt.scatter(ppx1,ppy1, label= "Buffon", color= "black",marker= "*", s=110)
                if playerp==2:
                    hp2=-1
                    plt.scatter(ppx2,ppy2, label= "Thiago Silva", color= "black",marker= "*", s=110)
                if playerp==3:
                    hp3=-1
                    plt.scatter(ppx3,ppy3, label= "Kimbempe", color= "black",marker= "*", s=110)
                if playerp==4:
                    hp4=-1
                    plt.scatter(ppx4,ppy4, label= "Meunier", color= "black",marker= "*", s=110)
                if playerp==5:
                    hp5=-1
                    plt.scatter(ppx5,ppy5, label= "Marquinhos", color= "black",marker= "*", s=110)
                if playerp==6:
                    hp6=-1
                    plt.scatter(ppx6,ppy6, label= "Verrati", color= "black",marker= "*", s=110)
                if playerp==7:
                    hp7=-1
                    plt.scatter(ppx7,ppy7, label= "Dani Alves", color= "black",marker= "*", s=110)
                if playerp==8:
                    hp8=-1
                    plt.scatter(ppx8,ppy8, label= "Rabiot", color= "black",marker= "*", s=110)
                if playerp==9:
                    hp9=-1
                    plt.scatter(ppx9,ppy9, label= "Cavani", color= "black",marker= "*", s=110)
                if playerp==10:
                    hp10=-1
                    plt.scatter(ppx10,ppy10, label= "Neymar JR", color= "black",marker= "*", s=110)
                if playerp==11:
                    hp11=-1
                    plt.scatter(ppx11,ppy11, label= "Mbappe", color= "black",marker= "*", s=110)
                    
                plt.xlabel('Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! ') 
            
                plt.ylabel('Messi! Messi! Messi! Messi! Messi! Messi!') 
            
                plt.title('FIFA PYTHON 18\nPSG(BLUE) VS BARCELONA(RED)')  
            
                plt.show()     
                
                print()

                continue

            else:
                playerp=playerp-1
                if playerb==1:
                    playerbn='Ter Stegnen'
                    if subb1!=0:
                        playerbn=playerbin1        
                if playerb==2:
                    playerbn='Umtiti'
                    if subb2!=0:
                        playerbn=playerbin2    
                if playerb==3:
                    playerbn='Pique'
                    if subb3!=0:
                        playerbn=playerbin3    
                if playerb==4:
                    playerbn='Rakitic'
                    if subb4!=0:
                        playerbn=playerbin4
                if playerb==5:
                    playerbn='Sergio Busquets'
                    if subb5!=0:
                        playerbn=playerbin5    
                if playerb==6:
                    playerbn='Denis Suarez'
                    if subb6!=0:
                        playerbn=playerbin6    
                if playerb==7:
                    playerbn='Coutinho'
                    if subb7!=0:
                        playerbn=playerbin7    
                if playerb==8:
                    playerbn='Arthur'
                    if subb8!=0:
                        playerbn=playerbin8    
                if playerb==9:
                    playerbn='Suarez'
                    if subb9!=0:
                        playerbn=playerbin9    
                if playerb==10:
                    playerbn='Messi'
                    if subb10!=0:
                        playerbn=playerbin10    
                if playerb==11:
                    playerbn='Dembele'
                    if subb11!=0:
                        playerbn=playerbin11    
                if playerp==1:
                    playerpn='Buffon'
                    if subp1!=0:
                        playerpn=playerpin1
                if playerp==2:
                    playerpn='Thiago Silva'
                    if subp2!=0:
                        playerpn=playerpin2    
                if playerp==3:
                    playerpn='Kimbempe'
                    if subp3!=0:
                        playerpn=playerpin3     
                if playerp==4:
                    playerpn='Meunier'
                    if subp4!=0:
                        playerpn=playerpin4    
                if playerp==5:
                    playerpn='Marquinhos'
                    if subp5!=0:
                        playerpn=playerpin5    
                if playerp==6:
                    playerpn='Verrati'
                    if subp6!=0:
                        playerpn=playerpin6    
                if playerp==7:
                    playerpn='Dani Alves'
                    if subp7!=0:
                        playerpn=playerpin7    
                if playerp==8:
                    playerpn='Rabiot'
                    if subp8!=0:
                        playerpn=playerpin8    
                if playerp==9:
                    playerpn='Cavani'
                    if subp9!=0:
                        playerpn=playerpin9    
                if playerp==10:
                    playerpn='Neymar JR'
                    if subp10!=0:
                        playerpn=playerpin10    
                if playerp==11:
                    playerpn='Mbappe'
                    if subp11!=0:
                        playerpn=playerpin11
                print('Commentatory: Pass to player',playerpn,'succesful !!')
                time=time+1
                print()
                
                print('           [ Time :',time,'min || PSG:',psggoal,'| BAR:',bargoal,']')    
            
                h=2
                ppx1=h*5
                ppx2=random.randint(h*10,h*30)
                ppx3=random.randint(h*10,h*30)
                ppx4=random.randint(h*10,h*30)
                ppx5=random.randint(h*10,h*30)
                ppx6=random.randint(h*35,h*55)
                ppx7=random.randint(h*35,h*55)
                ppx8=random.randint(h*35,h*55)
                ppx9=random.randint(h*60,h*85)
                ppx10=random.randint(h*65,h*90)
                ppx11=random.randint(h*60,h*85)
                
                ppy1=random.randint(h*40,h*60)
                ppy2=random.randint(h*0,h*15)
                ppy3=random.randint(h*30,h*45)
                ppy4=random.randint(h*55,h*70)
                ppy5=random.randint(h*85,h*100)
                ppy6=random.randint(h*0,h*20)
                ppy7=random.randint(h*40,h*60)
                ppy8=random.randint(h*80,h*100)
                ppy9=random.randint(h*15,h*30)
                ppy10=random.randint(h*45,h*55)
                ppy11=random.randint(h*70,h*85)
                
                pbx1=h*95
                pbx2=random.randint(h*70,h*90)
                pbx3=random.randint(h*70,h*90)
                pbx4=random.randint(h*70,h*90)
                pbx5=random.randint(h*70,h*90)
                pbx6=random.randint(h*45,h*65)
                pbx7=random.randint(h*45,h*65)
                pbx8=random.randint(h*45,h*65)
                pbx9=random.randint(h*15,h*40)
                pbx10=random.randint(h*10,h*35)
                pbx11=random.randint(h*15,h*40)
                
                pby1=random.randint(h*40,h*60)
                pby2=random.randint(h*0,h*15)
                pby3=random.randint(h*30,h*45)
                pby4=random.randint(h*55,h*70)
                pby5=random.randint(h*85,h*100)
                pby6=random.randint(h*0,h*20)
                pby7=random.randint(h*40,h*60)
                pby8=random.randint(h*80,h*100)
                pby9=random.randint(h*15,h*30)
                pby10=random.randint(h*45,h*55)
                pby11=random.randint(h*70,h*85)
                
                print('          ',end='')
                lines = [[(h*0, h*35), (h*0, h*65)], [(h*100, h*35), (h*100, h*65)], [(h*50, h*105), (h*50, h*-5)], [(h*-10, h*105), (h*110, h*105)], [(h*-10, h*-5), (h*110, h*-5)], [(h*-10, h*105), (h*-10, h*-5)], [(h*110, h*105), (h*110, h*-5)], [(h*0, h*35), (h*-10, h*35)], [(h*0, h*65), (h*-10, h*65)], [(h*100, h*35), (h*110, h*35)], [(h*100, h*65), (h*110, h*65)]]
                c = np.array([(1, 0, 0, 1), (1, 0, 0, 1), (1, 0, 0, 1)])
                
                lc = mc.LineCollection(lines, colors=c, linewidths=1)
                fig, ax = pl.subplots()
                ax.set_facecolor('xkcd:sky blue')
                ax.set_facecolor((0.8, 1, 0.5))
                ax.add_collection(lc)
                ax.autoscale()
                ax.margins(0.1)
            
                psgx = [ppx2,ppx3,ppx4,ppx5,ppx6,ppx7,ppx8,ppx9,ppx10,ppx11] 
                psgy = [ppy2,ppy3,ppy4,ppy5,ppy6,ppy7,ppy8,ppy9,ppy10,ppy11] 
            
                plt.scatter(ppx1,ppy1,color= "purple",marker= "*", s=100)      # GK edit colour
                plt.scatter(psgx, psgy,color= "blue",marker= "*", s=80)  
            
                barx = [pbx2,pbx3,pbx4,pbx5,pbx6,pbx7,pbx8,pbx9,pbx10,pbx11] 
                bary = [pby2,pby3,pby4,pby5,pby6,pby7,pby8,pby9,pby10,pby11]
            
                plt.scatter(pbx1,pby1,color= "violet",marker= "o", s=100)      # GK edit colour
                plt.scatter(barx, bary, color= "red",marker= "o", s=80)      
                        
                if playerp==1:
                    hp1=-1
                    plt.scatter(ppx1,ppy1, label= "Buffon", color= "black",marker= "*", s=110)
                if playerp==2:
                    hp2=-1
                    plt.scatter(ppx2,ppy2, label= "Thiago Silva", color= "black",marker= "*", s=110)
                if playerp==3:
                    hp3=-1
                    plt.scatter(ppx3,ppy3, label= "Kimbempe", color= "black",marker= "*", s=110)
                if playerp==4:
                    hp4=-1
                    plt.scatter(ppx4,ppy4, label= "Meunier", color= "black",marker= "*", s=110)
                if playerp==5:
                    hp5=-1
                    plt.scatter(ppx5,ppy5, label= "Marquinhos", color= "black",marker= "*", s=110)
                if playerp==6:
                    hp6=-1
                    plt.scatter(ppx6,ppy6, label= "Verrati", color= "black",marker= "*", s=110)
                if playerp==7:
                    hp7=-1
                    plt.scatter(ppx7,ppy7, label= "Dani Alves", color= "black",marker= "*", s=110)
                if playerp==8:
                    hp8=-1
                    plt.scatter(ppx8,ppy8, label= "Rabiot", color= "black",marker= "*", s=110)
                if playerp==9:
                    hp9=-1
                    plt.scatter(ppx9,ppy9, label= "Cavani", color= "black",marker= "*", s=110)
                if playerp==10:
                    hp10=-1
                    plt.scatter(ppx10,ppy10, label= "Neymar JR", color= "black",marker= "*", s=110)
                if playerp==11:
                    hp11=-1
                    plt.scatter(ppx11,ppy11, label= "Mbappe", color= "black",marker= "*", s=110)
                    
                plt.xlabel('Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! ') 
            
                plt.ylabel('Messi! Messi! Messi! Messi! Messi! Messi!') 
            
                plt.title('FIFA PYTHON 18\nPSG(BLUE) VS BARCELONA(RED)')  
            
                plt.show()     
                
                print()

                continue
        
        if n==2 and y!=2:
            if playerp<10:
                playerp=playerp+2
                if playerb==1:
                    playerbn='Ter Stegnen'
                    if subb1!=0:
                        playerbn=playerbin1        
                if playerb==2:
                    playerbn='Umtiti'
                    if subb2!=0:
                        playerbn=playerbin2    
                if playerb==3:
                    playerbn='Pique'
                    if subb3!=0:
                        playerbn=playerbin3    
                if playerb==4:
                    playerbn='Rakitic'
                    if subb4!=0:
                        playerbn=playerbin4
                if playerb==5:
                    playerbn='Sergio Busquets'
                    if subb5!=0:
                        playerbn=playerbin5    
                if playerb==6:
                    playerbn='Denis Suarez'
                    if subb6!=0:
                        playerbn=playerbin6    
                if playerb==7:
                    playerbn='Coutinho'
                    if subb7!=0:
                        playerbn=playerbin7    
                if playerb==8:
                    playerbn='Arthur'
                    if subb8!=0:
                        playerbn=playerbin8    
                if playerb==9:
                    playerbn='Suarez'
                    if subb9!=0:
                        playerbn=playerbin9    
                if playerb==10:
                    playerbn='Messi'
                    if subb10!=0:
                        playerbn=playerbin10    
                if playerb==11:
                    playerbn='Dembele'
                    if subb11!=0:
                        playerbn=playerbin11    
                if playerp==1:
                    playerpn='Buffon'
                    if subp1!=0:
                        playerpn=playerpin1
                if playerp==2:
                    playerpn='Thiago Silva'
                    if subp2!=0:
                        playerpn=playerpin2    
                if playerp==3:
                    playerpn='Kimbempe'
                    if subp3!=0:
                        playerpn=playerpin3     
                if playerp==4:
                    playerpn='Meunier'
                    if subp4!=0:
                        playerpn=playerpin4    
                if playerp==5:
                    playerpn='Marquinhos'
                    if subp5!=0:
                        playerpn=playerpin5    
                if playerp==6:
                    playerpn='Verrati'
                    if subp6!=0:
                        playerpn=playerpin6    
                if playerp==7:
                    playerpn='Dani Alves'
                    if subp7!=0:
                        playerpn=playerpin7    
                if playerp==8:
                    playerpn='Rabiot'
                    if subp8!=0:
                        playerpn=playerpin8    
                if playerp==9:
                    playerpn='Cavani'
                    if subp9!=0:
                        playerpn=playerpin9    
                if playerp==10:
                    playerpn='Neymar JR'
                    if subp10!=0:
                        playerpn=playerpin10    
                if playerp==11:
                    playerpn='Mbappe'
                    if subp11!=0:
                        playerpn=playerpin11
                print('Commentatory: Cross to player',playerpn,'succesful !! WOW! What a trap!! ')
                time=time+1
                print()
                
                print('           [ Time :',time,'min || PSG:',psggoal,'| BAR:',bargoal,']')    
            
                h=2
                ppx1=h*5
                ppx2=random.randint(h*10,h*30)
                ppx3=random.randint(h*10,h*30)
                ppx4=random.randint(h*10,h*30)
                ppx5=random.randint(h*10,h*30)
                ppx6=random.randint(h*35,h*55)
                ppx7=random.randint(h*35,h*55)
                ppx8=random.randint(h*35,h*55)
                ppx9=random.randint(h*60,h*85)
                ppx10=random.randint(h*65,h*90)
                ppx11=random.randint(h*60,h*85)
                
                ppy1=random.randint(h*40,h*60)
                ppy2=random.randint(h*0,h*15)
                ppy3=random.randint(h*30,h*45)
                ppy4=random.randint(h*55,h*70)
                ppy5=random.randint(h*85,h*100)
                ppy6=random.randint(h*0,h*20)
                ppy7=random.randint(h*40,h*60)
                ppy8=random.randint(h*80,h*100)
                ppy9=random.randint(h*15,h*30)
                ppy10=random.randint(h*45,h*55)
                ppy11=random.randint(h*70,h*85)
                
                pbx1=h*95
                pbx2=random.randint(h*70,h*90)
                pbx3=random.randint(h*70,h*90)
                pbx4=random.randint(h*70,h*90)
                pbx5=random.randint(h*70,h*90)
                pbx6=random.randint(h*45,h*65)
                pbx7=random.randint(h*45,h*65)
                pbx8=random.randint(h*45,h*65)
                pbx9=random.randint(h*15,h*40)
                pbx10=random.randint(h*10,h*35)
                pbx11=random.randint(h*15,h*40)
                
                pby1=random.randint(h*40,h*60)
                pby2=random.randint(h*0,h*15)
                pby3=random.randint(h*30,h*45)
                pby4=random.randint(h*55,h*70)
                pby5=random.randint(h*85,h*100)
                pby6=random.randint(h*0,h*20)
                pby7=random.randint(h*40,h*60)
                pby8=random.randint(h*80,h*100)
                pby9=random.randint(h*15,h*30)
                pby10=random.randint(h*45,h*55)
                pby11=random.randint(h*70,h*85)
                
                print('          ',end='')
                lines = [[(h*0, h*35), (h*0, h*65)], [(h*100, h*35), (h*100, h*65)], [(h*50, h*105), (h*50, h*-5)], [(h*-10, h*105), (h*110, h*105)], [(h*-10, h*-5), (h*110, h*-5)], [(h*-10, h*105), (h*-10, h*-5)], [(h*110, h*105), (h*110, h*-5)], [(h*0, h*35), (h*-10, h*35)], [(h*0, h*65), (h*-10, h*65)], [(h*100, h*35), (h*110, h*35)], [(h*100, h*65), (h*110, h*65)]]
                c = np.array([(1, 0, 0, 1), (1, 0, 0, 1), (1, 0, 0, 1)])
                
                lc = mc.LineCollection(lines, colors=c, linewidths=1)
                fig, ax = pl.subplots()
                ax.set_facecolor('xkcd:sky blue')
                ax.set_facecolor((0.8, 1, 0.5))
                ax.add_collection(lc)
                ax.autoscale()
                ax.margins(0.1)
            
                psgx = [ppx2,ppx3,ppx4,ppx5,ppx6,ppx7,ppx8,ppx9,ppx10,ppx11] 
                psgy = [ppy2,ppy3,ppy4,ppy5,ppy6,ppy7,ppy8,ppy9,ppy10,ppy11] 
            
                plt.scatter(ppx1,ppy1,color= "purple",marker= "*", s=100)      # GK edit colour
                plt.scatter(psgx, psgy,color= "blue",marker= "*", s=80)  
            
                barx = [pbx2,pbx3,pbx4,pbx5,pbx6,pbx7,pbx8,pbx9,pbx10,pbx11] 
                bary = [pby2,pby3,pby4,pby5,pby6,pby7,pby8,pby9,pby10,pby11]
            
                plt.scatter(pbx1,pby1,color= "violet",marker= "o", s=100)      # GK edit colour
                plt.scatter(barx, bary, color= "red",marker= "o", s=80)      
                        
                if playerp==1:
                    hp1=-1
                    plt.scatter(ppx1,ppy1, label= "Buffon", color= "black",marker= "*", s=110)
                if playerp==2:
                    hp2=-1
                    plt.scatter(ppx2,ppy2, label= "Thiago Silva", color= "black",marker= "*", s=110)
                if playerp==3:
                    hp3=-1
                    plt.scatter(ppx3,ppy3, label= "Kimbempe", color= "black",marker= "*", s=110)
                if playerp==4:
                    hp4=-1
                    plt.scatter(ppx4,ppy4, label= "Meunier", color= "black",marker= "*", s=110)
                if playerp==5:
                    hp5=-1
                    plt.scatter(ppx5,ppy5, label= "Marquinhos", color= "black",marker= "*", s=110)
                if playerp==6:
                    hp6=-1
                    plt.scatter(ppx6,ppy6, label= "Verrati", color= "black",marker= "*", s=110)
                if playerp==7:
                    hp7=-1
                    plt.scatter(ppx7,ppy7, label= "Dani Alves", color= "black",marker= "*", s=110)
                if playerp==8:
                    hp8=-1
                    plt.scatter(ppx8,ppy8, label= "Rabiot", color= "black",marker= "*", s=110)
                if playerp==9:
                    hp9=-1
                    plt.scatter(ppx9,ppy9, label= "Cavani", color= "black",marker= "*", s=110)
                if playerp==10:
                    hp10=-1
                    plt.scatter(ppx10,ppy10, label= "Neymar JR", color= "black",marker= "*", s=110)
                if playerp==11:
                    hp11=-1
                    plt.scatter(ppx11,ppy11, label= "Mbappe", color= "black",marker= "*", s=110)
                    
                plt.xlabel('Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! ') 
            
                plt.ylabel('Messi! Messi! Messi! Messi! Messi! Messi!') 
            
                plt.title('FIFA PYTHON 18\nPSG(BLUE) VS BARCELONA(RED)')  
            
                plt.show()     
                
                print()

                continue

            else:
                playerp=playerp-2
                if playerb==1:
                    playerbn='Ter Stegnen'
                    if subb1!=0:
                        playerbn=playerbin1        
                if playerb==2:
                    playerbn='Umtiti'
                    if subb2!=0:
                        playerbn=playerbin2    
                if playerb==3:
                    playerbn='Pique'
                    if subb3!=0:
                        playerbn=playerbin3    
                if playerb==4:
                    playerbn='Rakitic'
                    if subb4!=0:
                        playerbn=playerbin4
                if playerb==5:
                    playerbn='Sergio Busquets'
                    if subb5!=0:
                        playerbn=playerbin5    
                if playerb==6:
                    playerbn='Denis Suarez'
                    if subb6!=0:
                        playerbn=playerbin6    
                if playerb==7:
                    playerbn='Coutinho'
                    if subb7!=0:
                        playerbn=playerbin7    
                if playerb==8:
                    playerbn='Arthur'
                    if subb8!=0:
                        playerbn=playerbin8    
                if playerb==9:
                    playerbn='Suarez'
                    if subb9!=0:
                        playerbn=playerbin9    
                if playerb==10:
                    playerbn='Messi'
                    if subb10!=0:
                        playerbn=playerbin10    
                if playerb==11:
                    playerbn='Dembele'
                    if subb11!=0:
                        playerbn=playerbin11    
                if playerp==1:
                    playerpn='Buffon'
                    if subp1!=0:
                        playerpn=playerpin1
                if playerp==2:
                    playerpn='Thiago Silva'
                    if subp2!=0:
                        playerpn=playerpin2    
                if playerp==3:
                    playerpn='Kimbempe'
                    if subp3!=0:
                        playerpn=playerpin3     
                if playerp==4:
                    playerpn='Meunier'
                    if subp4!=0:
                        playerpn=playerpin4    
                if playerp==5:
                    playerpn='Marquinhos'
                    if subp5!=0:
                        playerpn=playerpin5    
                if playerp==6:
                    playerpn='Verrati'
                    if subp6!=0:
                        playerpn=playerpin6    
                if playerp==7:
                    playerpn='Dani Alves'
                    if subp7!=0:
                        playerpn=playerpin7    
                if playerp==8:
                    playerpn='Rabiot'
                    if subp8!=0:
                        playerpn=playerpin8    
                if playerp==9:
                    playerpn='Cavani'
                    if subp9!=0:
                        playerpn=playerpin9    
                if playerp==10:
                    playerpn='Neymar JR'
                    if subp10!=0:
                        playerpn=playerpin10    
                if playerp==11:
                    playerpn='Mbappe'
                    if subp11!=0:
                        playerpn=playerpin11
                print('Commentatory: Cross to player',playerpn,'succesful !!')
                time=time+1
                print()
                
                print('           [ Time :',time,'min || PSG:',psggoal,'| BAR:',bargoal,']')    
            
                h=2
                ppx1=h*5
                ppx2=random.randint(h*10,h*30)
                ppx3=random.randint(h*10,h*30)
                ppx4=random.randint(h*10,h*30)
                ppx5=random.randint(h*10,h*30)
                ppx6=random.randint(h*35,h*55)
                ppx7=random.randint(h*35,h*55)
                ppx8=random.randint(h*35,h*55)
                ppx9=random.randint(h*60,h*85)
                ppx10=random.randint(h*65,h*90)
                ppx11=random.randint(h*60,h*85)
                
                ppy1=random.randint(h*40,h*60)
                ppy2=random.randint(h*0,h*15)
                ppy3=random.randint(h*30,h*45)
                ppy4=random.randint(h*55,h*70)
                ppy5=random.randint(h*85,h*100)
                ppy6=random.randint(h*0,h*20)
                ppy7=random.randint(h*40,h*60)
                ppy8=random.randint(h*80,h*100)
                ppy9=random.randint(h*15,h*30)
                ppy10=random.randint(h*45,h*55)
                ppy11=random.randint(h*70,h*85)
                
                pbx1=h*95
                pbx2=random.randint(h*70,h*90)
                pbx3=random.randint(h*70,h*90)
                pbx4=random.randint(h*70,h*90)
                pbx5=random.randint(h*70,h*90)
                pbx6=random.randint(h*45,h*65)
                pbx7=random.randint(h*45,h*65)
                pbx8=random.randint(h*45,h*65)
                pbx9=random.randint(h*15,h*40)
                pbx10=random.randint(h*10,h*35)
                pbx11=random.randint(h*15,h*40)
                
                pby1=random.randint(h*40,h*60)
                pby2=random.randint(h*0,h*15)
                pby3=random.randint(h*30,h*45)
                pby4=random.randint(h*55,h*70)
                pby5=random.randint(h*85,h*100)
                pby6=random.randint(h*0,h*20)
                pby7=random.randint(h*40,h*60)
                pby8=random.randint(h*80,h*100)
                pby9=random.randint(h*15,h*30)
                pby10=random.randint(h*45,h*55)
                pby11=random.randint(h*70,h*85)
                
                print('          ',end='')
                lines = [[(h*0, h*35), (h*0, h*65)], [(h*100, h*35), (h*100, h*65)], [(h*50, h*105), (h*50, h*-5)], [(h*-10, h*105), (h*110, h*105)], [(h*-10, h*-5), (h*110, h*-5)], [(h*-10, h*105), (h*-10, h*-5)], [(h*110, h*105), (h*110, h*-5)], [(h*0, h*35), (h*-10, h*35)], [(h*0, h*65), (h*-10, h*65)], [(h*100, h*35), (h*110, h*35)], [(h*100, h*65), (h*110, h*65)]]
                c = np.array([(1, 0, 0, 1), (1, 0, 0, 1), (1, 0, 0, 1)])
                
                lc = mc.LineCollection(lines, colors=c, linewidths=1)
                fig, ax = pl.subplots()
                ax.set_facecolor('xkcd:sky blue')
                ax.set_facecolor((0.8, 1, 0.5))
                ax.add_collection(lc)
                ax.autoscale()
                ax.margins(0.1)
            
                psgx = [ppx2,ppx3,ppx4,ppx5,ppx6,ppx7,ppx8,ppx9,ppx10,ppx11] 
                psgy = [ppy2,ppy3,ppy4,ppy5,ppy6,ppy7,ppy8,ppy9,ppy10,ppy11] 
            
                plt.scatter(ppx1,ppy1,color= "purple",marker= "*", s=100)      # GK edit colour
                plt.scatter(psgx, psgy,color= "blue",marker= "*", s=80)  
            
                barx = [pbx2,pbx3,pbx4,pbx5,pbx6,pbx7,pbx8,pbx9,pbx10,pbx11] 
                bary = [pby2,pby3,pby4,pby5,pby6,pby7,pby8,pby9,pby10,pby11]
            
                plt.scatter(pbx1,pby1,color= "violet",marker= "o", s=100)      # GK edit colour
                plt.scatter(barx, bary, color= "red",marker= "o", s=80)      
                        
                if playerp==1:
                    hp1=-1
                    plt.scatter(ppx1,ppy1, label= "Buffon", color= "black",marker= "*", s=110)
                if playerp==2:
                    hp2=-1
                    plt.scatter(ppx2,ppy2, label= "Thiago Silva", color= "black",marker= "*", s=110)
                if playerp==3:
                    hp3=-1
                    plt.scatter(ppx3,ppy3, label= "Kimbempe", color= "black",marker= "*", s=110)
                if playerp==4:
                    hp4=-1
                    plt.scatter(ppx4,ppy4, label= "Meunier", color= "black",marker= "*", s=110)
                if playerp==5:
                    hp5=-1
                    plt.scatter(ppx5,ppy5, label= "Marquinhos", color= "black",marker= "*", s=110)
                if playerp==6:
                    hp6=-1
                    plt.scatter(ppx6,ppy6, label= "Verrati", color= "black",marker= "*", s=110)
                if playerp==7:
                    hp7=-1
                    plt.scatter(ppx7,ppy7, label= "Dani Alves", color= "black",marker= "*", s=110)
                if playerp==8:
                    hp8=-1
                    plt.scatter(ppx8,ppy8, label= "Rabiot", color= "black",marker= "*", s=110)
                if playerp==9:
                    hp9=-1
                    plt.scatter(ppx9,ppy9, label= "Cavani", color= "black",marker= "*", s=110)
                if playerp==10:
                    hp10=-1
                    plt.scatter(ppx10,ppy10, label= "Neymar JR", color= "black",marker= "*", s=110)
                if playerp==11:
                    hp11=-1
                    plt.scatter(ppx11,ppy11, label= "Mbappe", color= "black",marker= "*", s=110)
                    
                plt.xlabel('Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! ') 
            
                plt.ylabel('Messi! Messi! Messi! Messi! Messi! Messi!') 
            
                plt.title('FIFA PYTHON 18\nPSG(BLUE) VS BARCELONA(RED)')  
            
                plt.show()     
                
                print()

                continue
                
        if n==3 and y!=3:
            if playerp<9:
                playerp=playerp+3
                if playerb==1:
                    playerbn='Ter Stegnen'
                    if subb1!=0:
                        playerbn=playerbin1        
                if playerb==2:
                    playerbn='Umtiti'
                    if subb2!=0:
                        playerbn=playerbin2    
                if playerb==3:
                    playerbn='Pique'
                    if subb3!=0:
                        playerbn=playerbin3    
                if playerb==4:
                    playerbn='Rakitic'
                    if subb4!=0:
                        playerbn=playerbin4
                if playerb==5:
                    playerbn='Sergio Busquets'
                    if subb5!=0:
                        playerbn=playerbin5    
                if playerb==6:
                    playerbn='Denis Suarez'
                    if subb6!=0:
                        playerbn=playerbin6    
                if playerb==7:
                    playerbn='Coutinho'
                    if subb7!=0:
                        playerbn=playerbin7    
                if playerb==8:
                    playerbn='Arthur'
                    if subb8!=0:
                        playerbn=playerbin8    
                if playerb==9:
                    playerbn='Suarez'
                    if subb9!=0:
                        playerbn=playerbin9    
                if playerb==10:
                    playerbn='Messi'
                    if subb10!=0:
                        playerbn=playerbin10    
                if playerb==11:
                    playerbn='Dembele'
                    if subb11!=0:
                        playerbn=playerbin11    
                if playerp==1:
                    playerpn='Buffon'
                    if subp1!=0:
                        playerpn=playerpin1
                if playerp==2:
                    playerpn='Thiago Silva'
                    if subp2!=0:
                        playerpn=playerpin2    
                if playerp==3:
                    playerpn='Kimbempe'
                    if subp3!=0:
                        playerpn=playerpin3     
                if playerp==4:
                    playerpn='Meunier'
                    if subp4!=0:
                        playerpn=playerpin4    
                if playerp==5:
                    playerpn='Marquinhos'
                    if subp5!=0:
                        playerpn=playerpin5    
                if playerp==6:
                    playerpn='Verrati'
                    if subp6!=0:
                        playerpn=playerpin6    
                if playerp==7:
                    playerpn='Dani Alves'
                    if subp7!=0:
                        playerpn=playerpin7    
                if playerp==8:
                    playerpn='Rabiot'
                    if subp8!=0:
                        playerpn=playerpin8    
                if playerp==9:
                    playerpn='Cavani'
                    if subp9!=0:
                        playerpn=playerpin9    
                if playerp==10:
                    playerpn='Neymar JR'
                    if subp10!=0:
                        playerpn=playerpin10    
                if playerp==11:
                    playerpn='Mbappe'
                    if subp11!=0:
                        playerpn=playerpin11
                print('Commentatory: Through ball to player',playerpn,'succesful !! what ball man !! WOW!!')
                time=time+1
                print()
                
                print('           [ Time :',time,'min || PSG:',psggoal,'| BAR:',bargoal,']')    
            
                h=2
                ppx1=h*5
                ppx2=random.randint(h*10,h*30)
                ppx3=random.randint(h*10,h*30)
                ppx4=random.randint(h*10,h*30)
                ppx5=random.randint(h*10,h*30)
                ppx6=random.randint(h*35,h*55)
                ppx7=random.randint(h*35,h*55)
                ppx8=random.randint(h*35,h*55)
                ppx9=random.randint(h*60,h*85)
                ppx10=random.randint(h*65,h*90)
                ppx11=random.randint(h*60,h*85)
                
                ppy1=random.randint(h*40,h*60)
                ppy2=random.randint(h*0,h*15)
                ppy3=random.randint(h*30,h*45)
                ppy4=random.randint(h*55,h*70)
                ppy5=random.randint(h*85,h*100)
                ppy6=random.randint(h*0,h*20)
                ppy7=random.randint(h*40,h*60)
                ppy8=random.randint(h*80,h*100)
                ppy9=random.randint(h*15,h*30)
                ppy10=random.randint(h*45,h*55)
                ppy11=random.randint(h*70,h*85)
                
                pbx1=h*95
                pbx2=random.randint(h*70,h*90)
                pbx3=random.randint(h*70,h*90)
                pbx4=random.randint(h*70,h*90)
                pbx5=random.randint(h*70,h*90)
                pbx6=random.randint(h*45,h*65)
                pbx7=random.randint(h*45,h*65)
                pbx8=random.randint(h*45,h*65)
                pbx9=random.randint(h*15,h*40)
                pbx10=random.randint(h*10,h*35)
                pbx11=random.randint(h*15,h*40)
                
                pby1=random.randint(h*40,h*60)
                pby2=random.randint(h*0,h*15)
                pby3=random.randint(h*30,h*45)
                pby4=random.randint(h*55,h*70)
                pby5=random.randint(h*85,h*100)
                pby6=random.randint(h*0,h*20)
                pby7=random.randint(h*40,h*60)
                pby8=random.randint(h*80,h*100)
                pby9=random.randint(h*15,h*30)
                pby10=random.randint(h*45,h*55)
                pby11=random.randint(h*70,h*85)
                
                print('          ',end='')
                lines = [[(h*0, h*35), (h*0, h*65)], [(h*100, h*35), (h*100, h*65)], [(h*50, h*105), (h*50, h*-5)], [(h*-10, h*105), (h*110, h*105)], [(h*-10, h*-5), (h*110, h*-5)], [(h*-10, h*105), (h*-10, h*-5)], [(h*110, h*105), (h*110, h*-5)], [(h*0, h*35), (h*-10, h*35)], [(h*0, h*65), (h*-10, h*65)], [(h*100, h*35), (h*110, h*35)], [(h*100, h*65), (h*110, h*65)]]
                c = np.array([(1, 0, 0, 1), (1, 0, 0, 1), (1, 0, 0, 1)])
                
                lc = mc.LineCollection(lines, colors=c, linewidths=1)
                fig, ax = pl.subplots()
                ax.set_facecolor('xkcd:sky blue')
                ax.set_facecolor((0.8, 1, 0.5))
                ax.add_collection(lc)
                ax.autoscale()
                ax.margins(0.1)
            
                psgx = [ppx2,ppx3,ppx4,ppx5,ppx6,ppx7,ppx8,ppx9,ppx10,ppx11] 
                psgy = [ppy2,ppy3,ppy4,ppy5,ppy6,ppy7,ppy8,ppy9,ppy10,ppy11] 
            
                plt.scatter(ppx1,ppy1,color= "purple",marker= "*", s=100)      # GK edit colour
                plt.scatter(psgx, psgy,color= "blue",marker= "*", s=80)  
            
                barx = [pbx2,pbx3,pbx4,pbx5,pbx6,pbx7,pbx8,pbx9,pbx10,pbx11] 
                bary = [pby2,pby3,pby4,pby5,pby6,pby7,pby8,pby9,pby10,pby11]
            
                plt.scatter(pbx1,pby1,color= "violet",marker= "o", s=100)      # GK edit colour
                plt.scatter(barx, bary, color= "red",marker= "o", s=80)      
                        
                if playerp==1:
                    hp1=-1
                    plt.scatter(ppx1,ppy1, label= "Buffon", color= "black",marker= "*", s=110)
                if playerp==2:
                    hp2=-1
                    plt.scatter(ppx2,ppy2, label= "Thiago Silva", color= "black",marker= "*", s=110)
                if playerp==3:
                    hp3=-1
                    plt.scatter(ppx3,ppy3, label= "Kimbempe", color= "black",marker= "*", s=110)
                if playerp==4:
                    hp4=-1
                    plt.scatter(ppx4,ppy4, label= "Meunier", color= "black",marker= "*", s=110)
                if playerp==5:
                    hp5=-1
                    plt.scatter(ppx5,ppy5, label= "Marquinhos", color= "black",marker= "*", s=110)
                if playerp==6:
                    hp6=-1
                    plt.scatter(ppx6,ppy6, label= "Verrati", color= "black",marker= "*", s=110)
                if playerp==7:
                    hp7=-1
                    plt.scatter(ppx7,ppy7, label= "Dani Alves", color= "black",marker= "*", s=110)
                if playerp==8:
                    hp8=-1
                    plt.scatter(ppx8,ppy8, label= "Rabiot", color= "black",marker= "*", s=110)
                if playerp==9:
                    hp9=-1
                    plt.scatter(ppx9,ppy9, label= "Cavani", color= "black",marker= "*", s=110)
                if playerp==10:
                    hp10=-1
                    plt.scatter(ppx10,ppy10, label= "Neymar JR", color= "black",marker= "*", s=110)
                if playerp==11:
                    hp11=-1
                    plt.scatter(ppx11,ppy11, label= "Mbappe", color= "black",marker= "*", s=110)
                    
                plt.xlabel('Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! ') 
            
                plt.ylabel('Messi! Messi! Messi! Messi! Messi! Messi!') 
            
                plt.title('FIFA PYTHON 18\nPSG(BLUE) VS BARCELONA(RED)')  
            
                plt.show()     
                
                print()

                continue

            else:
                playerp=playerp-3
                if playerb==1:
                    playerbn='Ter Stegnen'
                    if subb1!=0:
                        playerbn=playerbin1        
                if playerb==2:
                    playerbn='Umtiti'
                    if subb2!=0:
                        playerbn=playerbin2    
                if playerb==3:
                    playerbn='Pique'
                    if subb3!=0:
                        playerbn=playerbin3    
                if playerb==4:
                    playerbn='Rakitic'
                    if subb4!=0:
                        playerbn=playerbin4
                if playerb==5:
                    playerbn='Sergio Busquets'
                    if subb5!=0:
                        playerbn=playerbin5    
                if playerb==6:
                    playerbn='Denis Suarez'
                    if subb6!=0:
                        playerbn=playerbin6    
                if playerb==7:
                    playerbn='Coutinho'
                    if subb7!=0:
                        playerbn=playerbin7    
                if playerb==8:
                    playerbn='Arthur'
                    if subb8!=0:
                        playerbn=playerbin8    
                if playerb==9:
                    playerbn='Suarez'
                    if subb9!=0:
                        playerbn=playerbin9    
                if playerb==10:
                    playerbn='Messi'
                    if subb10!=0:
                        playerbn=playerbin10    
                if playerb==11:
                    playerbn='Dembele'
                    if subb11!=0:
                        playerbn=playerbin11    
                if playerp==1:
                    playerpn='Buffon'
                    if subp1!=0:
                        playerpn=playerpin1
                if playerp==2:
                    playerpn='Thiago Silva'
                    if subp2!=0:
                        playerpn=playerpin2    
                if playerp==3:
                    playerpn='Kimbempe'
                    if subp3!=0:
                        playerpn=playerpin3     
                if playerp==4:
                    playerpn='Meunier'
                    if subp4!=0:
                        playerpn=playerpin4    
                if playerp==5:
                    playerpn='Marquinhos'
                    if subp5!=0:
                        playerpn=playerpin5    
                if playerp==6:
                    playerpn='Verrati'
                    if subp6!=0:
                        playerpn=playerpin6    
                if playerp==7:
                    playerpn='Dani Alves'
                    if subp7!=0:
                        playerpn=playerpin7    
                if playerp==8:
                    playerpn='Rabiot'
                    if subp8!=0:
                        playerpn=playerpin8    
                if playerp==9:
                    playerpn='Cavani'
                    if subp9!=0:
                        playerpn=playerpin9    
                if playerp==10:
                    playerpn='Neymar JR'
                    if subp10!=0:
                        playerpn=playerpin10    
                if playerp==11:
                    playerpn='Mbappe'
                    if subp11!=0:
                        playerpn=playerpin11
                print('Commentatory: Through ball to player',playerpn,'succesful !!')
                time=time+1
                print()
                
                print('           [ Time :',time,'min || PSG:',psggoal,'| BAR:',bargoal,']')    
            
                h=2
                ppx1=h*5
                ppx2=random.randint(h*10,h*30)
                ppx3=random.randint(h*10,h*30)
                ppx4=random.randint(h*10,h*30)
                ppx5=random.randint(h*10,h*30)
                ppx6=random.randint(h*35,h*55)
                ppx7=random.randint(h*35,h*55)
                ppx8=random.randint(h*35,h*55)
                ppx9=random.randint(h*60,h*85)
                ppx10=random.randint(h*65,h*90)
                ppx11=random.randint(h*60,h*85)
                
                ppy1=random.randint(h*40,h*60)
                ppy2=random.randint(h*0,h*15)
                ppy3=random.randint(h*30,h*45)
                ppy4=random.randint(h*55,h*70)
                ppy5=random.randint(h*85,h*100)
                ppy6=random.randint(h*0,h*20)
                ppy7=random.randint(h*40,h*60)
                ppy8=random.randint(h*80,h*100)
                ppy9=random.randint(h*15,h*30)
                ppy10=random.randint(h*45,h*55)
                ppy11=random.randint(h*70,h*85)
                
                pbx1=h*95
                pbx2=random.randint(h*70,h*90)
                pbx3=random.randint(h*70,h*90)
                pbx4=random.randint(h*70,h*90)
                pbx5=random.randint(h*70,h*90)
                pbx6=random.randint(h*45,h*65)
                pbx7=random.randint(h*45,h*65)
                pbx8=random.randint(h*45,h*65)
                pbx9=random.randint(h*15,h*40)
                pbx10=random.randint(h*10,h*35)
                pbx11=random.randint(h*15,h*40)
                
                pby1=random.randint(h*40,h*60)
                pby2=random.randint(h*0,h*15)
                pby3=random.randint(h*30,h*45)
                pby4=random.randint(h*55,h*70)
                pby5=random.randint(h*85,h*100)
                pby6=random.randint(h*0,h*20)
                pby7=random.randint(h*40,h*60)
                pby8=random.randint(h*80,h*100)
                pby9=random.randint(h*15,h*30)
                pby10=random.randint(h*45,h*55)
                pby11=random.randint(h*70,h*85)
                
                print('          ',end='')
                lines = [[(h*0, h*35), (h*0, h*65)], [(h*100, h*35), (h*100, h*65)], [(h*50, h*105), (h*50, h*-5)], [(h*-10, h*105), (h*110, h*105)], [(h*-10, h*-5), (h*110, h*-5)], [(h*-10, h*105), (h*-10, h*-5)], [(h*110, h*105), (h*110, h*-5)], [(h*0, h*35), (h*-10, h*35)], [(h*0, h*65), (h*-10, h*65)], [(h*100, h*35), (h*110, h*35)], [(h*100, h*65), (h*110, h*65)]]
                c = np.array([(1, 0, 0, 1), (1, 0, 0, 1), (1, 0, 0, 1)])
                
                lc = mc.LineCollection(lines, colors=c, linewidths=1)
                fig, ax = pl.subplots()
                ax.set_facecolor('xkcd:sky blue')
                ax.set_facecolor((0.8, 1, 0.5))
                ax.add_collection(lc)
                ax.autoscale()
                ax.margins(0.1)
            
                psgx = [ppx2,ppx3,ppx4,ppx5,ppx6,ppx7,ppx8,ppx9,ppx10,ppx11] 
                psgy = [ppy2,ppy3,ppy4,ppy5,ppy6,ppy7,ppy8,ppy9,ppy10,ppy11] 
            
                plt.scatter(ppx1,ppy1,color= "purple",marker= "*", s=100)      # GK edit colour
                plt.scatter(psgx, psgy,color= "blue",marker= "*", s=80)  
            
                barx = [pbx2,pbx3,pbx4,pbx5,pbx6,pbx7,pbx8,pbx9,pbx10,pbx11] 
                bary = [pby2,pby3,pby4,pby5,pby6,pby7,pby8,pby9,pby10,pby11]
            
                plt.scatter(pbx1,pby1,color= "violet",marker= "o", s=100)      # GK edit colour
                plt.scatter(barx, bary, color= "red",marker= "o", s=80)      
                        
                if playerp==1:
                    hp1=-1
                    plt.scatter(ppx1,ppy1, label= "Buffon", color= "black",marker= "*", s=110)
                if playerp==2:
                    hp2=-1
                    plt.scatter(ppx2,ppy2, label= "Thiago Silva", color= "black",marker= "*", s=110)
                if playerp==3:
                    hp3=-1
                    plt.scatter(ppx3,ppy3, label= "Kimbempe", color= "black",marker= "*", s=110)
                if playerp==4:
                    hp4=-1
                    plt.scatter(ppx4,ppy4, label= "Meunier", color= "black",marker= "*", s=110)
                if playerp==5:
                    hp5=-1
                    plt.scatter(ppx5,ppy5, label= "Marquinhos", color= "black",marker= "*", s=110)
                if playerp==6:
                    hp6=-1
                    plt.scatter(ppx6,ppy6, label= "Verrati", color= "black",marker= "*", s=110)
                if playerp==7:
                    hp7=-1
                    plt.scatter(ppx7,ppy7, label= "Dani Alves", color= "black",marker= "*", s=110)
                if playerp==8:
                    hp8=-1
                    plt.scatter(ppx8,ppy8, label= "Rabiot", color= "black",marker= "*", s=110)
                if playerp==9:
                    hp9=-1
                    plt.scatter(ppx9,ppy9, label= "Cavani", color= "black",marker= "*", s=110)
                if playerp==10:
                    hp10=-1
                    plt.scatter(ppx10,ppy10, label= "Neymar JR", color= "black",marker= "*", s=110)
                if playerp==11:
                    hp11=-1
                    plt.scatter(ppx11,ppy11, label= "Mbappe", color= "black",marker= "*", s=110)
                    
                plt.xlabel('Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! ') 
            
                plt.ylabel('Messi! Messi! Messi! Messi! Messi! Messi!') 
            
                plt.title('FIFA PYTHON 18\nPSG(BLUE) VS BARCELONA(RED)')  
            
                plt.show()     
                
                print()

                continue
                
        if n==4 and y==4:
            if playerp>8:
                psggoal=psggoal+1
                bar=1
                psg=0
                playerb=10
                print('Commentatory:',playerpn,'scores!!! Goooooal!! Awesome!!! BARCELONA',bargoal,'and PSG',psggoal)
                print('Commentatory: Now Messi starts...')
                print()
                time=time+1
                print()
                
                print('           [ Time :',time,'min || PSG:',psggoal,'| BAR:',bargoal,']')    
            
                h=2
                ppx1=h*5
                ppx2=random.randint(h*10,h*30)
                ppx3=random.randint(h*10,h*30)
                ppx4=random.randint(h*10,h*30)
                ppx5=random.randint(h*10,h*30)
                ppx6=random.randint(h*35,h*55)
                ppx7=random.randint(h*35,h*55)
                ppx8=random.randint(h*35,h*55)
                ppx9=random.randint(h*60,h*85)
                ppx10=random.randint(h*65,h*90)
                ppx11=random.randint(h*60,h*85)
                
                ppy1=random.randint(h*40,h*60)
                ppy2=random.randint(h*0,h*15)
                ppy3=random.randint(h*30,h*45)
                ppy4=random.randint(h*55,h*70)
                ppy5=random.randint(h*85,h*100)
                ppy6=random.randint(h*0,h*20)
                ppy7=random.randint(h*40,h*60)
                ppy8=random.randint(h*80,h*100)
                ppy9=random.randint(h*15,h*30)
                ppy10=random.randint(h*45,h*55)
                ppy11=random.randint(h*70,h*85)
                
                pbx1=h*95
                pbx2=random.randint(h*70,h*90)
                pbx3=random.randint(h*70,h*90)
                pbx4=random.randint(h*70,h*90)
                pbx5=random.randint(h*70,h*90)
                pbx6=random.randint(h*45,h*65)
                pbx7=random.randint(h*45,h*65)
                pbx8=random.randint(h*45,h*65)
                pbx9=random.randint(h*15,h*40)
                pbx10=random.randint(h*10,h*35)
                pbx11=random.randint(h*15,h*40)
                
                pby1=random.randint(h*40,h*60)
                pby2=random.randint(h*0,h*15)
                pby3=random.randint(h*30,h*45)
                pby4=random.randint(h*55,h*70)
                pby5=random.randint(h*85,h*100)
                pby6=random.randint(h*0,h*20)
                pby7=random.randint(h*40,h*60)
                pby8=random.randint(h*80,h*100)
                pby9=random.randint(h*15,h*30)
                pby10=random.randint(h*45,h*55)
                pby11=random.randint(h*70,h*85)
                
                print('          ',end='')
                lines = [[(h*0, h*35), (h*0, h*65)], [(h*100, h*35), (h*100, h*65)], [(h*50, h*105), (h*50, h*-5)], [(h*-10, h*105), (h*110, h*105)], [(h*-10, h*-5), (h*110, h*-5)], [(h*-10, h*105), (h*-10, h*-5)], [(h*110, h*105), (h*110, h*-5)], [(h*0, h*35), (h*-10, h*35)], [(h*0, h*65), (h*-10, h*65)], [(h*100, h*35), (h*110, h*35)], [(h*100, h*65), (h*110, h*65)]]
                c = np.array([(1, 0, 0, 1), (1, 0, 0, 1), (1, 0, 0, 1)])
                
                lc = mc.LineCollection(lines, colors=c, linewidths=1)
                fig, ax = pl.subplots()
                ax.set_facecolor('xkcd:sky blue')
                ax.set_facecolor((0.8, 1, 0.5))
                ax.add_collection(lc)
                ax.autoscale()
                ax.margins(0.1)
            
                psgx = [ppx2,ppx3,ppx4,ppx5,ppx6,ppx7,ppx8,ppx9,ppx10,ppx11] 
                psgy = [ppy2,ppy3,ppy4,ppy5,ppy6,ppy7,ppy8,ppy9,ppy10,ppy11] 
            
                plt.scatter(ppx1,ppy1,color= "purple",marker= "*", s=100)      # GK edit colour
                plt.scatter(psgx, psgy,color= "blue",marker= "*", s=80)  
            
                barx = [pbx2,pbx3,pbx4,pbx5,pbx6,pbx7,pbx8,pbx9,pbx10,pbx11] 
                bary = [pby2,pby3,pby4,pby5,pby6,pby7,pby8,pby9,pby10,pby11]
            
                plt.scatter(pbx1,pby1,color= "violet",marker= "o", s=100)      # GK edit colour
                plt.scatter(barx, bary, color= "red",marker= "o", s=80)      
                        
                if playerp==1:
                    hp1=-1
                    plt.scatter(ppx1,ppy1, label= "Buffon", color= "black",marker= "*", s=110)
                if playerp==2:
                    hp2=-1
                    plt.scatter(ppx2,ppy2, label= "Thiago Silva", color= "black",marker= "*", s=110)
                if playerp==3:
                    hp3=-1
                    plt.scatter(ppx3,ppy3, label= "Kimbempe", color= "black",marker= "*", s=110)
                if playerp==4:
                    hp4=-1
                    plt.scatter(ppx4,ppy4, label= "Meunier", color= "black",marker= "*", s=110)
                if playerp==5:
                    hp5=-1
                    plt.scatter(ppx5,ppy5, label= "Marquinhos", color= "black",marker= "*", s=110)
                if playerp==6:
                    hp6=-1
                    plt.scatter(ppx6,ppy6, label= "Verrati", color= "black",marker= "*", s=110)
                if playerp==7:
                    hp7=-1
                    plt.scatter(ppx7,ppy7, label= "Dani Alves", color= "black",marker= "*", s=110)
                if playerp==8:
                    hp8=-1
                    plt.scatter(ppx8,ppy8, label= "Rabiot", color= "black",marker= "*", s=110)
                if playerp==9:
                    hp9=-1
                    plt.scatter(ppx9,ppy9, label= "Cavani", color= "black",marker= "*", s=110)
                if playerb==10:
                    hb10=-1
                    plt.scatter(pbx10,pby10, label= "Messi", color= "black",marker= "o", s=110)
                if playerp==11:
                    hp11=-1
                    plt.scatter(ppx11,ppy11, label= "Mbappe", color= "black",marker= "*", s=110)
                    
                plt.xlabel('Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! ') 
            
                plt.ylabel('Messi! Messi! Messi! Messi! Messi! Messi!') 
            
                plt.title('FIFA PYTHON 18\nPSG(BLUE) VS BARCELONA(RED)')  
            
                plt.show()     
                
                print()

                continue

            if playerp<=8:
                psg=0
                bar=1
                playerb=1
                if playerb==1:
                    playerbn='Ter Stegnen'
                    if subb1!=0:
                        playerbn=playerbin1 
                print('Commentatory:',playerbin1,'saves it')
                time=time+1
                print()
                
                print('           [ Time :',time,'min || PSG:',psggoal,'| BAR:',bargoal,']')    
            
                h=2
                ppx1=h*5
                ppx2=random.randint(h*10,h*30)
                ppx3=random.randint(h*10,h*30)
                ppx4=random.randint(h*10,h*30)
                ppx5=random.randint(h*10,h*30)
                ppx6=random.randint(h*35,h*55)
                ppx7=random.randint(h*35,h*55)
                ppx8=random.randint(h*35,h*55)
                ppx9=random.randint(h*60,h*85)
                ppx10=random.randint(h*65,h*90)
                ppx11=random.randint(h*60,h*85)
                
                ppy1=random.randint(h*40,h*60)
                ppy2=random.randint(h*0,h*15)
                ppy3=random.randint(h*30,h*45)
                ppy4=random.randint(h*55,h*70)
                ppy5=random.randint(h*85,h*100)
                ppy6=random.randint(h*0,h*20)
                ppy7=random.randint(h*40,h*60)
                ppy8=random.randint(h*80,h*100)
                ppy9=random.randint(h*15,h*30)
                ppy10=random.randint(h*45,h*55)
                ppy11=random.randint(h*70,h*85)
                
                pbx1=h*95
                pbx2=random.randint(h*70,h*90)
                pbx3=random.randint(h*70,h*90)
                pbx4=random.randint(h*70,h*90)
                pbx5=random.randint(h*70,h*90)
                pbx6=random.randint(h*45,h*65)
                pbx7=random.randint(h*45,h*65)
                pbx8=random.randint(h*45,h*65)
                pbx9=random.randint(h*15,h*40)
                pbx10=random.randint(h*10,h*35)
                pbx11=random.randint(h*15,h*40)
                
                pby1=random.randint(h*40,h*60)
                pby2=random.randint(h*0,h*15)
                pby3=random.randint(h*30,h*45)
                pby4=random.randint(h*55,h*70)
                pby5=random.randint(h*85,h*100)
                pby6=random.randint(h*0,h*20)
                pby7=random.randint(h*40,h*60)
                pby8=random.randint(h*80,h*100)
                pby9=random.randint(h*15,h*30)
                pby10=random.randint(h*45,h*55)
                pby11=random.randint(h*70,h*85)
                
                print('          ',end='')
                lines = [[(h*0, h*35), (h*0, h*65)], [(h*100, h*35), (h*100, h*65)], [(h*50, h*105), (h*50, h*-5)], [(h*-10, h*105), (h*110, h*105)], [(h*-10, h*-5), (h*110, h*-5)], [(h*-10, h*105), (h*-10, h*-5)], [(h*110, h*105), (h*110, h*-5)], [(h*0, h*35), (h*-10, h*35)], [(h*0, h*65), (h*-10, h*65)], [(h*100, h*35), (h*110, h*35)], [(h*100, h*65), (h*110, h*65)]]
                c = np.array([(1, 0, 0, 1), (1, 0, 0, 1), (1, 0, 0, 1)])
                
                lc = mc.LineCollection(lines, colors=c, linewidths=1)
                fig, ax = pl.subplots()
                ax.set_facecolor('xkcd:sky blue')
                ax.set_facecolor((0.8, 1, 0.5))
                ax.add_collection(lc)
                ax.autoscale()
                ax.margins(0.1)
            
                psgx = [ppx2,ppx3,ppx4,ppx5,ppx6,ppx7,ppx8,ppx9,ppx10,ppx11] 
                psgy = [ppy2,ppy3,ppy4,ppy5,ppy6,ppy7,ppy8,ppy9,ppy10,ppy11] 
            
                plt.scatter(ppx1,ppy1,color= "purple",marker= "*", s=100)      # GK edit colour
                plt.scatter(psgx, psgy,color= "blue",marker= "*", s=80)  
             
                barx = [pbx2,pbx3,pbx4,pbx5,pbx6,pbx7,pbx8,pbx9,pbx10,pbx11] 
                bary = [pby2,pby3,pby4,pby5,pby6,pby7,pby8,pby9,pby10,pby11]
            
                plt.scatter(pbx1,pby1,color= "violet",marker= "o", s=100)      # GK edit colour
                plt.scatter(barx, bary, color= "red",marker= "o", s=80)       
                
                if playerb==1:
                    hb1-=1
                    plt.scatter(pbx1,pby1, label= "Ter Stegnen", color= "black",marker= "o", s=110)
                if playerb==2:
                    hb2-=1
                    plt.scatter(pbx2,pby2, label= "Umtiti", color= "black",marker= "o", s=110)
                if playerb==3:
                    hb3-=1
                    plt.scatter(pbx3,pby3, label= "Pique", color= "black",marker= "o", s=110)
                if playerb==4:
                    hb4-=1
                    plt.scatter(pbx4,pby4, label= "Rakitic", color= "black",marker= "o", s=110)
                if playerb==5:
                    hb5-=1
                    plt.scatter(pbx5,pby5, label= "Sergio Busquets", color= "black",marker= "o", s=110)
                if playerb==6:
                    hb6-=1
                    plt.scatter(pbx6,pby6, label= "Denis Suarez", color= "black",marker= "o", s=110)
                if playerb==7:
                    hb7-=1
                    plt.scatter(pbx7,pby7, label= "Coutinho", color= "black",marker= "o", s=110)
                if playerb==8:
                    hb8-=1
                    plt.scatter(pbx8,pby8, label= "Arthur", color= "black",marker= "o", s=110)
                if playerb==9:
                    hb9-=1
                    plt.scatter(pbx9,pby9, label= "Suarez", color= "black",marker= "o", s=110)
                if playerb==10:
                    hb10-=1
                    plt.scatter(pbx10,pby10, label= "Messi", color= "black",marker= "o", s=110)
                if playerb==11:
                    hb11-=1
                    plt.scatter(pbx11,pby11, label= "Dembele", color= "black",marker= "o", s=110)
                    
                plt.xlabel('Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! ') 
            
                plt.ylabel('Messi! Messi! Messi! Messi! Messi! Messi!') 
             
                plt.title('FIFA PYTHON 18\nPSG(BLUE) VS BARCELONA(RED)')  
            
                plt.show()     
                
                print()

                continue
        
        if n==4 and y!=4:
            bar=1
            psg=0
            playerb=1
            if playerb==1:
                playerbn='Ter Stegnen'
                if subb1!=0:
                    playerbn=playerbin1 
            print('Commentatory:',playerbin1,'saves it')
            time=time+1
            print()
            
            print('           [ Time :',time,'min || PSG:',psggoal,'| BAR:',bargoal,']')    
        
            h=2
            ppx1=h*5
            ppx2=random.randint(h*10,h*30)
            ppx3=random.randint(h*10,h*30)
            ppx4=random.randint(h*10,h*30)
            ppx5=random.randint(h*10,h*30)
            ppx6=random.randint(h*35,h*55)
            ppx7=random.randint(h*35,h*55)
            ppx8=random.randint(h*35,h*55)
            ppx9=random.randint(h*60,h*85)
            ppx10=random.randint(h*65,h*90)
            ppx11=random.randint(h*60,h*85)
            
            ppy1=random.randint(h*40,h*60)
            ppy2=random.randint(h*0,h*15)
            ppy3=random.randint(h*30,h*45)
            ppy4=random.randint(h*55,h*70)
            ppy5=random.randint(h*85,h*100)
            ppy6=random.randint(h*0,h*20)
            ppy7=random.randint(h*40,h*60)
            ppy8=random.randint(h*80,h*100)
            ppy9=random.randint(h*15,h*30)
            ppy10=random.randint(h*45,h*55)
            ppy11=random.randint(h*70,h*85)
            
            pbx1=h*95
            pbx2=random.randint(h*70,h*90)
            pbx3=random.randint(h*70,h*90)
            pbx4=random.randint(h*70,h*90)
            pbx5=random.randint(h*70,h*90)
            pbx6=random.randint(h*45,h*65)
            pbx7=random.randint(h*45,h*65)
            pbx8=random.randint(h*45,h*65)
            pbx9=random.randint(h*15,h*40)
            pbx10=random.randint(h*10,h*35)
            pbx11=random.randint(h*15,h*40)
            
            pby1=random.randint(h*40,h*60)
            pby2=random.randint(h*0,h*15)
            pby3=random.randint(h*30,h*45)
            pby4=random.randint(h*55,h*70)
            pby5=random.randint(h*85,h*100)
            pby6=random.randint(h*0,h*20)
            pby7=random.randint(h*40,h*60)
            pby8=random.randint(h*80,h*100)
            pby9=random.randint(h*15,h*30)
            pby10=random.randint(h*45,h*55)
            pby11=random.randint(h*70,h*85)
            
            print('          ',end='')
            lines = [[(h*0, h*35), (h*0, h*65)], [(h*100, h*35), (h*100, h*65)], [(h*50, h*105), (h*50, h*-5)], [(h*-10, h*105), (h*110, h*105)], [(h*-10, h*-5), (h*110, h*-5)], [(h*-10, h*105), (h*-10, h*-5)], [(h*110, h*105), (h*110, h*-5)], [(h*0, h*35), (h*-10, h*35)], [(h*0, h*65), (h*-10, h*65)], [(h*100, h*35), (h*110, h*35)], [(h*100, h*65), (h*110, h*65)]]
            c = np.array([(1, 0, 0, 1), (1, 0, 0, 1), (1, 0, 0, 1)])
            
            lc = mc.LineCollection(lines, colors=c, linewidths=1)
            fig, ax = pl.subplots()
            ax.set_facecolor('xkcd:sky blue')
            ax.set_facecolor((0.8, 1, 0.5))
            ax.add_collection(lc)
            ax.autoscale()
            ax.margins(0.1)
        
            psgx = [ppx2,ppx3,ppx4,ppx5,ppx6,ppx7,ppx8,ppx9,ppx10,ppx11] 
            psgy = [ppy2,ppy3,ppy4,ppy5,ppy6,ppy7,ppy8,ppy9,ppy10,ppy11] 
        
            plt.scatter(ppx1,ppy1,color= "purple",marker= "*", s=100)      # GK edit colour
            plt.scatter(psgx, psgy,color= "blue",marker= "*", s=80)  
        
            barx = [pbx2,pbx3,pbx4,pbx5,pbx6,pbx7,pbx8,pbx9,pbx10,pbx11] 
            bary = [pby2,pby3,pby4,pby5,pby6,pby7,pby8,pby9,pby10,pby11]
        
            plt.scatter(pbx1,pby1,color= "violet",marker= "o", s=100)      # GK edit colour
            plt.scatter(barx, bary, color= "red",marker= "o", s=80)      
                    
            if playerb==1:
                hb1=-1
                plt.scatter(pbx1,pby1, label= "Ter Stegnen", color= "black",marker= "o", s=110)
            if playerp==2:
                hp2=-1
                plt.scatter(ppx2,ppy2, label= "Thiago Silva", color= "black",marker= "*", s=110)
            if playerp==3:
                hp3=-1
                plt.scatter(ppx3,ppy3, label= "Kimbempe", color= "black",marker= "*", s=110)
            if playerp==4:
                hp4=-1
                plt.scatter(ppx4,ppy4, label= "Meunier", color= "black",marker= "*", s=110)
            if playerp==5:
                hp5=-1
                plt.scatter(ppx5,ppy5, label= "Marquinhos", color= "black",marker= "*", s=110)
            if playerp==6:
                hp6=-1
                plt.scatter(ppx6,ppy6, label= "Verrati", color= "black",marker= "*", s=110)
            if playerp==7:
                hp7=-1
                plt.scatter(ppx7,ppy7, label= "Dani Alves", color= "black",marker= "*", s=110)
            if playerp==8:
                hp8=-1
                plt.scatter(ppx8,ppy8, label= "Rabiot", color= "black",marker= "*", s=110)
            if playerp==9:
                hp9=-1
                plt.scatter(ppx9,ppy9, label= "Cavani", color= "black",marker= "*", s=110)
            if playerp==10:
                hp10=-1
                plt.scatter(ppx10,ppy10, label= "Neymar JR", color= "black",marker= "*", s=110)
            if playerp==11:
                hp11=-1
                plt.scatter(ppx11,ppy11, label= "Mbappe", color= "black",marker= "*", s=110)
                
            plt.xlabel('Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! ') 
        
            plt.ylabel('Messi! Messi! Messi! Messi! Messi! Messi!') 
        
            plt.title('FIFA PYTHON 18\nPSG(BLUE) VS BARCELONA(RED)')  
        
            plt.show()     
            
            print()

            continue
            
        
        if n!=4 and n==y :
                bar=1
                psg=0
                playerb=12-playerp
                if playerb==1:
                    playerbn='Ter Stegnen'
                    if subb1!=0:
                        playerbn=playerbin1        
                if playerb==2:
                    playerbn='Umtiti'
                    if subb2!=0:
                        playerbn=playerbin2    
                if playerb==3:
                    playerbn='Pique'
                    if subb3!=0:
                        playerbn=playerbin3    
                if playerb==4:
                    playerbn='Rakitic'
                    if subb4!=0:
                        playerbn=playerbin4
                if playerb==5:
                    playerbn='Sergio Busquets'
                    if subb5!=0:
                        playerbn=playerbin5    
                if playerb==6:
                    playerbn='Denis Suarez'
                    if subb6!=0:
                        playerbn=playerbin6    
                if playerb==7:
                    playerbn='Coutinho'
                    if subb7!=0:
                        playerbn=playerbin7    
                if playerb==8:
                    playerbn='Arthur'
                    if subb8!=0:
                        playerbn=playerbin8    
                if playerb==9:
                    playerbn='Suarez'
                    if subb9!=0:
                        playerbn=playerbin9    
                if playerb==10:
                    playerbn='Messi'
                    if subb10!=0:
                        playerbn=playerbin10    
                if playerb==11:
                    playerbn='Dembele'
                    if subb11!=0:
                        playerbn=playerbin11    
                if playerp==1:
                    playerpn='Buffon'
                    if subp1!=0:
                        playerpn=playerpin1
                if playerp==2:
                    playerpn='Thiago Silva'
                    if subp2!=0:
                        playerpn=playerpin2    
                if playerp==3:
                    playerpn='Kimbempe'
                    if subp3!=0:
                        playerpn=playerpin3     
                if playerp==4:
                    playerpn='Meunier'
                    if subp4!=0:
                        playerpn=playerpin4    
                if playerp==5:
                    playerpn='Marquinhos'
                    if subp5!=0:
                        playerpn=playerpin5    
                if playerp==6:
                    playerpn='Verrati'
                    if subp6!=0:
                        playerpn=playerpin6    
                if playerp==7:
                    playerpn='Dani Alves'
                    if subp7!=0:
                        playerpn=playerpin7    
                if playerp==8:
                    playerpn='Rabiot'
                    if subp8!=0:
                        playerpn=playerpin8    
                if playerp==9:
                    playerpn='Cavani'
                    if subp9!=0:
                        playerpn=playerpin9    
                if playerp==10:
                    playerpn='Neymar JR'
                    if subp10!=0:
                        playerpn=playerpin10    
                if playerp==11:
                    playerpn='Mbappe'
                    if subp11!=0:
                        playerpn=playerpin11
                print('Commentatory: Ball intercepted by player',playerbn,'of Barcelona')

                time=time+1
                print()
                
                print('           [ Time :',time,'min || PSG:',psggoal,'| BAR:',bargoal,']')    
            
                h=2
                ppx1=h*5
                ppx2=random.randint(h*10,h*30)
                ppx3=random.randint(h*10,h*30)
                ppx4=random.randint(h*10,h*30)
                ppx5=random.randint(h*10,h*30)
                ppx6=random.randint(h*35,h*55)
                ppx7=random.randint(h*35,h*55)
                ppx8=random.randint(h*35,h*55)
                ppx9=random.randint(h*60,h*85)
                ppx10=random.randint(h*65,h*90)
                ppx11=random.randint(h*60,h*85)
                
                ppy1=random.randint(h*40,h*60)
                ppy2=random.randint(h*0,h*15)
                ppy3=random.randint(h*30,h*45)
                ppy4=random.randint(h*55,h*70)
                ppy5=random.randint(h*85,h*100)
                ppy6=random.randint(h*0,h*20)
                ppy7=random.randint(h*40,h*60)
                ppy8=random.randint(h*80,h*100)
                ppy9=random.randint(h*15,h*30)
                ppy10=random.randint(h*45,h*55)
                ppy11=random.randint(h*70,h*85)
                
                pbx1=h*95
                pbx2=random.randint(h*70,h*90)
                pbx3=random.randint(h*70,h*90)
                pbx4=random.randint(h*70,h*90)
                pbx5=random.randint(h*70,h*90)
                pbx6=random.randint(h*45,h*65)
                pbx7=random.randint(h*45,h*65)
                pbx8=random.randint(h*45,h*65)
                pbx9=random.randint(h*15,h*40)
                pbx10=random.randint(h*10,h*35)
                pbx11=random.randint(h*15,h*40)
                
                pby1=random.randint(h*40,h*60)
                pby2=random.randint(h*0,h*15)
                pby3=random.randint(h*30,h*45)
                pby4=random.randint(h*55,h*70)
                pby5=random.randint(h*85,h*100)
                pby6=random.randint(h*0,h*20)
                pby7=random.randint(h*40,h*60)
                pby8=random.randint(h*80,h*100)
                pby9=random.randint(h*15,h*30)
                pby10=random.randint(h*45,h*55)
                pby11=random.randint(h*70,h*85)
                
                print('          ',end='')
                lines = [[(h*0, h*35), (h*0, h*65)], [(h*100, h*35), (h*100, h*65)], [(h*50, h*105), (h*50, h*-5)], [(h*-10, h*105), (h*110, h*105)], [(h*-10, h*-5), (h*110, h*-5)], [(h*-10, h*105), (h*-10, h*-5)], [(h*110, h*105), (h*110, h*-5)], [(h*0, h*35), (h*-10, h*35)], [(h*0, h*65), (h*-10, h*65)], [(h*100, h*35), (h*110, h*35)], [(h*100, h*65), (h*110, h*65)]]
                c = np.array([(1, 0, 0, 1), (1, 0, 0, 1), (1, 0, 0, 1)])
                
                lc = mc.LineCollection(lines, colors=c, linewidths=1)
                fig, ax = pl.subplots()
                ax.set_facecolor('xkcd:sky blue')
                ax.set_facecolor((0.8, 1, 0.5))
                ax.add_collection(lc)
                ax.autoscale()
                ax.margins(0.1)
            
                psgx = [ppx2,ppx3,ppx4,ppx5,ppx6,ppx7,ppx8,ppx9,ppx10,ppx11] 
                psgy = [ppy2,ppy3,ppy4,ppy5,ppy6,ppy7,ppy8,ppy9,ppy10,ppy11] 
            
                plt.scatter(ppx1,ppy1,color= "purple",marker= "*", s=100)      # GK edit colour
                plt.scatter(psgx, psgy,color= "blue",marker= "*", s=80)  
             
                barx = [pbx2,pbx3,pbx4,pbx5,pbx6,pbx7,pbx8,pbx9,pbx10,pbx11] 
                bary = [pby2,pby3,pby4,pby5,pby6,pby7,pby8,pby9,pby10,pby11]
            
                plt.scatter(pbx1,pby1,color= "violet",marker= "o", s=100)      # GK edit colour
                plt.scatter(barx, bary, color= "red",marker= "o", s=80)       
                
                if playerb==1:
                    hb1-=1
                    plt.scatter(pbx1,pby1, label= "Ter Stegnen", color= "black",marker= "o", s=110)
                if playerb==2:
                    hb2-=1
                    plt.scatter(pbx2,pby2, label= "Umtiti", color= "black",marker= "o", s=110)
                if playerb==3:
                    hb3-=1
                    plt.scatter(pbx3,pby3, label= "Pique", color= "black",marker= "o", s=110)
                if playerb==4:
                    hb4-=1
                    plt.scatter(pbx4,pby4, label= "Rakitic", color= "black",marker= "o", s=110)
                if playerb==5:
                    hb5-=1
                    plt.scatter(pbx5,pby5, label= "Sergio Busquets", color= "black",marker= "o", s=110)
                if playerb==6:
                    hb6-=1
                    plt.scatter(pbx6,pby6, label= "Denis Suarez", color= "black",marker= "o", s=110)
                if playerb==7:
                    hb7-=1
                    plt.scatter(pbx7,pby7, label= "Coutinho", color= "black",marker= "o", s=110)
                if playerb==8:
                    hb8-=1
                    plt.scatter(pbx8,pby8, label= "Arthur", color= "black",marker= "o", s=110)
                if playerb==9:
                    hb9-=1
                    plt.scatter(pbx9,pby9, label= "Suarez", color= "black",marker= "o", s=110)
                if playerb==10:
                    hb10-=1
                    plt.scatter(pbx10,pby10, label= "Messi", color= "black",marker= "o", s=110)
                if playerb==11:
                    hb11-=1
                    plt.scatter(pbx11,pby11, label= "Dembele", color= "black",marker= "o", s=110)
                    
                plt.xlabel('Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! ') 
            
                plt.ylabel('Messi! Messi! Messi! Messi! Messi! Messi!') 
             
                plt.title('FIFA PYTHON 18\nPSG(BLUE) VS BARCELONA(RED)')  
            
                plt.show()     
                
                print()   

                continue              
        
                    
        if m!='s' and m!='c' and m!='tb' and m!='p' and m!='sub' and m!='skill' and m!='skills' and m!='0' and m!='2' and m!='4' and m!='6' and m!='7' and m!='8' and m!='9':
            bar=1
            psg=0
            playerb=10
            time=time+1
            print()
            
            print('           [ Time :',time,'min || PSG:',psggoal,'| BAR:',bargoal,']')    
        
            h=2
            ppx1=h*5
            ppx2=random.randint(h*40,h*50)
            ppx3=random.randint(h*40,h*50)
            ppx4=random.randint(h*40,h*50)
            ppx5=random.randint(h*40,h*50)
            ppx6=random.randint(h*40,h*50)
            ppx7=random.randint(h*40,h*50)
            ppx8=random.randint(h*40,h*50)
            ppx9=random.randint(h*40,h*50)
            ppx10=random.randint(h*40,h*50)
            ppx11=random.randint(h*40,h*50)
            
            ppy1=random.randint(h*40,h*60)
            ppy2=random.randint(h*0,h*15)
            ppy3=random.randint(h*30,h*45)
            ppy4=random.randint(h*55,h*70)
            ppy5=random.randint(h*85,h*100)
            ppy6=random.randint(h*0,h*20)
            ppy7=random.randint(h*40,h*60)
            ppy8=random.randint(h*80,h*100)
            ppy9=random.randint(h*15,h*30)
            ppy10=random.randint(h*45,h*55)
            ppy11=random.randint(h*70,h*85)
            
            pbx1=h*95
            pbx2=random.randint(h*40,h*50)
            pbx3=random.randint(h*40,h*50)
            pbx4=random.randint(h*40,h*50)
            pbx5=random.randint(h*40,h*50)
            pbx6=random.randint(h*40,h*50)
            pbx7=random.randint(h*40,h*50)
            pbx8=random.randint(h*40,h*50)
            pbx9=random.randint(h*40,h*50)
            pbx10=h*20
            pbx11=random.randint(h*40,h*50)
            
            pby1=random.randint(h*40,h*60)
            pby2=random.randint(h*0,h*15)
            pby3=random.randint(h*30,h*45)
            pby4=random.randint(h*55,h*70)
            pby5=random.randint(h*85,h*100)
            pby6=random.randint(h*0,h*20)
            pby7=random.randint(h*40,h*60)
            pby8=random.randint(h*80,h*100)
            pby9=random.randint(h*15,h*30)
            pby10=h*50
            pby11=random.randint(h*70,h*85)
            
            print('          ',end='')
            lines = [[(h*0, h*35), (h*0, h*65)], [(h*100, h*35), (h*100, h*65)], [(h*50, h*105), (h*50, h*-5)], [(h*-10, h*105), (h*110, h*105)], [(h*-10, h*-5), (h*110, h*-5)], [(h*-10, h*105), (h*-10, h*-5)], [(h*110, h*105), (h*110, h*-5)], [(h*0, h*35), (h*-10, h*35)], [(h*0, h*65), (h*-10, h*65)], [(h*100, h*35), (h*110, h*35)], [(h*100, h*65), (h*110, h*65)]]
            c = np.array([(1, 0, 0, 1), (1, 0, 0, 1), (1, 0, 0, 1)])
            
            lc = mc.LineCollection(lines, colors=c, linewidths=1)
            fig, ax = pl.subplots()
            ax.set_facecolor('xkcd:sky blue')
            ax.set_facecolor((0.8, 1, 0.5))
            ax.add_collection(lc)
            ax.autoscale()
            ax.margins(0.1)
        
            psgx = [ppx2,ppx3,ppx4,ppx5,ppx6,ppx7,ppx8,ppx9,ppx10,ppx11] 
            psgy = [ppy2,ppy3,ppy4,ppy5,ppy6,ppy7,ppy8,ppy9,ppy10,ppy11] 
        
            plt.scatter(ppx1,ppy1,color= "purple",marker= "*", s=100)      # GK edit colour
            plt.scatter(psgx, psgy,color= "blue",marker= "*", s=80)  
         
            barx = [pbx2,pbx3,pbx4,pbx5,pbx6,pbx7,pbx8,pbx9,pbx10,pbx11] 
            bary = [pby2,pby3,pby4,pby5,pby6,pby7,pby8,pby9,pby10,pby11]
        
            plt.scatter(pbx1,pby1,color= "violet",marker= "o", s=100)      # GK edit colour
            plt.scatter(barx, bary, color= "red",marker= "o", s=80)      
                    
            if playerp==1:
                plt.scatter(ppx1,ppy1, label= "Buffon", color= "black",marker= "*", s=110)
            if playerp==2:
                plt.scatter(ppx2,ppy2, label= "Thiago Silva", color= "black",marker= "*", s=110)
            if playerp==3:
                plt.scatter(ppx3,ppy3, label= "Kimbempe", color= "black",marker= "*", s=110)
            if playerp==4:
                plt.scatter(ppx4,ppy4, label= "Meunier", color= "black",marker= "*", s=110)
            if playerp==5:
                plt.scatter(ppx5,ppy5, label= "Marquinhos", color= "black",marker= "*", s=110)
            if playerp==6:
                plt.scatter(ppx6,ppy6, label= "Verrati", color= "black",marker= "*", s=110)
            if playerp==7:
                plt.scatter(ppx7,ppy7, label= "Dani Alves", color= "black",marker= "*", s=110)
            if playerp==8:
                plt.scatter(ppx8,ppy8, label= "Rabiot", color= "black",marker= "*", s=110)
            if playerp==9:
                plt.scatter(ppx9,ppy9, label= "Cavani", color= "black",marker= "*", s=110)
            if playerp==10:
                plt.scatter(ppx10,ppy10, label= "Neymar JR", color= "black",marker= "*", s=110)
            if playerp==11:
                plt.scatter(ppx11,ppy11, label= "Mbappe", color= "black",marker= "*", s=110)
                
            plt.xlabel('Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! ') 
        
            plt.ylabel('Messi! Messi! Messi! Messi! Messi! Messi!') 
         
            plt.title('FIFA PYTHON 18\nPSG(BLUE) VS BARCELONA(RED)')  
        
            plt.show()     
            
            print()
            
            print('Foul!! Penalty awarded to Barcelona !')
            print('Messi is thinking of direction shot > (l or r)')
            freekick=input('>>>')
            g=random.randint(0,1)
            if freekick=='l' and g==0:
                bargoal=bargoal+1
                bar=0
                psg=1
                playerp=10
                if playerp==10:
                    playerpn='Neymar'
                    if subp10!=0:
                        playerpn=playerpin10
                print('Commentatory: Messi scores!!! Goooooal!! Awesome!!! BARCELONA',bargoal,'and PSG',psggoal)
                print('Commentatory: Now',playerpn,'starts...')
                print()
                time=time+1
                print()
                
                print('           [ Time :',time,'min || PSG:',psggoal,'| BAR:',bargoal,']')    
            
                h=2
                ppx1=h*5
                ppx2=random.randint(h*10,h*30)
                ppx3=random.randint(h*10,h*30)
                ppx4=random.randint(h*10,h*30)
                ppx5=random.randint(h*10,h*30)
                ppx6=random.randint(h*35,h*55)
                ppx7=random.randint(h*35,h*55)
                ppx8=random.randint(h*35,h*55)
                ppx9=random.randint(h*60,h*85)
                ppx10=random.randint(h*65,h*90)
                ppx11=random.randint(h*60,h*85)
                
                ppy1=random.randint(h*40,h*60)
                ppy2=random.randint(h*0,h*15)
                ppy3=random.randint(h*30,h*45)
                ppy4=random.randint(h*55,h*70)
                ppy5=random.randint(h*85,h*100)
                ppy6=random.randint(h*0,h*20)
                ppy7=random.randint(h*40,h*60)
                ppy8=random.randint(h*80,h*100)
                ppy9=random.randint(h*15,h*30)
                ppy10=random.randint(h*45,h*55)
                ppy11=random.randint(h*70,h*85)
                
                pbx1=h*95
                pbx2=random.randint(h*70,h*90)
                pbx3=random.randint(h*70,h*90)
                pbx4=random.randint(h*70,h*90)
                pbx5=random.randint(h*70,h*90)
                pbx6=random.randint(h*45,h*65)
                pbx7=random.randint(h*45,h*65)
                pbx8=random.randint(h*45,h*65)
                pbx9=random.randint(h*15,h*40)
                pbx10=random.randint(h*10,h*35)
                pbx11=random.randint(h*15,h*40)
                
                pby1=random.randint(h*40,h*60)
                pby2=random.randint(h*0,h*15)
                pby3=random.randint(h*30,h*45)
                pby4=random.randint(h*55,h*70)
                pby5=random.randint(h*85,h*100)
                pby6=random.randint(h*0,h*20)
                pby7=random.randint(h*40,h*60)
                pby8=random.randint(h*80,h*100)
                pby9=random.randint(h*15,h*30)
                pby10=random.randint(h*45,h*55)
                pby11=random.randint(h*70,h*85)
                
                print('          ',end='')
                lines = [[(h*0, h*35), (h*0, h*65)], [(h*100, h*35), (h*100, h*65)], [(h*50, h*105), (h*50, h*-5)], [(h*-10, h*105), (h*110, h*105)], [(h*-10, h*-5), (h*110, h*-5)], [(h*-10, h*105), (h*-10, h*-5)], [(h*110, h*105), (h*110, h*-5)], [(h*0, h*35), (h*-10, h*35)], [(h*0, h*65), (h*-10, h*65)], [(h*100, h*35), (h*110, h*35)], [(h*100, h*65), (h*110, h*65)]]
                c = np.array([(1, 0, 0, 1), (1, 0, 0, 1), (1, 0, 0, 1)])
                
                lc = mc.LineCollection(lines, colors=c, linewidths=1)
                fig, ax = pl.subplots()
                ax.set_facecolor('xkcd:sky blue')
                ax.set_facecolor((0.8, 1, 0.5))
                ax.add_collection(lc)
                ax.autoscale()
                ax.margins(0.1)
            
                psgx = [ppx2,ppx3,ppx4,ppx5,ppx6,ppx7,ppx8,ppx9,ppx10,ppx11] 
                psgy = [ppy2,ppy3,ppy4,ppy5,ppy6,ppy7,ppy8,ppy9,ppy10,ppy11] 
            
                plt.scatter(ppx1,ppy1,color= "purple",marker= "*", s=100)      # GK edit colour
                plt.scatter(psgx, psgy,color= "blue",marker= "*", s=80)  
            
                barx = [pbx2,pbx3,pbx4,pbx5,pbx6,pbx7,pbx8,pbx9,pbx10,pbx11] 
                bary = [pby2,pby3,pby4,pby5,pby6,pby7,pby8,pby9,pby10,pby11]
            
                plt.scatter(pbx1,pby1,color= "violet",marker= "o", s=100)      # GK edit colour
                plt.scatter(barx, bary, color= "red",marker= "o", s=80)      
                        
                if playerp==1:
                    hp1=-1
                    plt.scatter(ppx1,ppy1, label= "Buffon", color= "black",marker= "*", s=110)
                if playerp==2:
                    hp2=-1
                    plt.scatter(ppx2,ppy2, label= "Thiago Silva", color= "black",marker= "*", s=110)
                if playerp==3:
                    hp3=-1
                    plt.scatter(ppx3,ppy3, label= "Kimbempe", color= "black",marker= "*", s=110)
                if playerp==4:
                    hp4=-1
                    plt.scatter(ppx4,ppy4, label= "Meunier", color= "black",marker= "*", s=110)
                if playerp==5:
                    hp5=-1
                    plt.scatter(ppx5,ppy5, label= "Marquinhos", color= "black",marker= "*", s=110)
                if playerp==6:
                    hp6=-1
                    plt.scatter(ppx6,ppy6, label= "Verrati", color= "black",marker= "*", s=110)
                if playerp==7:
                    hp7=-1
                    plt.scatter(ppx7,ppy7, label= "Dani Alves", color= "black",marker= "*", s=110)
                if playerp==8:
                    hp8=-1
                    plt.scatter(ppx8,ppy8, label= "Rabiot", color= "black",marker= "*", s=110)
                if playerp==9:
                    hp9=-1
                    plt.scatter(ppx9,ppy9, label= "Cavani", color= "black",marker= "*", s=110)
                if playerp==10:
                    hp10=-1
                    plt.scatter(ppx10,ppy10, label= "Neymar", color= "black",marker= "*", s=110)
                if playerp==11:
                    hp11=-1
                    plt.scatter(ppx11,ppy11, label= "Mbappe", color= "black",marker= "*", s=110)
                    
                plt.xlabel('Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! ') 
            
                plt.ylabel('Messi! Messi! Messi! Messi! Messi! Messi!') 
            
                plt.title('FIFA PYTHON 18\nPSG(BLUE) VS BARCELONA(RED)')  
            
                plt.show()     
                
                print()

            if freekick=='r' and g==1:
                bargoal=bargoal+1
                bar=0
                psg=1
                playerp=10
                if playerp==10:
                    playerpn='Neymar'
                    if subp10!=0:
                        playerpn=playerpin10 
                print('Commentatory: Messi scores!!! Goooooal!! Awesome!!! BARCELONA',bargoal,'and PSG',psggoal)
                print('Commentatory: Now',playerpn,'starts...')
                print()
                time=time+1
                print()
                
                print('           [ Time :',time,'min || PSG:',psggoal,'| BAR:',bargoal,']')    
            
                h=2
                ppx1=h*5
                ppx2=random.randint(h*10,h*30)
                ppx3=random.randint(h*10,h*30)
                ppx4=random.randint(h*10,h*30)
                ppx5=random.randint(h*10,h*30)
                ppx6=random.randint(h*35,h*55)
                ppx7=random.randint(h*35,h*55)
                ppx8=random.randint(h*35,h*55)
                ppx9=random.randint(h*60,h*85)
                ppx10=random.randint(h*65,h*90)
                ppx11=random.randint(h*60,h*85)
                
                ppy1=random.randint(h*40,h*60)
                ppy2=random.randint(h*0,h*15)
                ppy3=random.randint(h*30,h*45)
                ppy4=random.randint(h*55,h*70)
                ppy5=random.randint(h*85,h*100)
                ppy6=random.randint(h*0,h*20)
                ppy7=random.randint(h*40,h*60)
                ppy8=random.randint(h*80,h*100)
                ppy9=random.randint(h*15,h*30)
                ppy10=random.randint(h*45,h*55)
                ppy11=random.randint(h*70,h*85)
                
                pbx1=h*95
                pbx2=random.randint(h*70,h*90)
                pbx3=random.randint(h*70,h*90)
                pbx4=random.randint(h*70,h*90)
                pbx5=random.randint(h*70,h*90)
                pbx6=random.randint(h*45,h*65)
                pbx7=random.randint(h*45,h*65)
                pbx8=random.randint(h*45,h*65)
                pbx9=random.randint(h*15,h*40)
                pbx10=random.randint(h*10,h*35)
                pbx11=random.randint(h*15,h*40)
                
                pby1=random.randint(h*40,h*60)
                pby2=random.randint(h*0,h*15)
                pby3=random.randint(h*30,h*45)
                pby4=random.randint(h*55,h*70)
                pby5=random.randint(h*85,h*100)
                pby6=random.randint(h*0,h*20)
                pby7=random.randint(h*40,h*60)
                pby8=random.randint(h*80,h*100)
                pby9=random.randint(h*15,h*30)
                pby10=random.randint(h*45,h*55)
                pby11=random.randint(h*70,h*85)
                
                print('          ',end='')
                lines = [[(h*0, h*35), (h*0, h*65)], [(h*100, h*35), (h*100, h*65)], [(h*50, h*105), (h*50, h*-5)], [(h*-10, h*105), (h*110, h*105)], [(h*-10, h*-5), (h*110, h*-5)], [(h*-10, h*105), (h*-10, h*-5)], [(h*110, h*105), (h*110, h*-5)], [(h*0, h*35), (h*-10, h*35)], [(h*0, h*65), (h*-10, h*65)], [(h*100, h*35), (h*110, h*35)], [(h*100, h*65), (h*110, h*65)]]
                c = np.array([(1, 0, 0, 1), (1, 0, 0, 1), (1, 0, 0, 1)])
                
                lc = mc.LineCollection(lines, colors=c, linewidths=1)
                fig, ax = pl.subplots()
                ax.set_facecolor('xkcd:sky blue')
                ax.set_facecolor((0.8, 1, 0.5))
                ax.add_collection(lc)
                ax.autoscale()
                ax.margins(0.1)
            
                psgx = [ppx2,ppx3,ppx4,ppx5,ppx6,ppx7,ppx8,ppx9,ppx10,ppx11] 
                psgy = [ppy2,ppy3,ppy4,ppy5,ppy6,ppy7,ppy8,ppy9,ppy10,ppy11] 
            
                plt.scatter(ppx1,ppy1,color= "purple",marker= "*", s=100)      # GK edit colour
                plt.scatter(psgx, psgy,color= "blue",marker= "*", s=80)  
             
                barx = [pbx2,pbx3,pbx4,pbx5,pbx6,pbx7,pbx8,pbx9,pbx10,pbx11] 
                bary = [pby2,pby3,pby4,pby5,pby6,pby7,pby8,pby9,pby10,pby11]
            
                plt.scatter(pbx1,pby1,color= "violet",marker= "o", s=100)      # GK edit colour
                plt.scatter(barx, bary, color= "red",marker= "o", s=80)       
                
                if playerb==1:
                    hb1-=1
                    plt.scatter(pbx1,pby1, label= "Ter Stegnen", color= "black",marker= "o", s=110)
                if playerb==2:
                    hb2-=1
                    plt.scatter(pbx2,pby2, label= "Umtiti", color= "black",marker= "o", s=110)
                if playerb==3:
                    hb3-=1
                    plt.scatter(pbx3,pby3, label= "Pique", color= "black",marker= "o", s=110)
                if playerb==4:
                    hb4-=1
                    plt.scatter(pbx4,pby4, label= "Rakitic", color= "black",marker= "o", s=110)
                if playerb==5:
                    hb5-=1
                    plt.scatter(pbx5,pby5, label= "Sergio Busquets", color= "black",marker= "o", s=110)
                if playerb==6:
                    hb6-=1
                    plt.scatter(pbx6,pby6, label= "Denis Suarez", color= "black",marker= "o", s=110)
                if playerb==7:
                    hb7-=1
                    plt.scatter(pbx7,pby7, label= "Coutinho", color= "black",marker= "o", s=110)
                if playerb==8:
                    hb8-=1
                    plt.scatter(pbx8,pby8, label= "Arthur", color= "black",marker= "o", s=110)
                if playerb==9:
                    hb9-=1
                    plt.scatter(pbx9,pby9, label= "Suarez", color= "black",marker= "o", s=110)
                if playerp==10:
                    hp10-=1
                    plt.scatter(ppx10,ppy10, label= "Neymar", color= "black",marker= "*", s=110)
                if playerb==11:
                    hb11-=1
                    plt.scatter(pbx11,pby11, label= "Dembele", color= "black",marker= "o", s=110)
                    
                plt.xlabel('Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! ') 
            
                plt.ylabel('Messi! Messi! Messi! Messi! Messi! Messi!') 
             
                plt.title('FIFA PYTHON 18\nPSG(BLUE) VS BARCELONA(RED)')  
            
                plt.show()     
                
                print()

            if freekick=='l' and g==1:
                bar=0
                psg=1
                playerp=1
                if playerp==1:
                    playerpn='Buffon'
                    if subp1!=0:
                        playerpn=playerpin1 
                print('Commentatory:',playerpin1,'saves it')
                time=time+1
                print()
                
                print('           [ Time :',time,'min || PSG:',psggoal,'| BAR:',bargoal,']')    
            
                h=2
                ppx1=h*5
                ppx2=random.randint(h*10,h*30)
                ppx3=random.randint(h*10,h*30)
                ppx4=random.randint(h*10,h*30)
                ppx5=random.randint(h*10,h*30)
                ppx6=random.randint(h*35,h*55)
                ppx7=random.randint(h*35,h*55)
                ppx8=random.randint(h*35,h*55)
                ppx9=random.randint(h*60,h*85)
                ppx10=random.randint(h*65,h*90)
                ppx11=random.randint(h*60,h*85)
                
                ppy1=random.randint(h*40,h*60)
                ppy2=random.randint(h*0,h*15)
                ppy3=random.randint(h*30,h*45)
                ppy4=random.randint(h*55,h*70)
                ppy5=random.randint(h*85,h*100)
                ppy6=random.randint(h*0,h*20)
                ppy7=random.randint(h*40,h*60)
                ppy8=random.randint(h*80,h*100)
                ppy9=random.randint(h*15,h*30)
                ppy10=random.randint(h*45,h*55)
                ppy11=random.randint(h*70,h*85)
                
                pbx1=h*95
                pbx2=random.randint(h*70,h*90)
                pbx3=random.randint(h*70,h*90)
                pbx4=random.randint(h*70,h*90)
                pbx5=random.randint(h*70,h*90)
                pbx6=random.randint(h*45,h*65)
                pbx7=random.randint(h*45,h*65)
                pbx8=random.randint(h*45,h*65)
                pbx9=random.randint(h*15,h*40)
                pbx10=random.randint(h*10,h*35)
                pbx11=random.randint(h*15,h*40)
                
                pby1=random.randint(h*40,h*60)
                pby2=random.randint(h*0,h*15)
                pby3=random.randint(h*30,h*45)
                pby4=random.randint(h*55,h*70)
                pby5=random.randint(h*85,h*100)
                pby6=random.randint(h*0,h*20)
                pby7=random.randint(h*40,h*60)
                pby8=random.randint(h*80,h*100)
                pby9=random.randint(h*15,h*30)
                pby10=random.randint(h*45,h*55)
                pby11=random.randint(h*70,h*85)
                
                print('          ',end='')
                lines = [[(h*0, h*35), (h*0, h*65)], [(h*100, h*35), (h*100, h*65)], [(h*50, h*105), (h*50, h*-5)], [(h*-10, h*105), (h*110, h*105)], [(h*-10, h*-5), (h*110, h*-5)], [(h*-10, h*105), (h*-10, h*-5)], [(h*110, h*105), (h*110, h*-5)], [(h*0, h*35), (h*-10, h*35)], [(h*0, h*65), (h*-10, h*65)], [(h*100, h*35), (h*110, h*35)], [(h*100, h*65), (h*110, h*65)]]
                c = np.array([(1, 0, 0, 1), (1, 0, 0, 1), (1, 0, 0, 1)])
                
                lc = mc.LineCollection(lines, colors=c, linewidths=1)
                fig, ax = pl.subplots()
                ax.set_facecolor('xkcd:sky blue')
                ax.set_facecolor((0.8, 1, 0.5))
                ax.add_collection(lc)
                ax.autoscale()
                ax.margins(0.1)
            
                psgx = [ppx2,ppx3,ppx4,ppx5,ppx6,ppx7,ppx8,ppx9,ppx10,ppx11] 
                psgy = [ppy2,ppy3,ppy4,ppy5,ppy6,ppy7,ppy8,ppy9,ppy10,ppy11] 
            
                plt.scatter(ppx1,ppy1,color= "purple",marker= "*", s=100)      # GK edit colour
                plt.scatter(psgx, psgy,color= "blue",marker= "*", s=80)  
             
                barx = [pbx2,pbx3,pbx4,pbx5,pbx6,pbx7,pbx8,pbx9,pbx10,pbx11] 
                bary = [pby2,pby3,pby4,pby5,pby6,pby7,pby8,pby9,pby10,pby11]
            
                plt.scatter(pbx1,pby1,color= "violet",marker= "o", s=100)      # GK edit colour
                plt.scatter(barx, bary, color= "red",marker= "o", s=80)       
                
                if playerp==1:
                    hp1-=1
                    plt.scatter(ppx1,ppy1, label= "Buffon", color= "black",marker= "*", s=110)
                if playerb==2:
                    hb2-=1
                    plt.scatter(pbx2,pby2, label= "Umtiti", color= "black",marker= "o", s=110)
                if playerb==3:
                    hb3-=1
                    plt.scatter(pbx3,pby3, label= "Pique", color= "black",marker= "o", s=110)
                if playerb==4:
                    hb4-=1
                    plt.scatter(pbx4,pby4, label= "Rakitic", color= "black",marker= "o", s=110)
                if playerb==5:
                    hb5-=1
                    plt.scatter(pbx5,pby5, label= "Sergio Busquets", color= "black",marker= "o", s=110)
                if playerb==6:
                    hb6-=1
                    plt.scatter(pbx6,pby6, label= "Denis Suarez", color= "black",marker= "o", s=110)
                if playerb==7:
                    hb7-=1
                    plt.scatter(pbx7,pby7, label= "Coutinho", color= "black",marker= "o", s=110)
                if playerb==8:
                    hb8-=1
                    plt.scatter(pbx8,pby8, label= "Arthur", color= "black",marker= "o", s=110)
                if playerb==9:
                    hb9-=1
                    plt.scatter(pbx9,pby9, label= "Suarez", color= "black",marker= "o", s=110)
                if playerb==10:
                    hb10-=1
                    plt.scatter(pbx10,pby10, label= "Messi", color= "black",marker= "o", s=110)
                if playerb==11:
                    hb11-=1
                    plt.scatter(pbx11,pby11, label= "Dembele", color= "black",marker= "o", s=110)
                    
                plt.xlabel('Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! ') 
            
                plt.ylabel('Messi! Messi! Messi! Messi! Messi! Messi!') 
             
                plt.title('FIFA PYTHON 18\nPSG(BLUE) VS BARCELONA(RED)')  
            
                plt.show()     
                
                print()

            if freekick=='r' and g==0:
                bar=0
                psg=1
                playerp=1
                if playerp==1:
                    playerpn='Buffon'
                    if subp1!=0:
                        playerpn=playerpin1 
                print('Commentatory:',playerpin1,'saves it')
                time=time+1
                print()
                
                print('           [ Time :',time,'min || PSG:',psggoal,'| BAR:',bargoal,']')    
            
                h=2
                ppx1=h*5
                ppx2=random.randint(h*10,h*30)
                ppx3=random.randint(h*10,h*30)
                ppx4=random.randint(h*10,h*30)
                ppx5=random.randint(h*10,h*30)
                ppx6=random.randint(h*35,h*55)
                ppx7=random.randint(h*35,h*55)
                ppx8=random.randint(h*35,h*55)
                ppx9=random.randint(h*60,h*85)
                ppx10=random.randint(h*65,h*90)
                ppx11=random.randint(h*60,h*85)
                
                ppy1=random.randint(h*40,h*60)
                ppy2=random.randint(h*0,h*15)
                ppy3=random.randint(h*30,h*45)
                ppy4=random.randint(h*55,h*70)
                ppy5=random.randint(h*85,h*100)
                ppy6=random.randint(h*0,h*20)
                ppy7=random.randint(h*40,h*60)
                ppy8=random.randint(h*80,h*100)
                ppy9=random.randint(h*15,h*30)
                ppy10=random.randint(h*45,h*55)
                ppy11=random.randint(h*70,h*85)
                
                pbx1=h*95
                pbx2=random.randint(h*70,h*90)
                pbx3=random.randint(h*70,h*90)
                pbx4=random.randint(h*70,h*90)
                pbx5=random.randint(h*70,h*90)
                pbx6=random.randint(h*45,h*65)
                pbx7=random.randint(h*45,h*65)
                pbx8=random.randint(h*45,h*65)
                pbx9=random.randint(h*15,h*40)
                pbx10=random.randint(h*10,h*35)
                pbx11=random.randint(h*15,h*40)
                
                pby1=random.randint(h*40,h*60)
                pby2=random.randint(h*0,h*15)
                pby3=random.randint(h*30,h*45)
                pby4=random.randint(h*55,h*70)
                pby5=random.randint(h*85,h*100)
                pby6=random.randint(h*0,h*20)
                pby7=random.randint(h*40,h*60)
                pby8=random.randint(h*80,h*100)
                pby9=random.randint(h*15,h*30)
                pby10=random.randint(h*45,h*55)
                pby11=random.randint(h*70,h*85)
                
                print('          ',end='')
                lines = [[(h*0, h*35), (h*0, h*65)], [(h*100, h*35), (h*100, h*65)], [(h*50, h*105), (h*50, h*-5)], [(h*-10, h*105), (h*110, h*105)], [(h*-10, h*-5), (h*110, h*-5)], [(h*-10, h*105), (h*-10, h*-5)], [(h*110, h*105), (h*110, h*-5)], [(h*0, h*35), (h*-10, h*35)], [(h*0, h*65), (h*-10, h*65)], [(h*100, h*35), (h*110, h*35)], [(h*100, h*65), (h*110, h*65)]]
                c = np.array([(1, 0, 0, 1), (1, 0, 0, 1), (1, 0, 0, 1)])
                
                lc = mc.LineCollection(lines, colors=c, linewidths=1)
                fig, ax = pl.subplots()
                ax.set_facecolor('xkcd:sky blue')
                ax.set_facecolor((0.8, 1, 0.5))
                ax.add_collection(lc)
                ax.autoscale()
                ax.margins(0.1)
            
                psgx = [ppx2,ppx3,ppx4,ppx5,ppx6,ppx7,ppx8,ppx9,ppx10,ppx11] 
                psgy = [ppy2,ppy3,ppy4,ppy5,ppy6,ppy7,ppy8,ppy9,ppy10,ppy11] 
            
                plt.scatter(ppx1,ppy1,color= "purple",marker= "*", s=100)      # GK edit colour
                plt.scatter(psgx, psgy,color= "blue",marker= "*", s=80)  
             
                barx = [pbx2,pbx3,pbx4,pbx5,pbx6,pbx7,pbx8,pbx9,pbx10,pbx11] 
                bary = [pby2,pby3,pby4,pby5,pby6,pby7,pby8,pby9,pby10,pby11]
            
                plt.scatter(pbx1,pby1,color= "violet",marker= "o", s=100)      # GK edit colour
                plt.scatter(barx, bary, color= "red",marker= "o", s=80)       
                
                if playerp==1:
                    hp1-=1
                    plt.scatter(ppx1,ppy1, label= "Buffon", color= "black",marker= "*", s=110)
                if playerb==2:
                    hb2-=1
                    plt.scatter(pbx2,pby2, label= "Umtiti", color= "black",marker= "o", s=110)
                if playerb==3:
                    hb3-=1
                    plt.scatter(pbx3,pby3, label= "Pique", color= "black",marker= "o", s=110)
                if playerb==4:
                    hb4-=1
                    plt.scatter(pbx4,pby4, label= "Rakitic", color= "black",marker= "o", s=110)
                if playerb==5:
                    hb5-=1
                    plt.scatter(pbx5,pby5, label= "Sergio Busquets", color= "black",marker= "o", s=110)
                if playerb==6:
                    hb6-=1
                    plt.scatter(pbx6,pby6, label= "Denis Suarez", color= "black",marker= "o", s=110)
                if playerb==7:
                    hb7-=1
                    plt.scatter(pbx7,pby7, label= "Coutinho", color= "black",marker= "o", s=110)
                if playerb==8:
                    hb8-=1
                    plt.scatter(pbx8,pby8, label= "Arthur", color= "black",marker= "o", s=110)
                if playerb==9:
                    hb9-=1
                    plt.scatter(pbx9,pby9, label= "Suarez", color= "black",marker= "o", s=110)
                if playerb==10:
                    hb10-=1
                    plt.scatter(pbx10,pby10, label= "Messi", color= "black",marker= "o", s=110)
                if playerb==11:
                    hb11-=1
                    plt.scatter(pbx11,pby11, label= "Dembele", color= "black",marker= "o", s=110)
                    
                plt.xlabel('Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! ') 
            
                plt.ylabel('Messi! Messi! Messi! Messi! Messi! Messi!') 
             
                plt.title('FIFA PYTHON 18\nPSG(BLUE) VS BARCELONA(RED)')  
            
                plt.show() 

                print()

                
else:
    if bargoal>psggoal:
        print('Commentatory: FULL TIME !! Barcelona wins',bargoal,'to PSG',psggoal)
    if psggoal>bargoal:
        print('Commentatory: FULL TIME !! PSG wins',psggoal,'to Barcelona',bargoal)
    

print()
print('Hope you enjoyed the game')
print('Thank you')
rating=input('Pls give feedback for this game >')
print()
for i in range(20):
    n=1
    for i in range(1,25000):
        n=n*i
    n=1
print('Thank you for your feedback !!!!')
print('          - Hanan Basheer')
print('            CEO , Hanu Corporations 2019')
print()
for i in range(20):
    n=1
    for i in range(1,25000):
        n=n*i
    n=1
print(' News: FIFA Python 2020 coming soon in your nearby stores.....')
stop=input('Prebook NOW...')
