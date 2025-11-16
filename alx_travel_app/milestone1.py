import sqlite3


conn = sqlite3.connect('pld_database.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS devices (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    type TEXT NOT NULL
)
''')

devices = [
    ('PLD Alpha', 'CPLD'),
    ('PLD Beta', 'FPGA'),
    ('PLD Gamma', 'GAL')
]

cursor.executemany('INSERT INTO devices (name, type) VALUES (?, ?)', devices)
conn.commit()

print("Database and table created successfully with sample devices!")


def fetch_devices():
    for row in cursor.execute("SELECT * FROM devices"):
        yield row

print("\nQuerying devices using generator:")
for device in fetch_devices():
    print(device)

conn.close()
