import sqlite3
import pandas as pd

def create_db():
    conn = sqlite3.connect('sales.db')
    c = conn.cursor()
    
    c.execute('''
        CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            product TEXT,
            quantity INTEGER,
            price INTEGER
        )
    ''')

    df = pd.read_csv('sales_data.csv')
    df.to_sql('sales', conn, if_exists='replace', index=False)
    
    conn.commit()
    conn.close()
