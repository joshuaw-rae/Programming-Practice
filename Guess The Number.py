from random import *

solved=0
isInt=0

randlower = randint(0,25)
randupper = randint(26,40)

randactual = randint(randlower,randupper)


print("Guess a number between" , randlower ,"and", randupper)

guess = int(input()) 

while(solved == 0):
    if(guess < randlower or guess > randupper):
          print("Please input a number within the range!")
          guess = int(input())
        
    else:
        if(guess<randactual):
            print("Higher!")
            guess = int(input())
        
        elif(guess>randactual):
            print("Lower!")
            guess = int(input())
            
        else:
            print("\n****Correct! Good Job!****")
            solved=1

            