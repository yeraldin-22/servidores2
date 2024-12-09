import sqlite3

def contectar():
    conector = sqlite3.connect('productos.db')
    conector.row_factory = sqlite3.Row
    return conector
    
def init_db():
    conector = contectar()
    conector.execute('''
        CREATE TABLE IF NOT EXISTS productos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            precio REAL NOT NULL,
            imagen TEXT                           
                     )                     
    ''')
    conector.commit()
    conector.close()

def get_all_products():
    conector = contectar()
    productos = conector.execute('SELECT * FROM productos').fetchall()
    conector.close()
    return productos

def add_product(nombre, descripcion, precio, imagen):
    conector = contectar ()
    conector.execute('INSERT  INTO productos(nombre, descripcion, precio, imagen) VALUES (?,?,?,?)',(nombre, descripcion, precio, imagen))
    conector.commit()
    conector.close()

def update_products(id, nombre, descripcion, precio, imagen):
    conector = contectar ()
    conector.execute('''
    UPDATE productos
    SET nombre=?, descripcion=?, precio=?, imagen=?
    WHERE id=?                                  
    ''', (nombre, descripcion, precio, imagen, id))
    conector.commit()
    conector.close()

def delete_product(id):
    conector = contectar()
    conector.execute('DELETE FROM productos WHERE id=?', (id,))
    conector.close()