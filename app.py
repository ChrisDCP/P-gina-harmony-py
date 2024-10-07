from flask import Flask, render_template, request
from fireconfig import db

app = Flask(__name__)

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

@app.route("/usuarios")
def usuarios():
    #usuarios
    usuarios_ref = db.reference('users')
    usuarios = usuarios_ref.get()

    usuarios_list = []
    if usuarios:
        for user_id, user_data in usuarios.items():
            user_data['id'] = user_id
            usuarios_list.append(user_data)

    #paginado
    page = request.args.get('page', 1, type=int)
    per_page = 4
    total = len(usuarios_list)
    start = (page - 1) * per_page
    end = start + per_page
    paginated_users = usuarios_list[start:end]

    total_pages = (total + per_page - 1) // per_page 

    return render_template('usuarios.html', usuarios=paginated_users, page= page, total_pages=total_pages)




if __name__ == '__main__':
    app.run(debug=True, port=5000)