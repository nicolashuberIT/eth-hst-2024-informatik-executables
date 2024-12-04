#########################
# Wie in C4 gezeigt
#########################

import sqlite3

con = sqlite3.connect('example.db', isolation_level=None)   # Datenbankdatei aufrufen
cur = con.cursor()                                          # Cursor-Objekt erstellen
cur.execute('SELECT * FROM employees;')                     # SQL-Abfrage ausführen

# Möglichkeit 1: Zeile ausgeben
print(f"First Employee: {cur.fetchone()}")                  # >>> First Employee: (1, Alice, Manager, 75000.00, 2)

# Möglichkeit 2: Alle Zeilen ausgeben
for row in cur.fetchall():                                  # Alle  Zeilen ausgeben
    print(row)                                              # >>> (1, Alice, Manager, 75000.00, 2)
                                                            # >>> (2, Bob, Entwickler, 60000.00, 2)
