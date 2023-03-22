import encryption_decryption

# determines the new message by calling the respective method
def functionalities(action,key,message):

    if action=="e":
        encrypted_message=encryption_decryption.encryption(message,key)
        return encrypted_message
    else:
        decrypted_message=encryption_decryption.decryption(message,key)
        return decrypted_message

