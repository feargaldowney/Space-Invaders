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
        while 7 != True:
            try:
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
                print()
                return user_input
            except ValueError:
                print("Please enter a number between 1 and 7")

# Just made this, I'm yet to apply it to other functions to determine winners etc.
# must change it up so that it works for all of them rather than having a separate function for each race.
def cork_minutes(ids):
    cork = open("cork.txt", "r")
    cork_runners = []
    [cork_runners.append(line.rstrip("\n")) for line in cork]
    times = []
    i = 1
    while i < len(cork_runners):
        times.append(cork_runners.pop(i))
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
    print(total_times)
    winner_time = min(total_times)
    winner_index = total_times.index(min(total_times))
    winner = (f"{ids[winner_index]} won the race with a time of {winner_time} ")
    return total_times, winner

"""
Changed up cork_minutes,
Must continue fixing up option 1 so that it displays the winnner's ID
Must still loop menu
"""
        
              


def option1(number, print_dashes, ids, total_times, winner):
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
            i = 0
            while i < len(total_times):
                print(ids[i] + ", " + total_times[i])
                i += 1
            print()
            print(winner)
            
        elif race_choice == 2:
            print("Kerry results:")
            print_dashes(15)
            kerry = open("kerry.txt", "r")
            print(kerry.read())
            kerry.close()
        
        else:        
            print()
            print("Uh Oh, incorrect data entered, please enter '1' or '2'.")
            print()



def option2(number, names, ids):
    if number == 2:
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
        print(runner_details)
        new.write(str(runner_details))
        new.close()


def option3(number, ids, names, print_dashes):
    if number == 3:
        print("Showing all competitors by county...")
        print()
        cork_runners = []
        kerry_runners = []
        Limerick_runners = []            
        i = 0
        while i < len(ids):
            if ids[i].startswith("CK"):
                cork_runners.append("\n     " + str(names[i]) + ", " + str(ids[i]) + "\n")   
            elif ids[i].startswith("KY"):
                kerry_runners.append("\n     " + str(names[i]) + ", " + str(ids[i]) + "\n")
            elif ids[i].startswith("LK"):
                Limerick_runners.append("\n     " + str(names[i]) + ", " + str(ids[i]) + "\n")
                
            i += 1
        print("Cork runners")
        print_dashes(30)
        print(*cork_runners)
        print("Kerry runners")
        print_dashes(30)
        print(*kerry_runners) 
        print("Limerick runners")
        print_dashes(30)
        print(*Limerick_runners)
        


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
    total_times, winner = cork_minutes(ids)
    option1(number, print_dashes, ids, total_times, winner)
    option2(number, names, ids)
    option3(number, ids, names, print_dashes)
    option4(number)
    option5(number)
    option6(number)
    option7(number)



main()