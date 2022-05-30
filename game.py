# this is a snake , water and gun game which we played in our childhod 
import random
from tkinter import N
randno=random.randint(1,2,3)
def game(comp,b):
    if comp==b:
        return None
    if comp=='s':
        if b=='w':
          return False
    elif b=='g':
        return True
    if comp=='w':
        if b=='g':
          return False
    elif b=='s':
        return True
    if comp=='g':
        if b=='s':
          return False
    elif b=='w':
        return True
    
    
print(" Let the computer  choose any one of from the three thing  ") 
print(randno)
if randno==1:
    comp='s'
elif randno==2:
    comp='w'
elif randno==3:
    comp='g'
b=input("choose anything thing from snake(s) , water (w) and gun(g)")
    
a=game(comp,b)

if a==None:
    print("this is a tie ")
    
elif a:
    print("you win ")
else:
    print("you loose ")