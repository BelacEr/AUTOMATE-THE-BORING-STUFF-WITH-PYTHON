import random

#variable declaration

numberOfStreaks = 0

for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    CoinFlip = [] # CHANGE: Reset the list for each sample.
    for i in range(100):
        CoinFlip.append(random.randint(0,1))
    #does not matter if it is 0 or 1, H or T, peas or lentils. I am going to check if there is multiple 0 or 1 in a row        

    # Code that checks if there is a streak of 6 heads or tails in a row.
    streak = 1 # CHANGE: Streaks start at 1
    for i in range(1, len(CoinFlip)):  # CHANGE: Start at index 1, since you are looking at the previous one.
        if CoinFlip[i] == CoinFlip[i-1]:  #checks if current list item is the same as before
            streak += 1 
        else:
            streak = 1

        if streak == 6:
            numberOfStreaks += 1
            break  # CHANGE: Break after finding one 6-streak, since you don't want to double count in the same series of 100-flips.

print('Chance of streak: %s%%' % (numberOfStreaks / 100))