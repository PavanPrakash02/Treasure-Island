print("Welcome to Treasure Island")
print("Your mission is to find the treasure.")

print("You're at a cross road. Where do you want to go? Type 'left' or 'right'")
answer = input()
if answer == "left":
    print("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for the boat. Type 'swim' to swim accross.")
    answer = input()
    if answer == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?")
        answer = input()
        if answer == "yellow":
            print("Congragulations! You found the treasure.")
        elif answer == "blue":
            print("Game over! You enter a room of beasts.")
        else:
            print("Game over! You enter a room of fire.")
    else:
        print("Game over! The crocodiles ate you.")
else:
    print("Game over! You fell inside a hole.")