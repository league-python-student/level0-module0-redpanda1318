from tkinter import messagebox, simpledialog, Tk
import sys
import random

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # 1. Change this line to give you a random number between 1 - 100.
    random_num = random.randint(1, 100)

    # 2. Print out the random variable above
    #print(random_num)

    # 3. Code a for loop to run steps 4-10, 10 times
    for i in range(10):



        # 4. Ask the user for a guess using a pop-up window, and save their response
        number = simpledialog.askstring(None, "Guess a number from 1-100")



        # 5. If the guess is correct
        if int(number) == random_num:
            print("Congrats You Guessed The Random Number!")
            # 6. Win. Use 'sys.exit(0)' to end the program
            sys.exit(0)


        # 7. if the guess is high

            # 8. Tell them it's too high
        if int(number) > random_num:
            print("Your number is too high")
        # 9. Else if the guess is low
        if int(number) < random_num:
            print("Your number is too low")

            # 10. Tell them it's too low

    #11. Outside of the loop, tell the user they lost
    print("Sorry you ran out of tries")

    window.mainloop()
