"""
Farhan Javed
farhan.javed47@gmail.com
12/9/2019
Working with Databases in Python. Basic SQL operations
"""
import sqlite3


def main():
    print('connect')
    db = sqlite3.connect('db-api.db')
    cur = db.cursor()
    print('create')
    cur.execute("DROP TABLE IF EXISTS test")
    cur.execute("""
        CREATE TABLE test (id INTEGER PRIMARY KEY, string TEXT, number INTEGER
        )
    """)
    print("inset row")
    cur.execute("""
        INSERT INTO test (string, number) VALUES ('one',1)
    """)
    print("inset row")
    cur.execute("""
        INSERT INTO test (string, number) VALUES ('two',2)
    """)
    print("inset row")
    cur.execute("""
        INSERT INTO test (string, number) VALUES ('three',3)
    """)
    print("inset row")
    cur.execute("""
        INSERT INTO test (string, number) VALUES ('four',4)
    """)
    print("inset row")
    cur.execute("""
        INSERT INTO test (string, number) VALUES ('five',5)
    """)
    print('commit')
    db.commit()
    print('count')
    cur.execute("SELECT COUNT(*) FROM test")
    count = cur.fetchone()[0]
    print(f'there are {count} rows in the table.')
    print('read')
    for row in cur.execute("SELECT * FROM test"):
        print(row)
    print('drop')
    cur.execute("DROP TABLE test")
    print('close')
    db.close()


if __name__ == '__main__': main()