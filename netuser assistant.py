# Created by Reece Pieri.

from tkinter import *
from tkinter import filedialog
import os
import csv

window = Tk()
window.title("NetUser Assistant")
frame = Frame(window)
frame.pack()

top_frame = Frame(window)
top_frame.pack(pady = 10, padx = 10)
text_frame = Frame(window)
text_frame.pack()
topbtn_frame = Frame(window)
topbtn_frame.pack(pady = 0)
btmbtn_frame = Frame(window)
btmbtn_frame.pack(pady = 0)
status_frame = Frame(window)
status_frame.pack(side = LEFT)

desktop = os.path.expanduser("~/Desktop")
n1 = StringVar()
n2 = StringVar()
n3 = StringVar()
n4 = StringVar()
n5 = StringVar()
n6 = StringVar()
n7 = StringVar()
n8 = StringVar()
n9 = StringVar()
n10 = StringVar()
n11 = StringVar()
n12 = StringVar()
n13 = StringVar()
n14 = StringVar()
n15 = StringVar()
n16 = StringVar()
n17 = StringVar()
n18 = StringVar()
n19 = StringVar()
n20 = StringVar()
s = StringVar()


def submit_btn():
    global s
    names = [n1.get(), n2.get(), n3.get(), n4.get(), n5.get(), n6.get(), n7.get(), n8.get(), n9.get(), n10.get(),
             n11.get(), n12.get(), n13.get(), n14.get(), n15.get(), n16.get(), n17.get(), n18.get(), n19.get(),
             n20.get()]
    for user in names:
            login = user[0].lower() + user.split(" ")[1].lower()
            txtbox.insert(END, 'net user ' + login + ' P@ssw0rd ' + '/ADD /PASSWORDCHG:YES /FULLNAME:' + '"' + user + '"' + "\n")


def copy_btn():
    global s
    window.clipboard_clear()
    window.clipboard_append(txtbox.get(1.0,END))
    s.set("Copied to clipboard")


def imp_btn():
    global s
    with open(filedialog.askopenfilename()) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        next(csv_file)
        for row in csv_reader:
            #login = (user[0][0]) + (user[0].split(" ")[1])
            txtbox.insert(END, 'net user ' + row[1] + ' ' + row[2] + ' ' + '/ADD /PASSWORDCHG:YES /FULLNAME:' + '"' + row[0] + '"' + "\n")
            line_count += 1
        #print(f'Processed {line_count} lines.')
        s.set(f"Processed {line_count} lines")


def exp_btn():
    global s
    with open(os.path.join(desktop, 'netuser.bat'), 'w') as OPATH:
        OPATH.writelines([txtbox.get(1.0, END)])
    s.set("Batch file saved to desktop")


def clrentry_btn():
    global s
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')
    entry3.delete(0, 'end')
    entry4.delete(0, 'end')
    entry5.delete(0, 'end')
    entry6.delete(0, 'end')
    entry7.delete(0, 'end')
    entry8.delete(0, 'end')
    entry9.delete(0, 'end')
    entry10.delete(0, 'end')
    entry11.delete(0, 'end')
    entry12.delete(0, 'end')
    entry13.delete(0, 'end')
    entry14.delete(0, 'end')
    entry15.delete(0, 'end')
    entry16.delete(0, 'end')
    entry17.delete(0, 'end')
    entry18.delete(0, 'end')
    entry19.delete(0, 'end')
    entry20.delete(0, 'end')
    s.set("Entries cleared")


def clrall_btn():
    global s
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')
    entry3.delete(0, 'end')
    entry4.delete(0, 'end')
    entry5.delete(0, 'end')
    entry6.delete(0, 'end')
    entry7.delete(0, 'end')
    entry8.delete(0, 'end')
    entry9.delete(0, 'end')
    entry10.delete(0, 'end')
    entry11.delete(0, 'end')
    entry12.delete(0, 'end')
    entry13.delete(0, 'end')
    entry14.delete(0, 'end')
    entry15.delete(0, 'end')
    entry16.delete(0, 'end')
    entry17.delete(0, 'end')
    entry18.delete(0, 'end')
    entry19.delete(0, 'end')
    entry20.delete(0, 'end')
    txtbox.delete(1.0, END)
    s.set("All cleared")


def close_btn():
    window.quit()


def resetstatus():
    global s
    s.set("Ready")


user1 = Label(top_frame, text = "User 1", relief = "ridge").grid(row = 0, column = 0, ipadx = 10)
user2 = Label(top_frame, text = "User 2", relief = "ridge").grid(row = 1, column = 0, ipadx = 10)
user3 = Label(top_frame, text = "User 3", relief = "ridge").grid(row = 2, column = 0, ipadx = 10)
user4 = Label(top_frame, text = "User 4", relief = "ridge").grid(row = 3, column = 0, ipadx = 10)
user5 = Label(top_frame, text = "User 5", relief = "ridge").grid(row = 4, column = 0, ipadx = 10)
user6 = Label(top_frame, text = "User 6", relief = "ridge").grid(row = 5, column = 0, ipadx = 10)
user7 = Label(top_frame, text = "User 7", relief = "ridge").grid(row = 6, column = 0, ipadx = 10)
user8 = Label(top_frame, text = "User 8", relief = "ridge").grid(row = 7, column = 0, ipadx = 10)
user9 = Label(top_frame, text = "User 9", relief = "ridge").grid(row = 8, column = 0, ipadx = 10)
user10 = Label(top_frame, text = "User 10", relief = "ridge").grid(row = 9, column = 0, ipadx = 7)
user11 = Label(top_frame, text = "User 11", relief = "ridge").grid(row = 0, column = 2, ipadx = 10)
user12 = Label(top_frame, text = "User 12", relief = "ridge").grid(row = 1, column = 2, ipadx = 10)
user13 = Label(top_frame, text = "User 13", relief = "ridge").grid(row = 2, column = 2, ipadx = 10)
user14 = Label(top_frame, text = "User 14", relief = "ridge").grid(row = 3, column = 2, ipadx = 10)
user15 = Label(top_frame, text = "User 15", relief = "ridge").grid(row = 4, column = 2, ipadx = 10)
user16 = Label(top_frame, text = "User 16", relief = "ridge").grid(row = 5, column = 2, ipadx = 10)
user17 = Label(top_frame, text = "User 17", relief = "ridge").grid(row = 6, column = 2, ipadx = 10)
user18 = Label(top_frame, text = "User 18", relief = "ridge").grid(row = 7, column = 2, ipadx = 10)
user19 = Label(top_frame, text = "User 19", relief = "ridge").grid(row = 8, column = 2, ipadx = 10)
user20 = Label(top_frame, text = "User 20", relief = "ridge").grid(row = 9, column = 2, ipadx = 10)

entry1 = Entry(top_frame, width = 50, textvariable = n1)
entry1.grid(row = 0, column = 1, padx = 4)
entry2 = Entry(top_frame, width = 50, textvariable = n2)
entry2.grid(row = 1, column = 1)
entry3 = Entry(top_frame, width = 50, textvariable = n3)
entry3.grid(row = 2, column = 1)
entry4 = Entry(top_frame, width = 50, textvariable = n4)
entry4.grid(row = 3, column = 1)
entry5 = Entry(top_frame, width = 50, textvariable = n5)
entry5.grid(row = 4, column = 1)
entry6 = Entry(top_frame, width = 50, textvariable = n6)
entry6.grid(row = 5, column = 1)
entry7 = Entry(top_frame, width = 50, textvariable = n7)
entry7.grid(row = 6, column = 1)
entry8 = Entry(top_frame, width = 50, textvariable = n8)
entry8.grid(row = 7, column = 1)
entry9 = Entry(top_frame, width = 50, textvariable = n9)
entry9.grid(row = 8, column = 1)
entry10 = Entry(top_frame, width = 50, textvariable = n10)
entry10.grid(row = 9, column = 1)
entry11 = Entry(top_frame, width = 50, textvariable = n11)
entry11.grid(row = 0, column = 4, padx = 4)
entry12 = Entry(top_frame, width = 50, textvariable = n12)
entry12.grid(row = 1, column = 4)
entry13 = Entry(top_frame, width = 50, textvariable = n13)
entry13.grid(row = 2, column = 4)
entry14 = Entry(top_frame, width = 50, textvariable = n14)
entry14.grid(row = 3, column = 4)
entry15 = Entry(top_frame, width = 50, textvariable = n15)
entry15.grid(row = 4, column = 4)
entry16 = Entry(top_frame, width = 50, textvariable = n16)
entry16.grid(row = 5, column = 4)
entry17 = Entry(top_frame, width = 50, textvariable = n17)
entry17.grid(row = 6, column = 4)
entry18 = Entry(top_frame, width = 50, textvariable = n18)
entry18.grid(row = 7, column = 4)
entry19 = Entry(top_frame, width = 50, textvariable = n19)
entry19.grid(row = 8, column = 4)
entry20 = Entry(top_frame, width = 50, textvariable = n20)
entry20.grid(row = 9, column = 4)

txtbox = Text(text_frame)
txtbox.pack(expand = True, pady = 15)

submitbtn = Button(topbtn_frame, width = 14, text = "Submit", command = submit_btn)
submitbtn.pack(side = LEFT, padx = 5, pady = 5)
copybtn = Button(topbtn_frame, width = 14, text = "Copy to Clipboard", command = copy_btn)
copybtn.pack(side = LEFT, padx = 5, pady = 5)
impbtn = Button(topbtn_frame, width = 14, text = "Import", command = imp_btn)
impbtn.pack(side = LEFT, padx = 5, pady = 5)
expbtn = Button(topbtn_frame, width = 14, text = "Export", command = exp_btn)
expbtn.pack(side = LEFT, padx = 5, pady = 5)
clrentrybtn = Button(btmbtn_frame, width = 14, text = "Clear Entries", command = clrentry_btn)
clrentrybtn.pack(side = LEFT, padx = 5, pady = 5)
clrallbtn = Button(btmbtn_frame, width = 14, text = "Clear All", command = clrall_btn)
clrallbtn.pack(side = LEFT, padx = 5, pady = 5)
closebtn = Button(btmbtn_frame, width = 14, text = "Close", command = close_btn)
closebtn.pack(side = LEFT, padx = 5, pady = 5)

stat1 = Label(status_frame, textvariable = s)
stat1.pack(side = LEFT, pady = 5, padx = 5)


mainloop()
