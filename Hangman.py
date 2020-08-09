import random
print('H A N G M A N\n')
words = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(words)
win_word = []
used = []
abc_list = "abcdefghijklmnopqrstuvwxyz"
for i in word:
    win_word += '-'
letters = set(word)
count = 0


def game():
    global count
    while count != 10:
        x = ''
        for o in win_word:
            x += o
        print(x)
        inp = input('Input a letter:')
        if len(inp) > 1:
            print('You should print a single letter')
            print()
        elif inp not in abc_list:
            print('It is not an ASCII lowercase letter')
            print()
        elif inp in letters:
            used.append(inp)
            letters.discard(inp)
            ind = word.index(inp)
            win_word[ind] = inp
            if word.count(inp) > 1:
                ind2 = word.index(inp, ind + 1, len(word))
                win_word[ind2] = inp
            if len(letters) == 0:
                print('''You guessed the word!
You survived!
                ''')
                break
            else:
                print()
        elif inp in used:
            print('You already typed this letter')
            if count == 8:
                print('You are hanged!')
                break
            else:
                print()
        else:
            used.append(inp)
            print('No such letter in the word')
            count += 1
            if count == 8:
                print('You are hanged!')
                break
            else:
                print()


def game_menu():
    menu = input('Type "play" to play the game, "exit" to quit:')
    if menu == 'play':
        game()
    elif menu == 'exit':
        exit()
    else:
        game_menu()


game_menu()


