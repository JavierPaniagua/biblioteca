# importar los paquetes que necesito
from flask import Flask, render_template, request, jsonify
import psycopg2

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

## CATEGORIAS ------------------------------------------------------------------------
## GET = RECUPERAR REGISTRO/S (RECURSO)
## POST = AGREGAR UN REGISTRO (RECURSO)
## PUT = MODIFICAR UN REGISTRO (RECURSO)
## DELETE = ELIMINAR UN REGISTRO (RECURSO)
@app.route('/api/categorias', methods=['GET'])
def get_categorias():
    ##  0 1  2   3           "id""nombre""apellido"
    ## [1,20,13,64]           [1,"Juan","Gonzalez"]
    dictData = []
    resp = jsonify(dictData)
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="1",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="biblioteca")
        cursor = connection.cursor()
        sql = "SELECT * FROM categorias ORDER BY id_categoria"
        cursor.execute(sql)
        row_headers=[x[0] for x in cursor.description]
        record = cursor.fetchall()
        data_json=[]
        for result in record:
            data_json.append(dict(zip(row_headers,result)))

        resp = jsonify(data_json)
    except (Exception, psycopg2.Error) as error:
        print("Error al conectarse a PostgreSQL",error)
    finally:
        if (connection):
            cursor.close()
            connection.close()

    return resp

@app.route('/api/categorias/<id>', methods=['GET'])
def get_categoria(id):
    dictData = {'id_categoria': 0, 'nombre_categoria': '' }
    resp = jsonify(dictData)
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="1",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="biblioteca")
        cursor = connection.cursor()
        sql = """SELECT * FROM categorias 
                 WHERE id_categoria ={0}
                 ORDER BY id_categoria""".format(id)
        cursor.execute(sql)
        record = cursor.fetchone()
        if record is None:
            print("No existe registro")
        else:
            row_headers=[x[0] for x in cursor.description]
            data_json = dict(zip(row_headers, record))
            resp = jsonify(data_json)
    except (Exception, psycopg2.Error) as error:
        print("Error al conectarse a PostgreSQL",error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
    return resp

@app.route('/api/categorias', methods=['POST'])
def add_categoria():
    nombre = request.form["nombre_categoria"]
    dictData = {'agregado': False}
    resp = jsonify(dictData)
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="1",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="biblioteca")
        cursor = connection.cursor()
        sql = """INSERT INTO categorias(nombre_categoria) 
                 VALUES('{0}')""".format(nombre)
        print(sql)
        cursor.execute(sql)
        connection.commit()
        dictData = {'agregado': True}
        resp = jsonify(dictData)
    except (Exception, psycopg2.Error) as error:
        print("Error al conectarse a PostgreSQL",error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
    return resp

@app.route('/api/categorias/<id>', methods=['PUT'])
def update_categoria(id):
    nombre = request.form["nombre_categoria"]
    dictData = {'modificado': False}
    resp = jsonify(dictData)
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="1",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="biblioteca")
        cursor = connection.cursor()
        sql = """UPDATE categorias 
                 SET nombre_categoria='{0}'
                 WHERE id_categoria={1}""".format(nombre,id)
        print(sql)
        cursor.execute(sql)
        connection.commit()
        dictData = {'modificado': True}
        resp = jsonify(dictData)
    except (Exception, psycopg2.Error) as error:
        print("Error al conectarse a PostgreSQL",error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
    return resp

@app.route('/api/categorias/<id>', methods=['DELETE'])
def delete_categoria(id):
    dictData = {'eliminado': False}
    resp = jsonify(dictData)
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="1",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="biblioteca")
        cursor = connection.cursor()
        sql = """DELETE FROM categorias 
                 WHERE id_categoria={0}""".format(id)
        print(sql)
        cursor.execute(sql)
        connection.commit()
        dictData = {'eliminado': True}
        resp = jsonify(dictData)
    except (Exception, psycopg2.Error) as error:
        print("Error al conectarse a PostgreSQL",error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
    return resp

## ESPECIALIDADES ---------------------------------------------------
@app.route('/api/especialidades', methods=['GET'])
def get_especialidades():
    dictData =[]
    resp = jsonify(dictData)

    try:
        connection = psycopg2.connect(user="postgres",
                                        password="1",
                                        host= "127.0.0.1",
                                        port="5432",
                                        database="biblioteca")
        cursor = connection.cursor()
        sql = "SELECT * FROM especialidades ORDER BY id_especialidad"
        cursor.execute(sql)
        row_headers=[x[0] for x in cursor.description]
        record = cursor.fetchall()
        data_json=[]
        for result in record:
            data_json.append(dict(zip(row_headers,result)))
            
        resp =jsonify(data_json)
    
    except (Exception, psycopg2.Error) as error:
        print ("Error al conectarse a PostfresSQL",error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
    return resp

@app.route('/api/especialidades/<id>', methods=['GET'])
def get_especialidad(id):
    dictData ={'id_especialidad':0, 'nombre_especialidad': ''}
    resp = jsonify(dictData)
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="1",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="biblioteca")
        cursor = connection.cursor()
        sql="""SELECT*FROM especialidades
            WHERE id_especialidad ={0}
            ORDER BY id_especialidad""".format(id)
        cursor.execute(sql)
        record = cursor.fetchone()
        if record is None:
            print ("no existe registro")
        else:
            row_headers=[x[0] for x in cursor.description]
            data_json =dict(zip(row_headers,record))
            resp =jsonify(data_json)
    except (Exception, psycopg2.Error) as error:
        print("Error al conectarse a PostgresSQL", error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
    return resp

@app.route('/api/especialidades',methods=['POST'])
def add_especialidad():
    nombre = request.form["nombre_especialidad"]
    dictData = {'agregado': False}
    resp = jsonify(dictData)
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="1",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="biblioteca")
        cursor = connection.cursor()
        sql = """INSERT INTO especialidades(nombre_especialidad) 
                 VALUES('{0}')""".format(nombre)
        print(sql)
        cursor.execute(sql)
        connection.commit()
        dictData = {'agregado': True}
        resp = jsonify(dictData)
    except (Exception, psycopg2.Error) as error:
        print("Error al conectarse a PostgreSQL",error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
    return resp

@app.route('/api/especialidades/<id>', methods=['PUT'])
def update_especialidad(id):
    nombre = request.form["nombre_especialidad"]
    dictData = {'modificado': False}
    resp = jsonify(dictData)
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="1",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="biblioteca")
        cursor = connection.cursor()
        sql = """UPDATE especialidades
                 SET nombre_especialidad='{0}'
                 WHERE id_especialidad={1}""".format(nombre,id)
        print(sql)
        cursor.execute(sql)
        connection.commit()
        dictData = {'modificado': True}
        resp = jsonify(dictData)
    except (Exception, psycopg2.Error) as error:
        print("Error al conectarse a PostgreSQL",error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
    return resp

@app.route('/api/especialidades/<id>', methods=['DELETE'])
def delete_especialidad(id):
    dictData = {'eliminado': False}
    resp = jsonify(dictData)
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="1",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="biblioteca")
        cursor = connection.cursor()
        sql = """DELETE FROM especialidades 
                 WHERE id_especialidad={0}""".format(id)
        print(sql)
        cursor.execute(sql)
        connection.commit()
        dictData = {'eliminado': True}
        resp = jsonify(dictData)
    except (Exception, psycopg2.Error) as error:
        print("Error al conectarse a PostgreSQL",error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
    return resp


## AUTORES ------------------------------------------------------------------------
@app.route('/api/autores', methods=['GET'])
def get_autores():
    dictData = []
    resp = jsonify(dictData)
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="1",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="biblioteca")
        cursor = connection.cursor()
        sql = "SELECT * FROM autores ORDER BY id_autor"
        cursor.execute(sql)
        row_headers=[x[0] for x in cursor.description]
        record = cursor.fetchall()
        data_json=[]
        for result in record:
            data_json.append(dict(zip(row_headers,result)))

        resp = jsonify(data_json)
    except (Exception, psycopg2.Error) as error:
        print("Error al conectarse a PostgreSQL",error)
    finally:
        if (connection):
            cursor.close()
            connection.close()

    return resp

@app.route('/api/autores/<id>', methods=['GET'])
def get_autor(id):
    dictData = {'id_autor': 0, 'nombre_autor': '' }
    resp = jsonify(dictData)
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="1",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="biblioteca")
        cursor = connection.cursor()
        sql = """SELECT * FROM autores 
                 WHERE id_autor ={0}
                 ORDER BY id_autor""".format(id)
        cursor.execute(sql)
        record = cursor.fetchone()
        if record is None:
            print("No existe registro")
        else:
            row_headers=[x[0] for x in cursor.description]
            data_json = dict(zip(row_headers, record))
            resp = jsonify(data_json)
    except (Exception, psycopg2.Error) as error:
        print("Error al conectarse a PostgreSQL",error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
    return resp
    
@app.route('/api/autores', methods=['POST'])
def add_autor():
    nombre = request.form["nombre_autor"]
    dictData = {'agregado': False}
    resp = jsonify(dictData)
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="1",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="biblioteca")
        cursor = connection.cursor()
        sql = """INSERT INTO autores(nombre_autor) 
                 VALUES('{0}')""".format(nombre)
        print(sql)
        cursor.execute(sql)
        connection.commit()
        dictData = {'agregado': True}
        resp = jsonify(dictData)
    except (Exception, psycopg2.Error) as error:
        print("Error al conectarse a PostgreSQL",error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
    return resp

@app.route('/api/autores/<id>', methods=['PUT'])
def update_autor(id):
    nombre = request.form["nombre_autor"]
    dictData = {'modificado': False}
    resp = jsonify(dictData)
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="1",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="biblioteca")
        cursor = connection.cursor()
        sql = """UPDATE autores
                 SET nombre_autor='{0}'
                 WHERE id_autor={1}""".format(nombre,id)
        print(sql)
        cursor.execute(sql)
        connection.commit()
        dictData = {'modificado': True}
        resp = jsonify(dictData)
    except (Exception, psycopg2.Error) as error:
        print("Error al conectarse a PostgreSQL",error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
    return resp

@app.route('/api/autores/<id>', methods=['DELETE'])
def delete_autor(id):
    dictData = {'eliminado': False}
    resp = jsonify(dictData)
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="1",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="biblioteca")
        cursor = connection.cursor()
        sql = """DELETE FROM autores
                 WHERE id_autor={0}""".format(id)
        print(sql)
        cursor.execute(sql)
        connection.commit()
        dictData = {'eliminado': True}
        resp = jsonify(dictData)
    except (Exception, psycopg2.Error) as error:
        print("Error al conectarse a PostgreSQL",error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
    return resp

## CURSOS ------------------------------------------------------------------------
@app.route('/api/cursos', methods=['GET'])
def get_cursos():
    dictData = []
    resp = jsonify(dictData)
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="1",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="biblioteca")
        cursor = connection.cursor()
        sql = "SELECT * FROM cursos ORDER BY id_curso"
        cursor.execute(sql)
        row_headers=[x[0] for x in cursor.description]
        record = cursor.fetchall()
        data_json=[]
        for result in record:
            data_json.append(dict(zip(row_headers,result)))

        resp = jsonify(data_json)
    except (Exception, psycopg2.Error) as error:
        print("Error al conectarse a PostgreSQL",error)
    finally:
        if (connection):
            cursor.close()
            connection.close()

    return resp

@app.route('/api/cursos/<id>', methods=['GET'])
def get_curso(id):
    dictData = {'id_curso': 0, 'nombre_curso': '' }
    resp = jsonify(dictData)
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="1",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="biblioteca")
        cursor = connection.cursor()
        sql = """SELECT * FROM cursos
                 WHERE id_curso ={0}
                 ORDER BY id_curso""".format(id)
        cursor.execute(sql)
        record = cursor.fetchone()
        if record is None:
            print("No existe registro")
        else:
            row_headers=[x[0] for x in cursor.description]
            data_json = dict(zip(row_headers, record))
            resp = jsonify(data_json)
    except (Exception, psycopg2.Error) as error:
        print("Error al conectarse a PostgreSQL",error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
    return resp

@app.route('/api/cursos', methods=['POST'])
def add_curso():
    nombre = request.form["nombre_curso"]
    dictData = {'agregado': False}
    resp = jsonify(dictData)
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="1",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="biblioteca")
        cursor = connection.cursor()
        sql = """INSERT INTO cursos(nombre_curso) 
                 VALUES('{0}')""".format(nombre)
        print(sql)
        cursor.execute(sql)
        connection.commit()
        dictData = {'agregado': True}
        resp = jsonify(dictData)
    except (Exception, psycopg2.Error) as error:
        print("Error al conectarse a PostgreSQL",error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
    return resp

@app.route('/api/curso/<id>', methods=['PUT'])
def update_curso(id):
    nombre = request.form["nombre_curso"]
    dictData = {'modificado': False}
    resp = jsonify(dictData)
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="1",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="biblioteca")
        cursor = connection.cursor()
        sql = """UPDATE cursos 
                 SET nombre_curso='{0}'
                 WHERE id_curso={1}""".format(nombre,id)
        print(sql)
        cursor.execute(sql)
        connection.commit()
        dictData = {'modificado': True}
        resp = jsonify(dictData)
    except (Exception, psycopg2.Error) as error:
        print("Error al conectarse a PostgreSQL",error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
    return resp

@app.route('/api/curso/<id>', methods=['DELETE'])
def delete_curso(id):
    dictData = {'eliminado': False}
    resp = jsonify(dictData)
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="1",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="biblioteca")
        cursor = connection.cursor()
        sql = """DELETE FROM cursos 
                 WHERE id_curso={0}""".format(id)
        print(sql)
        cursor.execute(sql)
        connection.commit()
        dictData = {'eliminado': True}
        resp = jsonify(dictData)
    except (Exception, psycopg2.Error) as error:
        print("Error al conectarse a PostgreSQL",error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
    return resp

## ALUMNOS ------------------------------------------------------------------------
@app.route('/api/alumnos', methods=['GET'])
def get_alumnos():
    dictData = []
    resp = jsonify(dictData)
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="1",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="biblioteca")
        cursor = connection.cursor()
        sql = '''SELECT * FROM alumnos a
                 LEFT JOIN cursos c ON a.id_curso = c.id_curso
                 LEFT JOIN especialidades e ON a.id_especialidad = e.id_especialidad
                 ORDER BY id_alumno'''
        cursor.execute(sql)
        row_headers=[x[0] for x in cursor.description]
        record = cursor.fetchall()
        data_json=[]
        for result in record:
            data_json.append(dict(zip(row_headers,result)))

        resp = jsonify(data_json)
    except (Exception, psycopg2.Error) as error:
        print("Error al conectarse a PostgreSQL",error)
    finally:
        if (connection):
            cursor.close()
            connection.close()

    return resp

@app.route('/api/alumnos/<id>', methods=['GET'])
def get_alumno(id):
    dictData = {'id_alumno': 0, 
                'nombre_alumno': '',
                'cedula_alumno':'',
                'direccion_alumno':'',
                'telefono_alumno':'',
                'id_curso':0,
                'nombre_curso':'',
                'id_especialidad':0,
                'nombre_especialidad':''
                 }
    resp = jsonify(dictData)
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="1",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="biblioteca")
        cursor = connection.cursor()
        sql = """SELECT * FROM alumnos a
                 LEFT JOIN cursos c ON a.id_curso = c.id_curso
                 LEFT JOIN especialidades e ON a.id_especialidad = e.id_especialidad
                 WHERE id_alumno ={0}
                 ORDER BY id_alumno""".format(id)
        cursor.execute(sql)
        record = cursor.fetchone()
        if record is None:
            print("No existe registro")
        else:
            row_headers=[x[0] for x in cursor.description]
            data_json = dict(zip(row_headers, record))
            resp = jsonify(data_json)
    except (Exception, psycopg2.Error) as error:
        print("Error al conectarse a PostgreSQL",error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
    return resp

@app.route('/api/alumnos', methods=['POST'])
def add_alumnos():
    nombre = request.form["nombre_alumno"]
    cedula = request.form["cedula_alumno"]
    direccion = request.form["direccion_alumno"]
    telefono = request.form["telefono_alumno"]
    id_curso = request.form["id_curso"]
    id_especialidad = request.form["id_especialidad"]
    dictData = {'agregado': False}
    resp = jsonify(dictData)
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="1",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="biblioteca")
        cursor = connection.cursor()
        sql = """INSERT INTO alumnos(nombre_alumno, cedula_alumno,
                 direccion_alumno, telefono_alumno, 
                 id_curso, id_especialidad) 
                 VALUES('{0}','{1}','{2}','{3}','{4}','{5}')""".format(nombre, 
                 cedula, direccion, telefono,
                 id_curso, id_especialidad)
        print(sql)
        cursor.execute(sql)
        connection.commit()
        dictData = {'agregado': True}
        resp = jsonify(dictData)
    except (Exception, psycopg2.Error) as error:
        print("Error al conectarse a PostgreSQL",error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
    return resp

@app.route('/api/alumno/<id>', methods=['PUT'])
def update_alumno(id):
    nombre = request.form["nombre_alumno"]
    cedula = request.form["cedula_alumno"]
    direccion = request.form["direccion_alumno"]
    telefono = request.form["telefono_alumno"]
    id_curso = request.form["id_curso"]
    id_especialidad = request.form["id_especialidad"]

    dictData = {'modificado': False}
    resp = jsonify(dictData)
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="1",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="biblioteca")
        cursor = connection.cursor()
        sql = """UPDATE alumnos 
                 SET nombre_alumno='{0}',
                 cedula_alumno='{1}',
                 direccion_alumno='{2}',
                 telefono_alumno='{3}',
                 id_curso='{4}',
                 id_especialidad='{5}'
                 WHERE id_alumno={6}""".format(nombre, cedula,
                 direccion,telefono,id_curso,id_especialidad,id)
        print(sql)
        cursor.execute(sql)
        connection.commit()
        dictData = {'modificado': True}
        resp = jsonify(dictData)
    except (Exception, psycopg2.Error) as error:
        print("Error al conectarse a PostgreSQL",error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
    return resp

@app.route('/api/alumno/<id>', methods=['DELETE'])
def delete_alumno(id):
    dictData = {'eliminado': False}
    resp = jsonify(dictData)
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="1",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="biblioteca")
        cursor = connection.cursor()
        sql = """DELETE FROM alumnos
                 WHERE id_alumno={0}""".format(id)
        print(sql)
        cursor.execute(sql)
        connection.commit()
        dictData = {'eliminado': True}
        resp = jsonify(dictData)
    except (Exception, psycopg2.Error) as error:
        print("Error al conectarse a PostgreSQL",error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
    return resp


## PROFESORES ------------------------------------------------------------------------
@app.route('/api/profesores', methods=['GET'])
def get_profesores():
    dictData = []
    resp = jsonify(dictData)
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="1",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="biblioteca")
        cursor = connection.cursor()
        sql = "SELECT * FROM profesores ORDER BY id_profesor"
        cursor.execute(sql)
        row_headers=[x[0] for x in cursor.description]
        record = cursor.fetchall()
        data_json=[]
        for result in record:
            data_json.append(dict(zip(row_headers,result)))

        resp = jsonify(data_json)
    except (Exception, psycopg2.Error) as error:
        print("Error al conectarse a PostgreSQL",error)
    finally:
        if (connection):
            cursor.close()
            connection.close()

    return resp

@app.route('/api/profesores/<id>', methods=['GET'])
def get_profesor(id):
    dictData = {'id_profesor': 0, 
                'nombre_profesor': '',
                'cedula_profesor':'',
                'direccion_profesor':'',
                'telefono_profesor':''               
                 }
    resp = jsonify(dictData)
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="1",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="biblioteca")
        cursor = connection.cursor()
        sql = """SELECT * FROM profesores
                 WHERE id_profesor={0}
                 ORDER BY id_profesor""".format(id)
        cursor.execute(sql)
        record = cursor.fetchone()
        if record is None:
            print("No existe registro")
        else:
            row_headers=[x[0] for x in cursor.description]
            data_json = dict(zip(row_headers, record))
            resp = jsonify(data_json)
    except (Exception, psycopg2.Error) as error:
        print("Error al conectarse a PostgreSQL",error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
    return resp

@app.route('/api/profesores', methods=['POST'])
def add_profesor():
    nombre = request.form["nombre_profesor"]
    cedula = request.form["cedula_profesor"]
    direccion = request.form["direccion_profesor"]
    telefono = request.form["telefono_profesor"]
    dictData = {'agregado': False}
    resp = jsonify(dictData)
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="1",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="biblioteca")
        cursor = connection.cursor()
        sql = """INSERT INTO categorias(nombre_profesor,cedula_profesor,
                        direccion_profesor,
                        telefono_profesor) 
                 VALUES('{0}','{1}','{2}','{3}')""".format(nombre,cedula,
                 direccion,telefono)
        print(sql)
        cursor.execute(sql)
        connection.commit()
        dictData = {'agregado': True}
        resp = jsonify(dictData)
    except (Exception, psycopg2.Error) as error:
        print("Error al conectarse a PostgreSQL",error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
    return resp

@app.route('/api/profesor/<id>', methods=['PUT'])
def update_profesor(id):
    nombre = request.form["nombre_profesor"]
    cedula = request.form["cedula_profesor"]
    direccion = request.form["direccion_profesor"]
    telefono = request.form["telefono_profesor"]
    
    dictData = {'modificado': False}
    resp = jsonify(dictData)
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="1",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="biblioteca")
        cursor = connection.cursor()
        sql = """UPDATE profesores
                 SET nombre_profesor='{0}',
                 cedula_profesor='{1}',
                 direccion_profesor='{2}',
                 telefono_profesor='{3}'
                 WHERE id_profesor={4}""".format(nombre,cedula,
                                            direccion,telefono,id)
        print(sql)
        cursor.execute(sql)
        connection.commit()
        dictData = {'modificado': True}
        resp = jsonify(dictData)
    except (Exception, psycopg2.Error) as error:
        print("Error al conectarse a PostgreSQL",error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
    return resp

@app.route('/api/profesor/<id>', methods=['DELETE'])
def delete_profesor(id):

    dictData = {'eliminado': False}
    resp = jsonify(dictData)
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="1",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="biblioteca")
        cursor = connection.cursor()
        sql = """DELETE FROM profesores
                 WHERE id_profesor={0}""".format(id)
        print(sql)
        cursor.execute(sql)
        connection.commit()
        dictData = {'eliminado': True}
        resp = jsonify(dictData)
    except (Exception, psycopg2.Error) as error:
        print("Error al conectarse a PostgreSQL",error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
    return resp
 
## LIBROS ------------------------------------------------------------------------
@app.route('/api/libros', methods=['GET'])
def get_libros():
    dictData = []
    resp = jsonify(dictData)
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="1",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="biblioteca")
        cursor = connection.cursor()
        sql = "SELECT * FROM libros ORDER BY id_libro"
        cursor.execute(sql)
        row_headers=[x[0] for x in cursor.description]
        record = cursor.fetchall()
        data_json=[]
        for result in record:
            data_json.append(dict(zip(row_headers,result)))

        resp = jsonify(data_json)
    except (Exception, psycopg2.Error) as error:
        print("Error al conectarse a PostgreSQL",error)
    finally:
        if (connection):
            cursor.close()
            connection.close()

    return resp

@app.route('/api/libros/<id>', methods=['GET'])
def get_libro(id):
    dictData = {'id_libro': 0, 
                'nombre_libro': '',
                'id_libro':'',
                'id_categoria':''     
                 }
    resp = jsonify(dictData)
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="1",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="biblioteca")
        cursor = connection.cursor()
        sql = """SELECT * FROM libros
                 WHERE id_libros={0}
                 ORDER BY id_libro""".format(id)
        cursor.execute(sql)
        record = cursor.fetchone()
        if record is None:
            print("No existe registro")
        else:
            row_headers=[x[0] for x in cursor.description]
            data_json = dict(zip(row_headers, record))
            resp = jsonify(data_json)
    except (Exception, psycopg2.Error) as error:
        print("Error al conectarse a PostgreSQL",error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
    return resp

@app.route('/api/libros', methods=['POST'])
def add_libro():
    nombre = request.form["nombre_libro"]
    id_categoria= request.form["id_categoria"]
   
    dictData = {'agregado': False}
    resp = jsonify(dictData)
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="1",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="biblioteca")
        cursor = connection.cursor()
        sql = """INSERT INTO libros(nombre_libro,id_categoria) 
                 VALUES('{0}','{1}')""".format(nombre,id_categoria)
        print(sql)
        cursor.execute(sql)
        connection.commit()
        dictData = {'agregado': True}
        resp = jsonify(dictData)
    except (Exception, psycopg2.Error) as error:
        print("Error al conectarse a PostgreSQL",error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
    return resp

@app.route('/api/libro/<id>', methods=['PUT'])
def update_libro(id):
    nombre = request.form["nombre_profesor"]
    cedula = request.form["cedula_profesor"]
    direccion = request.form["direccion_profesor"]
    telefono = request.form["telefono_profesor"]
    
    dictData = {'modificado': False}
    resp = jsonify(dictData)
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="1",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="biblioteca")
        cursor = connection.cursor()
        sql = """UPDATE profesores
                 SET nombre_profesor='{0}',
                 cedula_profesor='{1}',
                 direccion_profesor='{2}',
                 telefono_profesor='{3}'
                 WHERE id_profesor={4}""".format(nombre,cedula,
                                            direccion,telefono,id)
        print(sql)
        cursor.execute(sql)
        connection.commit()
        dictData = {'modificado': True}
        resp = jsonify(dictData)
    except (Exception, psycopg2.Error) as error:
        print("Error al conectarse a PostgreSQL",error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
    return resp

@app.route('/api/libro/<id>', methods=['DELETE'])
def delete_libro(id):

    dictData = {'eliminado': False}
    resp = jsonify(dictData)
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="1",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="biblioteca")
        cursor = connection.cursor()
        sql = """DELETE FROM libros
                 WHERE id_libro={0}""".format(id)
        print(sql)
        cursor.execute(sql)
        connection.commit()
        dictData = {'eliminado': True}
        resp = jsonify(dictData)
    except (Exception, psycopg2.Error) as error:
        print("Error al conectarse a PostgreSQL",error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
    return resp
 
