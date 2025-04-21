from flask import Flask, render_template, request
from utils import processar_dados

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        empresa = request.form['empresa']
        nome = request.form['nome']
        email = request.form['email']
        data_nascimento = request.form['data_nascimento']
        genero = request.form['genero']
        resultado = processar_dados(empresa, nome, email, data_nascimento, genero)
        return render_template("obrigado.html", nome=nome, resultado=resultado)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)