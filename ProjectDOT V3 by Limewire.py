from tkinter import *
from tkinter import ttk
from google import *
from datetime import datetime
from time import sleep
import requests
import sys

print(sys.version)

count = 1
now = datetime.now()

current_time = now.strftime("%H:%M:%S")   

window = Tk()

def Save(): #Define 'Save'
    with open("RenameThis.txt", "w") as text_file:
        line1 = "ProjectDOT V3 by Limewire"
        line2 = "Thank you for downloading! \(^o^)/"
        line3 = " "
        line4 = Name.get()
        line5 = Address.get()
        line6 = PhoneNumber.get()
        line7 = IP.get()
        line8 = Other.get()

        text_file.writelines ([line1+"\n", line2+"\n", line3+"\n", "Name: "+line4+"\n", "Address: "+line5+"\n", "Phone Number: "+line6+"\n", "IP: "+line7+"\n", "Other: "+line8+"\n"])
        text_file.close()

        print("Dox created successfully!")

def openWindow2(): #Username search window
    global name_search
    window2 = Tk()
    window2.title("ProjectDOT V3 by Limewire")
    window2.geometry("500x175")
    window2.configure(bg = "dark green")
    
    w2t1 = Label(window2,text = "ProjectDOT V3 by Limewire", fg = "lime green", bg = "dark green")
    w2t1.grid(row=1,column=1)
    
    w2t2 = Label(window2,text = "Input Username:", fg = "lime green", bg = "dark green")
    w2t2.grid(row=2,column=1)

    w2t3 = Label(window2,text = "Check console after searching.", fg = "lime green", bg = "dark green")
    w2t3.grid(row=3,column=2)
    
    Username = Entry(window2)
    Username.grid(row=2,column=2)

    buttonSearch = Button(window2,text = "Search", fg = "dark green", bg = "lime green", command = lambda Username = Username: Gsearch(Username.get()))
    buttonSearch.grid(row=2,column=3)

def openWindow3(): #IP geolocation window
    global response
    
    window3 = Tk()
    window3.title("ProjectDOT V3 by Limewire")
    window3.geometry("500x175")
    window3.configure(bg = "dark green")

    w3t1 = Label(window3, text = "ProjectDOT V3 by Limewire", fg = "lime green", bg = "dark green")
    w3t1.grid(row=1,column=1)

    w3t2 = Label(window3, text = "Input IP:", fg = "lime green", bg = "dark green")
    w3t2.grid(row=2,column=1)

    w3t3 = Label(window3, text = "Check console after geolocating.", fg = "lime green", bg = "dark green")
    w3t3.grid(row=3,column=2)

    IP2 = Entry(window3)
    IP2.grid(row=2,column=2)

    def response(): #Define 'response' on API request
        print(requests.get("https://api.ipgeolocation.io/ipgeo?apiKey=INSERTAPIKEY=" + IP2.get() + "&lang=EN&fields=geo&excludes=continent_code,continent_name").json())

    buttonSearch2 = Button(window3,text = "Geolocate", fg = "dark green", bg = "lime green", command = response)
    buttonSearch2.grid(row=2,column=3)

def Gsearch(searchQuery): #global count fixed counter, removing Gsearch fixed problem
    global count

    try :
        import googlesearch
        for i in googlesearch.search(term=searchQuery):
            print ("(" + current_time + ")")
            print (count)
            print(i + "\n")
            count += 1
            sleep(1)
            # gs = Gsearch(searchQuery)
            # gs.Gsearch() 
    except ImportError:
        print("No module named 'google' found. To install, type 'pip install google' into cmd.")



titleone = Label(window,text = "ProjectDOT V3 by Limewire", fg = "lime green", bg = "dark green")
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

buttonNext = Button(window,text = "Username Search", fg = "dark green", bg = "lime green", command = openWindow2)
buttonNext.grid(row=7,column=3)

buttonNext2 = Button(window,text = "Geolocate IP", fg = "dark green", bg = "lime green", command = openWindow3)
buttonNext2.grid(row=7,column=1)

window.geometry("500x175") #Dox compiler window
window.configure(bg = "dark green")
window.title("ProjectDOT V3 by Limewire")
window.mainloop()
