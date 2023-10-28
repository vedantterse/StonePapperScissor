import random

print('WELCOME FOR STONE PAPPER SCISSOR GAME')
print('\033[34m ' + 'its you🤠 ' + '\033[0m' ' vs', '\033[32m ' + ' computer🤖 ' + '\033[0m''\n lets see who wins🤨😮‍💨')
choices = ['stone', 'papper', 'scissor']
rounds = 4
computerS = 0
userS = 0
while True:
    for _ in range(rounds):
        computerC = random.choice(choices)
        userC = input('enter your choice:-(stone/papper/scissor):- ').lower()
        if userC =='exit':
            break
        if userC not in choices:
            print('please enter a valid choice!!')
            continue
        print('\033[34m' + 'user:-' + '\033[0m', userC)
        print('\033[32m' + 'computer:- ' + '\033[0m', computerC)

        if userC == computerC:
            print('its a tie')
        elif ((userC == 'stone' and computerC == 'scissor')
              or (userC == 'papper' and computerC == 'stone')
              or (userC == 'scissor' and computerC == 'papper')):
            print('!!you win🤩!!')
            userS += 1
        else:
            print('computer win🤖')
            computerS += 1

    print()
    print('\033[38;5;80m❗game over❗\033[0m')
    print(f'computer score is: {computerS}')
    print(f'user score is: {userS}')
    if userS > computerS:
        print('\033[35m' + 'you won the game🤩🥳🥳' + '\033[0m')
    elif computerS > userS:
        print('\033[38;5;208m'+'you lose the game😓' + '\033[0m')
    else:
        print('\033[38;5;220mits a tie😮‍💨\033[0m')
    print()

    playagain =input('\033[38;5;118m' +'do you want to play again\033[0m \033[38;5;30m(yes/no):-'+ '\033[0m').lower()
    if playagain != 'yes':
        break
