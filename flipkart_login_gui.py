from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

# ------------------ LOGIN HANDLER FUNCTION ------------------ #
def handle_login():
    email = email_input.get()
    password = password_input.get()
    
    if email == "maheshddhumal@gmail.com" and password == "1234":
        messagebox.showinfo("Login Successful", "Thank you Mahesh for Login")
    else:
        messagebox.showerror("Error", "Login Failed")


# ------------------ MAIN GUI FUNCTION ------------------ #
def main():
    global email_input, password_input

    root = Tk()
    root.title("Login Form")
    root.geometry("350x500")
    root.configure(background="#0096DC")

    # Set window icon
    try:
        root.iconbitmap("flipkart-logo.ico")
    except:
        print("Icon file not found.")

    # ------------------ LOGO ------------------ #
    try:
        img = Image.open("flipkart-logo.png")
        resized_img = img.resize((60, 70))
        img = ImageTk.PhotoImage(resized_img)
        img_label = Label(root, image=img, bg="#0096DC")
        img_label.image = img  # prevent image from being garbage collected
        img_label.pack(pady=(70, 10))
    except:
        print("Image file not found.")

    # ------------------ TITLE ------------------ #
    text_label = Label(root, text="Flipkart", fg="White", bg="#0096DC", font=("verdana", 24, "bold"))
    text_label.pack()

    # ------------------ EMAIL ------------------ #
    email_label = Label(root, text="Enter Email", fg="White", bg="#0096DC", font=("verdana", 12))
    email_label.pack(pady=(20, 5))

    email_input = Entry(root, width=50)
    email_input.pack(ipady=6, pady=(1, 15))

    # ------------------ PASSWORD ------------------ #
    password_label = Label(root, text="Enter Password", fg="White", bg="#0096DC", font=("verdana", 12))
    password_label.pack(pady=(20, 5))

    password_input = Entry(root, width=50, show="*")
    password_input.pack(ipady=6, pady=(1, 15))

    # ------------------ LOGIN BUTTON ------------------ #
    login_btn = Button(
        root,
        text="Click here to Login",
        bg="white",
        fg="black",
        width=20,
        height=2,
        font=("verdana", 10, "bold"),
        command=handle_login
    )
    login_btn.pack(pady=(10, 20))

    # ------------------ START MAINLOOP ------------------ #
    root.mainloop()


# ------------------ EXECUTE APP ------------------ #
if __name__ == "__main__":
    main()

