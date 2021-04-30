"""
Python Project
Week 10 
Student name:   Feargal Downey
Student ID:     R00202629
Group:          Comp 1CX
Date:           13/04/2021

 The following five functions allowed for easier manipulation of my program, e.g if I wanted to change from dashes to 
 equals signs I could do so more easily."""

# Function to print out dashes to improve UI.
def print_dashes(i):
    print("-" * i)


def print_races_list(lst):
    for i in lst:
        print(i)

def print_runners_list(lst):
    for i in lst:
        print(i[0])
        print(i[1])

def print_num_msg(num, msg):
    print(str(num) + ". " + msg)


def file_to_list(lst, filename): 
    for i in filename:
        lst.append(i.split(", "))
        
# Made my races lists global variables in order to make them more accessible to all of my functions.        
initial_races = ["Cork", "Kerry"]
extra_races = []
total_races = []
total_races += initial_races


# seperates runners names and ids
def convert(file):
    runners = open(file, "r")
    list_of_runners = []
    runners_ids = []
    runners_names = []
    fixed_ids = []
    for i in runners:
        list_of_runners.append(i.split(", "))
    for i in (list_of_runners):
        runners_ids.append(i.pop())
        runners_names.append(i.pop())
    for i in runners_ids:
        fixed_ids.append(i.rstrip("\n"))
    return runners_names, fixed_ids


# Function to display the list of options avaialbe to the user.
def display_menu():

    print("                   User options                          ")
    print_dashes(50)
    print_num_msg(1, "Show the results for a race")
    print_num_msg(2, "Add results for a race")
    print_num_msg(3, "Show all competitors by county")
    print_num_msg(4, "Show the winner of each race")
    print_num_msg(5, "Show all the race times for one competitor")
    print_num_msg(6, "Show all competitors who have won a race")
    print_num_msg(7, "Quit")
    print_dashes(50)
    user_input = int(input("Please enter your choice from 1 - 7 >>> "))
    print()
    if user_input == "":
        print("Uh oh, please enter a number from 1 - 7")
    return user_input

# combine global lists and use here in place of initial_races and anywhere I index into initial races
def times_to_mins(i):
    race = total_races[i - 1].lower() + ".txt"
    venue = open(race, "r")
    details = []
    ids = []
    times = []
    fixed_times = []
    for i in venue:
        details.append(i.split(", "))
    for i in details:
        times.append(i.pop())
        ids.append(i.pop())
    for i in times:
        fixed_times.append(i.rstrip("\n"))
    i = 1
    while i < len(details):
        times.append(details.pop(i))
        i += 1
    x = 0
    time = [int(i) for i in fixed_times]
    minutes = []
    seconds = []
    total_times = []
    while x < len(fixed_times):
        minutes.append(time[x] // 60)
        seconds.append(time[x] % 60)
        total_times.append(f"{minutes[x]} minutes and {seconds[x]} seconds")
        x +=1
    return total_times


def determine_winner(ids, total_times):
    winner_time = min(total_times)
    winner_index = total_times.index(min(total_times))
    winner = (f"{ids[winner_index]} won the race with a time of {winner_time} ")
    return winner

def option1(ids, counter):
    print("The races are the following:")
    print_dashes(15)
    print_num_msg(1,  "Cork")
    print_num_msg(2, "Kerry")
    if len(extra_races) > 0:
        for i in range(len(extra_races)):
            print_num_msg(i + 3, extra_races[i])
    print_dashes(15)
    race_choice = int(input("Which number race would you like the results of? >>> "))
    total_times = times_to_mins(race_choice - 1)
    winner = determine_winner(ids, total_times)
    print(total_races[race_choice - 1] + " results")
    print_dashes(15)
    i = 0
    while i < len(total_times):
        print(ids[i] + ", " + total_times[i])
        i += 1
    print()
    print(winner)            
    if counter >= 2:
        print("working")    


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
        runner_details.append(str(runner_ids[y]) + ", " + str(times[y] + ", ")) # added second comma
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
    for i in range(len(extra_races)):
        total_races.append(extra_races[i])


# function to show participants by county
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
    print_races_list(cork_runners)
    print("Kerry runners")
    print_dashes(30)
    print_races_list(kerry_runners) 

# Ran out of time while trying to loop data through the program
def option4(ids):
    print("Here are the winners of each race...")
    winners = []
    print_dashes(50)
    i = len(total_races) - 2
    while i > -1:
        total_times = times_to_mins(i)
        winner = determine_winner(ids, total_times)
        winners.append(winner)
        race_won = total_races.pop()
    print(winners)
    while i < len(winners):
        print(f"{race_won[i]}\t{winners[i]}")
    return winners
        

def option5():
    print("Which competitor's times do you want to see?")
    runners = open("runners.txt", "r")
    runner_details = []
    for i in runners:
        runner_details.append(i.split(", "))
    for i in total_races:
            total_times = times_to_mins(i)
            print(f"{runner_details[i]}, {total_times}")
    

def option6():
    print("Showing all competitor's who have won a race...")
    winnners = []
    for i in total_races:
        total_times = times_to_mins(i)
        winner = determine_winner(ids, total_times)
        winners.append(winner)
    print("The following particicpants have won a race.")
    print_dashes(30)
    for i in winners:
        if winners.count(i) > 1:
            winners.pop()

      # I underestimated how long this project would take and thus ran out of time. Apologies

def main():
    race = ""
    names, ids = convert("runners.txt")
    counter = 0
    while True:
        counter += 1
        number = display_menu()
        if number == 1:
            option1(ids, counter)
        elif number == 2:
            race = option2(names, ids)
        elif number == 3:
            option3(ids, names)
        elif number == 4:
            winners = option4(ids)
        elif number == 5:
            option5()
        elif number ==6:
            option6()
        else:
            print("Exiting the program, goodbye...")
            break
        
main()

