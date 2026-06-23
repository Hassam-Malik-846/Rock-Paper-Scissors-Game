import random
from Player_prof import Player


print("---------------Menu---------------")
print("Press 1 to play and 2 to view scores")
choose = int(input("Enter Your Choice: "))


def greet(fx):
    def wrapper():
        print("====================")
        print("Welcome to the game")
        print("====================")
        fx()
        print("====================")
        print("Good Bye! Thank You for playing")
        print("====================")
    return wrapper

@greet
def startgame():     
    while(True):

        user_choice = input("Enter Your Choice (R, P, S) or press a random key to exit: ").upper()
        c_options = ["R","P","S"]
        random.shuffle(c_options)
        computer_choice = random.choice(c_options)
        
        if user_choice not in c_options: 
            print("Unknown Choice")
            print("Your Score: ",user.score)
            break
        
        print(f"Your choice: {user_choice} | Computer's Choice: {computer_choice}")

        #Conditions 

        if user_choice == computer_choice:
            
            print("Draw")
        elif user_choice == "P" and computer_choice == "R":
            print("You Won")
            user.win_round()
        elif user_choice == "S" and computer_choice == "R":
            
            print("You lose")
            user.lose_round()
        elif user_choice == "R" and computer_choice == "P":
            
            print("You Lose")
            user.lose_round()
        elif user_choice == "R" and computer_choice == "S":
            
            print("You Won")
            user.win_round()
        elif user_choice == "P" and computer_choice == "S":
            
            print("You Lose")
            user.lose_round()
        elif user_choice == "S" and computer_choice == "P":
            
            print("You Won")
            user.win_round()
    with open("score.txt","a") as f:
        f.write(f"Player: {user.name} | Score: {user.score}\n")
if choose == 1:
    name = input("Enter you name: ")


    user = Player(name, score = 0)
    startgame()
elif choose == 2:
    try:
        with open("score.txt","r") as f:
            for line in f:
                print(line.strip())
    except FileNotFoundError:
        print("--- No scores recorded yet! Play a game first. ---")

else:
    print("Invalid Choice")
