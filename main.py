MORSE_CODE = {'F': '..-.', 'X': '-..-', 'P': '.--.', 'T': '-', '2': '..---', '4': '....-', '0': '-----', '7': '--...',
              'V': '...-', 'C': '-.-.', 'E': '.', 'J': '.---', 'O': '---', 'K': '-.-', '9': '----.', 'I': '..',
              'L': '.-..', '5': '.....', '3': '...--', 'Y': '-.--', '6': '-....', 'W': '.--', 'H': '....', 'N': '-.',
              'R': '.-.', 'B': '-...', '8': '---..', 'Z': '--..', 'D': '-..', 'Q': '--.-', 'G': '--.', 'M': '--',
              'U': '..-', 'A': '.-', 'S': '...', '1': '.----'}


def text_to_morse(text):
    """Returns a list of morse codes for the parameter text"""
    text = text.upper()
    output = ""
    # Converts text in morse by looping the dict MORSE_CODE
    for letter in text:
        if letter in MORSE_CODE:
            output += MORSE_CODE[letter] + " "
        elif letter not in MORSE_CODE:
            if letter == "." or letter == "-":
                pass
            else:
                output += letter + " "
    return output


def morse_to_text(morse):
    """"Returns text for the parameter morse"""
    output = ""
    morse = morse.split()
    # Converts text into Morse by utilising the dict MORSE_CODE
    for letter in morse:
        for key, value in MORSE_CODE.items():
            if letter == value:
                output += key + " "
    return output

# Input from user
translator_type = input("Enter a type translator you want to use, 'm' for Text to Morse or 't' for Morse to Text: ")
translator_type = translator_type.upper()

if translator_type == "M":  # Converting text to morse
    input_text = input("Enter your text: ")
    print(text_to_morse(input_text))
elif translator_type == "T":    # Converting morse to text
    input_morse = input("Enter your morse code: ")
    print(morse_to_text(input_morse))
else:   # Handling invalid inputs
    print("Please enter a valid input")
