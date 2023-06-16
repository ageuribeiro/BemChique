from flask import Flask, render_template, redirect, flash, request, send_file, send_from_directory, session, url_for
import secrets
app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

# Define a rota principal para o usuario
@app.route("/")
def home():
    return render_template("user/index.html", title='Showcase')

# Define a rota principal para o Administrador
@app.route("/admin")
def admin():
    return render_template("admin/index.html", title='Home')

# Define a rota principal para o Administrador
@app.route("/admin/login")
def admin_login():
    return render_template("admin/login.html", title='Login')

# Define a rota principal para o Administrador
@app.route("/admin/verify_account")
def admin_verify_account():
    return render_template("admin/verify_account.html", title='Verifying')


with app.test_request_context():
    url = url_for('home')
    print(url)

if __name__ == '__main__':
    app.run(debug=True)