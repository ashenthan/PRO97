import random
number=random.randint(1,9)
chances=0
print("guess a number from 1 to 9")
while chances<5:
    guess=int(input("Enter your guess"))
    if (guess==number):
        print("congrats you guessed right")
        break
    elif (guess<number):
        print("your guess was low")
    else:
        print("your guess was too high")
    chances+=1
if not chances<5:
    print("you lose... the number is ",number)