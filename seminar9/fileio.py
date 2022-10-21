import sqlite3
import pandas as pd

FILENAME = "school.db"


def pd_read_data():
    conn = sqlite3.connect(FILENAME)
    pdb = pd.read_sql_query("select Pupils.id,Pupils.fio,Pupils.birthdate, Classes.name, Placements.rowname, Placements.colname from Classes inner join Pupils ON Classes.id=Pupils.class INNER JOIN Placements ON Pupils.id=Placements.id ORDER BY Pupils.id", conn)
    conn.close()
    return pdb


def read_data():
    conn = sqlite3.connect(FILENAME)
    cur = conn.cursor()
    sql = '''select Pupils.id,Pupils.fio,Pupils.birthdate, Classes.name, Placements.rowname, Placements.colname from Classes inner join Pupils ON Classes.id=Pupils.class INNER JOIN Placements ON Pupils.id=Placements.id ORDER BY Pupils.id'''
    cursor = cur.execute(sql)
    names = [description[0] for description in cursor.description]
    rows = [(names[0], names[1], names[2], names[3],
             names[4], names[5])]+cur.fetchall()
    conn.close()
    return rows


def delete_data(str_id):
    conn = sqlite3.connect(FILENAME)
    cur = conn.cursor()
    cur.execute("BEGIN TRANSACTION")
    sql = '''DELETE FROM Pupils WHERE id=?'''
    cursor = cur.execute(sql, (str_id,))
    sql = '''DELETE FROM Placements WHERE id=?'''
    cursor = cur.execute(sql, (str_id,))
    cur.execute("COMMIT TRANSACTION")
    conn.close()


def update_data(data):
    conn = sqlite3.connect(FILENAME)
    cur = conn.cursor()
    cur.execute("BEGIN TRANSACTION")
    sql = '''SELECT id FROM Classes WHERE name=?'''
    cursor = cur.execute(sql, (data[3],))
    rows = cur.fetchall()

    if len(rows) == 0:
        print("No class, creating a new one")
        sql = '''INSERT INTO Classes(name) VALUES(?) '''
        cursor = cur.execute(sql, (data[3],))
        class_id = cursor.lastrowid
    else:
        class_id = rows[0][0]

    sql = '''UPDATE Pupils SET fio=?, birthdate=?, class=? WHERE id=?'''
    cursor = cur.execute(sql, (data[1], data[2], class_id, data[0]))
    sql = '''UPDATE Placements SET rowname=?, colname=? WHERE id=?'''
    cursor = cur.execute(sql, (data[4], data[5], data[0]))
    cur.execute("COMMIT TRANSACTION")
    conn.close()
    return


def write_data(data):
    conn = sqlite3.connect(FILENAME)
    cur = conn.cursor()
    cur.execute("BEGIN TRANSACTION")

    sql = '''SELECT id FROM Classes WHERE name=?'''
    cursor = cur.execute(sql, (data[2],))
    rows = cur.fetchall()

    if len(rows) == 0:
        print("No class, creating a new one")
        sql = '''INSERT INTO Classes(name) VALUES(?) '''
        cursor = cur.execute(sql, (data[2],))
        class_id = cursor.lastrowid
    else:
        class_id = rows[0][0]

    sql = '''INSERT INTO Pupils(fio, birthdate, class) VALUES(?,?,?) '''
    cursor = cur.execute(sql, (data[0], data[1], class_id))
    pupils_id = cursor.lastrowid

    sql = '''INSERT INTO Placements(id, rowname, colname) VALUES(?,?,?) '''
    cursor = cur.execute(sql, (pupils_id, data[3], data[4]))
    cur.execute("COMMIT TRANSACTION")
    conn.close()
    return
