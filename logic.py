from random import randint


def generate_number():
    """Create random 4-digit number.
    Return it as a string"""
    random_number = randint(1000,9999)
    return str(random_number)


class GameLogic:
    def __init__(self):
        self.sum_guessed_numbers = 0
        self.secret_number = generate_number()
        # have to remove it later
        print(f"Secret num is: {self.secret_number}")

    def check_guess(self, guess):
        # Have to be removed
        print(f"Your guess is: {guess}")
        if guess == self.secret_number:
            print("You guessed the number!")

    def correct_digits(self, guess):
        """Check how many exact digits are present in the number you entered it."""
        set_of_guess = set(guess)
        for number in guess:
            if number in self.secret_number:
                self.sum_guessed_numbers += 1
        #         # Have to be removed
        #         print(number)
        # # Have to be removed
        # print(f"Sum of guessed numbers: {self.sum_guessed_numbers}")

        return f"{self.sum_guessed_numbers}/{len(set_of_guess)}"


    def correct_position(self, guess):
        """Check how many of given digits are in the correct position."""
        sum_current_position = 0
        for index, guess_digit in enumerate(guess):
            for secret_digit in self.secret_number[index]:
                print(f"Index {index}, secret digit: {secret_digit}, Guess digit: {guess_digit}")
                if guess_digit == secret_digit:
                    sum_current_position += 1
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print(f"You guessed {sum_current_position} current position/s")
        return str(sum_current_position)



        # Compare guess to secret_number
        # Return how many digits are correct, and how many are in correct position
        # return correct_digits, correct_positions


game = GameLogic()
correct_num = game.correct_digits("1234")
correct_pos = game.correct_position("1234")
print(correct_num)
print(correct_pos)