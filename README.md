# key_gen_auto
Python program that generates random passwords and allows users to save them to a specific text file of their choice (line 34).

# Password composition
The generated password has a length of 12 characters, made by lowers, uppers, digits and symbols. Feel free to change the length of password any way you want by editing it (line 12).

# Requirements
The only external module is the one named "keyboard". You can install it via pip:
```python
pip install keyboard
```
Or download the requirements file and install the requirement:
```python
pip install -r requirements.txt
```

# Using key_gen_auto
Backspace key:
Generates a new password each time the backspace key is pressed.

Enter key:
Registers the last generated password as data about to be stored inside a text file of your choice. A message pops out informing that the password has been saved. If you press this key again, a message pops out informing to generate a new password with backspace key, and the last generated password won't be registered to be stored again in your file.

Esc key:
Stores the saved passwords in your file and finishes the program.

# keyboard module
key_gen_auto utilizes the "keyboard" module authored by Boppreh in 2016. Full credits and copyright for the "keyboard" module go to Boppreh. The original module and its license can be found [here](https://github.com/boppreh/keyboard).
