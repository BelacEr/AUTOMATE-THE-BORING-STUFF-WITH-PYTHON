# Ask for their name and age
print('What is your name?')
name = input()
print('How old are you?')
age = input()
age = int(age) # convert str to int

if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 100:
    print('You are not Alice, grannie.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
