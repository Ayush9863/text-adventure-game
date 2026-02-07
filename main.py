from playsound3 import playsound
import os

def playsound(file_name):
    """Safe sound play - agar file nahi mili to skip"""
    if os.path.exists(file_name):
        playsound(file_name)
    # else: silently skip (no crash)

name=input("enter your name:")
print(f"welcome to an exciting adventure {name}:")
playsound("welcome.mp3")
answer=input("you want to go on a jungle adventure or a horror house:") 
if answer=="jungle adventure":
    playsound("jungle adventure.mp3")
    print("welcome to jungle adventure")
    answer=input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? :").lower() 
    if answer=="left":
        answer = input(
        "You come to a river, you can walk around it or swim across? Type walk to walk around and swim to swim accross: ")

    if answer == "swim":
        print("You swam acrross and were eaten by an alligator.")
        playsound("crocodile_sound.mp3")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
        print('Not a valid option. You lose.')

elif answer == "right":
    answer = input(
        "You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ")

    if answer == "back":
        print("You go back and lose.")
    elif answer == "cross":
        answer = input(
            "You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ")

        if answer == "yes":
            print("You talk to the stranger and they give you gold. You WIN!")
        elif answer == "no":
            print("You ignore the stranger and they are offended and you lose.")
        else:
            print('Not a valid option. You lose.')
    else:
        print('Not a valid option. You lose.')

elif answer=="horror house":

    print("you are standing outside a creepy horror house")
    answer=input("do you want to enter in the house? yes or no")

    if answer=="yes":
        playsound("scary.mp3")
        print("you step inside the horror house and the entrance door shuts behind you with a bang sound")
        room=input("there are two rooms:left room and right room!!which one will you choose")

        if room=="left":
            playsound("man_scream.mp3")
            print("you step into left room and suddenly a ghost appears")
            situation=input("what will you choose? fight or run")

            if situation=="fight":
                print("wow !!you fight bravely and the ghost disappeared!!")
            elif situation=="run":
                playsound("door_sound.mp3")
                print("you try to run ,but the door is locked")
                print("the ghost catches you!! GAME OVER")

        elif room=="right":
            playsound("screaming.mp3")
            print("you step into right room and you fall into a trap door !!")
            print("GAME OVER!!")
        else:
            print("wrong direction!!GAME OVER")    

    if answer=="no":
        print("you decided to stay safe")
        print("sometimes running away is best choice!! YOU WIN")


print("Hope you enjoyed this game!!")
playsound("the end.wav")