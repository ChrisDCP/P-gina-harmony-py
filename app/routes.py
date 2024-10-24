from flask import render_template, request, redirect, url_for, flash
from app.models import get_users, post_user, put_user, delete_user
from app import app 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/relax')
def relax():
    return render_template('relax.html')

@app.route('/tense')
def tense():
    return render_template('tense.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/usuarios', methods=['GET'])
def mostrar_usuarios():
    usuarios = get_users()

    # Paginado
    page = request.args.get('page', 1, type=int)
    per_page = 5
    total = len(usuarios)
    start = (page - 1) * per_page
    end = start + per_page
    paginated_users = usuarios[start:end]

    total_pages = (total + per_page - 1) // per_page 

    return render_template('usuarios.html', usuarios=paginated_users, page=page, total_pages=total_pages)

@app.route('/usuario/crear', methods=['POST'])
def crear_usuario_route():
    try:
        data = {
            'name': request.form.get('name'),
            'email': request.form.get('email'),
            'age': request.form.get('age'),
            'country': request.form.get('country'),
            'sex': request.form.get('sex')
        }
        post_user(data)
        flash("Usuario agregado correctamente", "success") 
    except Exception as e:
        flash(f'Error al crear usuario: {e}', "danger")
    
    return redirect(url_for('mostrar_usuarios'))

@app.route('/usuario/actualizar/<user_id>', methods=['POST'])
def actualizar_usuario_route(user_id):
    try:
        data = {
            'name': request.form.get('name'),
            'email': request.form.get('email'),
            'age': request.form.get('age'),
            'country': request.form.get('country'),
            'sex': request.form.get('sex'),
        }
        put_user(user_id, data)
        flash("Usuario actualizado correctamente", "success") 
    except Exception as e:
        flash(f'Error al actualizar usuario: {e}', "danger")
    return redirect(url_for('mostrar_usuarios'))

@app.route('/usuario/eliminar/<user_id>', methods=['POST'])
def eliminar_usuario_route(user_id):
    try:
        delete_user(user_id)
        flash("Usuario eliminado correctamente", "success") 
    except Exception as e:
        flash(f'Error al eliminar usuario: {e}', "danger")
    return redirect(url_for('mostrar_usuarios'))
