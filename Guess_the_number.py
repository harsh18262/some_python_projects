#game of guessing the number
import random

num=random.randint(0,20)
chance=0

name=input("enter your name")

while chance!=5:
    num1=int(input("Enter a number"))
    if(num==num1):
        print("you guessed it right")
        break;
    elif(num>num1):
        print("you number is too low")
    elif(num<num1):
        print("your number is too high")
    chance +=1
    if(chance==5):
        print("number was",num)
