"""
**Code the Hangman game**
You are free on this assignment.
You can set the rules yourself.There is only on thing expected of you.
When entering the game,The User's name and for example "Welcome John" should be pressed to the screen.
When the game is over,exit the game.So let the game end.
"""
name = input("Enter name :")
print("Hello {}".format(name),"Welcome to hangman game :)")

print("*********")
print(f'The user name : {name}')
print("You have 10 attempts!!")
print("*********")
word = "Monty Python"
guess = ""
lives = 10
while lives > 0:
    character_left = 0
    for i in word:
        if i in guess:
            print(i)
        else:
            print("_")
            character_left+=1    
    if character_left==0:
        print("You Won")
        break

    guess2 = input("Enter letter:")
    guess +=guess2
    if guess2 not in word:
        lives-=1
        print("Wrong")
        print("You have {} left!".format(lives))

        if lives == 0:
            print("Game Over!!")
