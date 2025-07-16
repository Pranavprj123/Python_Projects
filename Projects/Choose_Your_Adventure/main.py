name = input("Enter your name: ")
print("Welcome",name,"to this adventure!")


answer = input("You are on a dirt road. It has come to an end and you can go left or right. Which way do you want to go? (left/right) ").lower()

if answer == "left":
    answer = input("You come to a river,you can walk around it or swim across. Type 'walk' to walk around or 'swim' to swim across: ").lower()

    if answer == "walk":
        print("You walk for many miles,run out of water and you lost the game.")

    elif answer == "swim":
        print("You swim across and were eaten by a alligator.")

    else:
        print("Not a valid option. You lose!")


elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly. Do you want to cross it or head back? Type 'cross' to cross the bridge or 'back' to go back: ").lower()

    if answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them or run away? Type 'talk' to talk or 'run' to run away: ").lower()

        if answer == "talk":
            print("You talk to the stranger and they give you treasure! You win!")

        elif answer == "run":
            print("You run away safely, but miss out on the treasure. You lose!")

        else:
            print("Not a valid option. You lose!")

    elif answer == "back":
        print("You go back and loose.")

    
else:
    print("Not a valid option. You lose!")

print("Thank you for trying", name, "!")
    


