"""
Python Project
Week 10 
Student name:   Feargal Downey
Student ID:     R00202629
Group:          Comp 1CX
Date:           13/04/2021
"""

# Function to print out dashes to improve UI.
def print_dashes(i):
    print("-" * i)


def convert():
    runners = open("runners.txt", "r")
    list_of_runners = []
    [list_of_runners.append(line.rstrip("\n")) for line in runners]
    runners_ids = []
    runners_names = []
    i = 9
    x = 4
    #Cork racers
    while i > 0:
        runners_ids.append(list_of_runners.pop(i))
        i -= 2
    while x >= 0:
        runners_names.append(list_of_runners.pop(x))
        x -= 1
    runners_ids.reverse()
    runners_names.reverse()
    return runners_names, runners_ids


# Function to display the list of options avaialbe to the user.
def display_menu(print_dashes):
    print("                   User options                          ")
    print_dashes(50)
    print("1. Show the results for a race")
    print("2. Add results for a race")
    print("3. Show all competitors by county")
    print("4. Show the winner of eachrace")
    print("5. Show all the race times for one competitor")
    print("6. Show all competitors who have won a race")
    print("7. Quit")
    print_dashes(50)
    user_input = int(input("Please enter your choice from 1 - 7 >>> "))
    return user_input

def option1(number, print_dashes):

    # while True:
        if number == 1:
            print("The races are the following:")
            print_dashes(15)
            print("1. Cork")
            print("2. Kerry")
            print_dashes(15)
            race_choice = int(input("Which number race would you like the results of? >>> "))
            if race_choice == 1:
                print("Cork results:")
                print_dashes(15)
                cork = open("cork.txt", "r")
                print(cork.read())
                cork.close()
                exit
            elif race_choice == 2:
                print("Kerry results:")
                print_dashes(15)
                kerry = open("kerry.txt", "r")
                print(kerry.read())
                kerry.close()
                exit
            else: 
                print()
                print("Uh Oh, incorrect data entered, please enter '1' or '2'.")
                print()

        elif number == 2:
            print("Adding results for a race...")
            new = open("new.txt", "w")
            new.write(input("Where did this race take place? >>> "))
            # runner_details = []
            # x = 0
            # runners = open("runners.txt", "r")
            # while x < runners:
            #     for i in runners:
            #         time = input("What was {runners.read[i]} time? >>> ")
            #     runner_details.append(input("Enter runners id followed by their time in seconds >>> "))
                
            #     print(runner_details[x])
            #     x += 1
            # print(runner_details)
            
            new.close()
        
        elif number == 3:
            print("Here are all the competitors by county")

        elif number == 4:
            print("Here are the winners of each race")
        
        elif number == 5:
            print("Which competitor's times do you want to see?")

        elif number == 6:
            print("Showing all competitor's who have won a race...")
            
        elif number == 7:
            print("Exiting the program...")
            # break
        
        else:
            print("Oops, you need to enter an option between 1 and 7.")



        
def main():
    names, ids = convert()
    number = display_menu(print_dashes)
    print(number)
    option1(number, print_dashes)


main()


