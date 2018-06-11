#!/usr/bin/env python3

import sqlite3

def connect():
	conn =sqlite3.connect("books.db")
	curr = conn.cursor()
	curr.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn text)")
	conn.commit()
	return conn

conn = connect()
curr = conn.cursor()

def get_conn():
	return conn

def insert(title,author,year,isbn):
	curr.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
	conn.commit()

def view():
	curr.execute("SELECT * FROM book")
	rows = curr.fetchall()
	conn.commit()
	return rows

def search(title="",author="",year="",isbn=""):
	curr.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
	rows = curr.fetchall()
	return rows

def delete(id):
	curr.execute("DELETE FROM book WHERE id=?",(id,))
	conn.commit()

def update(id,title,author,year,isbn):
	curr.execute("UPDATE book SET title=?,author=?,year=?,isbn=? WHERE id=?",(title,author,year,isbn,id))
	conn.commit()
	
def close():
	conn.close()


