# Program for Guessing number
print("        **Task13**        ")
print("# This is number Guessing game. you have only 3 chances")
new_list = [2,4,6]
for i in new_list:
    user_input = int(input("Guess number from avialable three numbers: "))
    if user_input == i:
        print('Guessed number is right and you are rewarded')
    else:
        print('Try Again!')
else:
    print('Better luck next time')    

    


