from tkinter import *
import backend

def get_selected_row(event):
    global selected_tuple
    index = listb.curselection()[0]
    selected_tuple = listb.get(index)

    ent1.delete(0, END)
    ent1.insert(END, selected_tuple[1])

    ent2.delete(0, END)
    ent2.insert(END, selected_tuple[2])

    ent3.delete(0, END)
    ent3.insert(END, selected_tuple[3])

    ent4.delete(0, END)
    ent4.insert(END, selected_tuple[4])


def add_command():
    backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    listb.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))


def view_command():
    listb.delete(0, END)
    for row in backend.view():
        listb.insert(END, row)


def search_command():
    listb.delete(0, END)
    for row in backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        listb.insert(END, row)

def update_command():
    backend.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())


def delete_command():
    backend.delete(selected_tuple[0])



window = Tk()
window.wm_title("Book Store Management")

l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

l2 = Label(window, text="Author")
l2.grid(row=0, column=2)

l3 = Label(window, text="Year")
l3.grid(row=1, column=0)

l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)

title_text = StringVar()
ent1 = Entry(window, textvariable = title_text)
ent1.grid(row=0, column=1)

author_text = StringVar()
ent2 = Entry(window, textvariable = author_text)
ent2.grid(row=0, column=3)

year_text = StringVar()
ent3 = Entry(window, textvariable = year_text)
ent3.grid(row=1, column=1)

isbn_text = StringVar()
ent4 = Entry(window, textvariable = isbn_text)
ent4.grid(row=1, column=3)

listb = Listbox(window, height=8, width=40)
listb.grid(row=2, column=0, rowspan=8, columnspan=2)

sb = Scrollbar(window)
sb.grid(row=2, column=2, rowspan=6)

listb.configure(yscrollcommand=sb.set)
sb.configure(command=listb.yview)

listb.bind('<<ListboxSelect>>',get_selected_row)

b1 = Button(window, text="View All", width=12, command=view_command)
b1.grid(row=2, column=3)

b2 = Button(window, text="Search", width=12, command=search_command)
b2.grid(row=3, column=3)

b3 = Button(window, text="Add", width=12, command=add_command)
b3.grid(row=4, column=3)

b4 = Button(window, text="Update", width=12, command=update_command)
b4.grid(row=5, column=3)

b5 = Button(window, text="Delete", width=12, command=delete_command)
b5.grid(row=6, column=3)

b6 = Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=7, column=3)



window.mainloop()

