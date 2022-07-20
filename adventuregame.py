name = str(input("Enter Player Name: ")) # username
print(f"{name}, you are on a camping trip alone.") # introduces the story
print("You go inside your tent, but suddenly you see a ghost. Now you have two options:") # introduces the conflict
print("1.Run. 2.Fight the ghost") # possible solutions
user = int(input("Choose 1 or 2: ")) # for user to enter their choice
if user == 1: # what happens if they choose 1
    print("You ran away from the ghost and back to your car.") # shows the result of their choice
    print("You drove back home and never saw the ghost again. Game over!") # game over 1
elif user == 2: # what happens if they choose 2
    print("You grab a knife and slash it through the ghost, and now the ghost is angry.") # shows the result of their choice
    print("It catches you and sends you to the underworld forever. Game over!") # game over 2
else: # if input is not 1 or 2
    print("Please check your input") # lets the user know their input doesn't work
