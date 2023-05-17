name = input("Welcome to Escape game, How is your name? ")

age = int(input(f"Nice to have you here {name}, this is a game it's just for adults, how old are you? "))
if age >= 18:
    print(f"Thanks for confrim your age {name}, let's do this!")
     
    response= str.lower(input("You wake up in a little room and you don't remamber how did you get there."
                                +"In the room you see a document with a CLIP and an old KEY, Which one do you want to pick up? "))
    # 1
    if response == "clip":
        # 2
        response = str.lower(input("You open the door with the clip and see a spider, do you want to RUN or KILL it? "))
        if response == "run":
            #3
            response = str.lower(input("The spider follows you, bites you and you start to feel dizzie, so you look in your backpack and found a BOTTLE of alchool and a BAND-AID, what do you use? "))
            if response == "bottle":
                print("You clean your wound but fall to the ground, the spider starts to grow big and eats you, game over")
            elif response == "band-aid":
                print("You didn't waste your time cleaning your wound, so you escape and became spiderman, you won!")
            else:
                print("Not a valid option , please try again")
        elif response == "kill":
            #3
            response = str.lower(input("You try to kill the spider, but she jumps and starts to fight against you, do you KICK or PUNCH it? "))
            if response == "kick":
                print("You smash the spider and escape, you won!")
            elif response == "punch":
                print("The spider avoid the hit, and capture you with it's web, you loose!")
            else:
                print("Not a valid option , please try again")
        else:
            print("Not a valid option , please try again")

    # 1
    elif response == "key":
        #2
        response = str.lower(input("You try to open the door and the key breaks, in that moment you see a little window behind the closet, do you try to OPEN the window or to BREAK the door? "))
        if response == "open":
        #3
            response = str.lower(input("You open the window and get out of the room just to see a dark forest, there's a road, do you go NORTH or SOUTH? "))
            if response == "north":
                print("You fall into deadly trap and die, game over!")
            elif response == "south":
                print("You find a car and escape, you won!")    
            else:
                print("Not a valid option , please try again")
        elif response == "break":
            #3
            response = str.lower(input("You break the door, and see a pile of gold, do you TAKE the gold, WAIT or LEAVE it? "))
            if response == "leave":
                print("You start to run, find a way out and escape, you won!")
            elif response == "take":
                print("When you are taking the gold a giant drangon appears and burn you for stealing it's treasures, you loose!")
            elif response == "wait":
                print("You wait and see a Dragon came, and rest over the gold, you make friend with the dragon and escape flying away, you won!")    
            else:
                print("Not a valid option , please try again")
        else:
            print("Not a valid option , please try again")
    # 1
    else:
        print("Not a valid option , please try again")

else:
    print(f"Sorry {name}, you should get permission of your parents first")