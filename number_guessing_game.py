import random

ans = 'y'
while ans =='y':
    lives =5
    random_number = random.randint(0,999)
    for i in range(1,lives+1):
        guess = int(input("Guess the number betweem 0 to 999: "))
        if guess == random_number:
            print("You Won in" , i , 'try' )
            ans = input("Do you want to play again? (if yes then press 'y' )")
            break
        elif guess > random_number:
            print("Enter lower number")
            continue 
        else:
            print("Enter greater number")
            continue 
    else:
        print("Game Over")
        ans = input("Do you want to play again? (if yes then press 'y' ): ")
