"""
 *
 * Project.02: Pizza delivery robot battery charge support application.
 *
 * File Name:  pizza_delivery.py
 * Name:       ?
 * Course:     CPTR 141
 * Date:       ?
 * Time Taken: ?
 *

 ---Code Review: Completed 2/7/22 at 8:00 PM by Karson Chrispens---
"""
# Here I just grouped up all the varibales I will be using
# total_charge
# op1
# deliveries
# entries
# re_charge
# count
# current_charge  
# suggested_charge
# charge_length
# new_charge
# x
# reset


# Have to re-define re-charge to allow user to run loop correctly
re_charge = 10
print()
print()
# Show the user how many hours of the has
print("The Domino's Pizza delivery robot has 10 hours of charge.")
# Set the total charge to 10
total_charge = 10
# Set a value to False
reset = False
# While the value is True my program will run and loop the main menu untill user exits.
while reset == False:
# Show the user a main menu to choose option from.
    print()
    print("Menu")
    print(" 1. Enter delivery times")
    print(" 2. Enter charge time")
    print(" 3. Exit")
    op1 = input("Choose an option: ")
    print()
# Set a new value to False
    x = False
# Set that new value to True to allow the user to run through the loop.
# In this loop it will check if the user entered one of the three options I gave them.
    while x == False:
        if(not(op1 == "1" or op1 == "2" or op1 == "3")):
            x = False
            print("Error! Please enter options 1, 2, or 3 to select option")
            print()
            op1 = input("Choose an option: ")
            print()
        else:
            x = True
    x = False
# If user chooses option 3 on main menu, the program will quit.
    if op1 == "3":
            print("Thanks for using the robot charge manager.")
            print("Goodbye!")
            quit()

    # I am making a list to hold the values that the user inputs.
    entries = []
    # Everytime the loop runs, the counter will go up by 1.
    count = 0
    if op1 == "1":
        deliveries = input("How many deliveries did the robot complete? ")
        while deliveries.isnumeric() == False:
            print("Error!")
            print("Please enter a number.")
            deliveries = input("How many deliveries did the robot complete? ")


    
    # Asking user how many deliveries they want to input
        for i in range(int(deliveries)):
            userInput = input("In hours, how long was delivery {}? ".format(count + 1))
            while userInput.isnumeric() == False:
                print("Error!")
                print("Please enter a number.")
                userInput = input("In hours, how long was delivery {}? ".format(count + 1))
                
            entries.append(float(userInput))
            count += 1
        re_charge = re_charge - (sum(entries) * 0.5)
        # If the re-charge time ends up being less than 0, an Error will occur, letting the user know the robot can only travel for 10 hours
        if re_charge < 0:
            print()
            print("---Error! Robot can only travel for 10 hours!---")
            print("Robot is currently at 0 hours of charge")
            # Since the re-charge was below 0, we have to reset the value back to 0, since they cannot negative hours.
            re_charge = 0
            # else if eberyting checks out, the program will tell you how many hours of charge you have left.
        else:
            print()
            print("The Domino's Pizza delivery robot has {} hours of charge.".format(re_charge))
    #current_charge = 10 - re_charge
    current_charge = re_charge
    print()
    print()
    # If user chooses option 2 in the main menu.
    # I created a charging table to show the user how many hours the robot should be charged with how much battery life it stil has.
    if op1 == "2":
        if (current_charge >=0 and current_charge < 3):
            print("With a current charge of {} hours, it is suggested to charge the robot 7 hours.".format(re_charge))
            print()
        elif (current_charge != 0 and current_charge >=3 and current_charge < 6.5):
            print("With a current charge of {} hours, it is suggested to charge the robot 3.5 hours.".format(re_charge))
            print()
        elif current_charge != 0 and current_charge >=6.5 and current_charge < 10:
            print("With a current charge of {} hours, it is suggested to charge the robot 0 hours.".format(re_charge))
            print()
        else:
            print("With a current charge of 10.0 hours, it is suggested to charge the robot 0.0 hours.")
        # After I tell the user how many it should charge for.
        # Ask the user again how many hours they would like the robot to charge for.
        charge_length = input("How long did the robot charge? ")
        print()
        while charge_length.isnumeric() == False:
            print("Error!")
            print("Please enter a number.")
            charge_length = input("How long did the robot charge? ")
            
        new_charge = re_charge + int(charge_length)
        re_charge = re_charge + int(charge_length)
        # If the robot is given less than 10 hours of charge time, print how manny hours the robot has left after charging.
        if new_charge < 10:
            print("The Domino's Pizza delivery robot has {} hours of charge.".format(new_charge))
            # If the user inputs more than 10 hours, This error will occur and the value of new_charge gets reset to 10.
        else:
            print("---KEEP IN MIND! The robot's max battery life is 10 hours---")
            new_charge == 10
            print("The Domino's Pizza delivery robot has 10.0 hours of charge.")

    print()
# If the user chooses option 3 from the main menu, the program will quit.


    


