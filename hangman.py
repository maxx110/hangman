
import random
from re import A

class Hangman:
    
    def __init__(self, word_list, num_lives=5):
        self.word_list=word_list
        self.num_lives=num_lives
        self.word = random.choice(word_list)
        self.letter_list=''
        self.word_guessed= list(len(self.word)*'_')
        self.isgameover=False
        self.num_letters=len(set(self.word))
          
        print(f'The mystery word has {len(self.word)} characters')
        print(self.word_guessed)
        pass

    def check_letter(self, letter):

        def letter_in():
            if letter in self.word: #if letter is in guessword
                self.num_letters-=1
                for i in range(0,len(self.word)): 
                    character=self.word[i]
                    if letter== character:
                        self.word_guessed[i]=letter

            else:
                self.num_lives-=1 #reduce number of lives by 1
                print(f'You entered the wrong one! you have {self.num_lives} left')
            win() #Call the win function
            
            pass

        def win(): #print congratulation to user
            if(all('_' != char for char in self.word_guessed)):
                print('Congratulation! you won')
                self.isgameover=True
                
        letter_in()
        print(self.word_guessed)
        

    def ask_letter(self):
       
       
        def alphabet():#checks if entered input is a single letter
            if len(letter) == 1:
                pass
            else:
                print("Please, enter just one character")

        def already_used():#checks if input has already been entered
            if letter not in self.letter_list:
                pass
            else:
                print(f'{letter} has already been tried')

        def lost():#checks is user has run out of lives
            if self.num_lives==0:
                print(f'You ran out of lives. The word was {self.word}')
                self.isgameover=True

        def image():#prints hangman images
            print('     ------')
            print('     |    ' +('|'if self.num_lives <=4 else ''))
            print('     |    ' +('0'if self.num_lives <=3 else '')) 
            print('     |    ' +('/\\'if self.num_lives <=2 else '')) 
            print('     |    ' +('|'if self.num_lives <=1 else ''))
            print('     |    ' +('/\\'if self.num_lives ==0 else ''))
                
        while not self.isgameover:
            image()
            print() #new line
            letter=input("Please Enter a letter: ") #asking the user for a letter
            letter=letter.lower()          
            print()#new line
            alphabet()
            already_used()
            self.letter_list += letter  
            self.check_letter(letter)
            print(self.num_letters)
            lost()       
        pass

def play_game(word_list):
    game = Hangman(word_list)
    game.ask_letter()
    pass

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)
    
# %%
