#!/usr/bin/env python

"""
Contact Management System

Author: Jitesh Golatar
Date Created: 28/05/2018
Python Version: 2.7.15rc1

"""

import sys
import sqlite3
import prettytable


tbl_name = 'tbl_contacts'

def print_menu():
	print('\n\t\t ========= MENU =========')
	print('\t\t 1. Create new contact')
	print('\t\t 2. Edit existing contact')
	print('\t\t 3. Search a contact')
	print('\t\t 4. Delete a contact')
	print('\t\t 5. View contact book')
	print('\t\t 6. Delete contact book')
	print('\t\t 0. Exit')
	print('\t\t ========================')

def create_contact(cur):
	print('\n\t CREATE NEW CONTACT: ')
	name = raw_input('\n\t Name: ')
	number = int(input('\t Phone Number: '))
	email = raw_input('\t Email: ')
	insert_contact = 'INSERT INTO {tn} (Name, Phone_No, Email) VALUES(?,?,?)'.format(tn=tbl_name)
	cur.execute(insert_contact,(name,number,email))
	print('\n\t Contact Created. ')


def edit_contact(cur,ch):
	if ch == 1:
		new_name = raw_input('\n Enter New Name: ')
		sr_no = int(input('\n Enter SrNo: '))
		update_name = 'UPDATE {tn} SET name = ? WHERE rowid = ?'.format(tn=tbl_name)
		cur.execute(update_name,(new_name,sr_no))
		print('\n\t Contact Name has been updated.')
	elif ch == 2:
		new_phone = raw_input('\n Enter New Phone Number: ')
		sr_no = int(input('\n Enter SrNo: '))
		update_phone = 'UPDATE {tn} SET Phone_No = ? WHERE rowid = ?'.format(tn=tbl_name)
		cur.execute(update_phone,(new_phone,sr_no))
		print('\n\t Contact Phone Number has been updated.')
	elif ch == 3:
		new_email = raw_input('\n Enter New Email: ')
		sr_no = int(input('\n Enter SrNo: '))
		update_email = 'UPDATE {tn} SET Email = ? WHERE rowid = ?'.format(tn=tbl_name)
		cur.execute(update_email,(new_email,sr_no))
		print('\n\t Contact Email has been updated.')
	else:
		edit_contact(int(input('\n Invalid choice. Please enter correct option: ')),cur)


def search(cur):
	print('\n\t SEARCH CONTACT: ')
	name = raw_input('\n\t Name: ')
	cur.execute('SELECT rowid as SrNo,* FROM {tn} WHERE name = ? or name like ?'.format(tn=tbl_name),(name,'%'+name+'%'))
	results = prettytable.from_db_cursor(cur)
	print('\n{}'.format(results))


def delete(cur):
	search(cur)
	sr_no = int(input('\n Enter SrNo: '))
	cur.execute('DELETE FROM {tn} WHERE rowid=?'.format(tn=tbl_name),(sr_no,))
	print('\t\t Contact deleted.')


def view_book(cur):
	cur.execute('SELECT rowid as SrNo, * FROM {tn} ORDER BY Name'.format(tn=tbl_name))
	x = prettytable.from_db_cursor(cur)
	print('\n{}'.format(x))


def delete_book(cur):
	confirm = raw_input('\n Are you sure you want to permanently delete contact book? [y/n] : ')
	if confirm == 'y' or confirm =='Y':
		cur.execute('DELETE FROM {tn}'.format(tn=tbl_name))
		print('\n\t\t Contact book deleted.')

def case(ch,cur):
	if ch == 0:
		conn.close()
		sys.exit()
	elif ch == 1:
		create_contact(cur)
	elif ch == 2:
		search(cur)
		ch = int(input('\n\t EDIT IN CONTACT: 1. NAME 2. PHONE NUMBER 3. EMAIL :'))
		edit_contact(cur,ch)
	elif ch == 3:
		search(cur)
	elif ch == 4:
		delete(cur)
	elif ch == 5:
		view_book(cur)
	elif ch == 6:
		delete_book(cur)
	else:
		case(int(input('\n Invalid choice. Please enter correct option: ')),cur)


# sqlite table creation

table_contacts_create = '''CREATE TABLE IF NOT EXISTS {tn} ( 
							Name TEXT NOT NULL COLLATE NOCASE,
							Phone_No TEXT NOT NULL PRIMARY KEY,
							Email TEXT );'''.format(tn=tbl_name)

# database connection
try:
	conn = sqlite3.connect('./contact_mgmt.db')
	c = conn.cursor()
	# -- create table if does not exist -- #
	c.execute(table_contacts_create)
except sqlite3.Error as er:
	print('\n Unable to connect to the database.',er)
	conn.close()
	sys.exit()
	
print('\n\t\t****** Welcome to Contact Management System ******\t\t')

while True:
	print_menu()
	
	ch1 = int(input('\t\t Enter your choice: '))
	try:
		case(ch1,c)
	except sqlite3.Error as er:
		print('\n Unable to perform the operation.',er)
		conn.close()
		sys.exit()

	conn.commit()

	ch2 = raw_input('\n Do you want to continue [y/n] : ')

	if ch2 == 'n' or ch2 == 'N':
		conn.close()
		sys.exit()
