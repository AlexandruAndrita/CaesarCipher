import formulas

# encrypts the message
# space and "." will be ignored considering the given examples
def encryption(message,key):
    e_message=""
    for letter in message:
        if letter==" ":
            e_message=e_message+" "
        elif letter==".":
            e_message=e_message + "."
        elif letter.isupper():
            e_message=e_message+formulas.e_letter_upper(key,letter)
        elif letter.islower():
            e_message=e_message+formulas.e_letter_lower(key,letter)

    return e_message

# decrypts the message
# space and "." will be ignored considering the given examples
def decryption(message,key):
    d_message=""
    for letter in message:
        if letter==" ":
            d_message=d_message+" "
        elif letter==".":
            d_message=d_message+"."
        else:
            d_message=d_message+formulas.d_letter(key,letter)

    return d_message