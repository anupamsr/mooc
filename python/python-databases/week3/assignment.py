# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 15:07:46 2016

@author: anupam.srivastava
"""

import xml.etree.ElementTree as ET
import sqlite3

def lookup(d, text):
    found = False
    for child in d:
        if found:
            return child.text
        if child.tag == 'key' and child.text == text:
            found = True
    return True

def com(conn):
    print 'Committing...'
    conn.commit()

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

# Make new table
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
)
''')

#fname = raw_input('Enter file name: ')
#if ( len(fname) < 1 ):
#    fname = 'Library.xml'
fname = 'tracks\Library.xml'

data = ET.parse(fname)
xmldata = data.findall('dict/dict/dict')

i = 0
for d in xmldata:
    if (lookup(d, 'Track ID') is None):
        # If there is no Track ID, we skip to next entry
        continue
    else:
        name = lookup(d, 'Name')
        artist = lookup(d, 'Artist')
        genre = lookup(d, 'Genre')
        album = lookup(d, 'Album')
        length = lookup(d, 'Total Time')
        rating = lookup(d, 'Rating')
        count = lookup(d, 'Play Count')
        
        if name is None or artist is None or album is None:
            # Name, Artist and Album must be present
            continue

        print ">", name, artist, album, count, rating, length

        cur.execute('''
        INSERT OR IGNORE INTO Artist (name) VALUES (?)''', (artist, ))
        cur.execute('''
        SELECT id FROM Artist WHERE name = ?''', (artist, ))
        artist_id = cur.fetchone()[0]

        cur.execute('''
        INSERT OR IGNORE INTO Genre (name) VALUES (?)''', (genre, ))
        cur.execute('''
        SELECT id FROM Genre WHERE name = ?''', (genre, ))
        genre_id = cur.fetchone()[0]
        
        cur.execute('''
        INSERT OR IGNORE INTO Album (artist_id, title) VALUES (?, ?)''',
        (artist_id, album))
        cur.execute('''
        SELECT id FROM Album WHERE title = ?''', (album, ))
        album_id = cur.fetchone()[0]

        cur.execute('''
        INSERT OR REPLACE INTO Track
        (title, album_id, genre_id, len, rating, count)
        VALUES (?, ?, ?, ?, ?, ?)''',
        (name, album_id, genre_id, length, rating, count))
        
        # Commit every 5 entries <- totally arbitrary number
        i += 1
        if i % 5 == 0:
            com(conn)

# Commit remaining and close connection to db
com(conn)
cur.close()
