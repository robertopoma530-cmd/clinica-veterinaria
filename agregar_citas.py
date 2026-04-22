import sqlite3

conn = sqlite3.connect('citas.db')
cursor = conn.cursor()

# Agregar citas de prueba
citas = [
    ('Max', 'Juan Pérez', 'Perro', '2024-12-25 10:00'),
    ('Luna', 'María García', 'Gato', '2024-12-26 15:30'),
    ('Rocky', 'Carlos López', 'Perro', '2024-12-27 09:00'),
    ('Coco', 'Ana Martínez', 'Ave', '2024-12-28 11:00')
]

for cita in citas:
    cursor.execute('INSERT INTO pacientes (mascota, propietario, especie, fecha) VALUES (?, ?, ?, ?)', cita)

conn.commit()
conn.close()

print(f'✅ Se agregaron {len(citas)} citas correctamente')
