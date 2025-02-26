import random
while True:
    List_Values = ["Rock", "Paper", "Sizer"]
    List_Values_int = [1, 2, 3]
    print(f"Choose \n1. {List_Values[0]}\n2. {List_Values[1]}\n3. {List_Values[2]}\nTo Exit select 4")
    player = int(input())
    if(player == 4):
        break
    computer = int(random.choice(List_Values_int))
    print(f"Computer picks {List_Values[computer-1]}")
    if(player == computer):
        print("Draw")
    elif(player == 1):
        if(computer == 2):
            print("You lost")
        if(computer == 3):
            print("You win")
    elif(player == 2):
        if(computer == 1):
            print("You win")
        if(computer == 3):
            print("You lost")
    elif(player == 3):
        if(computer == 1):
            print("You lost")
        if(computer == 2):
            print("You win")