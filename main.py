import random


computer=random.choice([1,2,3])
youstr=input("Enter your choice: ")
youdict={"stone": 1 , "paper": 2 , "scissor": 3}
#reversedict={1:"stone" , 2:"paper" , 3:"scissor"}
you=youdict[youstr]
#print(f"Your choice {reversedict[you]} \n Computer choice {reversedict[computer]}")

if (computer==you):
    print("It's a Draw")
else:
    if (computer==1 and you==2):
        print("You Win!")
    elif (computer==1 and you==3):
        print("You Lost!")
    elif (computer==2 and you==1):
        print("You Lost!")
    elif (computer==2 and you==3):
        print("You Win!")
    elif (computer==3 and you==1):
        print("You Win!")
    else:
        print("You Lost!")
