# Dictionary contains morse code
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'
}

def text_to_morse(text):
    morse_code = []
    for char in text.upper():
        if char == ' ':
            morse_code.append('/')
        elif char in morse_code_dict:
            morse_code.append(morse_code_dict[char])
    return ' '.join(morse_code)


def morse_to_text(morse_code):
    text = []
    morse_code_split = morse_code.split(' ')
    for code in morse_code_split:
        if code == '/':
            text.append(' ')
        else:
            for key, value in morse_code_dict.items():
                if value == code:
                    text.append(key)
                    break
    return ''.join(text)


input_text = input("Your text: ")
morse_result = text_to_morse(input_text)
print("Morse code:", morse_result)


# input_morse = input("Your morse: ")
# text_result = morse_to_text(input_morse)
# print("Text:", text_result)