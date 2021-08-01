import game_data
import art

import random

# choses random account from game_data module
def random_account():
    account = random.choice(game_data.data)
    return account

def compare_accounts(a,b):
    result = a['follower_count'] > b['follower_count']
    return result

def play_game():
    accounts = []
    score = 0
    game_over = False

    while not game_over:

        # populates 'accounts' list and doesnt allow doubles
        while len(accounts) < 2:
            account = random_account()
            if len(accounts) < 1:
                accounts.append(account)
            elif account != accounts[0]:
                accounts.append(account)
        print(art.logo)
        print(f"Your current score is {score}")
        print(f"Choice A: {accounts[0]['name']}, a {accounts[0]['description']}, from {accounts[0]['country']}")
        print(art.vs)
        print(f"Choice B: {accounts[1]['name']}, a {accounts[1]['description']}, from {accounts[1]['country']}")
        
        guess = input("Who has more followers? A or B? ").upper()
        
        if guess == "A":
            guess = compare_accounts(accounts[0],accounts[1])
        elif guess == "B":
            guess = compare_accounts(accounts[1],accounts[0])
        
        if guess:
            score += 1
            accounts.pop(0)
        else:
            game_over = True
            print(f"Wrong! Your final score is {score}!")

play_game()