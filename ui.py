from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

from logic import GameLogic

BACKGROUND = "#DFE4EA"
BACKGROUND_PNG = "assets/background.png"
TITLE_PNG = "assets/title_img.png"


class GuesserApp:
    def __init__(self, window):
        self.logic = GameLogic()
        self.current_row = 0

        self.window = window
        self.window.title("Guess the secret four-digit number")
        self.window.geometry("400x600")
        self.window.resizable(False, False)

        # === Background ===
        original_img = Image.open(BACKGROUND_PNG).resize((400, 600), Image.Resampling.LANCZOS)
        self.background_image = ImageTk.PhotoImage(original_img)
        self.bg_label = Label(self.window, image=self.background_image)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)


        # ?????
        # === Grid config ===
        for i in range(100):  # Adjust as needed
            self.window.grid_rowconfigure(i, weight=1)
        self.window.grid_columnconfigure((0, 1), weight=1)

        # === Title Pic ===
        self.canvas = Canvas(self.window, width=242, height=233,
                             highlightthickness=0, bg=BACKGROUND)
        self.canvas.grid(pady=5, row=1, column=0, columnspan=3)
        self.title_img = PhotoImage(file=TITLE_PNG)
        self.canvas.create_image(121, 117, image=self.title_img)

        # === Buttons ===
        self.button_hint = Button(self.window, text="Hint", width=12, command=self.hint_command)
        self.button_hint.grid(row=0, column=0, padx=5, pady=5)

        self.button_info = Button(self.window, text="Info", width=12, command=self.info_command)
        self.button_info.grid(row=0, column=2, padx=5, pady=5)

        self.button_search = Button(self.window, text="Submit", width=20, command=self.iterate_over_rows)
        self.button_search.grid(row=14, column=1)


        # === Labels ===
        self.label_guess = Label(text="YOUR GUESS")
        self.label_guess.grid(pady=5, row=2, column=0)
        self.label_correct_num = Label(text="Correct Numbers")
        self.label_correct_num.grid(pady=5, row=2, column=1)
        self.label_correct_positions = Label(text="Correct Position")
        self.label_correct_positions.grid(pady=5, row=2, column=2)

        # === Label rows ===
        self.guess_labels = []  # Stores all 10 rows (as tuples) of labels

        for i in range(10):
            guess = Label(self.window, text="", width=17, bg=BACKGROUND)
            guess.grid(row=i + 3, column=0, pady=2)

            correct_nums = Label(self.window, text="", width=13, bg=BACKGROUND)
            correct_nums.grid(row=i + 3, column=1, pady=2)

            correct_pos = Label(self.window, text="", width=10, bg=BACKGROUND)
            correct_pos.grid(row=i + 3, column=2, pady=2)

            self.guess_labels.append((guess, correct_nums, correct_pos))

        # self.guess_labels[current_row][0].config(text="1234")
        # self.guess_labels[current_row][1].config(text="2")
        # self.guess_labels[current_row][2].config(text="1")

        # === Entry ===
        self.guess_entry = Entry(width=20)
        # this will focus the cursor into that particular entry / text
        self.guess_entry.focus()
        self.guess_entry.grid(pady=5, row=13, column=1)

        guess = Label(self.window, text="", width=20, bg=BACKGROUND)
        guess.grid(row=15, column=0)



    def is_guess_correct(self, given_guess):
        """
        Checks for correct guess entry.
        :return: True
        """

        # checks for digits
        is_not_digit = False
        for element in range(len(given_guess)):
            if not given_guess[element].isdigit():
                is_not_digit = True
        if is_not_digit:
            messagebox.showwarning(title="Oops", message="You have to guess four-digit NUMBER.\nLetters not allowed !")
            self.guess_entry.delete(0, END)

        # checks for length
        elif len(given_guess) != len(self.logic.secret_number):
            messagebox.showwarning(title='Oops',
                                   message=f'The number you are trying to guess must be with length of {len(self.logic.secret_number)} digits!')
            self.guess_entry.delete(0, END)

        # checks for leading zeros:
        elif given_guess[0] == "0":
            messagebox.showwarning(title="Oops",
                                   message=f"{given_guess} is not a valid four-digit number because in mathematics, leading zeroes do not count.\n"
                                           f"A true four-digit number must be between 1000 and 9999.")
            self.guess_entry.delete(0, END)
        else:
            self.guess_entry.delete(0, END)
            return True




    # def get_current_guess(self):

    #     a_current_guess:str = self.guess_entry.get()
    #     print(a_current_guess, type(a_current_guess)) #class "str"
    #     return a_current_guess


    def iterate_over_rows(self):

        given_guess: str = self.guess_entry.get()

        if self.current_row > 10:
            messagebox.showwarning(title='Oops',
                                   message=f'You lose! ')

        if self.is_guess_correct(given_guess) and self.current_row <= 10:

            print("its correct")

            self.guess_labels[self.current_row][0].config(text=f"{given_guess}")
            self.guess_labels[self.current_row][1].config(text="2")
            self.guess_labels[self.current_row][2].config(text="1")
            self.current_row += 1







    def hint_command(self):
        print("Hint clicked")

    def info_command(self):
        print("Info clicked")







window_tab = Tk()
app = GuesserApp(window_tab)

curr_guess = app.guess_entry.get()




window_tab.mainloop()
