"""
Python Project
Week 10 
Student name:   Feargal Downey
Student ID:     R00202629
Group:          Comp 1CX
Date:           13/04/2021
"""


def display_menu():
    print("                   User options                         ")
    print("---------------------------------------------------------")
    print("1. Show the results for a race")
    print("2. Add results for a race")
    print("3. Show all competitors by county")
    print("4. Show the winner of eachrace")
    print("5. Show all the race times for one competitor")
    print("6. Show all competitors who have won a race")
    print("7. Quit")
    print("---------------------------------------------------------")
    user_input = int(input("Please enter your choice from 1 - 7 >>> "))
    return user_input

def option1(number):
    if number == 1:
        print("The races are the following:")
        print("-" * 15)
        print("1. Clonakilty")
        print("2. Bandon")
        print("-" * 15)
        race_choice = int(input("Which number race would you like the results of? >>> "))
        if race_choice == 1:
            clonakilty = open("clonakilty.txt", "r")
            print(clonakilty.read())
            clonakilty.close()
        elif race_choice == 2:
            bandon = open("bandon.txt", "r")
            print(bandon.read())
            bandon.close()
        else: 
            print()
            print("Uh Oh, Incorrect data entered, please enter '1' or '2'.")
            print()

    # elif number == 2:
    #     print("Adding results for a race...")
    #     race_name = input("Where did this race take place? >>> ")
    #     No. racers = int(input("How many racers where in the race?"))
        

    
def main():
    number = display_menu()
    print(number)
    option1(number)


main()

#test comment