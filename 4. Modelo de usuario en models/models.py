from flask_login import UserMixin
from conexion.conexion import get_db_connection

class Usuario(UserMixin):
    def __init__(self, id_usuario, nombre, email, password):
        self.id = id_usuario
        self.nombre = nombre
        self.email = email
        self.password = password

    @staticmethod
    def get_by_email(email):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        if user:
            return Usuario(user['id_usuario'], user['nombre'], user['email'], user['password'])
        return None

    @staticmethod
    def get_by_id(id_usuario):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuarios WHERE id_usuario = %s", (id_usuario,))
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        if user:
            return Usuario(user['id_usuario'], user['nombre'], user['email'], user['password'])
        return None

    def save(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO usuarios (nombre, email, password) VALUES (%s, %s, %s)",
            (self.nombre, self.email, self.password)
        )
        conn.commit()
        cursor.close()
        conn.close()
