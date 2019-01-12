from random import randint
player=input('rock(r), paper(p) or scissors(s)?')
print(player, 'vs ' ,end='')             
chosen=randint(1,3)
#chosen contains the random numbers
if chosen==1:
    computer='r'
elif chosen==2:
        computer='p'
else:
    computer='s'

print(computer)

if player==computer:
    print('Draw')
    print( 'Choose another letter')
elif player=='r' and computer=='p':
    print('Computer wins! Don\'t be sad, you\'ve still got potential')
    print('Try again')
elif player=='p' and computer=='s':
    print('Computer wins! Don\'t be sad, you\'ve still got potential')
    print('Try again')
elif player=='s' and computer=='r':
    print('Computer wins! Don\'t be sad, you\'ve still got potential')
    print('Try again')
else:
    print('Player wins! Congratulations, you\'re awesome')

