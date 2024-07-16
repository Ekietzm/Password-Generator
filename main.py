# Password Generator
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
           'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def main():
    print("Welcome to the PyPassword Generator!")
    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))
    letter_pass = ""
    sym_pass = ""
    num_pass = ""

    for letter in range(0, nr_letters):
        letter_pass += random.choice(letters)
    for symbol in range(0, nr_symbols):
        sym_pass += random.choice(symbols)
    for number in range(0, nr_numbers):
        num_pass += random.choice(numbers)

    unshuffled_pass = letter_pass + sym_pass + num_pass
    password_list = list(unshuffled_pass)
    random.shuffle(password_list)
    password = ""

    for x in password_list:
        password = password + str(x)

    print(password)


if __name__ == '__main__':
    main()
