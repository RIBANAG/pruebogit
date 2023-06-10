import mysql.connector

class Conexion:
    def __init__(self, host, port, user, password, database):
        self.conn = mysql.connector.connect(
            host='localhost',
            port=3306,
            user='root',
            password='Hillairet92,',
            database='big_bread_sa'
        )
        self.cursor = self.conn.cursor()

    def cerrar_conexion(self):
        self.cursor.close()
        self.conn.close()

    def ejecutar_consulta(self, query, params=None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.conn.commit()
            return True
        except mysql.connector.Error as e:
            print(f"Error en la consulta: {e}")
            return False

    def obtener_filas(self, query, params=None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            return self.cursor.fetchall()
        except mysql.connector.Error as e:
            print(f"Error en la consulta: {e}")
            return []












