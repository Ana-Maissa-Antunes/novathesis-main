#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 15:03:34 2022

@author: mac
"""
import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database = r"./curricularUnits.db" # db name with path 

    sql_create_employees_table = """ CREATE TABLE IF NOT EXISTS courses (
                                    course_id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    students_enrolled int
                                    ); """


    # create a database connection
    conn = create_connection(database)



    create_table(conn, sql_create_employees_table)

    conn.close()

if __name__ == '__main__':
    main()