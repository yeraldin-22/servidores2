from flask import Flask, url_for, render_template, request, redirect
import db

servidor2 = Flask(__name__)

@servidor2.route('/inicio')
def home():
   return render_template('index.html') 

@servidor2.route('/productos')
def productos():
   productos =db.get_all_products()
   return render_template('productos.html', productos=productos)

@servidor2.route('/productos/agregar', methods=('GET', 'POST'))
def crear_productos():
   if request.method == 'POST':
      nombre = request.form['nombre']
      descripcion = request.form ['descripcion']
      precio = request.form ['precio']
      imagen = request.form ['imagen']
      db.add_product(nombre, descripcion, precio, imagen)
      return redirect(url_for('productos'))
   return render_template('crear-productos.html', productos=None)

if __name__ == '__main__':
   db.init_db()
   servidor2.run(debug=True)