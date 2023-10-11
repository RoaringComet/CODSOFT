# to create a rock paper scissor game
import random
a = random.randint(1,3)
while True:
    print(' enter either rock, paper, scissor ')
    if(a==1):
        s='rock'
    elif(a==2):
        s='paper'
    else:
        s='scissors'

    w=input('enter your move !!! ')

    if(w==s):
        print('tie!!')
    elif((w=='rock' and s=='scissor')or(w=='paper' and s=='rock')or(w=='scissor' and s=='paper')):
        print(' congratulations! you win! ')
    else:
        print(' sorry! you lose XD ')
