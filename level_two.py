import random
#prints 1 random number between 1 and 100
user_number = input("choose a number between 1 and 100: ")
print(user_number)

for i in range(5):
    computer_num = random.randint(1,101)
    if(user_number == computer_num):
        print("The computer guessed correct! AI is smarter than people the robots will take over")
        break
    elif(user_number > computer_num):
        print("the computer guess is too high!")
    elif(user_number < computer_num):
        print("the computer guess is too low")

        if(i == 4):
            print("the computer is out of guesses, win for humanity!")
