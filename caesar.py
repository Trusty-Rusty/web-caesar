
def alphabet_position(letter):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cap_alpha = alphabet.upper()
    if letter in alphabet:
        pos = alphabet.rfind(letter)
    else:
        pos = cap_alpha.rfind(letter)
    return(pos)

def rotate_character(char, rot):
    if char.isalpha() == False:
        return char

    else:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        cap_alpha = alphabet.upper()
        if char.isupper() == True:
            pos = (alphabet_position(char))
            rotation = (pos + rot) % len(alphabet)
            return (alphabet[rotation].upper())

        else:
            pos = ((alphabet_position(char)))
            rotation = (pos + rot) % len(alphabet)
            return (alphabet[rotation])

def encrypt(text, rot):
    crypt_list = [rotate_character(char, rot) for char in text]
    return("".join(crypt_list))
