# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 14:28:19 2016

@author: Anupam Srivastava
"""

import json
import sqlite3

def com(conn, i):
    print 'Committing...', i
    conn.commit()
    
conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

# Do some setup
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

fname = raw_input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'roster_data.json'

str_data = open(fname).read()
json_data = json.loads(str_data)

i = 0
for entry in json_data:
    name = entry[0];
    title = entry[1];
    role = entry[2];

    cur.execute('''INSERT OR IGNORE INTO User (name) VALUES ( ? )''',
                ( name, ) )
    cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course (title) VALUES ( ? )''',
                ( title, ) )
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member (user_id, course_id, role)
                VALUES ( ?, ?, ? )''', ( user_id, course_id, role ) )

    # Commit every 5 entries <- totally arbitrary number
    i += 1
    if i % 10 == 0:
        com(conn, i)

# Commit remaining and close connection to db
com(conn, i)
cur.close()
