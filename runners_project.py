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



# Need to rename new.txt to the name of the race
# Next on agenda: make times appear beside participants id
def option2(number, names, ids):
        if number == 2:
            print("Adding results for a race...")
            new = open("new.txt", "w")
            race = (input("Where did this race take place? >>> "))
            new.write(race)
            runner_ids = []
            times = []
            runner_details = []
            x = 0
            while x < len(names):
                for i in names:
                    times = input(f"What was {names[x]}'s time? >>> ")
                    x += 1
                    runner_details.append(times)
            runner_ids = ids
            runner_details.append(ids)   
            print(runner_details)
            
            new.close()


def option3(number):
        if number == 3:
            print("Here are all the competitors by county")


def option4(number):
        if number == 4:
            print("Here are the winners of each race")


def option5(number):
        if number == 5:
            print("Which competitor's times do you want to see?")


def option6(number):
        if number == 6:
            print("Showing all competitor's who have won a race...")


def option7(number):           
        if number == 7:
            print("Exiting the program...")
            # break



# Just put else in option 7 
# def no_option(number):
#         if number != 1 or 2 or  3 or  4 or 5 or 6 or 7:
#             print("Oops, you need to enter an option between 1 and 7.")



        
def main():
    names, ids = convert()
    number = display_menu(print_dashes)
    print(number)
    option1(number, print_dashes)
    option2(number, names, ids)
    option3(number)
    option4(number)
    option5(number)
    option6(number)
    option7(number)
    


main()


