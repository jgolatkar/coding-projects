#!/usr/bin/env python3

import tkinter.messagebox
from tkinter import *
import backend


def view_command():
	listbox.delete(0,END)
	for row in backend.view():
		listbox.insert(END,row)

def search_command():
	listbox.delete(0,END)
	for row in backend.search(title_value.get(),author_value.get(),year_value.get(),isbn_value.get()):
		listbox.insert(END,row)

def add_command():
	listbox.delete(0,END)
	backend.insert(title_value.get(),author_value.get(),year_value.get(),isbn_value.get())
	try:
		tkinter.messagebox.showinfo("Book Added!!", "Title: {} Author: {} Year: {} ISBN: {}".format(title_value.get(),author_value.get(),year_value.get(),isbn_value.get()))
	except IndexError:
		pass

def get_selected_row(event):
	global row_tuple
	if len(listbox.curselection()) > 0:
		index = listbox.curselection()[0]
		row_tuple = listbox.get(index)
		title.delete(0,END)
		title.insert(END,row_tuple[1])
		author.delete(0,END)
		author.insert(END,row_tuple[2])
		year.delete(0,END)
		year.insert(END,row_tuple[3])
		isbn.delete(0,END)
		isbn.insert(END,row_tuple[4])
		
def delete_command():
	backend.delete(row_tuple[0])
	view_command()

def update_command():	
	backend.update(row_tuple[0],title_value.get(),author_value.get(),year_value.get(),isbn_value.get())
	view_command()

def close_command():
	backend.get_conn().close()
	window.destroy()

window = Tk()
window.title("Bookstore")
title_label = Label(window,text="Title")
title_label.grid(row=0,column=0)

title_value = StringVar()
title = Entry(window,textvariable=title_value)
title.grid(row=0,column=1)

author_label = Label(window,text="Author")
author_label.grid(row=0,column=2)

author_value = StringVar()
author = Entry(window,textvariable=author_value)
author.grid(row=0,column=3)

year_label = Label(window,text="Year")
year_label.grid(row=1,column=0)

year_value = StringVar()
year = Entry(window,textvariable=year_value)
year.grid(row=1,column=1)

isbn_label = Label(window,text="ISBN")
isbn_label.grid(row=1,column=2)

isbn_value = StringVar()
isbn = Entry(window,textvariable=isbn_value)
isbn.grid(row=1,column=3)


listbox = Listbox(window, height=8, width=40)
listbox.grid(row=2,column=0,rowspan=6,columnspan=2)

sb = Scrollbar(window)
sb.grid(row=2,column=2,rowspan=6)

listbox.configure(yscrollcommand=sb.set)
sb.configure(command=listbox.yview)

listbox.bind('<<ListboxSelect>>',get_selected_row)

btn1 = Button(window,text="View All", width=12, command=view_command)
btn1.grid(row=2,column=3)

btn2 = Button(window,text="Search Entry", width=12, command=search_command)
btn2.grid(row=3,column=3)

btn3 = Button(window,text="Add Entry", width=12, command=add_command)
btn3.grid(row=4,column=3)

btn4 = Button(window,text="Update", width=12, command=update_command)
btn4.grid(row=5,column=3)

btn5 = Button(window,text="Delete", width=12, command=delete_command)
btn5.grid(row=6,column=3)

btn6 = Button(window,text="Close", width=12, command=close_command)
btn6.grid(row=7,column=3)

window.mainloop()
