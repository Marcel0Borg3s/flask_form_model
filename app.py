from flask import Flask, render_template, request
from main import processar_dados



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
        return render_template("obrigado.html", resultado=resultado)

    return render_template("index.html")




if __name__ == "__main__":
    app.run(debug=True)