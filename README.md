# pyscord - Discord like program with Python

Primitive Discord like program created with PYTHON, connected to Firebase database to create a real-time chat.

## Firebase Database
You'll need to create your own *Firebase database* and generate your own `credentials.json` file to connect the program to the database to simulate a real-time chat. Without it, this code won't work.  
In *Firebase* you'll need to create a collection named `Messages` with three fields: *author* (type `string`), *content* (type `string`) and *date* (type `date`). 
Firebase will generate your own `credentials.json` file (though it will probably be named differentely, so either rename it to *credentials.json* or leave it like that, but in that case, you'll need to change the name of it inside `main.py`. 
