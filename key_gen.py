from keyboard import read_hotkey
from string import ascii_letters, digits
from random import randint
from secrets import choice


print("""
BACKSPACE: generates a random password
ENTER: saves password to be stored in your file
ESC: stores chosen passwords in your file and exits program
""")


def gen_key():
    characters = ascii_letters + digits + '!@#$%&+=-/~'
    password_length = randint(8, 12)
    password = ''.join(choice(characters) for _ in range(password_length))
    return password


def main():
    pass_gen = False

    while True:
        key = read_hotkey(suppress=False)

        if key == 'backspace':
            password = gen_key()
            print(password)
            pass_gen = True

        elif key == 'enter':
            if pass_gen:
                with open("random_keys.txt", 'a') as f:
                    f.write(password + '\n')

                print('{}Password saved ✓{}'.format('\033[1;32m', '\033[m'))
                pass_gen = False

            else:
                print('Press "Backspace" to generate a new password')

        elif key == 'esc':
            print(f"""Saved passwords stored at chosen file.
Exiting program.""")
            break


if __name__ == "__main__":
    main()
