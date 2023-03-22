# encrypts upper letters
# -65 because ASCII_Code(A) = 65
# %26 - 26 letters in the alphabet
def e_letter_upper(key,character):
    return chr((ord(character)+key-65)%26+65)

# encrypts lower letters
# -97 because ASCII_Code(a) = 97
# %26 - 26 letters in the alphabet
def e_letter_lower(key,character):
    return chr((ord(character)+key-97)%26+97)

# decrypts upper letters - as the examples used only contained upper letters concerning the decryption
# the signs inverted for decryption
def d_letter(key,character):
    return chr((ord(character)-key+65)%26+65)