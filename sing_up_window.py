'''GUI for sing up window'''
from tkinter import*
from db_connection import sign_up, login

email_label = None
email_entry = None
password_label = None
password_entry = None

'''Creating the main window'''
root = Tk()
root.geometry("900x900")
root.title("Login")

def login():
    email = email_entry.get()
    password = password_entry.get()
   
    print("Email: ", email)
    print("Password:", password)

root.title("Create account")
def sign_up_fields():
    '''function for showing creating new account fields'''
    global email_entry, email_label, password_entry, password_label
    email_label.grid_forget()
    email_entry.grid_forget()
    password_label.grid_forget()
    password_entry.grid_forget()

    '''Create labels and entry fields'''
    first_name_label = Label(root, text="First name: ")
    first_name_label.grid(padx=10, pady=5)
    first_name_label.place(x=350, y=200)
    first_name_entry = Entry(root)
    first_name_entry.grid(padx=10, pady=5)
    first_name_entry.place(x=350, y=230)

    last_name_label = Label(root, text="Last name: ")
    last_name_label.grid(padx=10, pady=5)
    last_name_label.place(x=350, y=250)
    last_name_entry = Entry(root)
    last_name_entry.grid(padx=10, pady=5)
    last_name_entry.place(x=350, y=270)

    email_label = Label(root, text="Email name: ")
    email_label.grid(padx=10, pady=5)
    email_label.place(x=350, y=300)
    email_entry = Entry(root)
    email_entry.grid(padx=10, pady=5)
    email_entry.place(x=350, y=320)

    password_label = Label(root, text="Password name: ")
    password_label.grid(padx=10, pady=5)
    password_label.place(x=350, y=350)
    password_entry = Entry(root, show="*")
    password_entry.grid(padx=10, pady=5)
    password_entry.place(x=350, y=370)


    create_account_button = Button(root, text="Sign up", command=sign_up_window)
    create_account_button.grid(columnspan=2, padx=10, pady=5)
    create_account_button.place(x=350, y=400)


def sign_up_window():
    '''Function for creating a new account'''
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    email = email.get()
    password = password.get()

    print("Last Name:", full_name)
    print("Last Name:", full_name)
    print("Email:", email)
    print("Password:", password)

'''crating labels and entry fields for sign in'''
first_name_label = Label(root, text="Firs Name:")
first_name_label.grid(padx=10, pady=5)
first_nam_label.place(x=350, y=230)
first_name_entry. = Entry(root)
first_name_entry.grid(padx=10, pady=5)
first_name_entry.place(x=350, y=250)

last_name_label = Label(root, text="Last Name:")
last_name_label.grid(padx=10, pady=5)
last_name_label.place(x=350, y=270)
last_name_entry = Entry(root)
last_name_entry.grid(padx=10, pady=5)
last_name_entry.place(x=350, y=300)

email_label = Label(root, text="Email:")
email_label.grid(padx=10, pady=5)
email_label.place(x=350, y=320)
email_entry = Entry(root)
email_entry.grid(padx=10, pady=5)
email_entry.place(x=350, y=350)

password_label = Label(root, text="Password:")
password_label.grid(padx=10, pady=5)
password_label.place(x=350, y=370)
password_entry = Entry(root, show="*")
password_entry.grid(padx=10, pady=5)
password_entry.place(x=350, y=400)


'''Creating login buttons'''

login_button = Button(root, text="Login", command=login)
login_button.grid(padx=10, pady=10)
login_button.place(x=350, y=420)
    
create_account_button = Button(root, text="Create Account", command=sign_up_fields)
create_account_button.grid(padx=10, pady=5)
create_account_button.place(x=350, y=450)

root.mainloop()




