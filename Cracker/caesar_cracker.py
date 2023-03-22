from tkinter import *
import string

import checking_methods

# main window
window=Tk()
window.geometry("600x700")
window.title("Caesar Cipher Cracker")
window.configure(bg="gray71")

title_frame=Frame(window,bg="gray71")
title_label=Label(title_frame,text="Brute-force attack",font=('Arial',16),justify=CENTER,bg="gray71")
title_label.pack()
title_frame.pack(pady=5)

message_frame=Frame(window,bg="gray71")
message_label=Label(message_frame,text="Message: ",font=('Arial',11),bg="gray71")
message_label.pack()

# user's input
message_entry=Entry(message_frame,font=('Arial',11),width=45)
message_entry.pack()

# used to offer the user a feedback concerning his message: whether is valid or not
message_label=Label(message_frame,text="Still waiting...",font=('Arial',11),fg="Red",bg="gray71")
message_label.pack(pady=3)

message_frame.pack(pady=10)

def crack_message(encrypted_message):
    if len(encrypted_message)==0 and crack_button['state']=='disabled':
        crack_button.configure(state="disabled")
    else:
        # enables the "Crack encryption" button only if the user's input is valid
        crack_button.configure(state="disabled")
        message_label.configure(text="Write another message...",font=('Arial',11),fg="Green")

        # generates the English alphabet in uppercase letters
        letters_available = string.ascii_uppercase
        result=""

        # goes through all possible values for the key
        for key in range(26):
            message = ""
            for character in encrypted_message:
                # if character is a space or a punctuation sign, then it is ignored according the example provided
                if character not in letters_available:
                    message += character
                else:
                    """
                    we search for the position of the character in the alphabet, subtract the value of the key
                    then we add the respective letter from the alphabet, its position is denoted by the value calculated before
                    """
                    position = letters_available.index(character)
                    position -= key
                    if position < 0:
                        position += 26
                    message += letters_available[position]

            # formatting output
            if key<10:
                res_format="Key: 0{} --- Message: {}".format(key,message)
            else:
                res_format="Key: {} --- Message: {}".format(key,message)

            result=result+res_format+"\n"

        result_label.configure(text=result)


# buttons used to validate the input
buttons_frame=Frame(window,bg="gray71")
validate_button=Button(buttons_frame,font=('Arial',11),width=15,text="Validate message",command=lambda : checking_methods.check_input(message_entry.get(),message_label,crack_button),bg="gray71")
validate_button.pack()

# buttons used to appy the cracking technique
crack_button=Button(buttons_frame,font=('Arial',11),width=15,text="Crack encryption",state="disabled",command=lambda : crack_message(message_entry.get()),bg="gray71")
crack_button.pack(pady=3)
buttons_frame.pack(pady=10)

result_frame = Frame(window,bg="gray71")

# widget used to display the result
result_label = Label(result_frame, font=('Arial', 10),justify=LEFT,bg="gray71")
result_label.pack()
result_frame.pack(pady=10)


if __name__=='__main__':
    window.mainloop()

