import random


def lose_and_win(options, user_choice_index):
    half_options = (len(options) - 1) / 2
    lose_options = options[user_choice_index + 1:]
    if len(lose_options) < half_options:
        diff = half_options - len(lose_options)
        lose_options.extend(options[:int(diff)])
    elif len(lose_options) > half_options:
        diff = len(lose_options) - half_options
        i = 0
        while i < diff:
            lose_options.pop()
            i = i + 1

    win_options = options[:user_choice_index]
    if len(win_options) < half_options:
        diff = int(half_options - len(win_options))
        win_options.extend(options[-diff:])
    elif len(win_options) > half_options:
        diff = len(win_options) - half_options
        i = 0
        while i < diff:
            win_options.pop(0)
            i = i + 1
    return win_options, lose_options


def score_changing(username, score, score_changed):
    with open('rating.txt', 'r') as f:
        old_data = f.read()

    new_data = old_data.replace(username + ' ' + score, username + ' ' + score_changed)

    with open('rating.txt', 'w') as f:
        f.write(new_data)


def select_options():
    user_options = input()
    if user_options == '':
        options = ['scissors', 'rock', 'paper']
    else:
        options = user_options.split(',')
    print("Okay, let's start")
    return options


def menu():
    username = input('Enter your name: ')
    print('Hello, {}'.format(username))
    options = select_options()
    rating = open('rating.txt', 'r')
    if username not in rating.read():
        score = 0
        rating = open('rating.txt', 'a')
        rating.write('{} 0'.format(username, score))
        rating.close()
        game(username, score, options)
    else:
        rating = open('rating.txt', 'r')
        for i in rating.readlines():
            if i.split()[0] == username:
                score = i.split()[1]
                rating.close()
                game(username, score, options)


def game(username, score, options):
    computer_chose = random.choice(options)
    user_input = input()
    if user_input in options:
        user_choice_index = options.index(user_input)
    if user_input == '!exit':
        print('Bye!')
        exit()
    elif user_input == '!rating':
        print('Your rating: ' + score)
        game(username, score, options)
    elif user_input not in options:
        print('Invalid input')
        game(username, score, options)
    elif user_input == computer_chose:
        print('There is a draw ({})'.format(computer_chose))
        score_changed = str(int(score) + 50)
        score_changing(username, str(score), str(score_changed))
        game(username, score_changed, options)
    elif computer_chose in lose_and_win(options, user_choice_index)[1]:
        print('Sorry, but computer chose {}'.format(computer_chose))
        game(username, score, options)
    elif computer_chose in lose_and_win(options, user_choice_index)[0]:
        print('Well done. Computer chose {} and failed'.format(computer_chose))
        score_changed = str(int(score) + 100)
        score_changing(username, str(score), str(score_changed))
        game(username, score_changed, options)


menu()
