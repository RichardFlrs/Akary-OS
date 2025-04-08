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

@app.route("/descargas")
def descargas():
    return render_template("descargas.html")

@app.route("/quienessomos")
def quienessomos():
    return render_template("quienessomos.html")

@app.route("/servicios")
def servicios():
    return render_template("servicios.html")

@app.route("/noticias")
def noticias():
    return render_template("noticias.html")

@app.route("/contacto")
def contacto():
    return render_template("contacto.html")

@app.route("/proceso", methods=['POST'])
def proceso():
    nombre = request.form.get("nombre")
    email = request.form.get("email")
    mensaje = request.form.get("mensaje")
    return render_template("datos.html", nombre=nombre, email=email, mensaje=mensaje)

if __name__ == "__main__":
    app.run(debug=True)
