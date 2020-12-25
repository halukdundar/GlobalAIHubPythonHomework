"""
The user will be defined.Get the data of this user by input method.Obtain information from user as follow:
First Name,Last Name,Age,Date of birth(just year).Pass the user's information to the list and displays the screen using the for loop.
Print all user information on the screen.
If he is under 18,print You can't go out because it's too dangerous on the screen.
If he is over 18,print You can go out to the street on the screen.
"""


ListOfPersonal=[]

first_name    = input("Enter Name :")

last_name     = input("Enter Last Name :")

age           = int(input("Enter Age :"))

year          = int(input("Enter Date of Birth(year) :"))

   
ListOfPersonal.append(first_name)
ListOfPersonal.append(last_name)
ListOfPersonal.append(age)
ListOfPersonal.append(year)


print("User information is below")


for i in ListOfPersonal:                           #Get the user's information using the for loop
    print(i)

if age<18:                                        #If he is under 18
    print("You can't go out because it's too dangerous.")
else:                                              #If he is over 18
    print("You can go out to the street.")   
