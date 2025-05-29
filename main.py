from ui import GuesserApp
from tkinter import *

"""
digit_guesser_game/
│
├── main.py              # Your main file that runs the app
├── ui.py                # Contains GuesserApp class (Tkinter GUI)
├── logic.py             # Contains GameLogic class (game brain)
├── assets/
│   └── background.png   # Images, icons, etc.
└── README.md            # Project info and usage

"""
# === Run App ===
window_tab = Tk()
app = GuesserApp(window_tab)

window_tab.mainloop()
