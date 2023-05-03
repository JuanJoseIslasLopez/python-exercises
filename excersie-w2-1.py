#Do you want to know how old will you be the next year?
age = input("How old are you? ")
year = 1
age_num = int(age) + year
age_str = str(age_num)

print ("On your next birthday, you will be " + age_str )

print()

#About the eggs
carton = input("How many eggs cartons do you have? ")
carton_num = int(carton) * 12
eggs = str(carton_num)
print("You have " + eggs + " eggs")

print()

#Cookies
cookies = input("How many cookies do you have? ")
people = input("How many people are there? ")
cookies_num = int(cookies)
people_num = int(people)
cookies_per_person = cookies_num / people_num
cookies_per_person_str = str(cookies_per_person)
print("Each person may have " + cookies_per_person_str + " cookies")