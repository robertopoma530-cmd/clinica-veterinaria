import sqlite3

DATABASE = "citas.db"

def init_db():
    """Inicializa la base de datos y crea la tabla pacientes si no existe"""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pacientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            mascota TEXT NOT NULL,
            propietario TEXT NOT NULL,
            especie TEXT,
            fecha TEXT NOT NULL
        )
    ''')
    
    conn.commit()
    conn.close()
    print("✅ Base de datos creada correctamente")

def get_db():
    """Retorna una conexión a la base de datos"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Permite acceder a columnas por nombre
    return conn

if __name__ == "__main__":
    init_db()