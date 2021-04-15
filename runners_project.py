"""
Python Project
Week 10
Student name:   Feargal Downey
Student ID:     R00202629
Group:          Comp 1CX
Date:           13/04/2021
"""

def display_menu():
    print("---------------------------------------------------------")
    print("1. Show the results for a race")
    print("2. Add results for a race")
    print("3. Show all competitors by county")
    print("4. Show the winner of eachrace")
    print("5.Show all the race times for one competitor")
    print("6. Show all competitors who have won a race")
    print("7. Quit")
    print("---------------------------------------------------------")
    user_input = int(input("Please enter your choice from 1 - 7 >>> "))
    return user_input

def choice(user_input):
    if user_input == 1:
        race_choice = int(input(("Which race would you like the results of? >>> "))
    #     if race_choice == 1:
    #         print("clonakilty")
    #     elif race_choice == 2:
    #         print(bandon)
    #     else: 
    #         print("Uh Oh, Incorrect data entered, please enter '1' or '2'.")
    # elif user_input == 2:
    #     print("Adding results for a race...")
    #     race_name = input("Where will this race take place? >>> ")
        


def main():
    user_input = display_menu()
    choice(user_input)


main()
