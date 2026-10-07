import random 
items = ["rock", "paper", "scissors"]

user_choice = input("Enter your choice = rock, paper, scissors= ")
comp_choice = random.choice(items)

print(f"User choice = {user_choice}, Computer choice = {comp_choice}")

if user_choice == comp_choice:
    print("both chooses same: = Match Tie")
    
elif user_choice == "rock":
    if comp_choice == "Paper":
        print("Paper covers rock, Computer wins")
    else:
        print("rock smashes Scissors, You win")
 
elif user_choice == "paper":
    if comp_choice == "scissors":
        print("Scissors cuts paper, Computer wins")
    else:
        print("Paper covers rock, You win")  
        
elif user_choice == "scissors":
    if comp_choice == "Paper":
        print("Scissors cuts paper, You win")
    else:
        print("Rock smashes scissors, Computer wins")         
             
            
            