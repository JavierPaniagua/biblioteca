# importar los paquetes que necesito
from flask import Flask, render_template, request

# crear una aplicación Flask
app = Flask(__name__)

# Rutas del cliente
# anotaciones o decoradores
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/admin', methods=['GET'])
def admin():
    return render_template('admin.html')

@app.route('/menu', methods=['GET'])
def menu():
    return render_template('menu.html')

# Rutas de la api
## CATEGORIAS
@app.route('/api/login', methods=['POST'])
def login():
    return 'login'

@app.route('/api/logout', methods=['GET'])
def logout():
    return 'logout'

@app.route('/api/usuarios', methods=['GET'])
def get_usuarios():
    return 'Todos los usuarios'

## CATEGORIAS
@app.route('/api/categorias', methods=['GET'])
def get_categorias():
    return 'Todas las categorias'

@app.route('/api/categorias/<id>', methods=['GET'])
def get_categoria(id):
    return 'Una sola categoria = '+id

@app.route('/api/categorias', methods=['POST'])
def add_categoria():
    return 'Agregar una categoria'

@app.route('/api/categorias/<id>', methods=['PUT'])
def update_categoria(id):
    return 'Modificar una sola categoria = '+id

@app.route('/api/categorias/<id>', methods=['DELETE'])
def delete_categoria(id):
    return 'Eliminar una sola categoria = '+id