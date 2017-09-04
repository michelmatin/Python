'''
Created on Aug 14, 2017

@author: michel
'''
import sqlite3
conn = sqlite3.connect('orgdb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

file_name = input('Please enter filename: ')
file_handle = open(file_name)

for line in file_handle:
    if not line.startswith('From:'):
        continue
    line = line.rstrip()
    pieces = line.split('@')
    print(pieces)
    org_id = pieces[1]
    print(org_id)

    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org_id,))
    row = cur.fetchone()
    if row is None:
        cur.execute(
            'INSERT INTO Counts (org, count) VALUES (?, 1)', (org_id,))
    else:
        cur.execute(
            'UPDATE Counts SET count = count + 1 WHERE org = ?', (org_id,))
    conn.commit()

cur.execute('SELECT * FROM Counts ORDER BY count DESC')
conn.commit()

#sqlstr = 'SELECT org, count FROM Counts ORDER BY count'
# for row in cur.execute(sqlstr):
#    print(str(row[0]), row[1])

cur.close()
