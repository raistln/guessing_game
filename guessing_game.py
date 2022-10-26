import tkinter as tk
import random

window = tk.Tk()
window.geometry("600x400")
window.config(bg="#065569")
window.resizable(width=False,height=False)
window.title('Number Guessing Game')


TARGET = 1.
NUM_RANGE = 0
RETRIES = 2
SELECT = False

def update_result(text):
    result.configure(text=text)

def new_game():
    range_button.config(state='normal')
    update_result(text="I will guess the number you are thinking \n between 0 and the number Push Guess to begin")


def range_game(): 
    global RETRIES, NUM_RANGE, CHOICE
    number = int(number_form.get())+1
    NUM_RANGE = range(int(number_form.get())+1)
    range_button.place_forget()
    number_form.place_forget()
    new_answer.place(x=180, y=153)
    guess_button.place(x=350, y=147) 
    choice = random.choices(NUM_RANGE[1:-1])[0]
    result = f"It´s your number bigger as {choice}. (Answer only y or n)"
    update_result(result)
    CHOICE = choice
    guess_button.config(state='normal')

def guess_game():
    global RETRIES, NUM_RANGE, CHOICE, SELECT
    answer = new_answer.get()
    try:
        if len(NUM_RANGE) > 2:
            if answer == "y" and RETRIES % 2 == 0:
                NUM_RANGE = range(CHOICE, NUM_RANGE[-1]+1)
                choice = random.choices(NUM_RANGE[1:])[0]
                result = f"It´s your number lesser as {choice}. (Answer only y or n)"
                update_result(result)
                new_answer.delete(0,"end")
                CHOICE = choice

            elif answer == "n" and RETRIES % 2 == 0:
                NUM_RANGE = range(NUM_RANGE[0], CHOICE)
                choice = random.choices(NUM_RANGE[1:])[0]
                result = f"It´s your number lesser as {choice}. (Answer only y or n)"
                update_result(result)
                new_answer.delete(0,"end")
                CHOICE = choice

            elif answer == "y" and RETRIES % 2 != 0:
                NUM_RANGE = range(NUM_RANGE[0], CHOICE)      
                choice = random.choices(NUM_RANGE[:-1])[0]
                result = f"It´s your number bigger as {choice}. (Answer only y or n)"
                update_result(result)
                new_answer.delete(0,"end")
                CHOICE = choice

            elif answer == "n" and RETRIES % 2 != 0:
                NUM_RANGE = range(CHOICE, NUM_RANGE[-1]+1)
                choice = random.choices(NUM_RANGE[:-1])[0]
                result = f"It´s your number bigger as {choice}. (Answer only y or n)"
                update_result(result)
                new_answer.delete(0,"end")
                CHOICE = choice

        final_choice = random.choices(NUM_RANGE, k=2)   
        if len(NUM_RANGE) == 2 and (answer == "y" or answer == "n"):
            result = f"Your number is {final_choice[0]}?"
            update_result(result)
            new_answer.delete(0,"end")
            
            if answer == "y" and SELECT == True:
                result = "Oh, my dear I WON."
                update_result(result)
                new_answer.place_forget()
                guess_button.place_forget()
            elif answer == "n" and SELECT == True:
                result = f"Shit I loose your number is {final_choice[1]}."
                update_result(result)
                new_answer.place_forget()
                guess_button.place_forget()
            SELECT = True

    except IndexError:
        if  len(NUM_RANGE) == 1:
            result = f"Oh, my dear your number is {NUM_RANGE[0]}. I WON."
            update_result(result)
            new_answer.delete(0,"end")
        
        new_answer.place_forget()
        guess_button.place_forget()



    RETRIES += 1
    
    
        
exit_button = tk.Button(window,text="Exit Game",font=("Arial",14), fg="White", bg="#b82741", command=window.destroy)
exit_button.place(x=250, y=310)
title = tk.Label(window,text="Guessing Game",font=("Arial",24),fg="#fffcbd",bg="#065569")
title.place(x=170, y=50)
result = tk.Label(window, text="Click on Play to start a new game", font=("Arial", 12, "normal", "italic"),fg = "White", bg="#065569", justify=tk.LEFT)
result.place(x=180, y=210)
play_button = tk.Button(window, text="Play Game", font=("Arial", 14, "bold"), fg = "Black", bg="#29c70a", command=new_game)
play_button.place(x=245, y=260)
range_button = tk.Button(window,text="Enter up to what number I should guess",font=("Arial",13), state='disabled', fg="#13d675",bg="Black", command=range_game)
range_button.place(x=270, y=147) 
guess_button = tk.Button(window,text="Guess",font=("Arial",13), state='disabled', fg="#13d675",bg="Black", command=guess_game)
guess_button.place(x=350, y=147) 
guess_button.place_forget()
num_range = tk.IntVar
number_form = tk.Entry(window,font=("Arial",11),textvariable=num_range)
number_form.place(x=100, y=153)
text_answer = tk.StringVar
new_answer = tk.Entry(window,font=("Arial",11),textvariable=text_answer)
new_answer.place(x=150, y=100)
new_answer.place_forget()




window.mainloop()