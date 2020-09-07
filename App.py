from flask import Flask, render_template, request
from flask_mysqldb import MySQL


app=Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_DB'] = 'flask'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_contact' , methods=['POST'])
def add_contact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone= request.form['phone']
        email= request.form['email']
        print(fullname)
        return 'recibido'

@app.route('/edit')
def edit_contact():
    return 'editar contacto'

@app.route('/delete')
def delete_contact():
    return 'eliminar contacto'

app.run(port=3000, debug=True)

if __name__ == '__main__':
    app.run(port=3000, debug=True)