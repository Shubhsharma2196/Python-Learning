import random

you = input("Rock/Paper/Scissor?: ")
you = you.capitalize()
print("You Choose:",you)


options = ["Rock", "Paper", "Scissor"]
computer = random.choice(options)
computer = computer.capitalize()

print("Computer Choose:", computer)

if(computer == you):
    print("Its a Draw")
else:
    if(computer == "Rock"and you == "Paper"):
        print("You WIN!")
    elif(computer == "Rock"and you == "Scissor"):
        print("You LOSE!")
    elif(computer == "Paper" and you == "Rock"):
        print("You LOSE!")
    elif(computer == "Paper" and you == "Scissor"):
        print("You WIN")
    elif(computer == "Scissor" and you == "Rock"):
        print("You WIN")
    elif(computer == "Scissor" and you == "Paper"):
        print("You LOSE")
   

