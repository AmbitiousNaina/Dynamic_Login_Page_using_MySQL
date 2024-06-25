from tkinter import *  #imports all functions from tkinter module for gui apps
from PIL import ImageTk  #used for displaying images in tkinter
from tkinter import messagebox #to display msgs in a msgbox
import mysql.connector #for MySQL database connectivity

class Login:   #represents the login interface,
    def __init__(self, root):  #self, is a ref, that allows u to access the variables which belong to the class,constructor method of the Login class.
        self.root = root  #assigns root window to self.root
        self.root.title("Login Page")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False, False)  #disables resizing of the window

        # Database connection setup
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Root@12345',
            port='3306',
            database='python_logindb'
        )                                           #cursor=for database interactions in Python apps
        self.mycursor = self.connection.cursor() #cursor() is called on self.connection(MySQL database) method returns a cursor object,which will execute,fetch queries from db

        self.bg=ImageTk.PhotoImage(file="images/uni.jpg")
        self.bg_image=Label(self.root, image=self.bg).place(x=0,y=0, relwidth=1, relheight=1)

        frame_login = Frame(self.root, bg="white")  #creates a frame with white bg
        frame_login.place(x=330, y=150, width=500, height=400) #frame

        title=Label(frame_login, text="Login Here", font=("Impact", 35, "bold"),fg="dark blue", bg="white").place(x=90, y=30)
        subtitle = Label(frame_login, text="Members Login Here", font=("Goudy old style", 15, "bold"), fg="black", bg="white").place(x=90,y=100)

        #username
        lbl_user = Label(frame_login, text="Username", font=("Goudy old style", 15, "bold"), fg="grey", bg="white").place(x=90,y=140) #Creates labels
        self.username = Entry(frame_login, font=("Goudy old style", 15), bg="#E7E6E6")  #entry widget for user i/p
        self.username.place(x=90, y=170, width=320, height=35)

        #password
        lbl_pswd = Label(frame_login, text="Password", font=("Goudy old style", 15, "bold"), fg="grey", bg="white").place(x=90, y=210)
        self.pswd = Entry(frame_login, font=("Goudy old style", 15), bg="#E7E6E6", show='*')
        self.pswd.place(x=90, y=240, width=320, height=35)

        #button
        forget_btn = Button(frame_login, text="Forgot Password? ",cursor="hand2",bd=0, font=("Goudy old style", 12), fg="#6162FF", bg="white").place(x=90, y=280)
        submit_btn = Button(frame_login,command=self.check_func,cursor="hand2", text="Submit ", bd=0, font=("Goudy old style", 15), bg="#6162FF", fg="white").place(x=90, y=320, width=180, height=40)

    def check_func(self):
        username = self.username.get()  #retrieve the entered text in username,pswd
        password = self.pswd.get()

        # Print username and password to the terminal
        print("The entered details are: ")
        print(f"Username: {username}")
        print(f"Password: {password}")

        # Query to check if the username and password match a record in the database
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        self.mycursor.execute(query, (username, password))  #The actual values for username and password are passed as a tuple (username, password) to replace the %s placeholders.
        user = self.mycursor.fetchone()  #to retrieve the result, user will contain either a tuple/none

        if user is None:
            messagebox.showerror("Error", "Invalid Username or Password!", parent=self.root)
        else:
            messagebox.showinfo("Welcome", f"Welcome {username}")

root = Tk()  # Tk() - is a class in Tkinter,creates the main window,This window serves as the container for all other widgets, assigned to root, root is a standard convention in Tkinter
obj = Login(root)  #creates an instance of a class (Login) that manages and interacts with the root window
root.mainloop()   #mainloop() is a method of the Tk class,that starts the Tkinter event loop. It listens for events like user input,clicks and dispatches them to the resp event handlers.
