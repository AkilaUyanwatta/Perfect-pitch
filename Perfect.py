from playsound import playsound
from random import random 
#

sounds=["C3","D3","E3","F3","G3","A3","B3","C4"]
while 1 : 
    a=int(random()*8)
    while 1: 
        playsound(sounds[a]+'.mp3')
        x=str(raw_input('Guess : '))
        if x== sounds[a]:
            print("Correct")
            break
        elif sounds.index(x)<a:
            print("Try higher")            
        elif sounds.index(x)>a:
            print("Try lower")
    print(sounds[a])
