import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class OpenNewWindow(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        tk.Toplevel.__init__(self, *args, **kwargs)
        self.geometry("500x500")
        self.title("New Window")
       

class LoginPage(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        main_frame = tk.Frame(self, bg="#708090", height=431, width=626)
        main_frame.pack(fill="both", expand="true")

        self.geometry("626x431")
        self.resizable(0, 0)
        title_styles = {"font": ("Trebuchet MS Bold", 16), "background": "blue"}

        text_styles = {"font": ("Verdana", 14),
                       "background": "blue",
                       "foreground": "#E1FFFF"}

        frame_login = tk.Frame(main_frame, bg="blue", relief="groove", bd=2)
        frame_login.place(rely=0.30, relx=0.17, height=130, width=400)

        label_title = tk.Label(frame_login, **title_styles, text="Login Page")
        label_title.grid(row=0, column=1, columnspan=1)

        label_user = tk.Label(frame_login, **text_styles, text="Username:")
        label_user.grid(row=1, column=0)

        label_pw = tk.Label(frame_login, **text_styles, text="Password:")
        label_pw.grid(row=2, column=0)

        self.entry_user = ttk.Entry(frame_login, width=45, cursor="xterm")
        self.entry_user.grid(row=1, column=1)

        self.entry_pw = ttk.Entry(frame_login, width=45, cursor="xterm", show="*")
        self.entry_pw.grid(row=2, column=1)

        button = ttk.Button(frame_login, text="Login", command=lambda: self.get_login())
        button.place(rely=0.70, relx=0.50)

        signup_btn = ttk.Button(frame_login, text="Register", command=lambda: self.open_signup_page())
        signup_btn.place(rely=0.70, relx=0.75)

    def get_login(self):
        username = self.entry_user.get()
        password = self.entry_pw.get()
        validation = self.validate(username, password)
        if validation:
            tk.messagebox.showinfo("Login Successful", "Welcome {}".format(username))
            self.open_new_window()
            self.withdraw()
        else:
            tk.messagebox.showerror("Information", "The Username or Password you have entered are incorrect ")

    def open_new_window(self):
        new_window = OpenNewWindow(self)
        new_window.title("New Window")

    def open_signup_page(self):
        SignupPage(self)

    def validate(self, username, password):
        # Checks the text file for a username/password combination.
        try:
            with open("credentials.txt", "r") as credentials:
                for line in credentials:
                    line = line.split(",")
                    if line[1] == username and line[3] == password:
                        return True
                return False
        except FileNotFoundError:
            print("You need to Register first or amend Line 71 to if True:")
            return False

class SignupPage(tk.Toplevel):

    def __init__(self, *args, **kwargs):
        tk.Toplevel.__init__(self, *args, **kwargs)

        main_frame = tk.Frame(self, bg="#3F6BAA", height=150, width=250)
        main_frame.pack_propagate(0)
        main_frame.pack(fill="both", expand="true")

        self.geometry("250x150")
        self.resizable(0, 0)
        self.title("Registration")

        text_styles = {"font": ("Verdana", 10),
                       "background": "#3F6BAA",
                       "foreground": "#E1FFFF"}

        label_user = tk.Label(main_frame, **text_styles, text="New Username:")
        label_user.grid(row=1, column=0)

        label_pw = tk.Label(main_frame, **text_styles, text="New Password:")
        label_pw.grid(row=2, column=0)

        self.entry_user = ttk.Entry(main_frame, width=20, cursor="xterm")
        self.entry_user.grid(row=1, column=1)

        self.entry_pw = ttk.Entry(main_frame, width=20, cursor="xterm", show="*")
        self.entry_pw.grid(row=2, column=1)

        button = ttk.Button(main_frame, text="Create Account", command=lambda: self.signup())
        button.grid(row=4, column=1)

    def signup(self):
        user = self.entry_user.get()
        pw = self.entry_pw.get()
        validation = self.validate_user(user)
        if not validation:
            tk.messagebox.showerror("Information", "That Username already exists")
        else:
            if len(pw) > 3:
                credentials = open("credentials.txt", "a")
                credentials.write(f"Username,{user},Password,{pw},\n")
                credentials.close()
                tk.messagebox.showinfo("Information", "Your account details have been stored.")
                self.destroy()
            else:
                tk.messagebox.showerror("Information", "Your password needs to be longer than 3 values.")

    def validate_user(self, username):
        try:
            with open("credentials.txt", "r") as credentials:
                for line in credentials:
                    line = line.split(",")
                    if line[1] == username:
                        return False
            return True
        except FileNotFoundError:
            return True

if __name__ == "__main__":
    top = LoginPage()
    top.title("Tkinter App Template - Login Page")
    top.mainloop()
