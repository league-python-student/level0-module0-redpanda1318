from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':

    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero.
    score = 0

    # ASK A QUESTION AND CHECK THE ANSWER

    #      // 2.  Ask the user a question 
    questiona = simpledialog.askstring("Do giraffes hum?")
    #      // 3.  Use an if statement to check if their answer is correct
    if questiona == 'yes':
        print("You're right!")
        score += 1

    if questiona == 'no':
        print("That's wrong")

    #      // 4.  if the user's answer was correct, add one to their score 
 
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
    questionb = simpledialog.askstring("Do pigs sweat?")
    if questionb == 'yes':
        print("That's wrong")

    if questionb == 'no':
        print("You're right!")
        score += 1

    questionc= simpledialog.askstring("Was there ever a cat mayor?")

    if questionc == 'yes':
        print("You're right!")
        score += 1

    if questionc == 'no':
        print("That's wrong")

    questiond = simpledialog.askstring("Can a cloud be a million pounds?")

    if questiond == 'yes':
        print("You're right!")
        score += 1

    if questiond == 'no':
        print("That's wrong")

    questione = simpledialog.askstring("Are there pink and purple lakes?")

    if questione == 'yes':
        print("You're right!")
        score += 1

    if questione == 'no':
        print("That's wrong")

    questionf = simpledialog.askstring("There are less than 100 types of potatos")

    if questionf == 'yes':
        print("That's wrong")

    if questionf == 'no':
        print("You're right!")
        score += 1



    # After all the questions have been asked, tell the user their final score
    messagebox.showinfo(None,"Your final score is " + str(score))
    # remember to convert your variable to a string using the str() function


    
    # Run the window's .mainloop() method
    window.mainloop()
