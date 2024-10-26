from art import logo_1


stages = ['''
 +---+
 !   !
 0   !
/!\  !
/ \  !
     !
     !
=========                                        
''', '''
+---+
 !   !
 0   !
/!\  !
/    !
     !
     !
=========  
''', '''
+---+
 !   !
 0   !
/!\  !
     !
     !
     !
=========  
''', '''
+---+
 !   !
 0   !
/!   !
     !
     !
     !
=========  
''', '''
+---+
 !   !
 0   !
 !   !
     !
     !
     !
=========  
''','''
+---+
 !   !
 0   !
     !
     !
     !
     !
=========  
''','''
+---+
 !   !
     !
     !
     !
     !
     !
=========  
''']

print(logo_1)
print("Fruit Name")
#Randomly choose a word from the word_list and assign it to a variable called choosen_word
import random
word_list = ["apple","banana","mango","grapes","orange","papaya","pineapple","Guava","kiwi","cranberry","litchi"]
choosen_word = random.choice(word_list)

#Create a variable called 'lives' to keep track of the number of lives left.
#Set 'lives' equal to 6.
lives = 6

#Create an empty list called display.
#For each letter in the choosen_word, add a "_" to 'display'.

display = []
word_length = len(choosen_word)
for _ in range(word_length):
    display += "_"


#Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the choosen_word
#and 'display' has no more blanks ("_"). Then you can tell the user they've won.

end_of_game = False
while not end_of_game:

    #Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lower case.
    guess = input("Guess a letter: ").lower()

    #Loop through each position in the choosen_word;
    #If the letter at the position matches 'guess' then reveal that letter in the display at the position.

    for position in range(word_length):
        letter = choosen_word[position]
        if letter == guess:
            display[position] = letter

    #Join all the elements in the list and turn it into a string.
    print(f"{' '.join(display)}")

    #If guess is not a letter in the choosen_word, then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose." 

    if guess not in choosen_word:
        lives -=1
        if lives == 0:
            end_of_game = True
            print("You lose.")  

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win")

    
    #Print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])
    
