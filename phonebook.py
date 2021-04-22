import sqlite3

conn = sqlite3.connect('phonebook.db')
c = conn.cursor()

try:
    c.execute("""CREATE TABLE phonebook (
            name text, number integer
        )""")
except:
    book = {}
    while True:
        print("What would you like to do?")
        print("    1 - Add an entry")
        print("    2 - Modify an entry")
        print("    3 - Delete an entry")
        print("    4 - Save entries to file")
        print("    5 - Clear database")
        print("    6 - Exit")
        choice = input("Enter an option: ")

        if choice == '1':
            name = input('Name: ')
            number = int(input('Telephone Number: '))
            book[name] = number
            c.execute("INSERT INTO phonebook VALUES (?, ?)", (name, number))
            conn.commit()

        elif choice == '2':
            print("What would you like to do?")
            print("    1 - Change name")
            print("    2 - Change number")
            choice2 = int(input("Enter your choice: "))
            if choice2 == 1:
                newname = input('Name: ')
                book[newname] = book[name]
                del book[name]
                c.execute("""UPDATE phonebook SET name = ?
                                WHERE number = ?
                    """, (newname, number))
                conn.commit()
            elif choice2 == 2:
                replacename = input('Name: ')
                newnumber = input('Number: ')
                book[name] = newnumber
                for name in book:
                    try:
                        if replacename not in book:
                            continue
                    except:
                        c.execute("""UPDATE phonebook SET number = ?
                                        WHERE name = ?
                            """, (newnumber, replacename))
                        conn.commit()

        elif choice == '3':
            name = input('Name: ')
            #number = input('Number: ')
            try:
                del book[name]
                if name not in book:
                    continue
            except:
                c.execute("""DELETE from phonebook where name is ?""", (name,))
                conn.commit()

        elif choice == '4':
            fn = '/home/shreyas/Downloads/contacts.txt'

            f = open(fn, "w")

            for name in book.keys():
                f.write(name + " : " + book[name] + "\n")
            f.close()

        elif choice == '5':
            c.execute("DELETE FROM phonebook")
            conn.commit()
        
        elif choice == '6':
            break
        
        else:
            print('Invalid option.')

    conn.close()
