from flask import Flask, request, render_template

app = Flask(__name__)

comentarios = []

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nombre = request.form['nombre']
        mensaje = request.form['comentario']
        comentarios.append({'nombre': nombre, 'mensaje': mensaje})

    return render_template('index.html', comentarios=comentarios)

if __name__ == "__main__":
    app.run(debug=True)
