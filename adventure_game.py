question_1= str.lower(input("You wake up in a little room and you don't remamber how did you get there. In the room you see a document with a CLIP and an old KEY, Which one do you want to pick up? "))

if question_1 == "clip":
    print("You open the door with the clip and see a spider, do you want RUN or HIDE? ")

elif question_1 == "key":
    print("You try to opem the door and the key breaks, sorry you are trap")

else:
    print("Not a valid option , please try again")