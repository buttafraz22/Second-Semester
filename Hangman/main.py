import hangman

def main():
    word = hangman.get_random_word()
    hangman.game_play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
       word = hangman.get_random_word()
       hangman.game_play(word)
    
if __name__ == "__main__":
    main()