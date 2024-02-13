print("""
\033[36mWELCOME!\033[m

BACKSPACE: generates a random password
ENTER: saves password to be stored in your file
ESC: stores chosen passwords in your file and exits program
""")


def gen_key(length=12):
    '''
    -> Generates a random password using uppers, lowers, digits and symbols
    :param length: Standard password length is defined as 12
    :return: Returns a randomly generated password
    '''
    from string import ascii_letters, digits
    from secrets import choice
    char = ascii_letters + digits + '!@#$%&+=-/~'
    password = ''.join(choice(char) for _ in range(length))
    return password


def main():
    '''
    -> Fuction with keyboard module imported. Allows keys to execute commands.
    Works with gen_key().
    :return: Returns
    '''
    from keyboard import read_hotkey
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

                print('{}Password saved ✓{}\n'.format('\033[1;32m', '\033[m'))
                pass_gen = False

            else:
                print('Press "Backspace" to generate a new password')

        elif key == 'esc':
            print(f"""Saved passwords stored at chosen file.
\033[36mExiting program. Thank you!\033[m""")
            break


if __name__ == "__main__":
    main()
