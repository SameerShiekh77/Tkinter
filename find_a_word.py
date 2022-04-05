# import random module
import random

# initialize variable for again play
again_play = 'y'

score = 0

# starting game
while again_play == 'y':
        # initalize user lives and scores
    lives = 5
    # game intro

    print("*************** WELCOME TO FIND A WORD GAME ***********************\n\n")

    # Game Start from choice
    gameChoice = int(input("Choose Game Level: \nPress 1 for Beginners\nPress 2 for Moderate\nPress 3 for Advance\n\n\n"))

    # hidden words list
    beginner_word_list = ['mic','mouse','notes','binary','octave','list'] 
    moderate_word_list = ['ascii','Argument','Arrays','Dictionary','decimal','interpreter'] 
    advance_word_list = ['Algorithm','Boolean','Desktop','Tkinter','django framework','compilation'] 

    # generate random number
    random_number = random.randint(0,len(beginner_word_list)-1)

    # randomly initialize special word
    simple_word = beginner_word_list[random_number]
    moderate_word = moderate_word_list[random_number]
    advance_word = advance_word_list[random_number]

    for i in range(lives):
        if gameChoice == 1:
            print(f"Find a word from this list: {beginner_word_list}")
            user_input = input("\nFind a word which I hidden in this program: ").lower()
            if user_input == simple_word.lower():
                print("Congratulation!! You Find Right Word")
                score +=10
                again_play = input("Do you want to play again? (if yes then press 'y' )")
                break
            else:
                lives -=1
                print(f"Try Again!!! You Just left {lives} lives\n")
        elif gameChoice == 2:
            print(f"Find a word from this list: {moderate_word_list}")

            user_input = input("\nFind a word which I hidden in this program: ").lower()
            if user_input == moderate_word.lower():
                print("Congratulation!! You Find Right Word")
                score +=10

                again_play = input("Do you want to play again? (if yes then press 'y' )")

                break
            else:
                lives -=1
                print(f"Try Again!!! You Just left {lives} lives\n")
        elif gameChoice == 3:
            print(f"Find a word from this list: {advance_word_list}")

            user_input = input("\nFind a word which I hidden in this program: ").lower()
            if user_input == advance_word.lower():
                print("Congratulation!! You Find Right Word")
                score +=10

                again_play = input("Do you want to play again? (if yes then press 'y' )")
                break
            else:
                lives -=1
                print(f"Try Again!!! You Just left {lives} lives\n")
    else:
        if gameChoice == 1:
            print(f"Game Over!!! The Word is {simple_word}")
            again_play = input("Do you want to play again? (if yes then press 'y' )")

        elif gameChoice ==2: 
            print(f"Game Over!!! The Word is {moderate_word}")
            again_play = input("Do you want to play again? (if yes then press 'y' )")

        elif gameChoice ==3: 
            print(f"Game Over!!! The Word is {advance_word}")
            again_play = input("Do you want to play again? (if yes then press 'y' )")

print("Your Score is: ", score)
