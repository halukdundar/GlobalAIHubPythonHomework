#Haluk Dündar, Global AI hub final Project

studentName = "Haluk Dündar" 
counter = 3 
course_List = [] #empty list
notes = {} #empty dictionary
mid = 0 #Midterm
fin = 0 #Final
pro = 0 #Project
av = 0 #Average
def courses():
    print("**Operation of Course selection**")
    choice = int(input("How many courses will be chosen :"))
    if choice < 3:
        print("You failed in class")
    elif choice > 5:
        print("The number of lessons cannot be more than 5")
    else:
        for i in range(choice):
            course = input("Course Name :")
            course_List.append(course)
        print("lessons you took :")
        print(course_List)
        choice2 = input("Which course exam scores would you like to enter :")
        if choice2 in course_List:
            mid = int(input("Enter midterm grade :"))
            fin = int(input("Enter your final grade :"))
            pro = int(input("Enter project grade :"))
            notes["midterm"] = mid
            notes["final"] = fin
            notes["project"] = pro
            print(notes)
            av = (mid*0.3)+(fin*0.5)+(pro*0.2)
            print("Grade average : {}".format(av))
            if av>90:
                print("AA")
            elif av>=70 and av<90:
                print("BB")
            elif av>=50 and av<70:
                print("CC")
            elif av>=30 and av<50:
                print("DD")
            elif av<30:
                print("FF")
        else:
             print("Wrong course name")
while counter > 0:
    name = input("Please, enter student Name :")
    if name == studentName:
        print("Welcome")
        courses()
        break
                
    else:
        print("Invalid username. Try again!")
    counter -= 1
    if(counter == 0):
        print("Please, try again later")
