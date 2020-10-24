'''THIS IS SNAKE_WATER_GUN GAME'''
import random
print("\n\t\t\t\t\t\t\t************* WELCOME TO SNAKE WATER GUN GAME *******************\n")
'''please enter
s for snake
w for water
g for gun'''

count1=0 #user
count2=0 #computer
comp = ['s', 'w', 'g']
i=10
ch='y'
while(ch=='y' or ch=='Y'):
    count1=0
    count2=0
    i=10
    while(i!=0):

        i = i - 1
        rnd = random.choice(comp)
        print("enter your choice: ")
        user = input()
        if((user=='s' and  rnd=='w') or (user=='w'and rnd=='g') or (user=='g'and rnd=='s')):
            print("chances left: ",i)
            count1=count1+1
            print("your score:",count1," computer score: ",count2)
            print("\n")
        else:
            count2=count2+1
            print("chances left: ", i)
            print("your score:", count1, " computer score: ", count2)
            print("\n")

    if(count1<count2):
        print("YOUR SCORE: ",count1)
        print("COMPUTER SCORE: ",count2)
        print("\nYOU LOSE!!!")
    elif(count1>count2):
        print("YOUR SCORE: ", count1)
        print("COMPUTER SCORE: ", count2)
        print("\nYOU WIN!!!")
    else:
        print("YOUR SCORE: ", count1)
        print("COMPUTER SCORE: ", count2)
        print("\nTIE MATCH!")
    print("\nG A M E   O V E R ... ! ! !")
    print("\n  WANNA TRY AGAIN ?\n type y or n....\n")
    ch=input()
