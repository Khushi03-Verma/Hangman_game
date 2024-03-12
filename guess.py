import random
from hangman_art import stages,logo
from hangman_words import word_list
print(logo)

lives=6
chosen_word=random.choice(word_list)
word_len=len(chosen_word)
display=[]
end_of_game=False
for _ in range(word_len):
    display+="_"
while not end_of_game:
    guess = input("Guess the letter:").lower()
    for position in range(word_len):
        letter=chosen_word[position]
        if letter==guess:
            display[position]=letter
    if guess not in chosen_word:
        lives-=1
        if lives==0:
            end_of_game=True
            print("you loose")
    print(display)
    if "_" not in display:
        end_of_game=True
        print("you win the game")
    print(stages[lives])

print(f"Answer is:{chosen_word}")