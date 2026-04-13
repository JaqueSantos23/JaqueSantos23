from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/mais-buscados")
def mais_buscados():
    return render_template("mais-buscados.html")

@app.route("/ofertas")
def ofertas():
    return render_template("ofertas.html")

@app.route("/medicamentos")
def medicamentos():
    return render_template("medicamentos.html")

@app.route("/perfumaria")
def perfumaria():
    return render_template("perfumaria.html")

if __name__ == "__main__":
    app.run(debug=True)