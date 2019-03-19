'''
A program which d'store the following book information:
Title
Author
Year
ISBN

User can:
View all records
Search for an entry
Add an entry
Update an entry
Delete an entry
Close program
'''


from tkinter import *
import backend      # custom script


def get_selected_row(event):     # NB event parameter, for booklist
    try:
        global selected_row_tuple       # make available outside function - no need to use this function if no event
        print(books_list.curselection())
        # if books_list.size() == 0:
        #     return
        index = books_list.curselection()[0]    # get 1st part of <<ListboxSelect>> tuple (i.e. the index)
        selected_row_tuple = books_list.get(index)
        # print(index)              # diagnostic
        # print(selected_row_tuple)       # diagnostic

        title_entry.delete(0, END)      # display selected book's details in entry boxes
        title_entry.insert(END, selected_row_tuple[1])
        author_entry.delete(0, END)
        author_entry.insert(END, selected_row_tuple[2])
        year_entry.delete(0, END)
        year_entry.insert(END, selected_row_tuple[3])
        isbn_entry.delete(0, END)
        isbn_entry.insert(END, selected_row_tuple[4])
    except IndexError:
        pass


def view_command():
    books_list.delete(0, END)            # clear list box
    for row in backend.view():
        books_list.insert(END, row)      # iterate over tuples in results and appEND to list


def search_command():
    books_list.delete(0, END)            # clear list box
    for row in backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        books_list.insert(END, row)


def add_command():
    backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    books_list.delete(0, END)
    books_list.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))

def delete_command():
    backend.delete(selected_row_tuple[0])   # get first (only?) element of selected row's tuple

def update_command():
    # backend.update(selected_row_tuple[0], selected_row_tuple[1], selected_row_tuple[2],
    #                selected_row_tuple[3], selected_row_tuple[4])
    backend.update(selected_row_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())

window = Tk()


window.wm_title = "Book Catalogue"

label1 = Label(window, text="Title")
label1.grid(row=0, column=0)

label1 = Label(window, text="Author")
label1.grid(row=0, column=2)

label1 = Label(window, text="Year")
label1.grid(row=1, column=0)

label1 = Label(window, text="ISBN")
label1.grid(row=1, column=2)

# NB zero-indexed grid

title_text = StringVar()        # NB type StringVar - http://effbot.org/tkinterbook/variable.htm Tkinter type
title_entry = Entry(window, textvariable=title_text)
title_entry.grid(row=0, column=1)

author_text = StringVar()        # NB type StringVar - http://effbot.org/tkinterbook/variable.htm Tkinter type
author_entry = Entry(window, textvariable=author_text)
author_entry.grid(row=0, column=3)

year_text = StringVar()        # NB type StringVar - http://effbot.org/tkinterbook/variable.htm Tkinter type
year_entry = Entry(window, textvariable=year_text)
year_entry.grid(row=1, column=1)

isbn_text = StringVar()        # NB type StringVar - http://effbot.org/tkinterbook/variable.htm Tkinter type
isbn_entry = Entry(window, textvariable=isbn_text)
isbn_entry.grid(row=1, column=3)

books_list = Listbox(window, height=6, width=35)
books_list.grid(row=2, column=0, rowspan=6, columnspan=2)       # NB rowspan, columnspan

books_list.bind('<<ListboxSelect>>', get_selected_row)

book_list_scroll = Scrollbar(window)
book_list_scroll.grid(row=1, column=2, rowspan=6)

books_list.configure(yscrollcommand=book_list_scroll.set)       # allow scroll bar to control list box
book_list_scroll.configure(command=books_list.yview)            # scrollbar to vertically scroll book list contents

view_all_button = Button(window, text="View all", width=12, command=view_command)   # no brackets, and for some reason not backend.view
# view_all_button = Button(window, text="View all", width=12, command=backend.view)   # no brackets, and for some reason not backend.view
view_all_button.grid(row=2, column=3)

search_entry_button = Button(window, text="Search entry", width=12, command=search_command)
search_entry_button.grid(row=3, column=3)

add_entry_button = Button(window, text="Add entry", width=12, command=add_command)
add_entry_button.grid(row=4, column=3)

update_button = Button(window, text="Update", width=12, command=update_command)
update_button.grid(row=5, column=3)

delete_button = Button(window, text="Delete", width=12, command=delete_command)
delete_button.grid(row=6, column=3)

close_button = Button(window, text="Close", width=12, command=window.destroy)
close_button.grid(row=7, column=3)

# TODO: case-insensitive search

window.mainloop()