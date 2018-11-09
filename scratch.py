import random
data = ["scissors","rocks","paper"]
keep_playing = True
count = 0
score = 0

while keep_playing == True:
    cmove = random.choice(data)
    pmove = str(input())

    if (cmove == pmove):
        score += 0.5
        print("Tie")
    elif(cmove == "scissors" and pmove == "rock"):
        score += 1
        print("Player wins!!!")
    elif (cmove == "scissors" and pmove == "paper"):
        print("Computer wins!!!")
    elif(cmove == "rocks" and pmove == "scissors"):
        print("Computer wins!!!")
    elif(cmove == "rocks" and pmove == "paper"):
        score += 1
        print("Player wins!!!")
    elif(cmove == "paper" and pmove == "scissors"):
        score += 1
        print("Player wins!!!")
    elif(cmove =="paper" and pmove == "rock"):
        print("Computer wins!!!")
    count +=1
    while (count == 5):

        print("Do you wish to continue?")
        print("The score is ",score)
        ans = input()
        if (ans == "yes"):
            keep_playing = True
        else:
            keep_playing = False
        count = 0