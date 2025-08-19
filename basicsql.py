import sqlite3

conn = sqlite3.connect('posdb.sqlite3')

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS product (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            barcode TEXT,
            title TEXT,
            price REAL,
            category TEXT )""")


def insert_product(barcode,title,price,category):
    with conn:
        command = 'INSERT INTO product VALUES (?,?,?,?,?)'
        c.execute(command,(None,barcode,title,price,category))
        conn.commit()
        print('saved')


def view_product(allfield=True):
    with conn:
        if allfield:
            command = 'SELECT * FROM product'
        else:
            command = 'SELECT barcode,title,price,category FROM product'
        c.execute(command)
        data = c.fetchall()
        print(data)

    return data



def delete_product(barcode):
    with conn:
        command = 'DELETE FROM product WHERE barcode=(?)'
        c.execute(command,([barcode]))
        conn.commit()

def search_barcode(barcode):
    with conn:
        command = 'SELECT barcode,title,price,category FROM product WHERE barcode=(?)'
        c.execute(command,([barcode]))
        data = list(c.fetchone())
        return data

if __name__ == '__main__':
    # insert_product('1002','Durian',200,'fruit')
    # delete_product('1002')
    search_barcode('1003')
    view_product()