# Import Statements
import pandas as pd
from morse_code_scrape import MorseCode
import sys
from pygame import mixer
import time

# Search for morse_code file and read into DataFrame
try:
    data = pd.read_csv("./Files/morse_code.csv", index_col=0)
except FileNotFoundError:
    # Generate the file by webscraping Wikipedia article
    morse_code_dict = MorseCode()
    data = pd.DataFrame.from_dict(morse_code_dict.dict)
    data.to_csv("./Files/morse_code.csv", index=False, encoding="utf-8")
    data=pd.read_csv("./Files/morse_code.csv", index_col=0)

# Generate Morse Code
def text_to_code(text):
    morse_code_list = []
    for symbol in text:
        try:
            morse_code_list.append(data.at[symbol, 'Code'])
        except KeyError:
            sys.exit(f"Sorry, this symbol was not recognized: {symbol}")

    morse_code = " ".join(morse_code_list)
    print(f"Your morse code message is below:\n\n{morse_code}\n\n")
    return morse_code_list

# Play the generated code back
def play_morse_code(code):
    mixer.init()
    dot = mixer.Sound("./Sounds/dot.wav")
    dash = mixer.Sound("./Sounds/dash.wav")
    for symbol in code:
        for beep in symbol:
            if beep == "·":
                dot.play()
                time.sleep(0.2)
            else:
                dash.play()
                time.sleep(0.4)
        time.sleep(0.5)
    print("End of Message")
    sys.exit()

# Run Program and Collect User Input

print(r"""___  ___                      _____           _      
|  \/  |                     /  __ \         | |     
| .  . | ___  _ __ ___  ___  | /  \/ ___   __| | ___ 
| |\/| |/ _ \| '__/ __|/ _ \ | |    / _ \ / _` |/ _ \
| |  | | (_) | |  \__ \  __/ | \__/\ (_) | (_| |  __/
\_|  |_/\___/|_|  |___/\___|  \____/\___/ \__,_|\___|                                          
                                                     """)
print("Welcome to the Text to Morse Code converter!")
user_message = input("What is your message? ").replace(" ", "/")
list_to_convert = [char for char in user_message.upper()]

# Return a list with text converted to morse code
output_code = text_to_code(list_to_convert)
play_sound = input("Would you like to hear the message? (Y/N)").upper()
if play_sound == "Y":
    play_morse_code(output_code)
else:
    print("Thank you for using the Text to Morse Code Converter!")
    sys.exit()


