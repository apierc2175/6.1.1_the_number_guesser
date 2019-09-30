import random
#prints 1 random number between 1 and 100
user_number = input("choose a number between 1 and 100: ")
print(user_number)

computer_num = random.randint(1,101)
for i in range(5):
    if(user_number == computer_num):
        print("The computer guessed correct! AI is smarter than people the robots will take over")
        break
    elif(user_number > computer_num):
        print("The computer guess is too high! The computer guessed ", computer_num)
        computer_num = random.randint(computer_num,101)
    elif(user_number < computer_num):
        print("The computer guess is too low! The computer guessed ", computer_num)
        computer_num = random.randint(1,computer_num)

    if i == 4:
        print('The computer is out of guesses. You win!')
