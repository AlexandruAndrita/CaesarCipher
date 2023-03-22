import tkinter as tk
from tkinter import ttk

import action_performed

# custom exception if the value introduced by the user is an integer but not in the specified range (i.e. 0 - 25)
class OutOfRangeException(Exception):
    pass

# creates instance of Tkinter frame
root = tk.Tk()
root.title("Caesar Cipher")

# checks that the action selected is either 'd' (decryption) or 'e' (encryption)
def action_validated():
    # gets the user's input in text format
    user_input=action_entry.get()
    if len(user_input)==0:
        action_status.configure(text="Waiting for input...")
        return False
    elif user_input=="e" or user_input=="d":
        action_status.configure(text=f"Correct. Option chosen: '{user_input}'")
        return True
    else:
        action_status.configure(text=f"Incorrect. You have chosen '{user_input}'")
        return False

# checks that the key is an integer between 0 and 25
def key_validated():
    # gets the user's input in text format
    user_input=key_entry.get()
    try:
        int(user_input)
    except ValueError:
        key_status.configure(text=f"Value introduced '{user_input}' is not a number")
        return False
    else:
        try:
            user_input=int(user_input)
            if user_input<0 or user_input>25:
                raise OutOfRangeException
        except OutOfRangeException:
            key_status.configure(text=f"Value introduced '{user_input}' is not in the specified range")
            return False
        else:
            key_status.configure(text=f"Correct. Chosen value: '{user_input}'")
            return True

# checks that the message field is not left empty
def message_validated():
    # gets the user's input in text format
    user_input=message_entry.get()
    if len(user_input)==0:
        message_status.configure(text="Waiting for input...")
        return False
    else:
        message_status.configure(text="Correct. Field filled")
        return True

# gets the user's input - the action to be perfomed
def get_action_entry():
    action_label = ttk.Label(window, text="Do you want to (e)ncrypt or (d)ecrypt? ")
    action_label.grid(row=0, column=0, padx=10, pady=15, sticky="EW")

    # creates an Entry widget to take over the user input
    # focusout - when the cell losses focus (is not clicked anymore), its content will be validated
    action_entry = ttk.Entry(window, validatecommand=action_validated, validate="focusout")
    action_entry.grid(row=0, column=1, padx=10, pady=15, sticky="NSEW")

    # changes to either "Correct" or "Incorrect" depending on the input of the user using the "action_validated" method
    action_status = ttk.Label(window, text="Waiting for input...")
    action_status.grid(row=0, column=2, padx=10, pady=15, sticky="WE")

    return action_label,action_entry,action_status

# gets the user's key
def get_key_entry():
    key_label = ttk.Label(window, text="Please enter the key [0 - 25] to use: ")
    key_label.grid(row=1, column=0, padx=10, pady=15, sticky="EW")

    # creates an Entry widget to take over the user input
    # focusout - when the cell losses focus (is not clicked anymore), its content will be validated
    key_entry = ttk.Entry(window, validatecommand=key_validated, validate="focusout")
    key_entry.grid(row=1, column=1, padx=10, pady=15, sticky="NSEW")

    # changes to either "Correct" or "Incorrect" depending on the input of the user using the "key_validated" method
    key_status = ttk.Label(window, text="Waiting for input...")
    key_status.grid(row=1, column=2, padx=10, pady=15, sticky="WE")

    return key_label,key_entry,key_status

# gets the user's message to be encrypted or decrypted
def get_message_entry():
    message_label = ttk.Label(window, text="Enter the message to perform action on: ")
    message_label.grid(row=2, column=0, padx=10, pady=15, sticky="EW")

    # creates an Entry widget to take over the user input
    # focusout - when the cell losses focus (is not clicked anymore), its content will be validated
    message_entry = ttk.Entry(window, validatecommand=message_validated, validate="focusout")
    message_entry.grid(row=2, column=1, padx=10, pady=15, sticky="NSEW")

    message_status = ttk.Label(window, text="Waiting for input...")
    message_status.grid(row=2, column=2, padx=10, pady=15, sticky="WE")

    return message_label,message_entry,message_status

# using the user's inputs, gets the encrypted/decrypted message
def get_result():
    action=action_entry.get()
    key=int(key_entry.get())
    message=message_entry.get()

    mod_message = action_performed.functionalities(action, key, message)
    modified_message.configure(text=f"{mod_message}")


# sets the dimensions of the frame
# it will be "considered" a grid with columns and rows
window = ttk.Frame(root, width=800, height=300)
window.grid(row=0, column=0)

action_label,action_entry,action_status=get_action_entry()
key_label,key_entry,key_status=get_key_entry()
message_label,message_entry,message_status=get_message_entry()

# button pressed for sending data in order to determine the new message
button = ttk.Button(window, text="Apply Caesar Cipher",padding=3,command=get_result)
button.grid(row=4, column=1)

result_label= ttk.Label(window, text="The new message is: ")
result_label.grid(row=3,column=0,padx=10,pady=15)

# the new message, marked as label and displayed on the screen
modified_message=ttk.Label(window)
modified_message.grid(row=3,column=1,padx=10,pady=15)

# sets the objects form the window resizable if the dimensions of the window are modified by the user
# by using the same weight, the columns and row will expand at the same rate
root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)

if __name__=='__main__':
    root.mainloop()
    root.quit()

