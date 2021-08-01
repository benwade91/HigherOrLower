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
    game_over = False

    while not game_over:

        # populates 'accounts' list and doesnt allow doubles
        while len(accounts) < 2:
            account = random_account()
            if len(accounts) < 1:
                accounts.append(account)
            elif account != accounts[0]:
                accounts.append(account)

        print(accounts[0]['name'])
        print(accounts[1]['name'])
        game_over = True

play_game()