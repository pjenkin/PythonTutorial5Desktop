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
# import backend      # custom script
from backend import Database

database = Database()


class FrontEnd:

    def __init__(self, window):
        print('in constructor')     # diagnostic
        self.window = window
        
        self.window.wm_title = "Book Catalogue"

        label1 = Label(window, text="Title")
        label1.grid(row=0, column=0)

        label1 = Label(window, text="Author")
        label1.grid(row=0, column=2)

        label1 = Label(window, text="Year")
        label1.grid(row=1, column=0)

        label1 = Label(window, text="ISBN")
        label1.grid(row=1, column=2)

        # NB zero-indexed grid

        self.title_text = StringVar()  # NB type StringVar - http://effbot.org/tkinterbook/variable.htm Tkinter type
        self.title_entry = Entry(window, textvariable=self.title_text)
        self.title_entry.grid(row=0, column=1)

        self.author_text = StringVar()  # NB type StringVar - http://effbot.org/tkinterbook/variable.htm Tkinter type
        self.author_entry = Entry(window, textvariable=self.author_text)
        self.author_entry.grid(row=0, column=3)

        self.year_text = StringVar()  # NB type StringVar - http://effbot.org/tkinterbook/variable.htm Tkinter type
        self.year_entry = Entry(window, textvariable=self.year_text)
        self.year_entry.grid(row=1, column=1)

        self.isbn_text = StringVar()  # NB type StringVar - http://effbot.org/tkinterbook/variable.htm Tkinter type
        self.isbn_entry = Entry(window, textvariable=self.isbn_text)
        self.isbn_entry.grid(row=1, column=3)

        self.books_list = Listbox(window, height=6, width=35)
        self.books_list.grid(row=2, column=0, rowspan=6, columnspan=2)  # NB rowspan, columnspan

        self.books_list.bind('<<ListboxSelect>>', self.get_selected_row)

        self.book_list_scroll = Scrollbar(window)
        self.book_list_scroll.grid(row=1, column=2, rowspan=6)

        self.books_list.configure(yscrollcommand=self.book_list_scroll.set)  # allow scroll bar to control list box
        self.book_list_scroll.configure(command=self.books_list.yview)  # scrollbar to vertically scroll book list contents

        view_all_button = Button(window, text="View all", width=12,
                                 command=self.view_command)  # no brackets, and for some reason not database.view
        # view_all_button = Button(window, text="View all", width=12, command=database.view)   # no brackets, and for some reason not database.view
        view_all_button.grid(row=2, column=3)

        search_entry_button = Button(window, text="Search entry", width=12, command=self.search_command)
        search_entry_button.grid(row=3, column=3)

        add_entry_button = Button(window, text="Add entry", width=12, command=self.add_command)
        add_entry_button.grid(row=4, column=3)

        update_button = Button(window, text="Update", width=12, command=self.update_command)
        update_button.grid(row=5, column=3)

        delete_button = Button(window, text="Delete", width=12, command=self.delete_command)
        delete_button.grid(row=6, column=3)

        close_button = Button(window, text="Close", width=12, command=window.destroy)
        close_button.grid(row=7, column=3)

    def get_selected_row(self, event):     # NB event parameter, for booklist
        try:
            global selected_row_tuple       # make available outside function - no need to use this function if no event
            print(self.books_list.curselection())
            # if self.books_list.size() == 0:
            #     return
            index = self.books_list.curselection()[0]    # get 1st part of <<ListboxSelect>> tuple (i.e. the index)
            selected_row_tuple = self.books_list.get(index)
            # print(index)              # diagnostic
            # print(selected_row_tuple)       # diagnostic

            self.title_entry.delete(0, END)      # display selected book's details in entry boxes
            self.title_entry.insert(END, selected_row_tuple[1])
            self.author_entry.delete(0, END)
            self.author_entry.insert(END, selected_row_tuple[2])
            self.year_entry.delete(0, END)
            self.year_entry.insert(END, selected_row_tuple[3])
            self.isbn_entry.delete(0, END)
            self.isbn_entry.insert(END, selected_row_tuple[4])
        except IndexError:
            pass


    def view_command(self):
        self.books_list.delete(0, END)            # clear list box
        for row in database.view():
            self.books_list.insert(END, row)      # iterate over tuples in results and appEND to list


    def search_command(self):
        self.books_list.delete(0, END)            # clear list box
        for row in database.search(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get()):
            self.books_list.insert(END, row)


    def add_command(self):
        database.insert(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get())
        self.books_list.delete(0, END)
        self.books_list.insert(END, (self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get()))

    def delete_command(self):
        database.delete(selected_row_tuple[0])   # get first (only?) element of selected row's tuple

    def update_command(self):
        # database.update(selected_row_tuple[0], selected_row_tuple[1], selected_row_tuple[2],
        #                selected_row_tuple[3], selected_row_tuple[4])
        database.update(selected_row_tuple[0], self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get())


window = Tk()
frontend = FrontEnd(window)



# TODO: case-insensitive search

window.mainloop()