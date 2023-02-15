from tkinter import *

window = Tk()

def Save(): #Define 'Save'
    with open("RenameThis.txt", "w") as text_file:
        line1 = "D.O.T. by Limewire "
        line2 = "Thank you for downloading! "
        line3 = " "
        line4 = Name.get()
        line5 = Address.get()
        line6 = PhoneNumber.get()
        line7 = IP.get()
        line8 = Other.get()

        text_file.writelines ([line1+"\n", line2+"\n", line3+"\n", line4+"\n", line5+"\n", line6+"\n", line7+"\n", line8+"\n"])
        text_file.close()

        print("Dox created successfully!")



titleone = Label(window,text = "D.O.T. by Limewire", fg = "lime green", bg = "dark green")
titleone.grid(row=1,column=1)

titletwo = Label(window,text = "Name: ", fg = "lime green", bg = "dark green")
titletwo.grid(row=2,column=1)

titlethree = Label(window,text = "Address: ", fg = "lime green", bg = "dark green")
titlethree.grid(row=3,column=1)

titlefour = Label(window,text = "Phone Number: ", fg = "lime green", bg = "dark green")
titlefour.grid(row=4,column=1)

titlefive = Label(window,text = "IP: ", fg = "lime green", bg = "dark green")
titlefive.grid(row=5,column=1)

titlesix = Label(window,text = "Other: ", fg = "lime green", bg = "dark green")
titlesix.grid(row=6,column=1)

Name = Entry(window)
Name.grid(row=2,column=2)

Address = Entry(window)
Address.grid(row=3,column=2)

PhoneNumber = Entry(window)
PhoneNumber.grid(row=4,column=2)

IP = Entry(window)
IP.grid(row=5,column=2)

Other = Entry(window)
Other.grid(row=6,column=2)


buttonSave = Button(window,text = "Save", fg = "dark green", bg = "lime green", command = Save)
buttonSave.grid(row=7,column=2)

window.geometry("350x175")
window.configure(bg = "dark green")
window.title("Dox Organization Tool by Limewire")
window.mainloop()
