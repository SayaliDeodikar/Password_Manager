from tkinter import * 
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for char in range(randint(4,6))]
    password_symbols = [choice(symbols) for char in range(randint(2,4))]
    password_numbers = [choice(numbers) for char in range(randint(2,4))]

    password_list = password_letters + password_symbols +password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()
    if website == "" or password == "" or username =="":
        messagebox.showinfo('Oops',"Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the deails entered: \nEmail/Username: {username} \nPassword : {password} \nIs it ok to save?")

        if is_ok:
            with open("./MyPass/data.txt", "a") as data_file:
                data_file.write(f"{website} | {username} | {password}\n")
                website_input.delete(0, END)
                password_input.delete(0, END)
        
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
lock_img = PhotoImage(file="./MyPass/logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

website_lebel = Label(text="Website:",bg="white")
website_lebel.grid(column=0, row=1)

website_input = Entry(width=50)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

username_label = Label(text="Email/Username:", bg="white")
username_label.grid(column=0,row=2)

username_input = Entry(width=50)
username_input.grid(column=1, row=2, columnspan=2)
username_input.insert(0, "sayaliwin@gmail.com")

password_label = Label(text="Password:", bg="white")
password_label.grid(column=0, row=3)

password_input = Entry(width=32)
password_input.grid(column=1, row=3)

generate_button = Button(text="Generate Password", bg="#ff7171",command=generate_password)
generate_button.grid(column=2,row=3)

add_button = Button(text="Add", bg="#f7d9d9",width=43,command=save)
add_button.grid(column=1, row=4,columnspan=2 )


window.mainloop()
