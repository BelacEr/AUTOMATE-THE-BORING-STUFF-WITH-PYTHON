import random, sys

print('ROCK, PAPER, SCISSORS')

wins = 0
losses = 0
ties = 0

while True:  # Main game loop
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    
    # Player input
    while True:
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit()
        if playerMove in ('r', 'p', 's'):
            break
        print('Type one of r, p, s or q')

    # Display player choice
    if playerMove == 'r':
        print('ROCK versus...')
    elif playerMove == 'p':
        print('PAPER versus...')
    else:
        print('SCISSORS versus...')

    # Computer choice
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    else:
        computerMove = 's'
        print('SCISSORS')

    # Determine winner
    if playerMove == computerMove:
        print('It is a tie!')
        ties += 1
    elif (playerMove == 'r' and computerMove == 's') or \
         (playerMove == 'p' and computerMove == 'r') or \
         (playerMove == 's' and computerMove == 'p'):
        print('You win!')
        wins += 1
    else:
        print('You lose!')
        losses += 1

    print()  # Blank line between rounds