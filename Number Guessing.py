import random
num = random.randint(0,100)
guesses = 9
take = 1
print("Guesses left = 9")
while(take<=9):
    user = int(input("Enter the number between 1 to 100---->"))
    if user>num:
        print("Very high")
        guesses = guesses - 1
        take = take + 1
        print("---------Guesses left= ",guesses,"----------")
        print("")
        continue
    elif user<num:
        print("Very low")
        guesses = guesses - 1
        take = take + 1
        print("---------Guesses left= ",guesses,"----------")
        print("")
        continue
    
    else:
        print("Congratulation, You won!!!!")
        print("You used",take, "Guesses")
        break
if guesses==0:
    print("Game Over")
