from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

BACKGROUND = "#DFE4EA"
BACKGROUND_PNG = "assets/background.png"
TITLE_PNG = "assets/title_img.png"


class GuesserApp:
    def __init__(self, window):
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

        self.button_search = Button(self.window, text="Submit", width=20, command=self.search_command)
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



    def search_command(self):
        print("Submit clicked!")
        given_guess: str = self.guess_entry.get()
        print(given_guess)
        print(len(given_guess))
        print(type(given_guess))

        # Try / Except block:
        if len(given_guess) != 4:
            messagebox.showwarning(title= 'Oops', message='The number you are trying to guess is with four digit!')
        if int(given_guess) not in range(1000,9999):
            messagebox.showwarning(title= 'Oops', message='The number you are trying to guess is with four digit!')
        else:
            print(given_guess)
        # for current_row in range(10):
        #
        #     self.guess_labels[current_row][0].config(text="1234")
        #     self.guess_labels[current_row][1].config(text="2")
        #     self.guess_labels[current_row][2].config(text="1")

    def hint_command(self):
        print("Hint clicked")

    def info_command(self):
        print("Info clicked")

