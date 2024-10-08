from flask import render_template, request, redirect, url_for
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
    per_page = 4
    total = len(usuarios)
    start = (page - 1) * per_page
    end = start + per_page
    paginated_users = usuarios[start:end]

    total_pages = (total + per_page - 1) // per_page 

    return render_template('usuarios.html', usuarios=paginated_users, page=page, total_pages=total_pages)

@app.route('/usuario/crear', methods=['POST'])
def crear_usuario_route():
    data = {
        'name': request.form['name'],
        'email': request.form['email']
    }
    post_user(data)
    return redirect(url_for('mostrar_usuarios'))

@app.route('/usuario/actualizar/<user_id>', methods=['POST'])
def actualizar_usuario_route(user_id):
    data = {
        'name': request.form['name'],
        'email': request.form['email']
    }
    put_user(user_id, data)
    return redirect(url_for('mostrar_usuarios'))

@app.route('/usuario/eliminar/<user_id>', methods=['POST'])
def eliminar_usuario_route(user_id):
    delete_user(user_id)
    return redirect(url_for('mostrar_usuarios'))
