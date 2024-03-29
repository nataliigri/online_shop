#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import sqlite3

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

    # Connecting to sqlite
    conn= sqlite3.connect('db.sqlite3')
    
    # create cursor
    c = conn.cursor()
    c.execute("INSERT INTO store_category VALUES ('11','Аксесуари','healthcare')")
   
    
    # Display data inserted
    print("Data Inserted in the table: ")
    data=c.execute('''SELECT * FROM store_category''')
    for row in data:
        print(row)
    
    # Commit your changes in the database    
    conn.commit()
    
    # Closing the connection
    conn.close()

if __name__ == '__main__':
    main()
