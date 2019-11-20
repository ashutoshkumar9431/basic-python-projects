import random as r
a = ["rock","paper","scissors"]
computer = 0
player = 0
play = 'y'
while play=='y':
    print("What do you want to be the winning score ?")
    maxm = int(input())
    
    while((player != maxm) or (computer != maxm)):
        print("start")
        response=input()
        compresponse = r.choice(a)
        print(compresponse)
        if(response == compresponse):
            print("you:",player,"comp:",computer)
        elif ((response=='rock') and (compresponse=='paper')):
            computer=computer+1
            print("you:",player,"comp:",computer)
        elif ((response=='paper') and (compresponse=='rock')):
            player=player+1
            print("you:",player,"comp:",computer)
        elif ((response=='scissors') and (compresponse=='paper')):
            player=player+1
            print("you:",player,"comp:",computer)
        elif ((response=='paper') and (compresponse=='scissors')):
            computer = computer+1
            print("you:",player,"comp:",computer)
        elif ((response=='scissors') and (compresponse=='rock')):
            computer = computer + 1
            print("you:",player,"comp:",computer)
        elif ((response=='rock') and (compresponse=='scissors')):
            player=player+1
            print("you:",player,"comp:",computer)
    if player==maxm:
        print("you won")
        print("Your score is",player,"Computer Score is ",computer)
    else :
        print("computer won")
        print("Your score is",player,"Computer Score is ",computer)
    print("do you want to play again")
    play = input()

        