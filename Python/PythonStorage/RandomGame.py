import random
number = random.randint(1,20)
for i in range(3):
    a=int(input())
    if a < number:
        print ("The guessed number is greater than the number entered")
    elif a > number:
        print ("The guessed number is less than the number entered")
    elif a == number:
        print ("You win!")
        break
    else:
        print ("You loose!")