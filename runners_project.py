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


def print_list(lst):
    for i in lst:
        print(i)

def print_num_msg(num, msg):
    print(str(num) + ". " + msg)
        
initial_races = ["Cork", "Kerry"]
extra_races = []

# comment me
def convert(file): # parameterise file
    runners = open(file, "r")
    list_of_runners = []
    [list_of_runners.append(line.rstrip("\n")) for line in runners]
    runners_ids = []
    runners_names = []
    i = 9 # could do len(list) -1
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
def display_menu():

    print("                   User options                          ")
    print_dashes(50)
    print("1. Show the results for a race")
    print("2. Add results for a race")
    print("3. Show all competitors by county")
    print("4. Show the winner of each race")
    print("5. Show all the race times for one competitor")
    print("6. Show all competitors who have won a race")
    print("7. Quit")
    print_dashes(50)
    user_input = int(input("Please enter your choice from 1 - 7 >>> "))
    print()
    if user_input == "":
        print("Uh oh, please enter a number from 1 - 7")
    return user_input

# combine global lists and use here in place of initial_races and anywhere I index into initial races
def minutes(i):
    race = initial_races[i - 1].lower() + ".txt"
    venue = open(race, "r")
    runners = []
    [runners.append(line.rstrip("\n")) for line in venue]
    times = []
    i = 1
    while i < len(runners):
        times.append(runners.pop(i))
        i += 1
    x = 0
    time = [int(i) for i in times]
    minutes = []
    seconds = []
    total_times = []
    while x < len(time):
        minutes.append(time[x] // 60)
        seconds.append(time[x] % 60)
        total_times.append(f"{minutes[x]} minutes and {seconds[x]} seconds")
        x +=1
    return total_times
    


# sort out this function
def winners(ids, total_times):
    winner_time = min(total_times)
    winner_index = total_times.index(min(total_times))
    winner = (f"{ids[winner_index]} won the race with a time of {winner_time} ")
    return winner

# fix hard coding
def option1(ids, counter):
    print("The races are the following:")
    print_dashes(15)
    print("1. Cork")
    print("2. Kerry")
    if len(extra_races) > 0:
        for i in range(len(extra_races)):
            print_num_msg(i + 3, extra_races[i])
    print_dashes(15)
    race_choice = int(input("Which number race would you like the results of? >>> "))
    total_times = minutes(race_choice)
    winner = winners(ids, total_times)
    print(initial_races[race_choice - 1] + " results")
    print_dashes(15)
    i = 0
    while i < len(total_times):
        print(ids[i] + ", " + total_times[i])
        i += 1
        print()
        print(winner)            
    if counter >= 2:
        print("working")    
    # elif counter >= 1:
    #     print(f"{race} results:")
    #     print_dashes(15)
    #     i = 0
    #     while i < len(total_times):
    #         print(ids[i] + ", " + total_times[i])
    #         i += 1
    #     print()
    #     print(winner)

    
    # else:        
    #     print()
    #     print("Uh Oh, incorrect data entered, please enter '1' or '2'.")
    #     print()


def option2(names, ids):
    print("Adding results for a race...")
    race = (input("Where did this race take place? >>> "))
    new = open(str(race) + ".txt", "w")
    runner_ids = []
    times = [] 
    runner_details = []
    x = 0

    while x < len(names):
        for i in names:
            time = input(f"What was {names[x]}'s time? >>> ")
            x += 1
            times.append(time)
    runner_ids = ids
    y = 0
    while y < len(times):
        runner_details.append(str(runner_ids[y]) + ", " + str(times[y]))
        y += 1
    z = 0
    while z < len(runner_details):
        print(runner_details[z])
        new.write(str(runner_details[z]))
        z += 1
    new.close()
    races = open("races.txt", "a")
    races.write(race)
    races.close
    extra_races.append(race)

# change up ids and names, use new function
def option3(ids, names):
    print("Showing all competitors by county...")
    print()
    cork_runners = []
    kerry_runners = []           
    i = 0
    while i < len(ids):
        if ids[i].startswith("CK"):
            cork_runners.append("\n\t" + str(names[i]) + ", " + str(ids[i]) + "\n")   
        elif ids[i].startswith("KY"):
            kerry_runners.append("\n\t" + str(names[i]) + ", " + str(ids[i]) + "\n")

        i += 1
    print("Cork runners")
    print_dashes(30)
    print_list(cork_runners)
    print("Kerry runners")
    print_dashes(30)
    print_list(kerry_runners) 

# rewrite
def option4(ids, winners):
    print("Here are the winners of each race...")
    # print_dashes(30)
    # x = 1
    # winners = []
    # while x < 3:
    #     total_mins = minutes(ids)
    #     x += 1
    #     winners.append(winner)
    # for i in winners:
    #     print(i)
        

def option5():
    print("Which competitor's times do you want to see?")


def option6():
    print("Showing all competitor's who have won a race...")


def main():
    race = ""
    names, ids = convert("runners.txt")
    counter = 0
    while True:
        counter += 1
        number = display_menu()
        # if counter >= 2:
        #     option1.append(race)
        if number == 1:
            option1(ids, counter)
        elif number == 2:
            race = option2(names, ids)
        elif number == 3:
            option3(ids, names)
        elif number == 4:
            option4(ids)
        elif number == 5:
            option5()
        elif number ==6:
            option6()
        else:
            print("Exiting the program, goodbye...")
            break
        
main()

