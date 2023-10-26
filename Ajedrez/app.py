from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def tablero_ajedrez_8x8():
    return render_template('tablero.html', filas=8, columnas=8)

@app.route('/<int:x>')
def tablero_ajedrez_x(x):
    return render_template('tablero.html', filas=8, columnas=x)

@app.route('/<int:x>/<int:y>')
def tablero_ajedrez_x_y(x, y):
    return render_template('tablero.html', filas=x, columnas=y)

if __name__ == '__main__':
    app.run(debug=True)
