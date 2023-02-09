### Imports
from tkinter import *
import firebase_admin
from firebase_admin import credentials, firestore

### Functions

# Creating a 'refresh' button
def refresh():
    chat_box.config(state=NORMAL)
    chat_box.delete("1.0", "end")
    for message in chat_ref.order_by(u'date', direction=firestore.Query.ASCENDING).stream():
        info = message.to_dict()
        author = info['author']
        content = info['content']
        chat_box.insert(END, f"{author}: {content}\n")
   
    chat_box.config(state=DISABLED)


# Creating a 'on_message' function that executes when clicked on SEND
def on_message():
    pseudo = username_var.get()
    msg = write_message_box.get()

    if len(msg) > 0: # if the message input is not empty
        chat_box.config(state=NORMAL)
        chat_box.insert(END, f"{pseudo}: {msg}\n") # insert 'PSEUDO: MESSAGE' when sent + line break for each new message
        write_message_box.delete(0, END) # clear the message input field when message gets send
        chat_box.config(state=DISABLED)

        # Adding the message do the DB
        chat_ref = db.collection(u'Messages')
        chat_ref.add({
            u'author': pseudo,
            u'content': msg,
            u'date': firestore.SERVER_TIMESTAMP
        })


### DB connection

# Connect to firebase with credentials
cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred)

# Creating a connection to a database
db = firestore.client()


### GUI

# Creating a window
root = Tk()
root.title("Pyscord")
root.minsize(600, 500)


# Creating an empty text zone
chat_box = Text(
    root,
    bg='#424549', 
    fg='white'
)
chat_ref = db.collection(u'Messages')

for message in chat_ref.order_by(u'date', direction=firestore.Query.ASCENDING).stream():
    info = message.to_dict()
    author = info['author']
    content = info['content']
    chat_box.insert(END, f"{author}: {content}\n")
    
chat_box.config(state=DISABLED)
chat_box.pack()


# Creating pseudo zone
username_var = StringVar()
username_var.set('User1')
username_box = Entry(root, textvariable=username_var)
username_box.pack()


# Create message box
write_message_box = Entry(root)
write_message_box.pack()


# Creating send button
submit_message_button = Button(
    root, 
    text='Send',
    command=on_message,

    # Styling
    bg='#7289da',
    fg='white',
    padx='10',
    pady='5'
)
submit_message_button.pack()


# Creating refresh button
refresh_button = Button(
    root,
    command=refresh,
    text='Refresh'
)
refresh_button.pack()


root.mainloop()

