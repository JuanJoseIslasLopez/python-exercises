when = input("Enter a phrase for 'when': ")
adjective = input("Enter an adjective: ")
animal = input("Enter an animal: ")
verb1 = input("Enter a verb: ")
exclamation = input("Enter an exclamation: ").capitalize()
verb2 = input("Enter another verb: ")
verb4 = input("Enter a word for 'verb': ")
verb3 = input("Enter one more verb: ")
who = input("Enter a phrase for 'who': ")

story = f"{when}, I was really in trouble. It all started when I saw a very {adjective} {animal} {verb1} down the hallway. \"{exclamation}\" I yelled. But all I could think to do was to {verb2} over and over. Miraculously, that caused it {verb4}, but not before it tried to {verb3} right in front of {who}."

print(story)
