import re

"""
validating user input
- if nothing is written, input is invalid
- if the input contains lowercase letters or digits, input is invalid
- if the input is valid, then we enable the "Crack encryption" message and inform the user the input is valid
"""

def check_input(message,message_label,crack_button):
    if len(message)==0:
        message_label.configure(text="Still waiting...",fg="Red")
        crack_button.configure(state='disabled')
        return False
    elif bool(re.search(r'\d',message)) or message.isupper() is False:
        message_label.configure(text="Invalid message",fg="Red")
        crack_button.configure(state='disabled')
        return False
    else:
        message_label.configure(text="Valid message",fg="Green")
        crack_button.configure(bg="gray71")
        crack_button.configure(state='active')
        return True