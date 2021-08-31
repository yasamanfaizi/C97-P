import random
num = random.randint(1,5)

chances = 5
while chances>0: 
    guess = int(input("enter your guess: "))
    if guess == num: 
        print("congratulations! your guess was correct.")
        break
    else:
        print("your guess was incorrect. try again.")
    chances = chances -1
    print("chances: ", chances)
if chances == 0:
    print("you have no more chances")