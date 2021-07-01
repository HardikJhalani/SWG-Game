# Snake Water Gun Game

from random import choice

choices = ["Snake","Water","Gun"]

print("Enter either s, or w, or g")
print("Here, s is for snake\nw is for water, and\ng is for gun")
user_score = 0
computer_score = 0
number_of_turns = 10
current_turns = 0
while(current_turns < number_of_turns):
    computer_choice = choice(choices)
    user_input = input("Enter the character: ")
    if(computer_choice == "Snake" and user_input == "w"):
        computer_score += 1
        current_turns += 1
    elif(computer_choice == "Snake" and user_input == "g"):
        user_score += 1
        current_turns += 1
    elif(computer_choice == "Water" and user_input == "g"):
        computer_score += 1
        current_turns += 1
    elif(computer_choice == "Water" and user_input == "s"):
        user_score += 1
        current_turns += 1
    elif(computer_choice == "Gun" and user_input == "w"):
        user_score += 1
        current_turns += 1
    elif(computer_choice == "Gun" and user_input == "s"):
        computer_score += 1
        current_turns += 1
    elif((computer_choice == "Gun" and user_input == "g") or (computer_choice == "Snake" and user_input == "s") or (computer_choice == "Water" and user_input == "w")):
        print("Same choice, try again")
    else:
        print("Incorrect character entered, try again")

print("The computer's score is:",computer_score)
print("Your score is:",user_score)
if(user_score > computer_score):
    print("You win!!")
elif(user_score < computer_score):
    print("You lose!!")
elif(user_score == computer_score):
    print("It is a draw.")