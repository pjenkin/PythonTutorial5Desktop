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

window = Tk()

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

book_list_scroll = Scrollbar(window)
book_list_scroll.grid(row=1, column=2, rowspan=6)

books_list.configure(yscrollcommand=book_list_scroll.set)       # allow scroll bar to control list box
book_list_scroll.configure(command=books_list.yview)            # scrollbar to vertically scroll book list contents

view_all_button = Button(window, text="View all", width=12)
view_all_button.grid(row=2, column=3)

search_entry_button = Button(window, text="Search entry", width=12)
search_entry_button.grid(row=3, column=3)

add_entry_button = Button(window, text="Add entry", width=12)
add_entry_button.grid(row=4, column=3)

update_button = Button(window, text="Update", width=12)
update_button.grid(row=5, column=3)

delete_button = Button(window, text="Delete", width=12)
delete_button.grid(row=6, column=3)

close_button = Button(window, text="Close", width=12)
close_button.grid(row=7, column=3)


window.mainloop()