import random
counter=0
guess=int(input())
number=int(random.randint(1,20))
while guess!=number:
    if guess < number:
        guess=int(input("your guess is small "))
        counter=counter+1
    if guess > number:
        guess=int(input("your guess is big "))
        counter=counter+1
if guess==number:
    print("You guessed the number, number of tries is {}".format(counter))