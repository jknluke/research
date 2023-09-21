import random
#these are the options - rock paper or scissors
options = ("rock", "paper", "scissors")
running = True
#while running code
while running:
#this randomises the computers choice when the game is run
    player = None
    computer = random.choice(options)
#when the code beigns it will print the choice
    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")
#this is code showing weather the computer wins or not 
    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("You lose!")
#this is a code for play again?
    if not input("Play again? (y/n): ").lower() == "y":
        running = False

print("Thanks for playing!")