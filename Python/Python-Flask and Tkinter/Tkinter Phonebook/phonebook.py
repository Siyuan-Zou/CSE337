from tkinter import *

phoneBookTable={}

def create_window():
    win = Toplevel()
    win.title("Create/Delete Record")

    nameLabel = Label(win, text="Name: ")
    nameLabel.grid(row=0, column=0)

    nameEntry=Entry(win, width = 25)
    nameEntry.grid(row=0, column=1)

    phoneLabel = Label(win, text="Phone: ")
    phoneLabel.grid(row=1, column=0)

    phoneEntry=Entry(win, width = 25)
    phoneEntry.grid(row=1, column=1)

    addressLabel = Label(win, text="Address: ")
    addressLabel.grid(row=2, column=0)

    addressEntry=Entry(win, width = 25)
    addressEntry.grid(row=2, column=1)

    v=IntVar()

    personalRadionBtn=Radiobutton(win, text="Personal", variable=v, value=1)
    personalRadionBtn.grid(row=3, column=0)
    businessRadionBtn=Radiobutton(win, text="Business", variable=v, value=2)
    businessRadionBtn.grid(row=3, column=1)

    warningLabel = Label(win, text="")
    warningLabel.grid(row=4, column=1)

    def save_record():
        l=[]
        global phoneBookTable
        if(not nameEntry.get()):
            warningLabel.configure(text="Please Fill in Name.")
        elif(not phoneEntry.get()):
            warningLabel.configure(text="Please Fill in Phone.")
        elif(not addressEntry.get()):
            warningLabel.configure(text="Please Fill in Address.")
        elif(v.get()!=1 and v.get()!=2):
            warningLabel.configure(text="Please Select Personal or Business")
        elif(nameEntry.get() not in phoneBookTable):
            l.append(phoneEntry.get())
            l.append(addressEntry.get())
            l.append(v.get())
            phoneBookTable[nameEntry.get()]=l
            warningLabel.configure(text="Record Added")
            print(phoneBookTable)
        else:
            warningLabel.configure(text="Name already in Phonebook.")

    saveBtn=Button(win, text="Save Record", command=save_record)
    saveBtn.grid(row=4, column=0)

def search_window():
    win2 = Toplevel()
    win2.title("Search Record")
    nameLabel = Label(win2, text="Name: ")
    nameLabel.grid(row=0, column=0)

    nameEntry=Entry(win2, width = 25)
    nameEntry.grid(row=0, column=1)

    label1=Label(win2, text="")
    label1.grid(row=1,column=1)
    label2=Label(win2, text="")
    label2.grid(row=2,column=1)
    label3=Label(win2, text="")
    label3.grid(row=3,column=1)
    label4=Label(win2, text="")
    label4.grid(row=4,column=1)
    label5=Label(win2, text="")
    label5.grid(row=5,column=1)

    def search_record():
        global phoneBookTable
        if(nameEntry.get() in phoneBookTable):
            label1.configure(text="Record found:")
            label2.configure(text="Name: "+nameEntry.get())
            label3.configure(text="Phone: "+phoneBookTable[nameEntry.get()][0])
            label4.configure(text="Address: "+phoneBookTable[nameEntry.get()][1])
            if(phoneBookTable[nameEntry.get()][2]==1):
                label5.configure(text="Type: Personal")
            else:
                label5.configure(text="Type: Business")
        else:
            label1.configure(text="Record not found.")
            label2.configure(text="")
            label3.configure(text="")
            label4.configure(text="")
            label5.configure(text="")


    searchBtn=Button(win2, text="Search", command=search_record)
    searchBtn.grid(row=0, column=2)

def delete_window():
    win3 = Toplevel()
    win3.title("Delete Record")

    nameLabel = Label(win3, text="Name: ")
    nameLabel.grid(row=0, column=0)

    nameEntry=Entry(win3, width = 25)
    nameEntry.grid(row=0, column=1)

    label1=Label(win3, text="")
    label1.grid(row=1,column=1)

    def delete_record():
        global phoneBookTable
        if(nameEntry.get() in phoneBookTable):
            del phoneBookTable[nameEntry.get()]
            label1.configure(text="Successfully Deleted")
        else:
            label1.configure(text="Record not found.")
        print(phoneBookTable)

    searchBtn=Button(win3, text="Delete", command=delete_record)
    searchBtn.grid(row=0, column=2)

def list_window():
    global phoneBookTable
    win4 = Toplevel()
    win4.title("List All Record")
    listbox = Listbox(win4, width=50, height=20)
    listbox.pack()

    listbox.delete(0, END)
    listbox.insert(END, "Name, Phone, Address, Type")

    for key in phoneBookTable:
        s=""
        s+=key
        s+=", "+phoneBookTable[key][0]
        s+=", "+phoneBookTable[key][1]
        s+=", "
        if(phoneBookTable[key][2]==1):
            s+="Personal"
        else:
            s+="Business"
        listbox.insert(END, s)

root = Tk()
root.title("CSE 337 Phonebook")
root.geometry("300x150")

createB = Button(root, text="Create/Edit Record", command=create_window)
searchB = Button(root, text="Search Record", command=search_window)
deleteB = Button(root, text="Delete Record", command=delete_window)
listB = Button(root, text="List All Record", command=list_window)
createB.pack()
searchB.pack()
deleteB.pack()
listB.pack()

root.mainloop()
