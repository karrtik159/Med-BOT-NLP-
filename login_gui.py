from tkinter import *

class Application(Frame):
    def __init__(self,master):
        super(Application, self).__init__(master)#Set __init__ to the master class
        self.grid()
        self.create_main()#Creates function

    def create_main(self):
        print("testing")
        self.title = Label(self, text=" Stuck In The Circle ")#TITLE 
        self.title.grid(row=0, column=2)

        self.user_entry_label = Label(self, text="Username: ")#USERNAME LABEL
        self.user_entry_label.grid(row=1, column=1)

        self.user_entry = Entry(self)                        #USERNAME ENTRY BOX
        self.user_entry.grid(row=1, column=2)

        self.pass_entry_label = Label(self, text="Password: ")#PASSWORD LABEL
        self.pass_entry_label.grid(row=2, column=1)

        self.pass_entry = Entry(self)                        #PASSWORD ENTRY BOX
        self.pass_entry.grid(row=2, column=2)

        self.sign_in_butt = Button(self, text="Sign In",command = self.logging_in)#SIGN IN BUTTON
        self.sign_in_butt.grid(row=5, column=2)

    def logging_in(self):
        print("hi")
        user_get = self.user_entry.get()#Retrieve Username
        pass_get = self.pass_entry.get()#Retrieve Password

        if user_get == 'sam':
            if pass_get == '123':
                print("Welcome!")
                






#Main
root = Tk()
root.title("Stuck in the Circle")
root.geometry("400x100")

app = Application(root)#The frame is inside the widgit
root.mainloop()#Keeps the window open/running