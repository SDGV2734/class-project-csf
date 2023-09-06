print('Welcome to the game')
user_input = input('What is your name: ')
print('Hello', user_input)
print('guess your secret number: ')

user_input = input()
secret_number = 8

if user_input == secret_number:
    print("correct")
else:
    print('sorry, try again')

user_input2 = input( 'Enter your number: ')
if user_input == secret_number:
    print("correct")
else:
    print('sorry, try again')

user_input3 = input( 'Enter your number: ')
if user_input == secret_number:
    print("correct")
else:
    print('game over')




