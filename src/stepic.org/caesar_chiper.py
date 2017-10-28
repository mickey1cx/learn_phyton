# https://stepik.org/lesson/23896/step/1?adaptive=true&unit=6422


def chiper(phrase, shift):

    alphabet = ' abcdefghijklmnopqrstuvwxyz'
    shift = shift % len(alphabet)
    new_alphabet = alphabet[shift:] + alphabet[:shift]
    result = ""

    for letter in phrase.strip():
        letter_index = alphabet.index(letter)
        result += new_alphabet[letter_index]

    return 'Result: "' + result + '"'


def chiper_2(phrase, shift):

    alphabet = ' abcdefghijklmnopqrstuvwxyz'
    result = ""

    for letter in phrase.strip():
        letter_index = (alphabet.index(letter) + shift) % len(alphabet)
        result += alphabet[letter_index]

    return 'Result: "' + result + '"'


# print(chiper_2('i am caesar', 3))     # Result: "lcdpcfdhvdu"
# print(chiper_2('az', -2))             # Result: "zx"
# print(chiper_2('abc', 27))            # Result: "abc"

shift = int(input())
phrase = input()
print(chiper(phrase, shift))