hide = 50
print("welcome to the guess game\n you have to find hidden number \n you have 9 guess limits")
count = 0
while(True):
    print("no of guess left>",9-count)
    guess = int(input("enter number:"))
    if guess==hide:
        print("congrats you won the game")
        count = count +1
        break
    if count==8:
        print("your guess limit is over ")
        exit()
    elif guess>45 and guess<55:
        print("you are closer to the number ")
        count = count +1
        continue
    elif guess > 30 and guess < 70:
        print("you are near to the number ")
        count = count + 1
        continue
    elif guess > 10 and guess < 90:
        print("you are still far  to the number ")
        count = count + 1
        continue
    else:
        print("u are so far ...  ")
        count = count +1
        continue
    print("you won this game after",count-1,'trails')

























