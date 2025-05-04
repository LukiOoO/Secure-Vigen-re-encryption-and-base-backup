from flask import request
from flask import Flask, render_template, request, redirect, url_for, session, send_file, flash
import sqlite3
from flask_bcrypt import Bcrypt
from crypto import vigenere_cipher

app = Flask(__name__)
app.secret_key = 'very_secret_key'
bcrypt = Bcrypt(app)
DB_PATH = 'database.db'


def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        );
    ''')
    conn.commit()
    conn.close()


init_db()


@app.before_request
def check_user_still_exists():
    if request.path.startswith('/static/') or request.endpoint in ('index', 'vigenere_view', 'login', 'register'):
        return

    if 'user' not in session:
        return

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('SELECT 1 FROM users WHERE username = ?', (session['user'],))
    exists = c.fetchone() is not None
    conn.close()

    if not exists:
        session.pop('user', None)
        flash('Twoje konto zostało usunięte', 'error')
        return redirect(url_for('login'))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/vigenere', methods=['GET', 'POST'])
def vigenere_view():
    result = None
    if request.method == 'POST':
        text = request.form['text']
        key = request.form['key']
        mode = request.form['mode']
        result = vigenere_cipher(text, key, mode)
    return render_template('vigenere.html', result=result)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        pw_hash = bcrypt.generate_password_hash(password).decode('utf-8')
        try:
            conn = sqlite3.connect(DB_PATH)
            c = conn.cursor()
            c.execute('INSERT INTO users (username, password_hash) VALUES (?, ?)',
                      (username, pw_hash))
            conn.commit()
            conn.close()
            flash('Rejestracja udana. Zaloguj się.', 'success')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('Nazwa użytkownika zajęta.', 'error')
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('SELECT password_hash FROM users WHERE username = ?', (username,))
        row = c.fetchone()
        conn.close()
        if row and bcrypt.check_password_hash(row[0], password):
            session['user'] = username
            return redirect(url_for('bank_panel'))
        flash('Błędne dane logowania.', 'error')
    return render_template('login.html')


@app.route('/bank', methods=['GET', 'POST'])
def bank_panel():
    if 'user' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        if 'backup' in request.form:
            return send_file(DB_PATH, as_attachment=True)
        elif 'restore' in request.files:
            f = request.files['restore']
            if f:
                f.save(DB_PATH)
                flash('Przywrócono bazę danych.', 'success')
                return redirect(url_for('bank_panel'))

    return render_template('bank.html', user=session['user'])


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
