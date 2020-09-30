from tkinter import*
import sqlite3

root = Tk()
root.title('testing 123')
root.iconbitmap('myicon.ico')
root.geometry('280x600')
root.resizable(width = False, height = False)
root.configure(bg = '#272822')


conn = sqlite3.connect('address_book2.db')

c = conn.cursor()
'''
c.execute("""CREATE TABLE addresses1(

            first_name text,
            last_name text,
            phone integer,
            address text,
            city text,
            state text,
            zipcode integer
    )""")
'''
'''
def allclear():

    f_name_up.delete(0, END)
    l_name_up.delete(0, END)
    phone_up.delete(0, END)
    address_up.delete(0, END)
    city_up.delete(0, END)
    state_up.delete(0, END)
    zipcode_up.delete(0, END)

    select_id.delete(0, END)
'''

def update():
    conn = sqlite3.connect('address_book2.db')

    c = conn.cursor()    

    c.execute("""UPDATE addresses1 SET
        first_name = :first,
        last_name = :last,
        phone = :phone,
        address = :address,
        city = :city,
        state = :state,
        zipcode = :zipcode

        WHERE oid = :oid""",
    {
        'first' : f_name_up.get(),
        'last' : l_name_up.get(),
        'phone' : phone_up.get(),
        'address' : address_up.get(),
        'city' : city_up.get(),
        'state' : state_up.get(),
        'zipcode' : zipcode_up.get(),

        'oid' : record_id
    })
    

    conn.commit()

    conn.close()


def edit():
    global record_id
    conn = sqlite3.connect('address_book2.db')

    c = conn.cursor()

    record_id = select_id.get()
    c.execute("SELECT * FROM addresses1 WHERE oid =" + record_id)
    records = c.fetchall()
    global f_name_up
    global l_name_up
    global phone_up
    global address_up
    global city_up
    global state_up
    global zipcode_up

    f_name_up = Entry(root, width = 30, bg = '#654321', fg = '#ffffff')
    f_name_up.grid(row = 0, column = 1, pady = (10,0))
    l_name_up = Entry(root, width = 30, bg = '#654321', fg = '#ffffff')
    l_name_up.grid(row = 1, column = 1)
    phone_up = Entry(root, width = 30, bg = '#654321', fg = '#ffffff')
    phone_up.grid(row = 2, column = 1)
    address_up = Entry(root, width = 30, bg = '#654321', fg = '#ffffff')
    address_up.grid(row = 3, column = 1)
    city_up = Entry(root, width = 30, bg = '#654321', fg = '#ffffff')
    city_up.grid(row = 4, column = 1)
    state_up = Entry(root, width = 30, bg = '#654321', fg = '#ffffff')
    state_up.grid(row = 5, column = 1)
    zipcode_up = Entry(root, width = 30, bg = '#654321', fg = '#ffffff')
    zipcode_up.grid(row = 6, column = 1)

    for record in records:
        f_name_up.insert(0, record[0])
        l_name_up.insert(0, record[1])
        phone_up.insert(0, record[2])
        address_up.insert(0, record[3])
        city_up.insert(0, record[4])
        state_up.insert(0, record[5])
        zipcode_up.insert(0, record[6])




def show():

    global show_label
    conn = sqlite3.connect('address_book2.db')

    c = conn.cursor()

    c.execute("SELECT *,oid FROM addresses1")
    records = c.fetchall()

    show_records = ''

    for record in records:
        show_records += str(record[0]) + " " + str(record[1]) + " " + " " + str(record[7]) + "\n"

    show_label = Label(root, text = show_records)
    show_label.grid(row = 13, column = 0, columnspan = 2)
    show_label.configure(bg = '#272822', fg = '#ffffff')
    show_label.after(15000, show_label.destroy)

    conn.commit()

    conn.close()

def submit():

    conn = sqlite3.connect('address_book2.db')

    c = conn.cursor()


    c.execute("INSERT INTO addresses1 VALUES(:f_name, :l_name, :phone, :address, :city, :state, :zipcode)",
    {
        'f_name' : f_name.get(),
        'l_name' : l_name.get(),
        'phone' : phone.get(),
        'address' : address.get(),
        'city' : city.get(),
        'state' : state.get(),
        'zipcode' : zipcode.get()
    }
    )


    f_name.delete(0, END)
    l_name.delete(0, END)
    phone.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

    conn.commit()

    conn.close()


def dele():

    conn = sqlite3.connect('address_book2.db')

    c = conn.cursor()

    c.execute("DELETE FROM addresses1 WHERE oid ="+ select_id.get())

    conn.commit()

    conn.close()

def main():

    conn = sqlite3.connect('address_book2.db')

    c = conn.cursor()

    global f_name_label
    global l_name_label
    global phone_label
    global address_label
    global city_label
    global state_label
    global zipcode_label

    global f_name
    global l_name
    global phone
    global address
    global city
    global state
    global zipcode

    global select_label
    global select_id

    global show_button
    global save_button
    global delete_button
    global edit_button


    f_name_label = Label(root, text = 'First Name')
    f_name_label.grid(row = 0, column = 0, padx = 10, pady = (10,0))
    l_name_label = Label(root, text = 'Last Name')
    l_name_label.grid(row = 1, column = 0)
    phone_label = Label(root, text = 'Phone')
    phone_label.grid(row = 2, column = 0)
    address_label = Label(root, text = 'Address')
    address_label.grid(row = 3, column = 0)
    city_label = Label(root, text = 'City')
    city_label.grid(row = 4, column = 0)
    state_label = Label(root, text = 'State')
    state_label.grid(row = 5, column = 0)
    zipcode_label = Label(root, text = 'Zipcode')
    zipcode_label.grid(row = 6, column = 0)


    f_name_label.configure(bg = '#272822', fg = '#ffffff')
    l_name_label.configure(bg = '#272822', fg = '#ffffff')
    phone_label.configure(bg = '#272822', fg = '#ffffff')
    address_label.configure(bg = '#272822', fg = '#ffffff')
    state_label.configure(bg = '#272822', fg = '#ffffff')
    city_label.configure(bg = '#272822', fg = '#ffffff')
    zipcode_label.configure(bg = '#272822', fg = '#ffffff')
    

    f_name = Entry(root, width = 30, bg = '#654321', fg = '#ffffff')
    f_name.grid(row = 0, column = 1, pady = (10,0))
    l_name = Entry(root, width = 30, bg = '#654321', fg = '#ffffff')
    l_name.grid(row = 1, column = 1)
    phone = Entry(root, width = 30, bg = '#654321', fg = '#ffffff')
    phone.grid(row = 2, column = 1)
    address = Entry(root, width = 30, bg = '#654321', fg = '#ffffff')
    address.grid(row = 3, column = 1)
    city = Entry(root, width = 30, bg = '#654321', fg = '#ffffff')
    city.grid(row = 4, column = 1)
    state = Entry(root, width = 30, bg = '#654321', fg = '#ffffff')
    state.grid(row = 5, column = 1)
    zipcode = Entry(root, width = 30, bg = '#654321', fg = '#ffffff')
    zipcode.grid(row = 6, column = 1)

    select_label = Label(root, text = 'Select ID')
    select_label.grid(row = 7, column = 0, pady = (10,0))

    select_label.configure(bg = '#272822', fg = '#ffffff')

    select_id = Entry(root, width = 30, bg = '#654321', fg = '#ffffff')
    select_id.grid(row = 7, column = 1, pady = (10,0))


    conn.commit()

    conn.close()
    

save_button = Button(root, text = 'Submit', command = submit, padx = 105, bg = '#291703', fg = '#ffffff')
save_button.grid(row= 8, column = 0, columnspan = 2, padx = (10,0),pady = (10,2))

show_button = Button(root, text = 'View Records', padx = 89.49, command = show, bg = '#291703', fg = '#ffffff')
show_button.grid(row= 9, column = 0, columnspan = 2, padx = (10,0))


delete_button = Button(root, text = 'Delete ID', padx = 101.49, command = dele, bg = 'brown')
delete_button.grid(row = 10, column= 0, columnspan = 2, padx = (10.5,1), pady = 2)


edit_button = Button(root, text = 'Edit ID', padx = 107.5, command = edit, bg = '#291703', fg = '#ffffff')
edit_button.grid(row = 11, column = 0, columnspan = 2, padx = (10,0))

allclear_button = Button(root, text = 'Clear all', command = main, bg = '#291703', fg = '#ffffff')
allclear_button.grid(row = 12, column = 0, sticky = E, padx = (0,21), pady = 5)

update_button = Button(root, text = 'update',command = update, bg = '#291703', fg = '#ffffff')
update_button.grid(row= 12, column = 1, stick = E, pady = 5)

main()

conn.commit()

conn.close()

root.mainloop()