import random
#prints 1 random number between 1 and 100
rand_num = random.randint(1,101)
print(rand_num)

for i in range(5):
    guess = input("guess a number between 1 and 100")
    if(guess == rand_num):
        print("You guessed correct!")
    elif(guess > rand_num):
        print("Your guess is too high!")
    elif(guess < rand_num):
        print("Your guess is too low")
