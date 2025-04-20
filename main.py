from flask import Flask, request, render_template
app = Flask(__name__)

def processar_dados(empresa, nome, email, data_nascimento, genero):
    print("==> Recebido no main.py")
    print(f"Empresa: {empresa}")
    print(f"Nome: {nome}")
    print(f"E-mail: {email}")
    print(f"Data de nascimento: {data_nascimento}")
    print(f"Gênero: {genero}")

    # Aqui você pode salvar, validar, ou transformar os dados
    return f"Dados de {nome} processados com sucesso."

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        empresa = request.form["empresa"]
        nome = request.form["nome"]
        email = request.form["email"]
        data_nascimento = request.form["data_nascimento"]
        genero = request.form["genero"]

        mensagem = processar_dados(empresa, nome, email, data_nascimento, genero)
        return f"<h2>{mensagem}</h2><a href='/'>Voltar</a>"

    return render_template("obrigado.html", mensagem=mensagem)

if __name__ == "__main__":
    app.run(debug=True)