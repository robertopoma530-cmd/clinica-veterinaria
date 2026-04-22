from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from models import init_db, get_db

app = Flask(__name__)

# Inicializar la base de datos al iniciar la aplicación
init_db()

# ==================== RUTAS ====================

@app.route('/')
def index():
    """Muestra todas las citas programadas"""
    conn = get_db()
    citas = conn.execute('SELECT * FROM pacientes ORDER BY fecha').fetchall()
    conn.close()
    return render_template('index.html', citas=citas)

@app.route('/nueva', methods=['GET', 'POST'])
def nueva_cita():
    """Registra una nueva cita médica"""
    if request.method == 'POST':
        mascota = request.form['mascota']
        propietario = request.form['propietario']
        especie = request.form['especie']
        fecha = request.form['fecha']
        
        conn = get_db()
        conn.execute('''
            INSERT INTO pacientes (mascota, propietario, especie, fecha) 
            VALUES (?, ?, ?, ?)
        ''', (mascota, propietario, especie, fecha))
        conn.commit()
        conn.close()
        
        return redirect(url_for('index'))
    
    return render_template('nueva_cita.html')

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_cita(id):
    """Edita una cita existente"""
    conn = get_db()
    
    if request.method == 'POST':
        mascota = request.form['mascota']
        propietario = request.form['propietario']
        especie = request.form['especie']
        fecha = request.form['fecha']
        
        conn.execute('''
            UPDATE pacientes 
            SET mascota=?, propietario=?, especie=?, fecha=? 
            WHERE id=?
        ''', (mascota, propietario, especie, fecha, id))
        conn.commit()
        conn.close()
        
        return redirect(url_for('index'))
    
    # GET: Mostrar formulario con datos actuales
    cita = conn.execute('SELECT * FROM pacientes WHERE id = ?', (id,)).fetchone()
    conn.close()
    
    return render_template('editar_cita.html', cita=cita)

@app.route('/eliminar/<int:id>')
def eliminar_cita(id):
    """Elimina (cancela) una cita del sistema"""
    conn = get_db()
    conn.execute('DELETE FROM pacientes WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

# ==================== EJECUCIÓN ====================

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)