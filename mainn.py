HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

tally = 0
print("Welcome to HANGMAN! You can pick a word with both letters and numbers")
print("Pick a word, Player 1: ")
choice = input()
choice = choice.lower()
comp = []
failed = []
for i in choice:
    comp.append(i)
layout = ["_"] * len(choice)

while layout != comp:
    if tally == 6:
        print(HANGMANPICS[tally])
        print(layout)
        print("YOU LOSE")
        print("THE WORD WAS: " + choice)
        break
    print(HANGMANPICS[tally])
    print(layout)
    print("Tries left: " + str(6-tally))
    print("Failed letters are: ")
    print(failed)
    print("Pick a letter: ")
    let = input()
    if let.lower() in choice:
        for i in range(len(choice)):
            if choice[i] == let.lower():
                layout[i] = let.lower()
    else:
        failed.append(let.lower())
        tally += 1

if layout == comp:
    print(HANGMANPICS[tally])
    print(layout)
    print("YOU WIN")
    print("THE WORD WAS: " + choice)