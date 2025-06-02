from random import randint

class GameLogic:
    def __init__(self):
        self.secret_number = self.generate_number()

    def generate_number(self):
        # Create random 4-digit number as a string
        return "1234"

    def check_guess(self, guess):
        # Compare guess to secret_number
        # Return how many digits are correct, and how many are in correct position
        return correct_digits, correct_positions