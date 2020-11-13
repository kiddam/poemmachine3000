# poemmachine3000
specs:
- django framework
- sqlite3 database

This program takes on a Django framework powered by a Python3 backend. A SQLite3 database acts as a "notebook," retaining all lines of poetry. The program has three primary functions: (1) generate poem, (2) write a new line, (3) view notebook.

To generate a poem, the application requests that the user input three alphabetical characters. The application, then, searches the database for lines beginning with each letter, respectively. Of the possibly numerous lines found, the application returns one at random. The resulting outcome should be three lines of poetry, corresponding to each user-provided letter, respectively.

​

Application users can write new lines to the database. Users can do so as Anonymous guests, or they may sign up and have their screenname displayed beside all of their entries in the global notebook.

​

Notebook view gives a list of all entries in the order they were submitted. It shows the entries as being written by Anonymous or a specific user.


