from tkinter import *
import tkinter.ttk as ttk

def on_keyrelease(event):
    # get text from entry
    value = event.widget.get()
    value = value.strip().lower()

    # get data from list
    if value == '':
        data = colors
    else:
        data = []
        for item in colors:
            if value in item.lower():
                data.append(item)

    # update data in listbox
    listbox_update(data)

    if data:
        listbox.selection_clear(0, 'end')
        index = colors.index(data[0])
        listbox.selection_set(index)
        # highlight the characters on the selected line
        listbox.activate(index)
        listbox.selection_anchor(index)
        listbox.see(index)

def listbox_update(data):
    # delete previous data
    listbox.delete(0, 'end')

    # sorting data
    data = sorted(data, key=str.lower)

    # put new data
    for item in data:
        listbox.insert('end', item)

    # configure the font for all items in the listbox
    for i in range(listbox.size()):
        listbox.itemconfig(i, font=('Helvetica', 12))

root = Tk()

# create a list of colors for autocompletion
colors = ['Red', 'Blue', 'Green', 'Yellow', 'Orange', 'Purple']

# create an entry widget
entry = Entry(root)
entry.pack()

# create a listbox widget
listbox = Listbox(root, font=('Helvetica', 12)) # default font size is 12
listbox.pack()

# update listbox with initial data
listbox_update(colors)

# link listbox to entry widget
entry.bind('<KeyRelease>', on_keyrelease)

# change font size and highlight focused line
def on_focusin(event):
    for i in listbox.curselection():
        listbox.itemconfig(i, font=('Helvetica', 14, 'bold'))

# restore font size and clear focus highlight
def on_focusout(event):
    for i in listbox.curselection():
        listbox.itemconfig(i, font=('Helvetica', 12, 'normal'))

# bind focus events to functions
listbox.bind('<FocusIn>', on_focusin)
listbox.bind('<FocusOut>', on_focusout)

root.mainloop()
